#
# spec file for package mailutils
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%define somajor 9
# See bug boo#1095783
# Currently disabled suid/sgid program dotlock and maidag
%bcond_with     set_user_identity
%bcond_with     guile_22
Name:           mailutils
Version:        3.15
Release:        0
Summary:        GNU Mailutils
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://mailutils.org/
Source:         https://ftp.gnu.org/gnu/mailutils/%{name}-%{version}.tar.xz
Source1:        %{name}-3.5-guile-2.0.tar.xz
Source2:        %{name}-rpmlintrc
Source3:        https://ftp.gnu.org/gnu/mailutils/%{name}-%{version}.tar.xz.sig
Source4:        %{name}.keyring
Patch0:         lisp-load-silent.patch
Patch2:         silent-rpmlint-with_initgroups.patch
Patch3:         mailutils-3.5-guile-2.0.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cpio
BuildRequires:  cyrus-sasl-gssapi
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  guile-devel
BuildRequires:  help2man
BuildRequires:  libmysqld-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  makeinfo
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
# Does not compile due API changes
BuildRequires:  readline-devel
BuildRequires:  tcpd-devel
BuildRequires:  update-alternatives
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(kyotocabinet)
BuildRequires:  pkgconfig(libgsasl)
BuildRequires:  pkgconfig(python3)
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Requires:       guile = %(rpm -q --queryformat '%%{VERSION}' guile-devel)
%if 0
# Seems not compatible with original radius (missing debug.h)
BuildRequires:  freeradius-server-devel
%endif
%if %{with set_user_identity}
Requires(post): permissions
Requires(verify):permissions
%endif
# Hard requirement as mimeview uses /usr/share/cups/mime/mime.types
Requires:       cups

%description
Mailutils is a set of utilities and daemons for processing e-mail.

All Mailutils programs are able to operate on mailboxes of various
formats, including UNIX maildrops, maildir, and transparently
accessed remote mailboxes (IMAP4, POP3, SMTP).

Included is an implementation of the traditional UNIX mail reader,
"mail", command line utilities such as "frm", "messages", "readmsg",
as well as "sieve", a flexible utility for filtering the incoming
mail.

A special feature of Mailutils is an implementation of the
MH Message Handling System, which combines the UNIX
philosophy with a flexibility of Mailutils libraries, thus
allowing to incorporate mail from remote mailboxes.

For system administrators, Mailutils provides a set of daemons
for delivering and reading electronic mail, including
pop3d, imap4d and a universal mail delivery agent, called maidag.

%package mh
Summary:        MH mailbox format support for Mailutils
Group:          Productivity/Networking/Email/Clients

%description mh
The implementation provides an interface between Mailutils and Emacs
using the mh-e module.

To use Mailutils MH with Emacs, add the following line to
site-start.el or .gnu-emacs file: (load "mailutils-mh")

%package delivery
Summary:        Mailutils's delivery agents
Group:          Productivity/Networking/Email/Servers

%description delivery
The name 'maidag' stands for Mail delivery agent.  It is a
general-purpose MDA offering a number of features. It can operate
both in traditional mode, reading a message from standard input,
and in LMTP mode.  'Maidag' is able to deliver mail to any mailbox
format supported by GNU Mailutils. These formats, among others,
include 'smtp://', 'prog://' and 'sendmail://', which are equivalent to
forwarding a message over SMTP to a remote node.

%package notify
Summary:        Mailutils's incoming e-mail notification daemon
Group:          Productivity/Networking/Email/Servers

%description notify
Comsatd is the server which receives reports of incoming mail and
notifies users wishing to get this service.

%package imap4d
Summary:        IMAP4 daemon from GNU Mailutils
Group:          Productivity/Networking/Email/Servers
Conflicts:      courier-imap
Conflicts:      cyrus-imapd
Conflicts:      imap

%description imap4d
GNU 'imap4d' is a daemon implementing IMAP4 rev1 protocol for accessing
and handling electronic mail messages on a server.

%package pop3d
Summary:        POP3 daemon from GNU Mailutils
Group:          Productivity/Networking/Email/Servers
Conflicts:      courier-imap
Conflicts:      cyrus-imapd
Conflicts:      imap

%description pop3d
The 'pop3d' daemon implements the Post Office Protocol Version 3 server.

%package devel
Summary:        Development files for GNU Mailutils
Group:          Development/Libraries/C and C++
Requires:       libmailutils%{somajor} = %{version}
Requires:       mailutils = %{version}

%description devel
This package includes libraries and header files for building tools to
access mailutils features.

%package -n libmailutils%{somajor}
Summary:        Generalized mailbox access library
Group:          System/Libraries

%description -n libmailutils%{somajor}
At the core of Mailutils is 'libmailutils', a library which provides
an API for accessing a generalized mailbox.  A set of complementary
libraries provide methods for handling particular mailbox
implementations: UNIX mailbox, Maildir, MH, POP3, IMAP4, even SMTP.

%prep
%setup -q
%patch0
%patch2
set -- %(rpm -q --queryformat '%%{VERSION}' guile-devel | sed -r 's@\.@ @g')
(cat > guile.list)<<-EOF
	%dir %{_datadir}/guile/site/$1.$2/
	%dir %{_datadir}/guile/site/$1.$2/mailutils/
	%{_datadir}/guile/site/$1.$2/mailutils/*
	EOF
if test $1 -gt 2 -o \( $1 -eq 2 -a $2 -ge 2 \)
then
 echo Using guile $1.$2.$3
else
 echo Using guile $1.$2.$3
 mv libmu_scm libmu_scm-guile-2.2
 mv include/mailutils/guile.h include/mailutils/guile-2.2.h
 tar xfJ %{SOURCE1}
%patch3 -b .p3
  autoreconf -fiv
fi
#
# Check our somajor value with the actual value of VI_CURRENT
#
test %{somajor} == $(sed -rn '/^VI_CURRENT=/{ s/VI_CURRENT[[:space:]]*=[[:space:]]*//p; }' < ./configure)

#
# Avoid build require for emacs as emacs does
# build require one the sub packages herein!
#
mkdir bin
(cat > bin/emacs)<<-'EOF'
	#!/bin/sh
	case "$@" in
	*byte-compile*)
	    for arg
	    do
	        case "$arg" in
	        *.elc)
	            > "$arg"
	            ;;
	        *)
	        esac
	    done
	    ;;
	*load-path*)
	    echo %{_datadir}/emacs/site-lisp
	    ;;
	*)
	esac
EOF
chmod 755 bin/emacs
#
# There is no python-config for python3
#
if type -p python3-config > /dev/null 2>&1
then
    sed -ri '\@python-config@{ s@python-config@python3-config@ }' configure
fi

%build
PATH="$PWD/bin:$PATH"
CC=gcc
CXX=g++
#
# In frm/frm.h wrong definition of MB_LEN_MAX if not defined
#
CFLAGS="-Wall %{optflags} -fexceptions -D_GNU_SOURCE -DMB_LEN_MAX=16 -fno-strict-aliasing"
CXXFLAGS="-Wall %{optflags} -D_GNU_SOURCE -DMB_LEN_MAX=16 -fno-strict-aliasing"
export PATH CC CXX CFLAGS CXXFLAGS
%configure --enable-ipv6	\
    --enable-build-servers	\
    --enable-build-clients	\
    --disable-debug		\
    --disable-rpath		\
%if %{without set_user_identity}
    --disable-build-dotlock	\
    --disable-build-mda	\
%endif
%if 0
    --disable-silent-rules	\
%endif
    --disable-static		\
    --with-gnu-ld		\
    --with-gssapi		\
    --with-tcp-wrappers		\
    --with-ldap			\
    --with-lispdir=%{_datadir}/emacs/site-lisp \
    --with-log-facility=LOG_MAIL    \
    --with-kyotocabinet		\
    CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" \
    DEFAULT_CUPS_CONFDIR=%{_datarootdir}/cups/mime

make %{?_smp_mflags} V=1

%install
PATH="$PWD/bin:$PATH"
%make_install
#
# Remove dir, .la and .elc files
#
find %{buildroot} \( -name dir -o -name '*.la' -o -name '*.elc' \) -print -delete

#
#
#
%if %{with set_user_identity}
mkdir -p %{buildroot}%{_sysconfdir}/permissions.d
(cat > %{buildroot}%{_sysconfdir}/permissions.d/mailutils) <<-'EOF'
	%{_bindir}/dotlock	root:root	02755
	%{_sbindir}/maidag	root:root	04755
	EOF
(cat > %{buildroot}%{_sysconfdir}/permissions.d/mailutils.paranoid) <<-'EOF'
	%{_bindir}/dotlock	root:root	00755
	%{_sbindir}/maidag	root:root	00755
	EOF
%endif

# Move system manual pages
mkdir -p %{buildroot}%{_mandir}/man8
for m in pop3d imap4d
do
    mv %{buildroot}%{_mandir}/man1/${m}.1 %{buildroot}%{_mandir}/man8/${m}.8
done
# Create missing manual pages
for m in %{buildroot}%{_bindir}/*
do
    case "${m##*/}" in
    guimb|mailutils-config|mu-mh) continue ;;
    esac
    if test ! -e %{buildroot}%{_mandir}/man1/${m##*/}.1
    then
	LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man $m > %{buildroot}%{_mandir}/man1/${m##*/}.1
    fi
done
for m in %{buildroot}%{_sbindir}/*
do
    if test ! -e %{buildroot}%{_mandir}/man8/${m##*/}.8
    then
	LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man $m > %{buildroot}%{_mandir}/man8/${m##*/}.8
    fi
done

#
# Rename the mail program to avoid conflicts
#
mv %{buildroot}%{_bindir}/mail %{buildroot}%{_bindir}/mu-mail
mv %{buildroot}%{_mandir}/man1/mail.1 %{buildroot}%{_mandir}/man1/mu-mail.1

mkdir -p %{buildroot}/bin

%if ! %{with libalternatives}
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
%if 0%{?suse_version} < 1550
ln -sf %{_sysconfdir}/alternatives/binmail %{buildroot}/bin/mail
%endif
ln -sf %{_sysconfdir}/alternatives/Mail    %{buildroot}%{_bindir}/Mail
ln -sf %{_sysconfdir}/alternatives/mail    %{buildroot}%{_bindir}/mail
ln -sf %{_sysconfdir}/alternatives/Mail.1%{?ext_man} %{buildroot}%{_mandir}/man1/Mail.1%{?ext_man}
ln -sf %{_sysconfdir}/alternatives/mail.1%{?ext_man} %{buildroot}%{_mandir}/man1/mail.1%{?ext_man}
#
%if 0%{?suse_version} < 1550
ln -sf %{_bindir}/mu-mail %{buildroot}%{_sysconfdir}/alternatives/binmail
%endif
ln -sf %{_bindir}/mu-mail %{buildroot}%{_sysconfdir}/alternatives/Mail
ln -sf %{_bindir}/mu-mail %{buildroot}%{_sysconfdir}/alternatives/mail
ln -sf %{_mandir}/man1/mu-mail.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/Mail.1%{?ext_man}
ln -sf %{_mandir}/man1/mu-mail.1%{?ext_man} %{buildroot}%{_sysconfdir}/alternatives/mail.1%{?ext_man}
%else
# libalternatives
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/Mail
%if 0%{?suse_version} < 1550
ln -sf %{_bindir}/alts %{buildroot}/bin/Mail
%endif
mkdir -p %{buildroot}%{_datadir}/libalternatives/Mail
cat > %{buildroot}%{_datadir}/libalternatives/Mail/10.conf <<EOF
binary=%{_bindir}/mu-mailx
man=mu-mail.1
group=mail, Mail
EOF
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/mail
%if 0%{?suse_version} < 1550
ln -sf %{_bindir}/alts %{buildroot}/bin/mail
%endif
mkdir -p %{buildroot}%{_datadir}/libalternatives/mail
cat > %{buildroot}%{_datadir}/libalternatives/mail/10.conf <<EOF
binary=%{_bindir}/mu-mail
man=mu-mail.1
group=mail, Mail
EOF
%endif

%fdupes -s %{buildroot}%{python3_sitelib}/mailutils/

%find_lang %{name}

%post
%if ! %{with libalternatives}
%{_sbindir}/update-alternatives --quiet --force \
    --install %{_bindir}/mail mail %{_bindir}/mu-mail 10 \
%if 0%{?suse_version} < 1550
    --slave   /bin/mail binmail %{_bindir}/mu-mail \
%endif
    --slave   %{_bindir}/Mail Mail %{_bindir}/mu-mail \
    --slave   %{_mandir}/man1/mail.1%{?ext_man} mail.1%{?ext_man} %{_mandir}/man1/mu-mail.1%{?ext_man} \
    --slave   %{_mandir}/man1/Mail.1%{?ext_man} Mail.1%{?ext_man} %{_mandir}/man1/mu-mail.1%{?ext_man}
%endif
%if %{with set_user_identity}
%set_permissions %{_bindir}/dotlock
%set_permissions %{_sbindir}/maidag
%endif

%if ! %{with libalternatives}
%postun
if test ! -e %{_bindir}/mu-mail; then
  %{_sbindir}/update-alternatives --quiet --force --remove mail %{_bindir}/mu-mail
fi
%else

%pre
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
  %{_sbindir}/update-alternatives --quiet --force --remove mail %{_bindir}/mu-mail
fi
%endif

%post -n libmailutils%{somajor} -p /sbin/ldconfig
%postun -n libmailutils%{somajor} -p /sbin/ldconfig

%if %{with set_user_identity}
%verifyscript
%verify_permissions %{_bindir}/dotlock
%verify_permissions %{_sbindir}/maidag
%endif

%files -f %{name}.lang -f guile.list
%license COPYING COPYING.LESSER
%doc ChangeLog README NEWS AUTHORS THANKS
%{_infodir}/mailutils.info*.gz
%{_mandir}/man1/*.1%{?ext_man}
%if %{with set_user_identity}
%config %{_sysconfdir}/permissions.d/mailutils*
%endif
%if ! 0%{with libalternatives}
%if 0%{?suse_version} < 1550
%ghost %config %{_sysconfdir}/alternatives/binmail
/bin/mail
%endif
%ghost %config %{_sysconfdir}/alternatives/Mail
%ghost %config %{_sysconfdir}/alternatives/mail
%ghost %config %{_sysconfdir}/alternatives/Mail.1%{?ext_man}
%ghost %config %{_sysconfdir}/alternatives/mail.1%{?ext_man}
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/mail
%dir %{_datadir}/libalternatives/Mail
%{_datadir}/libalternatives/Mail/10.conf
%{_datadir}/libalternatives/mail/10.conf
%endif
%{_bindir}/decodemail
%if %{with set_user_identity}
%attr(02755,root,root) %verify(not mode) %{_bindir}/dotlock
%endif
%{_bindir}/frm
%{_bindir}/from
%{_bindir}/guimb
%{_bindir}/Mail
%{_bindir}/mail
%{_bindir}/mu-mail
%{_bindir}/mailutils
%{_bindir}/mailutils-config
%{_bindir}/messages
%{_bindir}/mimeview
%{_bindir}/movemail
%{_bindir}/popauth
%{_bindir}/readmsg
%{_bindir}/sieve
%dir %{_libexecdir}/mailutils/
%{_libexecdir}/mailutils/mailutils-*
%dir %{python3_sitelib}/mailutils/
%{python3_sitelib}/mailutils/*.p*
%dir %{python3_sitelib}/mailutils/__pycache__/
%{python3_sitelib}/mailutils/__pycache__/*
%dir %{_libdir}/mailutils/
%{_libdir}/mailutils/*.so
%dir %{python3_sitearch}/mailutils/
%{python3_sitearch}/mailutils/c_api.so

%files mh
%dir %{_bindir}/mu-mh/
%{_bindir}/mu-mh/*
%{_datadir}/emacs/site-lisp/mailutils-mh.el
%dir %{_datadir}/mailutils/
%dir %{_datadir}/mailutils/mh/
%{_datadir}/mailutils/mh/*

%files delivery
%{_sbindir}/lmtpd
%if %{with set_user_identity}
%attr(04755,root,root) %verify(not mode) %{_sbindir}/mda
%{_mandir}/man8/mda.8%{?ext_man}
%endif
%{_bindir}/putmail
%{_mandir}/man8/lmtpd.8%{?ext_man}

%files notify
%{_sbindir}/comsatd
%{_mandir}/man8/comsatd.8%{?ext_man}

%files imap4d
%{_sbindir}/imap4d
%{_mandir}/man8/imap4d.8%{?ext_man}

%files pop3d
%{_sbindir}/pop3d
%{_mandir}/man8/pop3d.8%{?ext_man}

%files devel
%{_libdir}/*.so
%dir %{_includedir}/mailutils/
%{_includedir}/mailutils/*.h
%dir %{_includedir}/mailutils/sys/
%{_includedir}/mailutils/sys/*.h
%{_datadir}/aclocal/mailutils.m4

%files -n libmailutils%{somajor}
%{_libdir}/*.so.*

%changelog
