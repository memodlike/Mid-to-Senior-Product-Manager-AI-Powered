# Mid to Senior Product Manager (AI-Powered)

Umbrella project under `/Users/memodlike/Developer`. Shared engineering instructions live in the parent
`Developer/CLAUDE.md` (local only).

## Sub-projects (each its own git repo; read its own instructions first)
- `Portfolio/` — Product Masters portfolio site (formerly `RFM-Portfolio`; GitHub remote `memodlike/portfolio`).
- `StudyReminders/` — daily launchd job `kz.productmasters.reminders` (plist copy in the folder, live copy in `~/Library/LaunchAgents/`).
- `DZ_week2_hard/` — week 2 homework.

## Where homework is published (never create new repos for a week)
Every new week's solution goes to ALL of these, kept in sync:
1. Course repo `memodlike/Mid-to-Senior-Product-Manager-AI-Powered` = this umbrella folder's own git:
   one folder per assignment, e.g. `Week4_hard_FinanceApp/` (README = solution, data + check script).
2. Portfolio on Vercel: `Portfolio/` → `memodlike/portfolio`, Vercel project `memodlike-portfolio`
   (deploy `dist/`). Add a week section with anchor `#w<week>-l<level>` (e.g. `#w4-l3`) and a link to the course-repo folder.
3. Mirror on GitHub Pages: `memodlike/portfolio-site` (`index.html` = copy of `Portfolio/dist/index.html`,
   branch `main`, root) → https://memodlike.github.io/portfolio-site/
The course repo is the single home for ALL solutions: weeks 1–3 and the Claims case are copied in as folders
(`Week1_easy_RFM_Insurance`, `Week1_medium_RFM_Retention`, `Week2_hard_RFM_Budget`, `Week3_easy_BookLover`,
`Week3_medium_ProjectPro`, `Case_Claim_Status_Assistant`); the root `README.md` is the index — add a row per new task.
Never name the user's employer or its brands anywhere public (site, repos, file names, PDFs, commit messages):
cases are written about an anonymised "retail insurance company".
The link to hand in is the portfolio section URL (`…/#w<week>-l<level>`).

## Rules
- Work inside one sub-project per change; never touch other projects.
- No destructive git (reset --hard, force push, branch deletion) or production deploys without explicit approval.
- Verify with the project's real commands before claiming success. Animated-site changes follow `web-motion-performance`.
- Do not commit secrets, `.env` files or credentials.
