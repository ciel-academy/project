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

## 2026-10-15 — v2.6.10 update preparation (PARTIAL / PAUSED)

- Operator: CIEL Notion AI, workspace patch requester approved the complete update plan.
- Target: v2.6.10. Read-only source: hada-notion/project1 main ffa61566a7e9ce4dfcf0dd740b4657747379fadb.
- Operational baseline inspected: ciel-academy/project main 160d5551b8263bc2d3537fc2e705dbfe7d31e27e. Last fully accepted version remains NOT VERIFIED; the installation baseline label is not acceptance evidence.
- Private pre-change snapshot: four Notion database configurations, including schemas and layouts; retained in internal system information. Button actions and automation definitions were not exposed by the Notion tools. Nested formula references were opaque; not a complete restorable formula export.
- Completed safe pre-deployment preparation: session checkbox 보강, attendance text 메모 below teacher comment, learning-record text 주제 above range, and registration report-link property renamed 안내 링크 to 학생 페이지 while preserving the operational formula and URL. Structured update results confirmed schema and layout changes; real-device behavior not tested.
- Supabase checks: operational project identity confirmed, 17 existing migrations listed, queue Vault key name exists (value not read). These checks do not prove queued tasks or webhooks work end-to-end.
- PAUSED: v2.5.10 requires operator confirmation that attendance creation/edit automation no longer calls the individual sync-attendance webhook (or confirmation that no such action exists). Preserve modification-time recording and unrelated buttons/actions.
- Source code changes, deployments and new migrations: NOT PERFORMED. v2.5.11 and v2.6 functional acceptance: NOT VERIFIED. No version promotion.
- Preserve operation-specific deployment-target guards, connection settings, public-assets-only Pages staging and all previous history during subsequent code work. Scheduled attendance workflow definitions were inspected; their curl calls do not fail on HTTP errors, so job success alone is not sync verification.
- Optional security/search/copy-read settings, legacy-function deletion and historical bulk changes: ON HOLD. No student deletion, parent messaging, token regeneration, or secret changes were performed.
- Next: operator confirms the v2.5.10 prerequisite; proceed with remaining patch preconditions and operator-only formula/automation work before code deployment in an idle academy window.


## 2026-10-15 — v2.5.10·v2.5.11 선행 코드 적용 (배포 결과 대기)

- 전체 업데이트 및 CL 운영 고유 설정 보존 병합: 운영자 승인.
- 개별 출석 sync-attendance 웹훅은 운영자가 없음 확인. 자동화 액션 원문을 직접 검증한 것은 아님. 보고서 동기화·삭제·이름 조정 자동화는 유지.
- 원본 v2.5.10 f9be7fc327d752ef78fea811027dc2353199e5e1 함수 패치 반영. 운영 고유 워크플로에 원본의 scheduled-only 테스트 단계만 추가.
- 그 뒤 v2.5.11-code.patch git apply --check 성공 후 적용. 운영 Supabase 프로젝트 대상 가드·서울 DB pooler·공개 자산 전용 Pages 구성 보존.
- 일정 DB 학부모 공개 checkbox 추가, 기본 템플릿 false 확인. 학원일정 캘린더에 숨김=false 필터 추가. 전체 학사일정의 원본 보기 필터 보존. 기존 일정 공개 일괄 변경 없음.
- 후속 v2.6.9 준비: 학습활동 메모 text·🟡 일부 제출 select 옵션 추가, 기존 옵션 ID 보존. 과제제출됨 수식은 🔵 제출 동등 비교여서 변경 불필요.
- 로컬 Deno 1.46.3: 104 tests passed, 0 failed. 모든 함수 entrypoint deno check 통과. 회귀 가드 통과.
- 이 기록의 코드 커밋은 배포 트리거이며 CI·실환경 검증 결과는 별도로 기록한다. 현재 버전 완료 확정, 학생 데이터 삭제·대량 변경·실발송·토큰 재발급·Secrets 변경 없음.


## 2026-10-15 — 선행 배포 실패 / v2.6.10 검토본 준비

- 선행 코드 커밋: b7d0731e99a5c003d7c1c6ae295033970d5543f1.
- CI https://github.com/ciel-academy/project/actions/runs/38732858258 : 테스트·타입검사·회귀 가드·CLI 설치·DB 마이그레이션 단계 성공, Deploy all Edge Functions 실패(exit code 1). 이후 함수 목록/Secrets/마이그레이션 목록 검증 단계 skipped.
- 상세 로그 다운로드는 공개 API 403, 공개 체크 주석·웹페이지는 exit code 1만 제공. 원인 미확정. 코드·Secret 추측 변경이나 자동 재배포하지 않음. 운영자에게 실패 단계 로그 화면 확인 요청. 키 값은 가리고 제공.
- 실패 후 Supabase 읽기 전용 확인: 함수 41개 모두 기존 version 1, updated_at 2026-10-07T16:51:08.775Z. sync-attendance 배포 원문에 구형 개별 pageId 경로가 남아 있고 새 미지원 mode 거절 문구 없음. 서버 반영 완료가 아니며 v2.5.11 완료·현재 버전 갱신 보류.
- 일정 안내에 새 학부모 공개 정책 서버 적용 대기 경고 추가. 체크박스만으로 비공개를 보장하지 않음. 기존 일정 공개값 일괄 변경 없음.
- v2.6.10 별도 로컬 검토본: source ffa61566a7e9ce4dfcf0dd740b4657747379fadb, base b7d0731. 운영 URL·공개 연결키·프로젝트 가드·서울 pooler·REPORT_PATH 기본값·운영 이력 보존. 기존 마이그레이션 17개 바이트 동일, 새 파일 15개. 원본 학생 번호 시드 재반입 없음. Pages는 공개 assets만 추가. 옛 출석 cron 제거/수동 워크플로 전환은 검토본에만 있으며 운영 예약은 유지.
- 운영화로 인해 SQL cron 테스트의 기대 URL 한 곳만 CL URL로 보정. Deno 259 tests passed / 0 failed, 전체 entrypoint 타입검사·회귀 가드·디자인 검사 통과. 모의 PostgreSQL 보안 118 checks 및 복사본/cron SQL 검사 통과. 실제 운영 DB에 새 마이그레이션 적용 또는 업무 데이터 쓰기 없음.
- 차기 검토본은 main 미반영·서버/Pages 미배포. 선행 배포 오류 해결 및 수업·키오스크 미사용 시간 확인 필요. 생성 오류 수식·자동화 정리·단원 관계/버튼 등 수동/후속 항목은 미완료. 실제 출결·발송·학생 삭제·단원 대량 백필·Secrets 변경 안 함.

## 2026-10-15 — 선행 배포 재실행 성공 (attempt 2)

- 운영자가 제공한 attempt 1 상세 오류는 401 Invalid access token. 만료·폐기·잘못된 값 중 구체적 원인은 미확정이며 코드 오류로 단정하지 않음.
- 운영자가 GitHub Actions Secret SUPABASE_ACCESS_TOKEN을 교체하고 재실행함. 값은 읽거나 기록하지 않음.
- https://github.com/ciel-academy/project/actions/runs/38732858258 의 attempt 2가 success. 배포 코드 b7d0731e99a5c003d7c1c6ae295033970d5543f1. 모든 테스트·타입검사·회귀 가드·DB 마이그레이션·함수 전체 배포·함수 목록 대조·기본 필수 Secret 이름 확인·마이그레이션 상태 단계 성공 확인.
- Supabase MCP에서 sync-attendance / get-report-fast / sync-school-calendar version 2 ACTIVE 확인. 반환된 원문 발췌에서 예약 모드 전용 출석 경로 및 일정 공개 정책 모듈 적용 확인. 전체 반환 원문은 파일로 받았으나 로컬 비교 도구가 인프라 오류를 반환하여 바이트 단위 전체 비교는 미완료. CI 성공과 전체 배포 원문 대조를 구분함.
- Notion 일정 안내의 서버 배포 실패 경고를 배포 확인·동기화·실제 화면 검수 안내로 교체. 숨김/학부모 공개 규칙과 등록별 학생 페이지 동기화 필요성을 설명. 출석 웹훅 매핑과 예약 실행 안내도 v2.5.10 기준으로 갱신. 기존 버튼·자동화 동작 자체는 변경하지 않음.
- 위 배포 실패/대기 기록은 이전 시도 이력이며 현재 재실행 성공으로 해소됨. 선행 코드 배포는 성공했으나 실제 일정 생성·공개값 변경·재동기화/화면 검수, 출석 변경/삭제 반영, 실발송 검수는 미수행. 전체 설치/운영 인수 완료 또는 v2.6.10 적용 완료를 뜻하지 않음.
- v2.6.10 검토본은 여전히 미배포. 다음 전환 전에 수업·키오스크 미사용 시간 확인과 수동 수식·자동화 작업 확인 필요. 현재 버전 최종 완료 표기는 보류. 실데이터 삭제·대량 변경·학부모 발송을 수행하지 않음.
