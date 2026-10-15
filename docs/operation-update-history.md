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


## 2026-10-15 — v2.6.10 본전환 검증본 준비 (배포 결과 대기)

- 수업·키오스크 미사용 확인 질문에 운영자가 “진행시켜”로 진행 확인. 전체 업데이트·CL 고유 설정 보존 병합 승인 유지. 실발송·학생 삭제·단원 대량 백필은 제외.
- 원본 고정 커밋 ffa61566a7e9ce4dfcf0dd740b4657747379fadb. 운영 기준 e0402b05acdf7e7bebb11a4bd9394a554a696eae. 컴퓨터 재생성으로 로컬 검토본을 저장소에서 복구하고 재검사.
- 운영 URL·공개 연결키·프로젝트 대상 가드·서울 DB pooler·REPORT_PATH 기본값·공개 자산 전용 Pages 구성·기존 이력 보존. 기존 마이그레이션 17개 바이트 동일(원본 학생 번호 시드 미반입), 새 마이그레이션 15개. SQL cron 테스트의 기대 URL만 CL로 보정.
- 검증은 격리 브랜치 update/cl-v2.6.10. 최초 임시 준비 스크립트의 과거 함수명 문자열 때문에 회귀 가드가 실패해, 검사 기준 변경 없이 임시 파일을 검사 전에 제거함. 일반 자산과 워크플로 파일은 허용된 연결 경로로 분리 반영. 임시 준비/진단 파일은 최종 검증본에서 모두 제거.
- https://github.com/ciel-academy/project/actions/runs/38744228568 : 함수 테스트 259개·전체 타입검사·회귀 가드·디자인 검사·SQL 보안 118 checks 및 복사본/cron SQL 검사·자산 브랜치 기록 단계 success. 그 뒤 운영 전용 워크플로를 MCP로 반영하고 전체 파일을 로컬 검증본과 직접 비교해 불일치 0건 확인(3709f3f60fa3a174f03be6260e74520977cebe5f 기준).
- Vault 큐 관리자 키 이름 존재 재확인, 값 미열람. 이전 서버 함수 실제 삭제·선택 보안 모드·외부 검색 키 설정은 보류.
- Notion 수동 확인 안내 페이지를 작성했으나 완료 증거는 아님. 생성 오류 수식 교체 및 이전 자동화 정리는 미확인. 최소 선행 속성 보강/메모/주제·학생 페이지 이름·학습활동 메모/일부 제출은 확인됨.
- 다음은 squash 한 커밋으로 main 반영 후 서버/Pages 배포·새 함수 OPTIONS·예약/복사본 상태·공개 파일을 확인한다. 배포 후 단원 양방향 관계는 별도 변경하며, 기존 수식은 참조 검증·백필 승인 전 삭제하지 않는다. 현재 버전 최종 완료 표기는 보류.


## 2026-10-15 — v2.6.10 코드 본전환 성공 / 수동 설정·인수 대기

- PR https://github.com/ciel-academy/project/pull/1 을 승인 범위로 squash 병합. 운영 코드 f81c46082b1af4873a025689e2b70fa7c4402e4f, 원본 고정 ffa61566a7e9ce4dfcf0dd740b4657747379fadb. 병합 직전 운영 main e0402b05acdf7e7bebb11a4bd9394a554a696eae 일치 확인. PR 검사 38745276804 success.
- 서버 배포 https://github.com/ciel-academy/project/actions/runs/38745440641 success. Pages 배포 https://github.com/ciel-academy/project/actions/runs/38745440350 success. main 웹·문서 검사 38745440245 success. 서버 워크플로의 마이그레이션·전체 함수 배포·함수 목록·기본 Secret 이름·상태 확인 단계 성공. Secret 값 미열람.
- 실환경 읽기 검증: 적용 마이그레이션 32개(기존17+신규15). 신규 함수6개 ACTIVE, 인증 없는 OPTIONS 각각200(admin-security/class-room/fill-record-units/kiosk-prepare/sync-class-room-copy/textbook-api). OPTIONS는 인증 업무 동작 검증이 아님. 공개 HTML/JS/vendor/assets 총20개가 검증본과 바이트 일치. class-room 번들21개 파일과 sync-registration-textbook 번들13개 파일 모두 검증본과 내용 일치. 다른 함수 전체 번들 직접 비교는 하지 않았으며 CI 전체 배포·목록 확인과 구분.
- 예약 실행표 확인: 큐 매분·워치독15분·실패점검30분·과제마감10분·키오스크 KST04시·수업 복사본 처음3분/증분5분/밤 정합성·라이브러리10분. 복사본 커서 cr_sessions/cr_attendance/cr_records/cr_activities/lib_books 5개 확인. 2026-10-15 14:00:36 UTC 읽기 확인에서 처음 채우기 예약이 자동 해제되었고 커서5개 유지 확인.
- Notion N-9: 학습기록 기존 단원 수식의 이름만 단원(수식)으로 바꾸고 숨겨 보존. 단원목록과 양방향 단원↔학습기록 관계를 추가하고 주제→범위→단원→내용 배치 확인. 과거 기록 백필·기존 수식 삭제 안 함.
- 웹페이지 표 관리자 설정/라이브러리/수업 관리3행 추가, 관리자 서류를 법정 서류로 이름 변경, 운영 기준 주소 유지. 수업·출석/교재·학습/학부모 리포트/시스템 운영/매핑/수강 등록 주요 안내를 갱신하고 새 관리 화면 사용 안내 추가. 변경 전 원문은 시스템 정보 하위 진행 기록에 보존.
- 미완료: N-3 생성 오류 수식 화면 교체, N-8 이전 자동화 점검, N-10 단원 입력 버튼, v2.6.10 시간표 설정·교재 생성 버튼/자동화 전환, 실제 로그인·기기·시험 데이터 인수 검증. 자동화 원문은 도구에서 볼 수 없어 완료 추정 안 함. 원본 Notion 최신 문구 전체·키 발급 안내 대조는 미완료이며 주요 변경만 반영. N-13 이름 맞추기 권장 단계는 보류(기존 이름도 코드 호환).
- 선택 보안 모드/외부 검색 키/복사본 읽기 모드 설정은 변경 안 함. 예전 서버 함수4개는 삭제하지 않고 유지. 학생 삭제·학부모 실발송·과거 단원 대량 변경 안 함. 전체 현재 버전은 수동 설정·검수 전 승격하지 않음. 코드 배포 성공과 전체 업데이트 인수 완료는 구분한다.
