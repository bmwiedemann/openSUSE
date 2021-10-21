LDAP_SRC = ../../..
LDAP_BUILD = $(LDAP_SRC)
LDAP_INC = -I$(LDAP_BUILD)/include -I$(LDAP_SRC)/include -I$(LDAP_SRC)/servers/slapd
LDAP_LIB = $(LDAP_BUILD)/libraries/libldap_r/libldap_r.la \
	$(LDAP_BUILD)/libraries/liblber/liblber.la

LIBTOOL = $(LDAP_BUILD)/libtool
CC = gcc
OPT = -g -O2 -Wall -fpic -DHAVE_CRACKLIB -DCRACKLIB_DICTPATH="\"/usr/share/cracklib/pw_dict\"" -DCONFIG_FILE="\"/etc/openldap/check_password.conf\"" -lcrack
INCS = $(LDAP_INC)
LIBS = $(LDAP_LIB)

PROGRAMS = ppolicy-check-password.la
LTVER = 0:0:0

prefix=/usr/local
exec_prefix=$(prefix)
ldap_subdir=/openldap

libdir=$(exec_prefix)/lib64
libexecdir=$(exec_prefix)/libexec
moduledir=$(libdir)$(ldap_subdir)

.SUFFIXES: .c .o .lo

.c.lo:
	$(LIBTOOL) --mode=compile $(CC) $(OPT) $(DEFS) $(INCS) -c $<

all:		$(PROGRAMS)

ppolicy-check-password.la:	check_password.lo
	$(LIBTOOL) --mode=link $(CC) $(OPT) -version-info $(LTVER) \
	-rpath $(moduledir) -module -o $@ $? $(LIBS)

clean:
	rm -rf *.o *.lo *.la .libs

install:	$(PROGRAMS)
	mkdir -p $(DESTDIR)$(moduledir)
	for p in $(PROGRAMS) ; do \
		$(LIBTOOL) --mode=install cp $$p $(DESTDIR)$(moduledir) ; \
	done

