[program:sentry-web]
directory={{ sentry.virtualenv }}
command={{ sentry.virtualenv }}bin/sentry --config=/etc/sentry.conf.py start
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog

[program:sentry-worker]
directory={{ sentry.virtualenv }}
command={{ sentry.virtualenv }}bin/sentry --config=/etc/sentry.conf.py celery worker -B
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=syslog
stderr_logfile=syslog