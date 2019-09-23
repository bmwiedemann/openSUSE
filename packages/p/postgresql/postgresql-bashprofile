
# Get PGDATA from /etc/sysconfig/postgresql
if test -f /etc/sysconfig/postgresql; then
   eval eval $(sed -n '/^POSTGRES_DATADIR=/s//PGDATA=/p' /etc/sysconfig/postgresql)
   export PGDATA
fi
