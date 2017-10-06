[program:sentry-web]
directory={{ sentry.virtualenv }}
environment=C_FORCE_ROOT="true"
user=root
command={{ sentry.virtualenv }}bin/sentry --config=/etc/sentry/sentry.conf.py run web
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-worker]
directory={{ sentry.virtualenv }}
environment=C_FORCE_ROOT="true"
user=root
command={{ sentry.virtualenv }}bin/sentry --config=/etc/sentry/sentry.conf.py run worker
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-cron]
directory={{ sentry.virtualenv }}
environment=C_FORCE_ROOT="true"
user=root
command={{ sentry.virtualenv }}bin/sentry --config=/etc/sentry/sentry.conf.py run cron
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog