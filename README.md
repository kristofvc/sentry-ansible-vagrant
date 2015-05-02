# [Sentry](https://getsentry.com/welcome/) vagrant box

- Run `vagrant up`
- Add `192.168.33.89 sentry.server` to `/etc/hosts`
- Run `vagrant ssh`
- Run `/www/sentry/bin/sentry --config=/etc/sentry.conf.py changepassword sentry@sentry.com` and set a password
- Go to `http://sentry.server`
- Log in with `sentry@sentry.com

## Testing

This script was only tested on Mac OSX 10.10.3 and a vagrant box with Ubuntu 14.04

## Contributing

Feel free to fork this box and contribute to make it better!