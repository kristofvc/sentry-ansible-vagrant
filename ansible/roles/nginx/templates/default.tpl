server {
    listen  80;

    server_name {{ servername }};

    location / {
      proxy_pass         http://localhost:{{ sentry.port }};
      proxy_redirect     off;

      proxy_set_header   Host              $host;
      proxy_set_header   X-Real-IP         $remote_addr;
      proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
      proxy_set_header   X-Forwarded-Proto $scheme;
    }
}
