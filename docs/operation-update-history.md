# CL Academy operation update history

- Baseline: v2.5.9, hada-notion/project1 main commit 91e224113c405f8838c51ebf31fd2c22f534c8d5.
- Work date (Asia/Seoul): 2026-10-08.
- Operator: Notion AI, workspace owner approved deployment continuation.
- Full installation status: NOT VERIFIED / IN PROGRESS.
- Code preparation: operational URLs and legacy public anon key replaced; original student-number seed omitted; deployment-target guards added; public-assets-only Pages workflow added.
- Regression guard, all function type checks and Deno test groups: passed in deployment CI.
- Database migrations, all Edge Functions and Pages deployment: successful; operational acceptance remains pending.
- Notion buttons, automations, integration access, Solapi templates and real device checks: not verified.
- No real parent messages, student deletions or sample-data backfill performed.
- Existing frontend configuration embedding is retained; this is not a no-hardcoding redesign.

## Partial deployment checkpoint

- Code commit: 4aab9bddcfa3ef38fa763bc73caa96b66aac6333; 148 files matched prepared source.
- Pages run 37653853199: success; four HTML screens returned HTTP 200 and matched source.
- Supabase run 37653853492: target guard, type checks, tests and regression guard passed; DB connection failed before migration application, and function deployment was skipped.
- Failure cause: session-pooler endpoint did not match the operational project. Correct endpoint verified from the owner dashboard; migration push and status lookup corrected. Password and secrets unchanged.
- Retry outcome: SUCCESS. Supabase run https://github.com/ciel-academy/project/actions/runs/37655023128 completed all steps successfully for commit 88b4e701c7037d09ce2043b66a0f3eba4d42d48b. Seventeen database migrations were confirmed via Supabase MCP. The complete function deployment and repository function-list check passed. The baseline secret-name check passed; secret values and all integration mappings are not verified.
- Notion registration report-link formula updated; actual button and automation actions remain unverified.
- Vault secret-name inspection returned empty; queue admin key setup remains pending.
- Full installation is INCOMPLETE; real-student use and parent messaging have not been approved or tested.

- Post-deployment database checks: source student-number seed count is zero. Four scheduled jobs are active and target this operation. Vault queue admin key is still absent, so scheduled queue processing is not ready.
- Deployment success is confirmed; full installation acceptance remains incomplete pending Vault setup, Notion webhooks/integration mappings, and approved functional tests.

## Vault and Notion follow-up

- Owner saved the queue admin key in Vault. Secret-name existence confirmed; no secret value was read or printed.
- Latest scheduled HTTP response returned 200 without timeout or network error; earlier responses were 401. This does not verify every scheduled job or a real task end-to-end.
- School search formula changed from the source Pages URL to operational Pages. Pre-edit formula preserved privately. Actual school connection and calendar import are not tested.
- Earlier missing-Vault notes above describe the previous checkpoint and are superseded by this follow-up.
- Next operator step: inspect the registration student-page-sync button webhook endpoint, page-ID payload and masked authentication configuration. Do not expose credentials.
