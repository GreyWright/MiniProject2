# MiniProject2 — gwright30

This repository contains the collection notebook, analysis notebook, data, graphs, and interpretations of the collected project histories. The original WoC collection is preserved in `sources/gwright30_project_summary.csv`. The root summary adds 36 GitHub-recovered records, with provenance in `gwright30_recovered_commits.csv`. There are 69,113 analyzed project-commit rows and 32 unresolved records. No missing messages or timestamps were fabricated.

## Notebooks and data sources

1. The retrieval notebook is included as `gwright30.ipynb`. The ten GitHub repository pages were manually checked on October 8, 2026. GitHub rounded some displayed counts for CatBoost and pandas-datareader, so API calls supplied their exact figures. GitHub API snapshots preserve the recorded values and default-branch details for reproducibility.
2. Review `gwright30_vis.ipynb`, the ten plots, and the ten reflection files. Run the visualization notebook from this folder with pandas, matplotlib, and a Jupyter kernel, or upload a ZIP of the `gwright30_MP2` folder in Google Colab. `python generate_analysis.py` reproduces the generated CSVs, plots, and reflections from the bundled source snapshots.
3. The assignment asks for GitHub values for all ten projects. The retrieval notebook includes the checked GitHub observations and the original WoC collection table. The recorded GitHub values are as of October 8, 2026; later changes to counts or dates should be identified as new observations, not silently substituted.
4. The student deliverables belong alongside the course starter files in the MiniProject2 repository. Follow Canvas for the submission link. The assignment README does not specify a pull request.

## Definitions and exceptions

- Time is the commit author's Unix timestamp, converted to UTC. GitHub's latest default-branch commit date uses the committer timestamp. These can differ.
- Each project's timeline begins at its first observed commit month and ends at its last observed commit month. It includes all intervening zero months, but no leading/trailing inactivity beyond those endpoints.
- Longest gap means the longest run of complete zero-commit months. Ties select the earliest run. NumberOfGapsInTimeline counts all runs of at least three months. NumCommitsAfterLastGap follows the assignment's definition: commits after LongestGapEnd, not after the chronologically last gap.
- Projects without a gap have length/count-after-gap 0 and N/A gap boundaries/themes/recovery. No artificial pre/post rows are inserted for them.
- The gap sample is the last ten commits before and first ten after the longest gap, or all available if fewer. Driller has one post-gap commit and Sancus has six. A nonexistent second theme is N/A.
- Author counts count distinct raw author strings. Alias/email reconciliation was not performed. Different SHA values remain separate even when messages are identical. Merge records are retained.
- Theme labels and trajectory classes are qualitative readings, stored in sources/interpretations.json. Other includes merges, CI configuration, refactoring, tests, and vague messages when no more specific theme is justified. They are not a keyword classifier or a causal test.
- README says WoC stops in January 2025, but the supplied records actually extend as late as April 24, 2026. Coverage varies by project. The data are not silently truncated to the outdated stated cutoff.
- `Currentstatus` is evaluated **as of September 30, 2025**: Active if the last default-branch commit on or before that date was on or after April 1, 2025; otherwise Inactive. The exact commit dates, SHA values, links, and GitHub API queries are recorded in `gwright30_github_historical_status.csv` and `sources/github_historical_2025.json`. These queries inspect commit history currently reachable from the recorded default branch; they do not establish all branch tips or repository settings as they existed in 2025. `StatusAsOf2026_10_08` remains a separate six-month check based on the original October 8, 2026 observations.
- QCX-SSB now resolves to threeme3/usdx; sancus-pma/sancus-core resolves to sancus-tee/sancus-core. Assigned WoC IDs and filenames remain unchanged.
- BLUES and uSDX have WoC author-time histories that differ from the inspected default-branch head; the uSDX head was authored in June 2024 but committed in August 2025. Do not interpret this as a proven main-branch revival. The corpus can include branch/PR-related history.
- All 68 missing WoC IDs were checked against GitHub. Thirty-six were recovered and 32 remain unavailable. Restoring the 36 did not change the longest-gap boundaries. Remaining missing records could still alter month counts or gaps; they are explicitly retained in the missing-record CSV.
- Hypothesized reasons are qualified when evidence is insufficient. A returning commit proves renewed recorded activity, not sustained recovery or a particular funding/staffing explanation.

## File layout

This folder contains the requested summary/stats/gap CSVs, ten monthly CSVs, ten 300-DPI plots, ten reflections, and the visualization notebook. Supplemental CSVs document recovery, validation, recent GitHub evidence, GitHub observations, and dated historical-status evidence. `sources/` preserves raw collection and API snapshots for reproducibility. `generate_analysis.py` performs the calculations. Preserve the folder layout when running it.

## Packaging note

The written interpretations and reflections were reviewed alongside the supporting commit evidence. Numerical project data, analysis rules, and plot settings are preserved. The original starter notebooks are already maintained separately in the repository.
