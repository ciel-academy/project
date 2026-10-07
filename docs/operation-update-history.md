# CL Academy operation update history

- Baseline: v2.5.9, hada-notion/project1 main commit 91e224113c405f8838c51ebf31fd2c22f534c8d5.
- Work date (Asia/Seoul): 2026-10-08.
- Operator: Notion AI, workspace owner approved deployment continuation.
- Full installation status: NOT VERIFIED / IN PROGRESS.
- Code preparation: operational URLs and legacy public anon key replaced; original student-number seed omitted; deployment-target guards added; public-assets-only Pages workflow added.
- Local regression guard: passed. Type checks and Deno tests: pending CI.
- Database migrations, Edge Function deployment, Pages deployment: pending CI verification.
- Notion buttons, automations, integration access, Solapi templates and real device checks: not verified.
- No real parent messages, student deletions or sample-data backfill performed.
- Existing frontend configuration embedding is retained; this is not a no-hardcoding redesign.

## Partial deployment checkpoint

- Code commit: 4aab9bddcfa3ef38fa763bc73caa96b66aac6333; 148 files matched prepared source.
- Pages run 37653853199: success; four HTML screens returned HTTP 200 and matched source.
- Supabase run 37653853492: target guard, type checks, tests and regression guard passed; DB connection failed before migration application, and function deployment was skipped.
- Failure cause: session-pooler endpoint did not match the operational project. Correct endpoint verified from the owner dashboard; migration push and status lookup corrected. Password and secrets unchanged.
- Retry outcome: pending.
- Notion registration report-link formula updated; actual button and automation actions remain unverified.
- Vault secret-name inspection returned empty; queue admin key setup remains pending.
- Full installation is INCOMPLETE; real-student use and parent messaging have not been approved or tested.
