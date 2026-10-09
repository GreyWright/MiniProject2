from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

ROOT = Path.cwd()
SRC = ROOT / 'sources'
NETID = 'gwright30'
AS_OF = pd.Timestamp('2026-10-08T23:59:59Z')
COLS = ['project_wocid','commit_sha1','author','time','commit message']
raw = pd.read_csv(SRC/f'{NETID}_project_summary.csv',sep=';',keep_default_na=False)
missing_original = pd.read_csv(SRC/f'{NETID}_missing_commits.csv',sep=';')
assigned = pd.read_csv(SRC/f'{NETID}_assigned_projects.csv')
meta = json.loads((SRC/'github_current.json').read_text())
historical = json.loads((SRC/'github_historical_2025.json').read_text())
HISTORICAL_START = pd.Timestamp('2025-04-01T00:00:00Z')
HISTORICAL_END = pd.Timestamp('2025-09-30T23:59:59Z')
recovery = json.loads((SRC/'github_recovery.json').read_text())
interpretations = json.loads((SRC/'interpretations.json').read_text())
recovered = []
provenance = []
for item in recovery:
    response = item['result'].get('structuredContent',{})
    obj = json.loads(response['content']) if 'content' in response else {}
    if obj.get('sha') != item['sha']:
        continue
    for _, row in missing_original[missing_original.commit_sha1==item['sha']].iterrows():
        author = obj['author']
        recovered.append([row.project_wocid,item['sha'],f"{author['name']} <{author['email']}>",int(pd.Timestamp(author['date']).timestamp()),obj['message']])
        provenance.append({'project_wocid':row.project_wocid,'commit_sha1':item['sha'],'source':'GitHub git commit object','url':obj.get('url',''),'retrieved_on':'2026-10-08'})
df = pd.concat([raw,pd.DataFrame(recovered,columns=COLS)],ignore_index=True)
assert not df.duplicated(['project_wocid','commit_sha1']).any()
assert df.project_wocid.nunique()==10
assert df.commit_sha1.str.fullmatch('[0-9a-f]{40}').all()
df['time'] = pd.to_numeric(df.time,errors='raise').astype('int64')
df['date'] = pd.to_datetime(df.time,unit='s',utc=True)
assert df.date.max() <= AS_OF
df = df.sort_values(['project_wocid','time','commit_sha1'])
df[COLS].to_csv(ROOT/f'{NETID}_project_summary.csv',sep=';',index=False)
pd.DataFrame(provenance).to_csv(ROOT/f'{NETID}_recovered_commits.csv',sep=';',index=False)
unresolved = missing_original.merge(df[['project_wocid','commit_sha1']],how='left',on=['project_wocid','commit_sha1'],indicator=True)
unresolved = unresolved[unresolved._merge=='left_only'][['project_wocid','commit_sha1']]
unresolved.to_csv(ROOT/f'{NETID}_missing_commits.csv',sep=';',index=False)
statistics, gap_samples, recent_samples, observations, monthly_check, historical_evidence = [], [], [], [], [], []

def gap_runs(series):
    runs, current = [], []
    for month, count in series.items():
        if count == 0:
            current.append(month)
        elif current:
            runs.append(current)
            current = []
    if current:
        runs.append(current)
    return runs

for _, assignment in assigned.iterrows():
    project = assignment.WoC
    original_repo = assignment.GH.removeprefix('https://github.com/')
    info = json.loads(meta[original_repo][0]['content'])
    commits = json.loads(meta[original_repo][1]['content'])
    text = interpretations[project]
    group = df[df.project_wocid==project].copy()
    months = group.date.dt.tz_localize(None).dt.to_period('M')
    monthly = months.value_counts().reindex(pd.period_range(months.min(),months.max(),freq='M'),fill_value=0).sort_index()
    assert int(monthly.sum()) == len(group)
    runs = gap_runs(monthly)
    # max preserves the earliest run when multiple runs tie in length.
    longest = max(runs,key=len,default=[])
    start, end = (longest[0],longest[-1]) if longest else (None,None)
    timeseries = pd.DataFrame({'Month':monthly.index.astype(str),'#Commits':monthly.values})
    timeseries.to_csv(ROOT/f'{NETID}_commits_timeseries_{project}.csv',sep=';',index=False)
    fig, ax = plt.subplots(figsize=(11,4.8))
    ax.plot(monthly.index.to_timestamp(),monthly.values,lw=1.35,color='#225b8d')
    if longest:
        ax.axvspan(start.start_time,(end+1).start_time,color='#efb85c',alpha=.28,label=f'Longest gap: {len(longest)} months')
        ax.legend(frameon=False,loc='upper right')
    ax.set(title=project,xlabel='Month (YYYY-MM)',ylabel='Number of commits')
    locator = mdates.AutoDateLocator(minticks=5,maxticks=11)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax.tick_params(axis='x',rotation=40)
    ax.grid(alpha=.25)
    ax.set_ylim(bottom=0)
    fig.tight_layout()
    fig.savefig(ROOT/f'{NETID}_timeseries_{project}.png',dpi=300)
    plt.close(fig)
    pre = group[months<start].tail(10) if longest else group.iloc[:0]
    post = group[months>end].head(10) if longest else group.iloc[:0]
    for side,sample in [('pre',pre),('post',post)]:
        sample = sample[COLS].copy()
        sample.insert(0,'pre/post',side)
        gap_samples.append(sample)
    head = commits[0]
    last_date = pd.Timestamp(head['commit']['committer']['date'])
    # Determine the status *as of September 30, 2025*, rather than
    # comparing the October 2026 latest commit against an old cutoff.
    historical_commit = historical[original_repo]
    assert historical_commit['resolved_repository'].lower() == info['full_name'].lower()
    assert historical_commit['default_branch_checked'] == info['default_branch']
    hist_date = pd.Timestamp(historical_commit['latest_commit_committer_date_utc'])
    assert hist_date <= HISTORICAL_END
    hist_sha = historical_commit['latest_commit_sha_on_or_before_2025_09_30']
    assert len(hist_sha) == 40
    status = 'Active' if hist_date >= HISTORICAL_START else 'Inactive'
    today_status = 'Inactive' if last_date < pd.Timestamp('2026-04-08T00:00:00Z') else 'Active'
    for c in commits:
        recent_samples.append({'project_wocid':project,'commit_sha1':c['sha'],'author':c['commit']['author']['name'],'author_date':c['commit']['author']['date'],'committer_date':c['commit']['committer']['date'],'commit message':c['commit']['message'],'url':c['html_url']})
    missing_n = int((unresolved.project_wocid==project).sum())
    row = {'Project':project,'ncommits':len(group),'nauthors':group.author.nunique(),'from':group.date.min().isoformat(),'to':group.date.max().isoformat(),'nstars':info['stargazers_count'],'nforks':info['forks_count'],'lastGHCommitDate':last_date.isoformat(),'LongestGapStart':str(start) if longest else 'N/A','LongestGapEnd':str(end) if longest else 'N/A','LongestGapLength':len(longest),'NumCommitsAfterLastGap':int((months>end).sum()) if longest else 0,'ActivityPattern':text['pattern'],'NumberOfGapsInTimeline':sum(len(r)>=3 for r in runs),'BeforeThemes':text['before'],'AfterThemes':text['after'],'HypothesizedGapReason':text['reason'],'HasRecovered':text['recovered'],'WhyRecovered':text['why'],'WhoRecovered':text['who'],'Currentstatus':status,'RecentThemes':text['recent'],'Notes':text['notes'],'MissingCommitCount':missing_n,'GitHubRecoveredCommitCount':sum(z['project_wocid']==project for z in provenance),'GitHubRepository':info['full_name'],'GitHubDefaultBranch':info['default_branch'],'GitHubObservedOn':'2026-10-08','StatusAsOf2026_10_08':today_status,'HistoricalLastCommitDateUTC':hist_date.isoformat(),'HistoricalLastCommitSHA':hist_sha,'HistoricalReferenceDate':'2025-09-30','HistoricalEvidenceURL':historical_commit['commit_url']}
    statistics.append(row)
    historical_evidence.append({'Project':project,'AssignedRepository':original_repo,
        'ResolvedGitHubRepository':info['full_name'],'DefaultBranch':info['default_branch'],
        'ReferenceDateUTC':'2025-09-30','WindowStartUTC':'2025-04-01',
        'LastCommitAtOrBeforeReferenceUTC':hist_date.isoformat(),
        'HistoricalCommitSHA':hist_sha,'Currentstatus':status,
        'CommitURL':historical_commit['commit_url'],
        'GitHubAPIQuery':historical_commit['api_request']})
    observations.append({'Project':project,'GitHubURL':info['html_url'],'DefaultBranch':info['default_branch'],'Stars':info['stargazers_count'],'Forks':info['forks_count'],'LatestDefaultBranchCommit':head['sha'],'LastCommitDateUTC':last_date.isoformat(),'Source':('GitHub page manually checked; API used for exact counts rounded in UI' if project in {'catboost_catboost', 'pydata_pandas-datareader'} else 'GitHub page manually checked; API snapshot retained for exact recorded values'),'ObservedOn':'2026-10-08'})
    monthly_check.append({'Project':project,'Rows':len(group),'MonthlySum':int(monthly.sum()),'Months':len(monthly),'ZeroMonths':int((monthly==0).sum()),'PreSample':len(pre),'PostSample':len(post),'RemainingMissing':missing_n})
    lines=[f'# {project}', '', '## Reflection', '', text['reflection'], '',
           '## Commit activity and evidence', '',
           f'**Analyzed records:** {len(group):,} commits, {group.author.nunique():,} distinct author strings ({group.date.min().date()} to {group.date.max().date()}).',
           f'**Activity pattern:** {text["pattern"]}. **Gaps of at least three months:** {row["NumberOfGapsInTimeline"]}.',
           f'**Longest gap:** {start} through {end} ({len(longest)} zero-commit months); {row["NumCommitsAfterLastGap"]:,} commits afterward.' if longest else '**Longest gap:** None; there is at least one commit in every observed month.',
           '']
    if longest:
        lines += [f'**My best explanation for the gap:** {text["reason"]}',
                  '', f'**Recovery:** {text["recovered"]}. {text["why"]}',
                  '', f'**Contributors after the gap:** {text["who"]}',
                  '', f'**Themes before the gap:** {text["before"].replace(":", ", ")}. **After:** {text["after"].replace(":", ", ")}.',
                  '', '## Boundary-commit evidence', '',
                  '| Sample | UTC date | Author | Commit | Message |', '|---|---|---|---|---|']
        for side,sample in [('Before',pre),('After',post)]:
            for _,r in sample.iterrows():
                message=r['commit message'].splitlines()[0] if r['commit message'] else '(empty message)'
                author=r.author.split('<')[0].strip().replace('|','/')
                lines.append(f'| {side} | {r.date.date()} | {author} | [{r.commit_sha1[:8]}](https://github.com/{info["full_name"]}/commit/{r.commit_sha1}) | {message.replace(chr(124),"/")} |')
    else:
        lines += ['No pre/post-gap themes or recovery comparison applies because there is no zero-commit month in the observed timeline.']
    lines += ['', '## GitHub status and recent activity','',f'The GitHub default branch I checked was `{info["default_branch"]}` of [{info["full_name"]}]({info["html_url"]}). Its latest commit is [{head["sha"][:8]}]({head["html_url"]}), dated {last_date.isoformat()}. For the September 30, 2025 reference date, the latest commit found on that branch by then was [{hist_sha[:8]}]({historical_commit['commit_url']}) (committer date {hist_date.isoformat()}). That makes its historical status **{status}** using the April 1–September 30, 2025 window. Separately, the most recent October 2026 observation gives **{today_status}** for the six months ending October 8, 2026. These are default-branch commit-history checks, not a claim about every branch or fork.', '',f'The recent-ten themes are **{text["recent"]}**. The complete messages and links are in `{NETID}_github_recent_commits.csv`.','', '## Limits and supporting sources','',f'{missing_n} listed commits remain unavailable for this project, so a missing record could affect a gap measurement.' if missing_n else 'No commits from the supplied retrieval list remain unresolved for this project.', 'Author counts represent recorded author strings, not necessarily distinct people. The WoC timeline and the GitHub default branch may cover different histories; author timestamps and merge dates can also differ.']
    lines += ['',*[f'- {url}' for url in text['sources']], '']
    (ROOT/f'{NETID}_reflection_{project}.md').write_text('\n'.join(lines))

stats = pd.DataFrame(statistics)
stats.to_csv(ROOT/f'{NETID}_project_stats.csv',sep=';',index=False)
pd.concat(gap_samples,ignore_index=True).to_csv(ROOT/f'{NETID}_project_gap_commits.csv',sep=';',index=False)
pd.DataFrame(recent_samples).to_csv(ROOT/f'{NETID}_github_recent_commits.csv',sep=';',index=False)
pd.DataFrame(observations).to_csv(ROOT/f'{NETID}_github_observations.csv',sep=';',index=False)
pd.DataFrame(historical_evidence).to_csv(ROOT/f'{NETID}_github_historical_status.csv',sep=';',index=False)
pd.DataFrame(monthly_check).to_csv(ROOT/f'{NETID}_validation.csv',sep=';',index=False)
print(f'Original WoC rows: {len(raw):,}; recovered from GitHub: {len(recovered)}; analyzed: {len(df):,}; unresolved: {len(unresolved)}')
print(stats[['Project','ncommits','LongestGapLength','NumberOfGapsInTimeline','Currentstatus']].to_string(index=False))
