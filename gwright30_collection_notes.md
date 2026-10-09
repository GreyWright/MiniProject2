# Retrieval notebook text cells

These counts refer to the original WoC retrieval only, before GitHub recovery. Author counts are distinct raw author strings.

| project_wocid | ncommits | nauthors | min_time | max_time |
| --- | --- | --- | --- | --- |
| catboost_catboost | 51141 | 1550 | 2017-07-18 05:33:21+00:00 | 2025-11-08 18:22:21+00:00 |
| humanbrainproject_fairgraph | 1793 | 14 | 2018-03-22 15:47:20+00:00 | 2025-11-03 21:58:18+00:00 |
| juliamanifolds_manifolds.jl | 8262 | 88 | 2019-06-05 18:27:27+00:00 | 2026-04-24 14:59:59+00:00 |
| mobleylab_blues | 1657 | 45 | 2016-06-28 00:20:31+00:00 | 2025-10-15 20:00:56+00:00 |
| pydata_pandas-datareader | 1750 | 203 | 2014-12-06 19:46:57+00:00 | 2025-09-24 18:22:20+00:00 |
| sancus-pma_sancus-core | 459 | 18 | 2011-03-04 20:17:50+00:00 | 2025-05-19 08:19:58+00:00 |
| shellphish_driller | 568 | 35 | 2015-06-13 06:01:25+00:00 | 2025-03-24 19:44:27+00:00 |
| threeme3_qcx-ssb | 459 | 20 | 2019-01-28 17:44:15+00:00 | 2025-10-31 21:10:28+00:00 |
| vcflib_vcflib | 1759 | 118 | 2010-09-22 23:26:17+00:00 | 2025-11-04 09:36:40+00:00 |
| vinecopulib_rvinecopulib | 1229 | 11 | 2017-03-30 18:54:11+00:00 | 2025-10-20 12:43:10+00:00 |

## GitHub observations (manually checked October 8, 2026)

I checked all ten GitHub repository pages. CatBoost and pandas-datareader showed rounded counts, so I used GitHub API calls for their exact values. The saved API snapshots also preserve branch information and latest commit timestamps.

| Project | GitHubURL | DefaultBranch | Stars | Forks | LastCommitDateUTC | ObservedOn |
| --- | --- | --- | --- | --- | --- | --- |
| juliamanifolds_manifolds.jl | https://github.com/JuliaManifolds/Manifolds.jl | master | 436 | 72 | 2026-09-30T11:06:58+00:00 | 2026-10-08 |
| pydata_pandas-datareader | https://github.com/pydata/pandas-datareader | main | 3272 | 693 | 2026-07-21T08:27:57+00:00 | 2026-10-08 |
| shellphish_driller | https://github.com/shellphish/driller | master | 984 | 163 | 2025-03-24T19:44:27+00:00 | 2026-10-08 |
| threeme3_qcx-ssb | https://github.com/threeme3/usdx | master | 861 | 263 | 2025-08-26T01:52:23+00:00 | 2026-10-08 |
| humanbrainproject_fairgraph | https://github.com/HumanBrainProject/fairgraph | master | 14 | 10 | 2026-10-06T14:00:28+00:00 | 2026-10-08 |
| sancus-pma_sancus-core | https://github.com/sancus-tee/sancus-core | master | 24 | 15 | 2025-05-19T08:19:58+00:00 | 2026-10-08 |
| vcflib_vcflib | https://github.com/vcflib/vcflib | master | 686 | 223 | 2026-10-02T09:59:30+00:00 | 2026-10-08 |
| mobleylab_blues | https://github.com/MobleyLab/blues | master | 34 | 16 | 2021-01-22T02:24:57+00:00 | 2026-10-08 |
| vinecopulib_rvinecopulib | https://github.com/vinecopulib/rvinecopulib | main | 40 | 11 | 2026-09-18T14:32:39+00:00 | 2026-10-08 |
| catboost_catboost | https://github.com/catboost/catboost | master | 9133 | 1345 | 2026-10-07T19:18:23+00:00 | 2026-10-08 |

## Collection limitations

The original retrieval returned 69,077 of 69,145 listed commits. The commit.tch lookup and commit-object fallback still left 68 missing records. A later GitHub recovery pass retrieved 36, leaving 32 unresolved. The original and supplemented datasets are both preserved. Installation of python-woc 0.4.1 failed under the Colab Python 3.13 runtime, so the official pure-Python remote.py and base.py modules were loaded directly without the unused local database extensions. Collection used batches of ten with one-second pauses and a persistent SQLite checkpoint.

## Historical activity status for the assignment

The professor specifies a September 30, 2025 reference date. To avoid using a 2026 commit to infer 2025 activity, I checked the latest commit dated on or before September 30, 2025 on each saved GitHub default branch. I classified a project as Active if that commit was on or after April 1, 2025, and Inactive otherwise. The individual SHA values, UTC dates, links, and API query URLs are saved in `gwright30_github_historical_status.csv`. This is separate from the stars, forks, and latest commits I checked in October 2026.

The two inactive projects are shellphish/driller and MobleyLab/blues. The other eight were active during the specified 2025 window. GitHub's currently reachable default-branch history cannot prove what all branch tips looked like in September 2025.
