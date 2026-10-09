# mobleylab_blues

## Reflection

BLUES had 1,658 commits in the collected data, but its activity declined over time. There were two gaps lasting at least three months, with the longest running from August 2022 through January 2025. That's 30 straight months without a recorded commit, which is a pretty significant break.

What made this one harder to figure out was that WoC and GitHub didn't completely agree. WoC showed activity picking back up in 2025, but the main GitHub branch hadn't been updated since January 2021. There was also a pull request from 2022 that was never merged. So even though there were newer commits, I don't think there's enough evidence to say the original project actually recovered.

Looking at the commit messages, the work before the gap included documentation changes, installation instructions, and some development involving RDKit. After the gap, the commits focused more on updating outdated dependencies, fixing compatibility issues, and testing. Most of that later work came from Steven Ayoub, whereas the earlier commits involved different contributors.

My best guess is that the project lost active maintenance or that contributions stopped getting integrated into the main branch. I couldn't find anything that definitively explained why. The later commits show that someone was trying to get the software working again, but that doesn't necessarily mean the project itself was revived.

## Commit activity and evidence

**Analyzed records:** 1,658 commits, 45 distinct author strings (2016-06-28 to 2025-10-15).
**Activity pattern:** declining. **Gaps of at least three months:** 2.
**Longest gap:** 2022-08 through 2025-01 (30 zero-commit months); 35 commits afterward.

**My best explanation for the gap:** The activity was already declining, and a 2022 RDKit contribution in PR #175 was still unmerged in the available GitHub record. Maintenance or integration may have slowed down, but I can't pin down the actual reason for the gap.

**Recovery:** Partially: collected-history activity only. Commits in February and March 2025 add tests, replace deprecated simtk imports, and update CI. They show someone trying to maintain the code, but they don't show those changes reaching the GitHub default branch.

**Contributors after the gap:** Steven Ayoub wrote the first ten post-gap commits in the sample. The pre-gap sample includes Yunhui Ge, sgill2, and Ke, so the people driving the sampled work changed.

**Themes before the gap:** Documentation updates, Other. **After:** Dependency updates, Other.

## Boundary-commit evidence

| Sample | UTC date | Author | Commit | Message |
|---|---|---|---|---|
| Before | 2021-01-21 | Yunhui Ge | [7a7cf310](https://github.com/MobleyLab/blues/commit/7a7cf310bc867b9bfb01dbbe5904a453c2d645a4) | Remove several unnecessary lines |
| Before | 2021-01-21 | Yunhui Ge | [90c4bfa7](https://github.com/MobleyLab/blues/commit/90c4bfa7ddd4ef3ea9f5110889222bdbec7c5c5f) | Update BLUES version |
| Before | 2021-01-21 | yunhuige | [c38bd013](https://github.com/MobleyLab/blues/commit/c38bd013c74810dd0c23209cd337e1aca8c58d43) | necessary to merge |
| Before | 2021-01-21 | Yunhui Ge | [b24b2618](https://github.com/MobleyLab/blues/commit/b24b2618ad708f91aa234b16703ea36671d24a29) | Updated conda installation instructions |
| Before | 2021-01-22 | Yunhui Ge | [fa17dcd9](https://github.com/MobleyLab/blues/commit/fa17dcd9ebf001b24bb90efc41c33bb4b07a7088) | Updated conda installation instructions |
| Before | 2021-01-22 | Yunhui Ge | [d2ef3647](https://github.com/MobleyLab/blues/commit/d2ef364749d4cbd7554add3ee61a5e90588760e1) | Updated conda installation instructions (#171) |
| Before | 2021-02-22 | sgill2 | [93fe44a8](https://github.com/MobleyLab/blues/commit/93fe44a8ba8683f0a6c031c9f2ceafb85a8de5db) | Merge 28c60abdf4a7cdfd9e7235c106afccf8f5d28a18 into d2ef364749d4cbd7554add3ee61a5e90588760e1 |
| Before | 2022-07-11 | Ke | [b3a23141](https://github.com/MobleyLab/blues/commit/b3a23141f7c5617d84ae17b480748219b86b631f) | Merge branch 'TorsionalMove_New' |
| Before | 2022-07-11 | Ke | [68b889ba](https://github.com/MobleyLab/blues/commit/68b889ba25e91ce15991fa3a55454ae177260de2) | Use rdkit to rotate  molecule |
| Before | 2022-07-11 | Ke | [465e21cf](https://github.com/MobleyLab/blues/commit/465e21cfbf20645a53ac596969cc9e1d19a74c0d) | Merge 68b889ba25e91ce15991fa3a55454ae177260de2 into d2ef364749d4cbd7554add3ee61a5e90588760e1 |
| After | 2025-02-28 | steven ayoub | [14758fc5](https://github.com/MobleyLab/blues/commit/14758fc5d6584588c0eb72a3832f0743f1dc83a1) | test_water_translation_after test function to check whether the water is outside the given region or not |
| After | 2025-03-22 | steven ayoub | [c92e6058](https://github.com/MobleyLab/blues/commit/c92e6058b3cfe1c5ea798304c7a23f475350e65f) | update syntax 'simtk' is deprecated just use 'openmm' |
| After | 2025-03-22 | steven ayoub | [6cc273ac](https://github.com/MobleyLab/blues/commit/6cc273ac2ae8b3b3ba25cd23fdc54bd3be36822c) | Updated deprecated libraries and made update in selection of PARMED atoms |
| After | 2025-03-22 | steven ayoub | [b56919d6](https://github.com/MobleyLab/blues/commit/b56919d61320a398b2f19fe4d52bc550d8258ebc) | Remove import simtk since its deprecated and replaced with openmm |
| After | 2025-03-22 | steven ayoub | [1437a496](https://github.com/MobleyLab/blues/commit/1437a4963c2c2718d64fd5f950f745eda77e708a) | It runs multiple BLUES simulations on a propane system to assure that the engine correctly samples the dihedral conformations of the propane molecule—in the trans and gauche states, specifically. |
| After | 2025-03-22 | steven ayoub | [3bdd4fd2](https://github.com/MobleyLab/blues/commit/3bdd4fd2717bdf9e790b6dc68c285f9a594aa0e7) | Tests are not complete running into errors |
| After | 2025-03-22 | steven ayoub | [1407b7bb](https://github.com/MobleyLab/blues/commit/1407b7bbe47b85a7de0f051f092ec716cefab1db) | Created GitHub Action that runs tests on push and pull requests |
| After | 2025-03-22 | steven ayoub | [9affa766](https://github.com/MobleyLab/blues/commit/9affa7666ef83c60a17721bf90ab13a483742baa) | Created GitHub Action that runs tests on push and pull requests |
| After | 2025-03-22 | steven ayoub | [4dad9846](https://github.com/MobleyLab/blues/commit/4dad9846e2965949045bb37af6d499b502efd054) | merge conflicts run CI on any branch |
| After | 2025-03-22 | steven ayoub | [6e60aabf](https://github.com/MobleyLab/blues/commit/6e60aabfab391b22f5977afcddc5e0b4cd0dc97c) | Install openeye toolkit |

## GitHub status and recent activity

The GitHub default branch I checked was `master` of [MobleyLab/blues](https://github.com/MobleyLab/blues). Its latest commit is [d2ef3647](https://github.com/MobleyLab/blues/commit/d2ef364749d4cbd7554add3ee61a5e90588760e1), dated 2021-01-22T02:24:57+00:00. For the September 30, 2025 reference date, the latest commit found on that branch by then was [d2ef3647](https://github.com/MobleyLab/blues/commit/d2ef364749d4cbd7554add3ee61a5e90588760e1) (committer date 2021-01-22T02:24:57+00:00). That makes its historical status **Inactive** using the April 1–September 30, 2025 window. Separately, the most recent October 2026 observation gives **Inactive** for the six months ending October 8, 2026. These are default-branch commit-history checks, not a claim about every branch or fork.

The recent-ten themes are **Documentation updates:Bug fixes**. The complete messages and links are in `gwright30_github_recent_commits.csv`.

## Limits and supporting sources

1 listed commits remain unavailable for this project, so a missing record could affect a gap measurement.
Author counts represent recorded author strings, not necessarily distinct people. The WoC timeline and the GitHub default branch may cover different histories; author timestamps and merge dates can also differ.

- https://github.com/MobleyLab/blues/pull/175
- https://github.com/MobleyLab/blues/pull/171
- https://github.com/MobleyLab/blues/commits/
