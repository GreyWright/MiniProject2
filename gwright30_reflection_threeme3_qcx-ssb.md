# threeme3_qcx-ssb

## Reflection

QCX-SSB was a little messy to trace because the assigned WoC project name no longer matches the repository name on GitHub. It now redirects to threeme3/usdx. I found 460 commits in the collected history and six gaps of at least three months, with the longest lasting nine months from November 2022 through July 2023. Overall, the activity looks like a decline from earlier development into occasional updates.

The two commits that end the longest gap both modify usdx.ino, but their messages don't explain what was actually being changed. That's a problem when the assignment asks why a project started up again. I can see that commits happened, but I don't think those messages are enough to build a convincing story about why.

There is better evidence for later maintenance. GitHub PR #86 describes an I2C fix, and there were also email and documentation changes afterward. The first post-gap author was Davi Lopes Dos Santos, with other names appearing later in the sample. I wouldn't assume every different label is a different person without checking identities more carefully.

The GitHub dates add another complication: the latest default-branch commit was authored in June 2024 but committed in August 2025. Since the WoC graph uses author timestamps, I can't treat those two dates as interchangeable. My best interpretation is sporadic maintenance rather than a clear revival, and I couldn't find a definite cause for the original gap.

## Commit activity and evidence

**Analyzed records:** 460 commits, 20 distinct author strings (2019-01-28 to 2025-10-31).
**Activity pattern:** declining. **Gaps of at least three months:** 6.
**Longest gap:** 2022-11 through 2023-07 (9 zero-commit months); 38 commits afterward.

**My best explanation for the gap:** The project was already down to sporadic documentation and compatibility changes after its earlier activity. Occasional hobby-project maintenance is plausible, but nothing I found clearly says why the nine-month pause happened.

**Recovery:** Partially: intermittent collected-history activity. Two August 2023 commits update usdx.ino without explaining much. Later message edits and the I2C fix in PR #86 show more maintenance, but not why those first changes restarted.

**Contributors after the gap:** Davi Lopes Dos Santos wrote the first post-gap commits; threeme3 and sq5bpf appear later in that sample. The earlier sample has guido and other labels, but those labels alone aren't proof of different people.

**Themes before the gap:** Documentation updates, Bug fixes. **After:** Other, Bug fixes.

## Boundary-commit evidence

| Sample | UTC date | Author | Commit | Message |
|---|---|---|---|---|
| Before | 2021-10-30 | John Zhong | [cdfbf039](https://github.com/threeme3/usdx/commit/cdfbf03908484f0af9cd95f4406bb8f6b3c07412) | Merge 3b032f35c6a647e6be5f5ac3d7300f4fc194dae0 into 4fc60f5c8d74ba7364cf891e008b920ab5e5c82d |
| Before | 2021-11-17 | guido | [8be911fb](https://github.com/threeme3/usdx/commit/8be911fb38413a2b7ad678bd06e01e024dbee839) | Update README. |
| Before | 2021-11-17 | guido | [ee0bf454](https://github.com/threeme3/usdx/commit/ee0bf454fddf20cd0426a5cb4dbcd332c7ace357) | Add reference to master branch. |
| Before | 2021-11-17 | guido | [7245a135](https://github.com/threeme3/usdx/commit/7245a135b156b2322c80324d8db9813f060fbbf5) | Change README. |
| Before | 2021-11-18 | guido | [7aa3589a](https://github.com/threeme3/usdx/commit/7aa3589abe3017ebe9cbf009dc5dd8564c40de38) | Change project name. |
| Before | 2021-11-18 | guido | [c3114c99](https://github.com/threeme3/usdx/commit/c3114c99f089c01c6c8895f18483a02b92eb571c) | Minor changes. |
| Before | 2022-03-22 | guido | [63fb397e](https://github.com/threeme3/usdx/commit/63fb397ee68de7a33a693c7bd5b4f0144c0dfb51) | Fix CW key-down/key-up waveform issue (TNX Dave, M0JTS). Fix index key-up waveform. |
| Before | 2022-05-01 | UnknownRider | [8987e3e3](https://github.com/threeme3/usdx/commit/8987e3e3e30fcf124c6149f562275d480f5ad196) | Initial submittal |
| Before | 2022-05-02 | John Zhong | [369515cb](https://github.com/threeme3/usdx/commit/369515cb405fcfa3c90dc18fcb7b650a4298775f) | Merge pull request #2 from plainpylut/feature-rx-improved |
| Before | 2022-10-31 | threeme3 | [a13d7d34](https://github.com/threeme3/usdx/commit/a13d7d34073017b30b2a5c22ef299ae5e2332000) | Fix for Arduino 2.0 IDE |
| After | 2023-08-18 | Davi Lopes Dos Santos | [fec6ecca](https://github.com/threeme3/usdx/commit/fec6eccadb66643fffa796666efdcfd10fe7f74e) | Update usdx.ino |
| After | 2023-08-18 | Davi Lopes Dos Santos | [87873464](https://github.com/threeme3/usdx/commit/87873464b7d3e9a9fade70d799b8141f850ec744) | Update usdx.ino |
| After | 2024-06-29 | threeme3 | [618a1277](https://github.com/threeme3/usdx/commit/618a12771a43688ae9dba6069b8bed75485dadc9) | Email change |
| After | 2024-06-29 | threeme3 | [87599cd2](https://github.com/threeme3/usdx/commit/87599cd29a629b1e7450445c486a612d7233e341) | Email change |
| After | 2024-06-29 | threeme3 | [f49d227a](https://github.com/threeme3/usdx/commit/f49d227aff14ce9365f22f9f59e9d8a2b469711f) | Email change |
| After | 2024-11-11 | sq5bpf | [5be78bb6](https://github.com/threeme3/usdx/commit/5be78bb63a264d0e325a563661f1597c450f76d7) | fix RecvByte() for multi-byte i2c reads --sq5bpf |
| After | 2024-11-12 | sq5bpf | [70ba6f2e](https://github.com/threeme3/usdx/commit/70ba6f2e7a9f2c7380586b1261a0d41470640f26) | split settings into a separate file |
| After | 2024-11-12 | threeme3 | [a4a94ce4](https://github.com/threeme3/usdx/commit/a4a94ce4c037d99f6432a7fb37c32b34138d1468) | Merge pull request #86 from sq5bpf/master |
| After | 2024-11-12 | sq5bpf | [51f454ca](https://github.com/threeme3/usdx/commit/51f454ca5e0b54609caba81591ba81d7be64df92) | change 27MHz clock to be more spot-on, move CW message definition to usdx_settings.ino |
| After | 2024-11-12 | sq5bpf | [db54605a](https://github.com/threeme3/usdx/commit/db54605aa086ce9494d6dc03c84c12aa29037ddd) | Merge pull request #1 from threeme3/master |

## GitHub status and recent activity

The GitHub default branch I checked was `master` of [threeme3/usdx](https://github.com/threeme3/usdx). Its latest commit is [f49d227a](https://github.com/threeme3/usdx/commit/f49d227aff14ce9365f22f9f59e9d8a2b469711f), dated 2025-08-26T01:52:23+00:00. For the September 30, 2025 reference date, the latest commit found on that branch by then was [f49d227a](https://github.com/threeme3/usdx/commit/f49d227aff14ce9365f22f9f59e9d8a2b469711f) (committer date 2025-08-26T01:52:23+00:00). That makes its historical status **Active** using the April 1–September 30, 2025 window. Separately, the most recent October 2026 observation gives **Inactive** for the six months ending October 8, 2026. These are default-branch commit-history checks, not a claim about every branch or fork.

The recent-ten themes are **Other:Documentation updates**. The complete messages and links are in `gwright30_github_recent_commits.csv`.

## Limits and supporting sources

1 listed commits remain unavailable for this project, so a missing record could affect a gap measurement.
Author counts represent recorded author strings, not necessarily distinct people. The WoC timeline and the GitHub default branch may cover different histories; author timestamps and merge dates can also differ.

- https://github.com/threeme3/usdx/pull/86
- https://github.com/threeme3/usdx/commits/
