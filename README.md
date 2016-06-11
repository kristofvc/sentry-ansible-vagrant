# [Sentry](https://getsentry.com/welcome/) vagrant box

- Run `vagrant up`
- Add `192.168.33.89 sentry.server` to `/etc/hosts`
- Run `vagrant ssh`
- Run `/www/sentry/bin/sentry --config=/etc/sentry/sentry.conf.py createuser` and set a username and password
- Go to `http://sentry.server`
- Log in with `sentry@sentry.com

## Leverage this box in a symfony2 application

### Install raven 

```json
	"require": {
        ...
        "raven/raven": "~0.8",
        ...
    }    
```

### Add some monolog config

```yml
monolog:
    handlers:
        main:
            type:         fingers_crossed
            action_level: error
            handler:      grouped_main

        sentry:
            type:  raven
            dsn: http://<public_key>:<private_key>@sentry.server/<project_id>
            level: notice

        # Groups
        grouped_main:
            type:    group
            members: [sentry, streamed_main]

        # Streams
        streamed_main:
            type:  stream
            path:  %kernel.logs_dir%/%kernel.environment%.log
            level: error
```

### Demo

See an implemented version by cloning or forking the following repository: [kristofvc/qa-test](https://github.com/kristofvc/qa-test)

## Testing

This ansible scripts were only tested on Mac OSX and a vagrant box with Ubuntu 14.04

## Contributing

Feel free to fork this box and contribute to make it better!