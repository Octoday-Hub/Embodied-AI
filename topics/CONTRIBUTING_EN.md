## Contributing Guide

If you discover a useful tool, a promising company, a valuable paper, or notice a broken link, feel free to open a [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls) or [Issue](https://github.com/Octoday-Hub/Embodied-AI/issues) directly. Every update helps the next person move faster.

### Quick Start

#### Only fixing one link?

1. Open the target file and click `Edit this file`.
2. Make your change and click `Propose changes`.
3. Submit the [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls) by following the prompts; no local fork required.

Best for:

- One or two small edits, such as a broken link, typo, or single entry update.
- GitHub web editing will create a temporary branch for you automatically, so you do not need to name a local branch.

#### Planning a larger update?

1. Fork this repository to your account.
2. Create a new branch from `main`.
3. Make your edits locally and submit a [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls).

Best for:

- Batch updates across multiple entries.
- Adding a new company, multiple papers, or a group of job postings.
- Cases where you should use the branch naming rules below so maintainers can quickly identify the scope.

#### Branch Naming

Please follow these naming rules so maintainers can quickly identify the scope:

- `update-basics-[topic]` for `00-basics.md`.
- `add-company-[company-name]` for `01-companies.md`.
- `update-jobs-[company-name]` for `02-jobs.md`.
- `update-paper-[paper-title]` for `03-papers.md`.
- `update-tools-[tool-name]` for `04-tools.md`.

If you are unsure whether to open a [PR](https://github.com/Octoday-Hub/Embodied-AI/pulls) or an [Issue](https://github.com/Octoday-Hub/Embodied-AI/issues):

- **PR**: Best for direct content edits, link fixes, or typo fixes.
- **Issue**: Best for reporting problems, sharing leads, or discussing changes first.

### Content Guidelines

Please follow the formatting guidelines below:

#### Cognitive Foundation (00-basics.md)

- Recommended books should include **title**, **author**, **publication year**, and **reason for recommendation** (optional).
- Recommended courses should include **course title**, **institution**, **link**, and **description**.

Template:

```md
| **Title** | Author | Year | Why it is useful |
| :-- | :-- | :-- | :-- |
| **Example Book** | Author Name | 2024 | One-line recommendation |
```

Course example:

```md
| **Course Title** | Institution | Description | Link |
| :-- | :-- | :-- | :-- |
| **Example Course** | Example Org | One-line course summary | [Course Link](https://example.com) |
```

#### Company List (01-companies.md)

- Provide **company name**, **official website link**, **one-sentence introduction**, **technical focus**, and **location**.
- Remain objective and neutral; summarize core business in one sentence.

Template:

```md
| **Company Name** | One-sentence introduction | Technical focus | Official Site |
| :-- | :-- | :-- | :-- |
| **Example Company** | One-line introduction | `focus-a` `focus-b` | [Official Site](https://example.com) |
```

#### Job Openings (02-jobs.md)

- Provide **job title**, **company**, **location**, **type** (full-time / internship / campus), and **application link**.
- Job postings should include a **deadline** or **last updated** date. If you find expired information, please mark it clearly.

Template:

```md
<tr>
<td rowspan="2"><strong>Example Company</strong></td>
<td>Robotics Algorithm Engineer</td>
<td>Full-time</td>
<td>Shanghai</td>
<td><a href="https://example.com/jobs/123">Apply</a></td>
</tr>
<tr>
<td>Reinforcement Learning Intern</td>
<td>Internship</td>
<td>Beijing</td>
<td><a href="https://example.com/jobs/456">Apply</a></td>
</tr>

Last updated: 2026-05-21
```

#### Paper Collection (03-papers.md)

- Provide **paper title**, **authors**, **venue / journal**, **year**, and **code link** (if available).
- Include a **one-sentence summary** of the core contribution when possible.
- Group by research direction (e.g., Manipulation, Locomotion, Navigation, etc.).

Template:

```md
- **[arXiv May 2026](https://arxiv.org/abs/2605.12345)** Example Paper Title. One sentence summarizing the core contribution. [Code](https://github.com/example/repo)
```

#### Tool Matrix (04-tools.md)

- Provide **tool name**, **type** (simulation / control / dataset, etc.), **official link**, and a **one-sentence description**.
- Indicate whether it is open-source and the main programming language.

Template:

```md
| **Tool Name** | Description | Link |
| :-- | :-- | :-- |
| **Example Tool** | One-line description | [Link](https://example.com) |
```

### Information Accuracy

- Verifiable: The information you provide should be confirmable via official websites or authoritative sources.
- Timely: Please provide the latest information for time-sensitive content such as jobs and financing updates.
- Content Authorization: Submitting a PR means you agree to publish your contribution under the same license as this repository. Please cite the source when quoting third-party content.

### Review and Merge

- Maintainers will complete an initial review within 3 business days. If changes are needed, they will leave comments for follow-up.
- After approval, the maintainers will merge the PR into the `main` branch.
- For major structural changes, such as adding new categories or modifying the directory layout, please open an Issue first to discuss it and avoid PR rejection.

### Code of Conduct

- Be friendly and respectful.
- Respect intellectual property rights.
- For business collaborations, please contact us by email instead of posting advertisements in Issues or PRs.

### Acknowledgments

Thank you to every contributor! ❤️

If you have any questions, feel free to contact: [octoday@yeah.net](mailto:octoday@yeah.net).
