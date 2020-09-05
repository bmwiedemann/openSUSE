#
# spec file for package kopano
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Kopano B.V.
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


%define version_unconverted 10.0.6

Name:           kopano
Version:        10.0.6
Release:        0
Summary:        Groupware server suite
License:        AGPL-3.0-only
Group:          Productivity/Networking/Email/Servers
URL:            https://kopano.io/
Source:         kopanocore-%version.tar.xz
Source3:        %name-rpmlintrc
# Workaround obs-service-source_validator
Source9:        debian.php7-mapi.triggers
BuildRequires:  gcc-c++ >= 6
BuildRequires:  gettext-devel
%ifarch %ix86 x86_64 ppc ppc64 ppc64le %arm aarch64 mips s390x
BuildRequires:  gperftools-devel
%endif
BuildRequires:  gsoap-devel >= 2.8.73
BuildRequires:  krb5-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libcurl-devel
BuildRequires:  libdb-4_8-devel
BuildRequires:  libical-devel >= 0.42
BuildRequires:  libicu-devel
BuildRequires:  libs3-devel >= 4.1
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libvmime-devel >= 0.9.2.85
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  pam-devel
BuildRequires:  php7-devel
BuildRequires:  pkg-config
%if !0%{?kc_without_python}
BuildRequires:  python3 >= 3.6
BuildRequires:  python3-devel >= 3.6
BuildRequires:  python3-setuptools
%endif
BuildRequires:  swig
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(jsoncpp) >= 1.4
BuildRequires:  pkgconfig(libHX) >= 1.10
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(librrd)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(xapian-core)
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?fedora_version} || 0%{?centos_version}
BuildRequires:  mysql-devel >= 4.1
%endif
%if 0%{?suse_version}
BuildRequires:  libmysqlclient-devel >= 4.1
# Satisfy Requires(pre) for bs_worker's rpmlint run
BuildRequires:  pwdutils
%endif
%if 0%{?suse_version}
	%define apache_group www
%else
	%define apache_group apache
%endif
%if !0%{?kc_phpconfig:1}
	%define kc_phpconfig php-config
%endif
%define phpextdir %(%kc_phpconfig --extension-dir)

%description
Kopano provides email storage on the server side and brings its own
Web-based mail client called WebApp. Kopano integrates with WebApp,
Push clients and other mail services as an alternative to Microsoft
Exchange and other comparable mail servers. Personal address book,
calendar, notes and tasks, "Public Folders" and shared calendar
functionalities (inviting internal and external users, resource
management) can be handled by the software as well.

%package archiver
Summary:        Hierarchial Storage Management for the Kopano Core platform
Group:          Productivity/Networking/Email/Servers
Requires:       kopano-lang = %version
%if 0%{?suse_version} || 0%{?fedora_version}
Recommends:     kopano-python-utils = %version
%endif

%description archiver
The Kopano Archiver provides a Hierarchical Storage Management (HSM)
solution for Kopano Core.

To decrease the database size of your production Kopano server, the
Kopano Archiver copies or moves messages to a secondary Kopano
server. Clients will still be able to open the message from the
secondary Kopano server directly.

%package bash-completion
Summary:        bash TAB completion for Kopano Core command-line utilities
Group:          System/Shells
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Some kopano commands offer bash completion, but it is an optional
feature.

%package client
Summary:        Kopano client utilities and MAPI provider plugins
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version
Requires:       kopano-lang = %version
Provides:       kopano-contacts = %version-%release
Obsoletes:      kopano-contacts < %version-%release
Provides:       kopano-utils = %version-%release
Obsoletes:      kopano-utils < %version-%release

%description client
The Kopano client-side programs and plugins.

* Command-line clients to control and check the Kopano server, server
  database, and mailbox settings.
* Plugin which provides the main MAPI service that will interface
  with a Kopano server.
* Additional MAPI provider which finds all contact folders of a user
  and adds the contents transparently into the MAPI addrbook.

%package common
Summary:        Shared files for Kopano Core services
Group:          Productivity/Networking/Email/Servers
%if 0%{?suse_version}
Requires:       cron
%else
Requires:       cronie
%endif
Requires:       logrotate
Requires(pre):  %_sbindir/groupadd
Requires(pre):  %_sbindir/useradd
%if 0%{?distro_without_intelligent_package_manager}
Obsoletes:      libkcarchivercore0
Obsoletes:      libkchl0
Obsoletes:      libkcmapi0
Obsoletes:      libkcrosie0
Obsoletes:      libkcservice0
Obsoletes:      libkcsoapclient0
Obsoletes:      libkcsoapserver0
Obsoletes:      libkcssl0
Obsoletes:      libkcsync0
%endif
Obsoletes:      kopano-core-common
Provides:       kopano-core-common

%description common
This package contains a basic set of files for distro integration:
* Definition for system user and group "kopano"
Kopano Groupware Core:
* GWC front manpage, Release Notes
* Logrotate definitions for GWC daemons
* Apparmor definitions for GWC daemons

%package dagent
Summary:        E-Mail Delivery Agent for the Kopano platform
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version
Requires:       kopano-dagent-pytils >= 9.0.2
Requires:       kopano-lang = %version
%if 0%{?suse_version} || 0%{?fedora_version}
# kcpyplug is dlopened / RedHat7 has no Recommends
Recommends:     libkcpyplug0 = %version
%endif
Conflicts:      kopano-dagent-pytils < 9.0.2

%description dagent
Delivers incoming e-mail from your SMTP server to stores in the
Kopano server.

%package devel
Summary:        C++ development files for Kopano Core
Group:          Development/Libraries/C and C++
Requires:       kopano-common = %version
Requires:       libkcarchiver0 = %version-%release
Requires:       libkcfreebusy0 = %version-%release
Requires:       libkcicalmapi0 = %version-%release
Requires:       libkcinetmapi0 = %version-%release
Requires:       libkcserver0 = %version-%release
Requires:       libkcsoap0 = %version-%release
Requires:       libkcutil0 = %version-%release
Requires:       libmapi1 = %version-%release

%description devel
Development files to create programs for use with Kopano Core.

%package gateway
Summary:        POP3 and IMAP Gateway for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version

%description gateway
The gateway enables other e-mail clients to connect through POP3 or
IMAP to the Kopano server to read their e-mail. With IMAP, it is also
possible to view the contents of other folders and subfolders. The
gateway can be configured to listen for POP3, POP3S, IMAP and/or
IMAPS.

%package ical
Summary:        ICal and CalDAV Gateway for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version

%description ical
The iCal/CalDAV gateway enables users to retrieve their calendar
using iCalendar compliant clients. The iCal/CalDAV gateway can be
configured to listen for HTTP and HTTPS requests.

%package indexer
Summary:        Fulltext indexer service for Kopano Core
Group:          Productivity/Networking/Email/Servers

%description indexer
kopano-indexd offers the fulltext indexing of libkcindex over the
network. kopano-server can make use of this service or the libkcindex
library to offload search queries from the SQL database.

%package lang
# More or less a copy of /usr/lib/rpm/suse_macros %%lang_package
Summary:        Translations for Kopano Core components
Group:          System/Localization

%description lang
Provides translations to various Kopano Core subpackages.

%package migration-imap
Summary:        Utility to migrate between IMAP mailboxes
Group:          Productivity/Networking/Email/Servers
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(Digest::HMAC_SHA1)
Requires:       perl(Digest::MD5)
Requires:       perl(English)
Requires:       perl(Errno)
Requires:       perl(Fcntl)
Requires:       perl(File::Basename)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(File::Glob)
Requires:       perl(File::Path)
Requires:       perl(File::Spec)
Requires:       perl(File::stat)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(IO::Socket)
Requires:       perl(IO::Tee)
Requires:       perl(IPC::Open3)
Requires:       perl(MIME::Base64)
Requires:       perl(Mail::IMAPClient)
Requires:       perl(POSIX)
Requires:       perl(Readonly)
Requires:       perl(Term::ReadKey)
Requires:       perl(Test::More)
Requires:       perl(Time::HiRes)
Requires:       perl(Time::Local)
Requires:       perl(Unicode::String)
Requires:       perl(strict)
Requires:       perl(warnings)

%description migration-imap
kopano-migration-imap provides a utility based on imapsync to migrate
between IMAP mailboxes (including Kopano).

%package monitor
Summary:        Quota monitor for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version

%description monitor
Regularly checks stores for total usage. If a quota limit has been
exceeded, an e-mail will be internally sent to this account.

%package server
Summary:        Server component for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version
# Needed for createstore scripts' functionality
Requires:       kopano-utils
# dlopened:
Requires:       libs3-4

%description server
This package provides the key component of Kopano Core, providing the
server to which Kopano clients connect. The server requires a MySQL
server to use for storage.

%package spooler
Summary:        E-mail Spooler for Kopano Core
Group:          Productivity/Networking/Email/Servers
Requires(pre):  kopano-common = %version
Requires:       kopano-dagent-pytils >= 9.0.2
Requires:       kopano-lang = %version
%if 0%{?suse_version} || 0%{?fedora_version}
# kcpyplug is dlopened
Recommends:     libkcpyplug0 = %version
%endif
Conflicts:      kopano-dagent-pytils < 9.0.2

%description spooler
The outgoing e-mail spooler. This service makes sure that e-mails
sent by clients are converted to Internet e-mail and forwarded to an
SMTP server.

%package statsd
Summary:        Statistics aggregator for Kopano Core services
Group:          Productivity/Networking/Email/Servers

%description statsd
kopano-statsd is a daemon with a HTTP endpoint that can receive
statistics submissions from kopano-dagent, kopano-spooler and
kopano-server and stores them in a round-robin database from which
graphs can be created at a later time with rrdgraph(1).

%package -n libkcarchiver0
Summary:        Library with shared Kopano archiver functionality
Group:          System/Libraries

%description -n libkcarchiver0
Library with shared archiver functionality for Kopano Core.

%package -n libkcfreebusy0
Summary:        Implementation of Free/Busy time scheduling
Group:          System/Libraries

%description -n libkcfreebusy0
RFC 5545

%package -n libkcicalmapi0
Summary:        iCal interface for MAPI
Group:          System/Libraries

%description -n libkcicalmapi0
Provides an interface between iCal and MAPI.

%package -n libkcindex0
Summary:        Fulltext indexing API for Kopano Core
Group:          System/Libraries

%description -n libkcindex0
This library implements a Xapian-based fulltext search index for
messages and attachments. kopano-server can load this library into
its memory space to access this indexer API through shared memory,
saving the round-trip latency between kopano-server and a separate
kopano-indexd instance.

%package -n libkcinetmapi0
Summary:        Internet e-mail interface for MAPI
Group:          System/Libraries

%description -n libkcinetmapi0
Provides an interface to convert between RFC 5322 Internet e-mail and
MAPI messages.

%package -n libkcpyplug0
Summary:        Python interpreter plugin for dagent/spooler
Group:          System/Libraries
Obsoletes:      libkcpyplug < %version-%release
Provides:       libkcpyplug = %version-%release

%description -n libkcpyplug0
This plugin enables the use of the Python interpreter from within
dagent/spooler. It is controlled via the "plugin_enable" directive in
the dagent/spooler config file. Multithreading will be turned OFF
when using this plugin.

%package -n libkcserver0
Summary:        The Kopano Server library
Group:          System/Libraries

%description -n libkcserver0
This library contains the central server code which is responsible
for handling RPC calls from libmapi, loading/storing objects in the
database, etc.

%package -n libkcsoap0
Summary:        SOAP (de)serializer functions for Kopano's RPCs
Group:          System/Libraries

%description -n libkcsoap0
This library contains autogenerated code to (de)serialize the SOAP RPCs
that are sent between Kopano clients and server.

Remote Procedure Call more or less means that a callable function
translates its arguments (C++ objects in our case) into a
representation that can be sent over the network. On the receiving
side, this representation is translated back to objects again.

%package -n libkcutil0
Summary:        Miscellaneous utility functions for Kopano Core
Group:          System/Libraries

%description -n libkcutil0
A lot of utility functions used from all over Kopano Core.

%package -n libmapi1
Summary:        Kopano's implementation of the Messaging API
Group:          System/Libraries

%description -n libmapi1
MAPI allows client programs to become (e-mail) messaging-enabled,
-aware, or -based by calling MAPI subsystem routines that interface
with certain messaging servers.

%package -n php-mapi
Summary:        PHP bindings for MAPI
Group:          Development/Languages/PHP
Requires:       kopano-client = %version
Obsoletes:      php5-mapi
Provides:       php5-mapi

%description -n php-mapi
Using this module, you can create PHP programs which use MAPI calls
to interact with Kopano.

%package -n python3-mapi
Summary:        Python3 bindings for MAPI
Group:          Development/Languages/Python
Requires:       kopano-client = %version

%description -n python3-mapi
Low-level (SWIG-generated) Python 3 bindings for MAPI. Using this
module, you can create Python programs which use MAPI calls to
interact with Kopano.

%prep
%autosetup -n kopanocore-%version -p1

%build
autoreconf -fi
# Grab new compiler from prjconf
export CC="%__cc"
export CXX="%__cxx"
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z -Wl,relro"
echo "kc_phpconfig=%kc_phpconfig"

%if !0%{?kc_without_python}
cpy_flags="--disable-python --enable-pybind"
PYTHON_CFLAGS=$(pkg-config python3 --cflags)
PYTHON_LIBS=$(pkg-config python3 --libs)
%else
cpy_flags="--disable-python --disable-pybind"
%endif

mkdir obj
pushd obj/
%define _configure ../configure

%configure \
	--docdir="%_docdir/%name" \
	--with-quotatemplate-prefix="%_sysconfdir/kopano/quotamail" \
	--with-php-config="%kc_phpconfig" --enable-release \
	$cpy_flags PYTHON="$(which python3)" \
	PYTHON_CFLAGS="$PYTHON_CFLAGS" PYTHON_LIBS="$PYTHON_LIBS"

echo "%version" >version
make V=1 %{?_smp_mflags}
popd

%install
b="%buildroot"
%make_install -C obj/
find "$b" -type f -name "*.la" -print -delete
cp -a RELNOTES.txt "$b/%_docdir/kopano/"
# dlopened or no headers
rm -Rfv "$b/%_libdir/libkcpyconv.so" "$b/%_libdir/libkcpydirector.so" "$b/%_libdir/libkcpyplug.so"
rm -Rfv "$b/%_libdir/libkcindex.so"

%if "%_repository" == "RHEL_7_PHP_70"
mkdir -p "$b/%_prefix/lib/systemd/system/kopano-dagent.service.d"
cat >"$b/%_prefix/lib/systemd/system/kopano-dagent.service.d/scl.conf" <<-EOF
	[Service]
	Environment=X_SCLS=rh-php70
	Environment=LD_LIBRARY_PATH=/opt/rh/rh-php70/root/usr/lib64
	Environment=PATH=/usr/local/sbin:/usr/local/bin:/opt/rh/rh-php70/root/usr/sbin:/opt/rh/rh-php70/root/usr/bin:/usr/sbin:/usr/bin
EOF
%endif
%if "%_repository" == "RHEL_7_PHP_71"
mkdir -p "$b/%_prefix/lib/systemd/system/kopano-dagent.service.d"
cat >"$b/%_prefix/lib/systemd/system/kopano-dagent.service.d/scl.conf" <<-EOF
	[Service]
	Environment=X_SCLS=rh-php71
	Environment=LD_LIBRARY_PATH=/opt/rh/rh-php71/root/usr/lib64
	Environment=PATH=/usr/local/sbin:/usr/local/bin:/opt/rh/rh-php71/root/usr/sbin:/opt/rh/rh-php71/root/usr/bin:/usr/sbin:/usr/bin
EOF
%endif

%if 0%{?fdupes:1}
%fdupes %buildroot/%_prefix
%endif

# some default dirs
mkdir -p "$b/%_defaultdocdir" "$b/var/lib/kopano/autorespond"
mkdir -p "$b/%_localstatedir/log/kopano"
chmod 750 "$b/%_localstatedir/log/kopano"
%find_lang kopano

%triggerpostun archiver -- kopano-archiver
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/archiver.cfg" -a \
     -e "%_sysconfdir/kopano/archiver.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/archiver.cfg.rpmsave" \
		"%_sysconfdir/kopano/archiver.cfg"
fi

%post   client -p /sbin/ldconfig
%postun client -p /sbin/ldconfig

%pre common
%_bindir/getent group kopano >/dev/null || \
	%_sbindir/groupadd -r kopano
%_bindir/getent passwd kopano >/dev/null || \
	%_sbindir/useradd -c "Kopano unprivileged account" \
		-g kopano -r kopano -s /sbin/nologin

%post common
if [ -x /usr/bin/systemd-tmpfiles ]; then
	/usr/bin/systemd-tmpfiles --create kopano-tmpfiles.conf || :
fi

%triggerpostun common -- kopano-common
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/sysconfig/kopano" -a \
     -e "%_sysconfdir/sysconfig/kopano.rpmsave" ]; then
	mv -v "%_sysconfdir/sysconfig/kopano.rpmsave" \
		"%_sysconfdir/sysconfig/kopano"
fi

%pre dagent
%{?_unitdir:%{?suse_version:%service_add_pre kopano-dagent.service}}

%post dagent
%{?_unitdir:%{?suse_version:%service_add_post kopano-dagent.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-dagent.service}}

%preun dagent
%{?_unitdir:%{?suse_version:%service_del_preun kopano-dagent.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-dagent.service}}
%{!?_unitdir:%stop_on_removal kopano-dagent}

%postun dagent
%{?_unitdir:%{?suse_version:%service_del_postun kopano-dagent.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-dagent.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-dagent}

%triggerpostun dagent -- kopano-dagent
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/autorespond" -a \
     -e "%_sysconfdir/kopano/autorespond.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/autorespond.rpmsave" \
		"%_sysconfdir/kopano/autorespond"
fi
if [ ! -e "%_sysconfdir/kopano/dagent.cfg" -a \
     -e "%_sysconfdir/kopano/dagent.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/dagent.cfg.rpmsave" \
		"%_sysconfdir/kopano/dagent.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-dagent.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-dagent.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-dagent}

%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%pre gateway
%{?_unitdir:%{?suse_version:%service_add_pre kopano-gateway.service}}

%post gateway
%{?_unitdir:%{?suse_version:%service_add_post kopano-gateway.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-gateway.service}}

%preun gateway
%{?_unitdir:%{?suse_version:%service_del_preun kopano-gateway.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-gateway.service}}
%{!?_unitdir:%stop_on_removal kopano-gateway}

%postun gateway
%{?_unitdir:%{?suse_version:%service_del_postun kopano-gateway.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-gateway.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-gateway}

%triggerpostun gateway -- kopano-gateway
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/gateway.cfg" -a \
     -e "%_sysconfdir/kopano/gateway.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/gateway.cfg.rpmsave" \
		"%_sysconfdir/kopano/gateway.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-gateway.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-gateway.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-gateway}

%pre ical
%{?_unitdir:%{?suse_version:%service_add_pre kopano-ical.service}}

%post ical
%{?_unitdir:%{?suse_version:%service_add_post kopano-ical.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-ical.service}}

%preun ical
%{?_unitdir:%{?suse_version:%service_del_preun kopano-ical.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-ical.service}}
%{!?_unitdir:%stop_on_removal kopano-ical}

%postun ical
%{?_unitdir:%{?suse_version:%service_del_postun kopano-ical.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-ical.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-ical}

%triggerpostun ical -- kopano-ical
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/ical.cfg" -a \
     -e "%_sysconfdir/kopano/ical.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/ical.cfg.rpmsave" \
		"%_sysconfdir/kopano/ical.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-ical.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-ical.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-ical}

%pre monitor
%{?_unitdir:%{?suse_version:%service_add_pre kopano-monitor.service}}

%post monitor
%{?_unitdir:%{?suse_version:%service_add_post kopano-monitor.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-monitor.service}}

%preun monitor
%{?_unitdir:%{?suse_version:%service_del_preun kopano-monitor.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-monitor.service}}
%{!?_unitdir:%stop_on_removal kopano-monitor}

%postun monitor
%{?_unitdir:%{?suse_version:%service_del_postun kopano-monitor.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-monitor.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-monitor}

%triggerpostun monitor -- kopano-monitor
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/monitor.cfg" -a \
     -e "%_sysconfdir/kopano/monitor.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/monitor.cfg.rpmsave" \
		"%_sysconfdir/kopano/monitor.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-monitor.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-monitor.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-monitor}

%pre server
%{?_unitdir:%{?suse_version:%service_add_pre kopano-server.service}}

%post server
%{?_unitdir:%{?suse_version:%service_add_post kopano-server.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-server.service}}

%preun server
%{?_unitdir:%{?suse_version:%service_del_preun kopano-server.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-server.service}}
%{!?_unitdir:%stop_on_removal kopano-server}

%postun server
%{?_unitdir:%{?suse_version:%service_del_postun kopano-server.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-server.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-server}

%triggerpostun server -- kopano-server
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/server.cfg" -a \
     -e "%_sysconfdir/kopano/server.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/server.cfg.rpmsave" \
		"%_sysconfdir/kopano/server.cfg"
fi
if [ ! -e "%_sysconfdir/kopano/unix.cfg" -a \
     -e "%_sysconfdir/kopano/unix.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/unix.cfg.rpmsave" \
		"%_sysconfdir/kopano/unix.cfg"
fi
if [ ! -e "%_sysconfdir/kopano/ldap.propmap.cfg" -a \
     -e "%_sysconfdir/kopano/ldap.propmap.cfg.rpmsave" ]; \
then
	mv -v "%_sysconfdir/kopano/ldap.propmap.cfg.rpmsave" \
		"%_sysconfdir/kopano/ldap.propmap.cfg"
elif grep -q ldap.propmap.cfg "%_sysconfdir/kopano/server.cfg"; then
	# No private modifications. Make sure it exists,
	# if loosely referenced.
	ln -Tsv "%_datadir/kopano/ldap.propmap.cfg" \
		"%_sysconfdir/kopano/ldap.propmap.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-server.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-server.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-server}

%pre spooler
%{?_unitdir:%{?suse_version:%service_add_pre kopano-spooler.service}}

%post spooler
%{?_unitdir:%{?suse_version:%service_add_post kopano-spooler.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-spooler.service}}

%preun spooler
%{?_unitdir:%{?suse_version:%service_del_preun kopano-spooler.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-spooler.service}}
%{!?_unitdir:%stop_on_removal kopano-spooler}

%postun spooler
%{?_unitdir:%{?suse_version:%service_del_postun kopano-spooler.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-spooler.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-spooler}

%triggerpostun spooler -- kopano-spooler
if [ "$1" -ne 2 ]; then exit 0; fi
# putback previously existing cfgs after they get untracked once
if [ ! -e "%_sysconfdir/kopano/spooler.cfg" -a \
     -e "%_sysconfdir/kopano/spooler.cfg.rpmsave" ]; then
	mv -v "%_sysconfdir/kopano/spooler.cfg.rpmsave" \
		"%_sysconfdir/kopano/spooler.cfg"
fi
%{?_unitdir:%{?suse_version:%service_del_postun kopano-spooler.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-spooler.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-spooler}

%pre statsd
%{?_unitdir:%{?suse_version:%service_add_pre kopano-statsd.service}}

%post statsd
%{?_unitdir:%{?suse_version:%service_add_post kopano-statsd.service}}
%{?_unitdir:%{!?suse_version:%systemd_post kopano-statsd.service}}

%preun statsd
%{?_unitdir:%{?suse_version:%service_del_preun kopano-statsd.service}}
%{?_unitdir:%{!?suse_version:%systemd_preun kopano-statsd.service}}
%{!?_unitdir:%stop_on_removal kopano-statsd}

%postun statsd
%{?_unitdir:%{?suse_version:%service_del_postun kopano-statsd.service}}
%{?_unitdir:%{!?suse_version:%systemd_postun_with_restart kopano-statsd.service}}
%{!?_unitdir:%insserv_cleanup}
%{!?_unitdir:%restart_on_update kopano-statsd}

%post   -n libkcarchiver0 -p /sbin/ldconfig
%postun -n libkcarchiver0 -p /sbin/ldconfig
%post   -n libkcfreebusy0 -p /sbin/ldconfig
%postun -n libkcfreebusy0 -p /sbin/ldconfig
%post   -n libkcicalmapi0 -p /sbin/ldconfig
%postun -n libkcicalmapi0 -p /sbin/ldconfig
%post   -n libkcinetmapi0 -p /sbin/ldconfig
%postun -n libkcinetmapi0 -p /sbin/ldconfig
%post   -n libkcpyplug0 -p /sbin/ldconfig
%postun -n libkcpyplug0 -p /sbin/ldconfig
%post   -n libkcserver0 -p /sbin/ldconfig
%postun -n libkcserver0 -p /sbin/ldconfig
%post   -n libkcsoap0 -p /sbin/ldconfig
%postun -n libkcsoap0 -p /sbin/ldconfig
%post   -n libkcutil0 -p /sbin/ldconfig
%postun -n libkcutil0 -p /sbin/ldconfig
%post   -n libmapi1 -p /sbin/ldconfig
%postun -n libmapi1 -p /sbin/ldconfig

%post -n python3-mapi
/sbin/ldconfig
%if 0%{?_unitdir:1}
if systemctl is-active kopano-dagent >/dev/null; then
	systemctl try-restart kopano-dagent
fi
if systemctl is-active kopano-spooler >/dev/null; then
	systemctl try-restart kopano-spooler
fi
%else
%restart_on_update kopano-dagent
%restart_on_update kopano-spooler
%endif

%postun -n python3-mapi -p /sbin/ldconfig

%files archiver
%defattr(-,root,root)
%_sbindir/kopano-archiver
%_mandir/man5/kopano-archiver.cfg.5*
%_mandir/man8/kopano-archiver.8*
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/archiver.cfg

%files bash-completion
%defattr(-,root,root)
%_datadir/bash-completion/

%files client
%defattr(-,root,root)
%_bindir/kopano-fsck
%_bindir/kopano-ibrule
%_bindir/kopano-oof
%_bindir/kopano-passwd
%_bindir/kopano-stats
%_bindir/kopano-vcfimport
%_sbindir/kopano-admin
%_sbindir/kopano-srvadm
%_sbindir/kopano-storeadm
%_mandir/man*/kopano-admin.*
%exclude %_mandir/man*/kopano-cfgchecker.*
%_mandir/man*/kopano-fsck.*
%_mandir/man*/kopano-ibrule.*
%_mandir/man*/kopano-oof.*
%_mandir/man*/kopano-passwd.*
%_mandir/man*/kopano-srvadm.*
%_mandir/man*/kopano-stats.*
%_mandir/man*/kopano-storeadm.*
%_mandir/man*/kopano-vcfimport.*
%dir %_libexecdir/kopano/
%_libexecdir/kopano/eidprint
%_libexecdir/kopano/mapitime
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/admin.cfg
%dir %_prefix/lib/mapi.d/
%_prefix/lib/mapi.d/kopano.inf
%_prefix/lib/mapi.d/zcontacts.inf
%exclude %_datadir/locale/
%dir %_libdir/kopano/
%_libdir/kopano/libkcclient.so
%_libdir/kopano/libkccontacts.so

%files common
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/logrotate.d/*
%doc AGPL-3
%dir %_prefix/lib/systemd/
%dir %_prefix/lib/systemd/system/
%_prefix/lib/sysusers.d/
%_prefix/lib/tmpfiles.d/
%_mandir/man5/kopano-coredump.5*
%_mandir/man7/kopano.7*
%_mandir/man7/mapi.7*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%_docdir/kopano/RELNOTES.txt
%dir %_docdir/kopano/example-config/
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/*.aa

%files dagent
%defattr(-,root,root)
%_sbindir/kopano-dagent
%_prefix/lib/systemd/system/kopano-dagent.service
%if "%_repository" == "RHEL_7_PHP_56" || "%_repository" == "RHEL_7_PHP_70" || "%_repository" == "RHEL_7_PHP_71"
%_prefix/lib/systemd/system/kopano-dagent.service.d/
%endif
%_mandir/man*/kopano-dagent.*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %_localstatedir/lib/kopano/autorespond/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/dagent.cfg
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/usr.sbin.kopano-dagent

%files devel
%defattr(-,root,root)
%_includedir/*
%_libdir/libkcfreebusy.so
%_libdir/libkcicalmapi.so
%_libdir/libkcinetmapi.so
%_libdir/libmapi.so
%_libdir/libkcarchiver.so
%_libdir/libkcserver.so
%_libdir/libkcsoap.so
%_libdir/libkcutil.so
%_libdir/pkgconfig/*
%_datadir/gdb/

%files gateway
%defattr(-,root,root)
%_sbindir/kopano-gateway
%_prefix/lib/systemd/system/kopano-gateway.service
%_mandir/man*/kopano-gateway.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/gateway.cfg

%files ical
%defattr(-,root,root)
%_sbindir/kopano-ical
%_prefix/lib/systemd/system/kopano-ical.service
%_mandir/man*/kopano-ical.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/ical.cfg

%files indexer
%defattr(-,root,root)
%dir %_libexecdir/kopano/
%_libexecdir/kopano/kopano-indexd
%_mandir/man8/kopano-indexd.8*

%files lang -f kopano.lang
%defattr(-,root,root)

%files migration-imap
%defattr(-,root,root)
%_bindir/kopano-migration-imap

%files monitor
%defattr(-,root,root)
%dir %_sysconfdir/kopano/
%config %_sysconfdir/kopano/quotamail
%_sbindir/kopano-monitor
%_prefix/lib/systemd/system/kopano-monitor.service
%_mandir/man*/kopano-monitor.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/monitor.cfg

%files server
%defattr(-,root,root)
%dir %_prefix/lib/kopano/
%_prefix/lib/kopano/userscripts/
%dir %_libexecdir/kopano/
%_libexecdir/kopano/kscriptrun
%_sbindir/kopano-dbadm
%_sbindir/kopano-server
%dir %_libdir/kopano/
%_libdir/kopano/libkcserver-[a-z]*.so
%_prefix/lib/systemd/system/kopano-server.service
%_mandir/man*/kopano-dbadm.*
%_mandir/man*/kopano-server.*
%_mandir/man*/kopano-ldap.cfg.*
%_mandir/man*/kopano-unix.cfg.*
%attr(0750,kopano,kopano) %dir %_localstatedir/lib/kopano/
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_datadir/kopano/
%_datadir/kopano/ldap.active-directory.cfg
%_datadir/kopano/ldap.openldap.cfg
%_datadir/kopano/ldap.propmap.cfg
%dir %_docdir/kopano/
%_docdir/kopano/audit-parse.pl
%_docdir/kopano/createuser.dotforward
%_docdir/kopano/db-calc-storesize
%_docdir/kopano/db-convert-attachments-to-files
%_docdir/kopano/db-remove-orphaned-attachments
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/ldap.cfg
%_docdir/kopano/example-config/server.cfg
%_docdir/kopano/example-config/unix.cfg
%_docdir/kopano/ldap-switch-sendas.pl
%_docdir/kopano/ssl-certificates.sh
%_docdir/kopano/kopano.ldif
%_docdir/kopano/kopano.schema
%dir %_docdir/kopano/example-config/apparmor.d/
%_docdir/kopano/example-config/apparmor.d/usr.sbin.kopano-server

%files spooler
%defattr(-,root,root)
%_sbindir/kopano-spooler
%_prefix/lib/systemd/system/kopano-spooler.service
%_mandir/man*/kopano-spooler.*
%attr(0750,kopano,kopano) %dir %_localstatedir/log/kopano/
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/spooler.cfg

%files statsd
%_prefix/lib/systemd/system/kopano-statsd.service
%dir %_libexecdir/kopano/
%_libexecdir/kopano/kopano-statsd
%_mandir/man*/kopano-statsd.*
%dir %_docdir/kopano/
%dir %_docdir/kopano/example-config/
%_docdir/kopano/example-config/statsd.cfg

%files -n libkcarchiver0
%defattr(-,root,root)
%_libdir/libkcarchiver.so.0*

%files -n libkcfreebusy0
%defattr(-,root,root)
%_libdir/libkcfreebusy.so.0*

%files -n libkcicalmapi0
%defattr(-,root,root)
%_libdir/libkcicalmapi.so.0*

%files -n libkcindex0
%defattr(-,root,root)
%_libdir/libkcindex.so.0*

%files -n libkcinetmapi0
%defattr(-,root,root)
%_libdir/libkcinetmapi.so.0*

%if !0%{?kc_without_python}
%files -n libkcpyplug0
%defattr(-,root,root)
%_libdir/libkcpyplug.so.0*
%endif

%files -n libkcserver0
%defattr(-,root,root)
%_libdir/libkcserver.so.0*

%files -n libkcsoap0
%defattr(-,root,root)
%_libdir/libkcsoap.so.0*

%files -n libkcutil0
%defattr(-,root,root)
%_libdir/libkcutil.so.0*

%files -n libmapi1
%defattr(-,root,root)
%_libdir/libmapi.so.1*

%files -n php-mapi
%defattr(-,root,root)
%if 0%{?fedora_version} || 0%{?centos_version}
%if "%_repository" == "RHEL_6_PHP_70" || "%_repository" == "RHEL_7_PHP_70"
%dir /etc/opt/rh/rh-php70/php.d/
%config(noreplace) /etc/opt/rh/rh-php70/php.d/mapi.ini
%else
%if "%_repository" == "RHEL_7_PHP_71"
%dir /etc/opt/rh/rh-php71/php.d/
%config(noreplace) /etc/opt/rh/rh-php71/php.d/mapi.ini
%else
%dir %_sysconfdir/php.d/
%config(noreplace) %_sysconfdir/php.d/mapi.ini
%endif
%endif
%endif
%if 0%{?suse_version} >= 1330 || "%_repository" == "SLE_12_PHP7" || "%_repository" == "openSUSE_Leap_42.3"
%dir %_sysconfdir/php7/
%dir %_sysconfdir/php7/conf.d/
%config(noreplace) %_sysconfdir/php7/conf.d/mapi.ini
%endif
%phpextdir/mapi*
%dir %_datadir/kopano/

%if !0%{?kc_without_python}
%files -n python3-mapi
%defattr(-,root,root)
%_libdir/libkcpyconv-3*.so
%_libdir/libkcpydirector-3*.so
%python3_sitelib/MAPI/
%python3_sitelib/MAPI-*.egg-info
%python3_sitelib/MAPICore.*
%python3_sitelib/icalmapi.*
%python3_sitelib/inetmapi.*
%python3_sitelib/*libfreebusy.*
%python3_sitearch/*MAPICore.*
%python3_sitearch/*icalmapi.*
%python3_sitearch/*inetmapi.*
%python3_sitearch/*libfreebusy.*
%if 0%{?fedora_version} || 0%{?centos_version}
%python3_sitelib/__*/MAPICore.*
%python3_sitelib/__*/icalmapi.*
%python3_sitelib/__*/inetmapi.*
%python3_sitelib/__*/libfreebusy.*
%endif
%endif

%changelog
