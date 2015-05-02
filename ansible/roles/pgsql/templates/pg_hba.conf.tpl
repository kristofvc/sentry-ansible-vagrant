# TYPE  DATABASE        USER            ADDRESS                 METHOD

local   all             postgres                                md5

# "local" is for Unix domain socket connections only
local   all             all                                     md5

# IPv4 local connections:
host    all             all             127.0.0.1/32            md5

# IPv6 local connections:
host    all             all             ::1/128                 md5