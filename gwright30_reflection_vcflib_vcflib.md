# vcflib_vcflib

## Reflection

vcflib has 1,763 commits in the collected data, and its timeline is all over the place compared with a steady development pattern. The longest gap lasted seven months, from June through December 2021. There were three gaps of at least three months overall, but the huge increase in commits during 2022 was what stood out most to me. That's why I classified the pattern as irregular.

The first commits after the long gap fix an issue with installing man pages. I checked GitHub PR #321, and it was merged in January 2022. More dependency and bug fixes came after that, so I think there's enough evidence to say people actually returned to maintaining the project.

Alexander Regueiro authored the first fix after the gap. Pjotr Prins, who appeared frequently before it, also returned, along with other contributors such as Tim Massingham and Mathias Schmitt. So I wouldn't describe the recovery as one entirely new group replacing another.

The harder part was figuring out why the project had been quiet for seven months. Before the pause there were installation, test, and documentation changes, which could fit a maintenance lull, but that's not proof of the cause. I also kept commits with similar messages when they had different SHA values, since they were distinct records in the collected history.

## Commit activity and evidence

**Analyzed records:** 1,763 commits, 118 distinct author strings (2010-09-22 to 2025-11-04).
**Activity pattern:** irregular. **Gaps of at least three months:** 3.
**Longest gap:** 2021-06 through 2021-12 (7 zero-commit months); 654 commits afterward.

**My best explanation for the gap:** The pre-gap commits were mostly installation, tests, and documentation work, so a maintenance lull is possible. There isn't enough evidence to say why no commits appeared from June through December 2021.

**Recovery:** Yes. The January 2022 commits fix man-page installation, and PR #321 was merged. More dependency and bug fixes came afterward, so the restart shows continued development rather than one isolated change.

**Contributors after the gap:** Alexander Regueiro wrote the first post-gap fix. Pjotr Prins, who had been active before the gap, returned as well; Tim Massingham and Mathias Schmitt also appear afterward.

**Themes before the gap:** Documentation updates, Bug fixes. **After:** Bug fixes, Dependency updates.

## Boundary-commit evidence

| Sample | UTC date | Author | Commit | Message |
|---|---|---|---|---|
| Before | 2021-02-16 | Pjotr Prins | [6a02b471](https://github.com/vcflib/vcflib/commit/6a02b4712f65e6d85aedbb724a6031feeacaab34) | Also install scripts |
| Before | 2021-02-16 | Pjotr Prins | [a5995def](https://github.com/vcflib/vcflib/commit/a5995def667c0caabd5903672619f0ea54c4f159) | Also install scripts |
| Before | 2021-02-17 | Pjotr Prins | [288ff56e](https://github.com/vcflib/vcflib/commit/288ff56ed5789d6ea8c0f42fb4a05ba1295356ec) | Fix badges |
| Before | 2021-02-17 | Pjotr Prins | [507b35ed](https://github.com/vcflib/vcflib/commit/507b35ed81c7d17d0e4af5a4efbb71ac2ce1481f) | Fix badges |
| Before | 2021-02-17 | Pjotr Prins | [a14f03ee](https://github.com/vcflib/vcflib/commit/a14f03ee8ca832cba94fd89f609e9ad3cef7b709) | Fixed failing test |
| Before | 2021-02-17 | Pjotr Prins | [f77c2a9a](https://github.com/vcflib/vcflib/commit/f77c2a9a1bddff42563eaef09b12000ae274968e) | Fixed failing test |
| Before | 2021-02-17 | Pjotr Prins | [83e6414f](https://github.com/vcflib/vcflib/commit/83e6414fe913433dc176b558a75a27a25cc23ea5) | Fix badge |
| Before | 2021-02-17 | Pjotr Prins | [b836c2b3](https://github.com/vcflib/vcflib/commit/b836c2b3e35e3314ac202ac285fad020693b2763) | Fix badge |
| Before | 2021-05-27 | Pjotr Prins | [a549707d](https://github.com/vcflib/vcflib/commit/a549707d8e33006ed89c46ca7fbda007123418ab) | README: add bibtex reference |
| Before | 2021-05-27 | Pjotr Prins | [f92f3d95](https://github.com/vcflib/vcflib/commit/f92f3d9531f7248c629127d270e337c610079a46) | README: add bibtex reference |
| After | 2022-01-12 | Alexander Regueiro | [0f03b0b6](https://github.com/vcflib/vcflib/commit/0f03b0b628300c8008a8411431ef26ecdce20bad) | Fix man page installation |
| After | 2022-01-12 | Alexander Regueiro | [c648b642](https://github.com/vcflib/vcflib/commit/c648b642fab2cfb3f1c25d29efef9d819700876b) | Fix man page installation |
| After | 2022-01-17 | Pjotr Prins | [71ffb341](https://github.com/vcflib/vcflib/commit/71ffb34114d600bf95816ed0098c3ccb64d44874) | Merge pull request #321 from alexreg/patch-1 |
| After | 2022-01-17 | Pjotr Prins | [d13c16d2](https://github.com/vcflib/vcflib/commit/d13c16d214ef1a9d819bd1b1285aced4711308af) | README: change to matrix badge |
| After | 2022-01-17 | Pjotr Prins | [e0cb656c](https://github.com/vcflib/vcflib/commit/e0cb656cb0e224dc078ba1e06079a88a5ea7b6ab) | README: change to matrix badge |
| After | 2022-01-17 | Tim Massingham | [186d4f7c](https://github.com/vcflib/vcflib/commit/186d4f7ceb1bd56572c978c597b6ba5a12ebf228) | Bump intervaltree dependency |
| After | 2022-01-17 | Tim Massingham | [fe906dee](https://github.com/vcflib/vcflib/commit/fe906dee7080e8e44338af803fabfef3ffbff785) | Bump intervaltree dependency |
| After | 2022-01-17 | Mathias Schmitt | [1d30fd5e](https://github.com/vcflib/vcflib/commit/1d30fd5eff3fdbaac570ebb70ffe57e19e4d5ed9) | vcfflatten: fix segfault when no 'AF' field is present (#47). |
| After | 2022-01-17 | Mathias Schmitt | [f2ed5380](https://github.com/vcflib/vcflib/commit/f2ed53809b5be801a78b3e2e01398a8bc0a2945b) | vcfflatten: fix segfault when no 'AF' field is present (#47). |
| After | 2022-01-18 | Pjotr Prins | [bdfb024b](https://github.com/vcflib/vcflib/commit/bdfb024b9f440b113bcd81a263aae1c2e95c0251) | Merge pull request #322 from timmassingham/issue320 |

## GitHub status and recent activity

The GitHub default branch I checked was `master` of [vcflib/vcflib](https://github.com/vcflib/vcflib). Its latest commit is [6f16fb86](https://github.com/vcflib/vcflib/commit/6f16fb86da8ddf490702772d954c66e88331ba37), dated 2026-10-02T09:59:30+00:00. For the September 30, 2025 reference date, the latest commit found on that branch by then was [885afe1a](https://github.com/vcflib/vcflib/commit/885afe1abb9c7ec3e72696bd7dbf796e75e1daa8) (committer date 2025-07-06T07:55:54+00:00). That makes its historical status **Active** using the April 1–September 30, 2025 window. Separately, the most recent October 2026 observation gives **Active** for the six months ending October 8, 2026. These are default-branch commit-history checks, not a claim about every branch or fork.

The recent-ten themes are **Bug fixes:Feature development**. The complete messages and links are in `gwright30_github_recent_commits.csv`.

## Limits and supporting sources

1 listed commits remain unavailable for this project, so a missing record could affect a gap measurement.
Author counts represent recorded author strings, not necessarily distinct people. The WoC timeline and the GitHub default branch may cover different histories; author timestamps and merge dates can also differ.

- https://github.com/vcflib/vcflib/pull/321
- https://github.com/vcflib/vcflib/commits/
