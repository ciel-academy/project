import subprocess,re,json,importlib.util
from pathlib import Path
SRC='ffa61566a7e9ce4dfcf0dd740b4657747379fadb'
def show(ref,p):return subprocess.check_output(['git','show',f'{ref}:{p}'])
oldreport=show('HEAD','student_report_part1.js').decode()
url=re.search(r'const SUPABASE_URL\s*=\s*["\']([^"\']+)',oldreport).group(1)
key=re.search(r'const SUPABASE_ANON_KEY\s*=\s*["\']([^"\']+)',oldreport).group(1)
assert url=='https://xccfjfzpvqginpeviupn.supabase.co'
oldmig=subprocess.check_output(['git','ls-tree','-r','--name-only','HEAD','supabase/migrations'],text=True).splitlines()
assert len(oldmig)==17
back={p:show('HEAD',p) for p in oldmig+['docs/operation-update-history.md','.github/workflows/deploy-pages.yml']}
oldwf=show('HEAD','.github/workflows/deploy-supabase-functions.yml').decode()
guard=oldwf[oldwf.index('      - name: Guard CIEL deployment target'):oldwf.index('      - name: Checkout repository')]
assert 'xccfjfzpvqginpeviupn' in guard
subprocess.run(['git','checkout',SRC,'--','.'],check=True)
config=Path('hada_config.js').read_text();oldurl=re.search(r'supabaseUrl:\s*"([^"]+)"',config).group(1);oldkey=re.search(r'supabaseAnonKey:\s*"([^"]+)"',config).group(1)
spec=importlib.util.spec_from_file_location('setup','scripts/setup-new-academy.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
for p in m.TARGET_FILES_URL_KEY:m.replace_in_file(Path(p),[(oldurl,url),(oldkey,key)])
for p in m.TARGET_FILES_PAGES_PATH:m.replace_in_file(Path(p),[('https://hada-notion.github.io/project1/','https://ciel-academy.github.io/project/'),('https://hada-notion.github.io/project1','https://ciel-academy.github.io/project'),('github.io/project1/','github.io/project/'),('(project1)','(project)')])
for p,b in back.items():Path(p).write_bytes(b)
for p in ['supabase/functions/send-report/index.ts','supabase/functions/send-daily-report/index.ts','supabase/functions/send-class-daily-reports/index.ts']:
 q=Path(p);s=q.read_text();assert '/project1/student_report.html' in s;q.write_text(s.replace('/project1/student_report.html','/project/student_report.html'))
p=Path('.github/workflows/deploy-supabase-functions.yml');s=p.read_text();s=s.replace('      - name: Checkout repository',guard+'      - name: Checkout repository',1).replace('aws-0-ap-northeast-1.pooler.supabase.com','aws-0-ap-northeast-2.pooler.supabase.com');s=s.replace("      - 'supabase/migrations/**'","      - 'supabase/migrations/**'\n      - '.github/workflows/deploy-supabase-functions.yml'",1);p.write_text(s)
p=Path('.github/workflows/deploy-pages.yml');s=p.read_text().replace("'vendor/**',", "'vendor/**', 'assets/**',").replace('          cp -r vendor _site/vendor','          cp -r vendor _site/vendor\n          cp -r assets _site/assets');p.write_text(s)
for name in ['sync-attendance-incremental','sync-attendance-reconcile']:
 p=Path('.github/workflows/'+name+'.yml');s=p.read_text();assert 'schedule:' not in s;s=s.replace('    steps:\n','    steps:\n'+guard,1);p.write_text(s)
removed=['supabase/functions/_shared/registrationTimetableTarget.ts','.github/workflows/sync-attendance-incremental-cron.yml','.github/workflows/sync-attendance-reconcile-cron.yml','admin_config.json']
for p in removed:
 if Path(p).exists():subprocess.run(['git','rm','-q',p],check=True)
for d in ['mark-report-source-dirty','sync-registration-timetable','sync-school-schedules','sync-student-report']:
 p='supabase/functions/'+d
 if Path(p).exists():subprocess.run(['git','rm','-rq',p],check=True)
p=Path('tests/class-room-copy-cron-sql.cjs');s=p.read_text();assert s.count(oldurl)==1;p.write_text(s.replace(oldurl,url))
for p in oldmig:assert Path(p).read_bytes()==back[p]
assert url in Path('hada_config.js').read_text() and key in Path('hada_config.js').read_text()
for root in [Path('supabase/functions'),Path('supabase/migrations')]:
 for p in root.rglob('*'):
  if p.is_file():assert oldurl not in p.read_text(errors='ignore'),str(p)
newmig=[str(p) for p in Path('supabase/migrations').glob('*.sql') if str(p) not in oldmig];assert len(newmig)==15
print('PASS: 17 historical migrations byte-identical; 15 new migrations; CIEL configuration/guards/pooler/report fallbacks retained; source URL absent from runtime')
