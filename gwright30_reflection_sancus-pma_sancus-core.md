# sancus-pma_sancus-core

## Reflection

Sancus-core had one of the more irregular timelines I looked at. There were only 459 commits in the data, but fourteen different gaps lasted at least three months. The longest ran from June 2023 through November 2024, or 18 months. With that many stops and starts, I don't think it makes sense to describe the project as steadily active.

The reason the work picked up again is much clearer here than in most of the other projects. The first commit after the gap changes the cryptographic state machine so that verification takes constant time, and GitHub issue #27 describes the timing-side-channel problem. PR #33 connects directly to that fix. That's strong evidence of what brought someone back to the code.

Ruben Van Dijck authored the security change, and Jo Van Bulck also contributed afterward on CI maintenance. Jo had appeared before the gap too, so it wasn't an entirely different group replacing the original contributors.

The part I still couldn't explain is why the project stopped for 18 months before the fix. It could fit an intermittent research or maintenance schedule, but I didn't find a direct explanation. There are only six commits after the gap in this dataset, so even with a clear security-driven restart, I can't say it had returned to regular development.

## Commit activity and evidence

**Analyzed records:** 459 commits, 18 distinct author strings (2011-03-04 to 2025-05-19).
**Activity pattern:** irregular. **Gaps of at least three months:** 14.
**Longest gap:** 2023-06 through 2024-11 (18 zero-commit months); 6 commits afterward.

**My best explanation for the gap:** The project had worked on DMA attacks and tests before the gap, and its history is already intermittent. I couldn't find evidence establishing why the 18-month pause happened; the older timing issue gives context, not an explanation for the silence.

**Recovery:** Yes. The first returning commit changes the crypto state machine to make tag verification constant-time. PR #33 and issue #27 tie that work to an identified timing side channel.

**Contributors after the gap:** Ruben Van Dijck led the post-gap security work, and Jo Van Bulck returned for CI maintenance. Jo also appears before the gap, so there was at least some contributor continuity.

**Themes before the gap:** Other, Feature development. **After:** Security patches, Other.

## Boundary-commit evidence

| Sample | UTC date | Author | Commit | Message |
|---|---|---|---|---|
| Before | 2022-04-01 | Jo Van Bulck | [8f91e9d0](https://github.com/sancus-tee/sancus-core/commit/8f91e9d017e53cd9f99484cda808ba618f780caf) | Initial PoC setup for OS-level Nemesis SW defense. |
| Before | 2022-05-24 | Jo Van Bulck | [f909290e](https://github.com/sancus-tee/sancus-core/commit/f909290eba638ac6f6904a36ec9e31e39bb9a8eb) | Trigger CI re-run and add cron job. |
| Before | 2022-05-24 | Jo Van Bulck | [bf89c0b8](https://github.com/sancus-tee/sancus-core/commit/bf89c0b81ef142c5434037b79b6513226e11e315) | Merge branch 'mitigations' of github.com:martonbognar/sancus-core-gap into mitigations |
| Before | 2022-05-24 | marton bognar | [8df6f461](https://github.com/sancus-tee/sancus-core/commit/8df6f4610e9da7595326c6f8943eba154be4efab) | Merge bf89c0b81ef142c5434037b79b6513226e11e315 into 7c7d7fa9360439360d1eff0d26135c3d93a4b846 |
| Before | 2022-10-17 | Jo Van Bulck | [09adaef9](https://github.com/sancus-tee/sancus-core/commit/09adaef918ea54fac8eeb6c5bac40b9104c138f0) | Supress warnings in recent verilator. |
| Before | 2022-10-17 | Jo Van Bulck | [c3a8b7af](https://github.com/sancus-tee/sancus-core/commit/c3a8b7af7d8574b2387870e55decc0472a7d197f) | Fix missing timescale error option on Ubuntu < 22.04. |
| Before | 2022-10-27 | marton bognar | [79958d42](https://github.com/sancus-tee/sancus-core/commit/79958d426c65ebb026531e284949f8828af36059) | Parameterize the capture trace length of the DMA peripheral |
| Before | 2023-04-17 | marton bognar | [bd2e2dfa](https://github.com/sancus-tee/sancus-core/commit/bd2e2dfa6b49565f79abd66aebc0a69f1369fa80) | Add test case to demonstrate a DMA-based covert channel |
| Before | 2023-05-09 | Jo Van Bulck | [d83a5207](https://github.com/sancus-tee/sancus-core/commit/d83a5207dc5b079847dba39ac17e98fcb4bc088f) | Merge pull request #32 from sancus-tee/dma-attack |
| Before | 2023-05-09 | Fritz Alder | [7f7ef7f6](https://github.com/sancus-tee/sancus-core/commit/7f7ef7f689eb04114d1e28590c1cbc01166c4d26) | Merge 1802027aa3a6721d3e9d1527a104dc73d18d9c06 into d83a5207dc5b079847dba39ac17e98fcb4bc088f |
| After | 2024-12-21 | Ruben Van Dijck | [d71b04dc](https://github.com/sancus-tee/sancus-core/commit/d71b04dcefd007907f3da6e6e3aec0fe136c6835) | Changes to the crypto unit state machine: added register ensuring cst time. |
| After | 2025-05-11 | Ruben Van Dijck | [a5c762cb](https://github.com/sancus-tee/sancus-core/commit/a5c762cb761ffaa8ebf14fc60b9da19f1a4dff05) | change fsm to mitigate enable timing leak |
| After | 2025-05-12 | Jo Van Bulck | [3f6d12d0](https://github.com/sancus-tee/sancus-core/commit/3f6d12d032b615a2935eaa42275bd93ad0c4c2a9) | CI: move to ubuntu 22.04 |
| After | 2025-05-18 | Ruben Van Dijck | [385b8be7](https://github.com/sancus-tee/sancus-core/commit/385b8be7ea5602d4af7ce2be1c5e253676bca248) | ci: trigger tests |
| After | 2025-05-19 | Ruben Van Dijck | [976636ec](https://github.com/sancus-tee/sancus-core/commit/976636ecaac14604c31cb314e17c6dab9e6d524d) | Merge branch 'sancus-tee:master' into unwrap-timing-fix |
| After | 2025-05-19 | Ruben Van Dijck | [b6b53bb3](https://github.com/sancus-tee/sancus-core/commit/b6b53bb3c2c38b079d1c8210ab4940f0af77a6fb) | Changes to the crypto unit state machine: added register ensuring constant-time execution (#33) |

## GitHub status and recent activity

The GitHub default branch I checked was `master` of [sancus-tee/sancus-core](https://github.com/sancus-tee/sancus-core). Its latest commit is [b6b53bb3](https://github.com/sancus-tee/sancus-core/commit/b6b53bb3c2c38b079d1c8210ab4940f0af77a6fb), dated 2025-05-19T08:19:58+00:00. For the September 30, 2025 reference date, the latest commit found on that branch by then was [b6b53bb3](https://github.com/sancus-tee/sancus-core/commit/b6b53bb3c2c38b079d1c8210ab4940f0af77a6fb) (committer date 2025-05-19T08:19:58+00:00). That makes its historical status **Active** using the April 1–September 30, 2025 window. Separately, the most recent October 2026 observation gives **Inactive** for the six months ending October 8, 2026. These are default-branch commit-history checks, not a claim about every branch or fork.

The recent-ten themes are **Security patches:Bug fixes**. The complete messages and links are in `gwright30_github_recent_commits.csv`.

## Limits and supporting sources

No commits from the supplied retrieval list remain unresolved for this project.
Author counts represent recorded author strings, not necessarily distinct people. The WoC timeline and the GitHub default branch may cover different histories; author timestamps and merge dates can also differ.

- https://github.com/sancus-tee/sancus-core/issues/27
- https://github.com/sancus-tee/sancus-core/pull/33
