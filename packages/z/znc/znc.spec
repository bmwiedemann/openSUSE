#
# spec file for package znc
#
# Copyright (c) 2024 SUSE LLC
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


Name:           znc
Version:        1.9.1
Release:        0
Summary:        Advanced IRC Bouncer
License:        Apache-2.0
Group:          Productivity/Networking/IRC
URL:            https://wiki.znc.in/ZNC
Source0:        https://znc.in/releases/%{name}-%{version}.tar.gz
Source1:        https://znc.in/releases/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Patch0:         harden_znc.service.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_locale-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  swig >= 4.0.1
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(zlib)
Provides:       group(%{name})
Provides:       user(%{name})
Requires(pre):  shadow
%systemd_ordering

%description
ZNC is an IRC bouncer with many features like detaching, multiple
users, per channel playback buffer, SSL, IPv6, transparent DCC bouncing, and
C++ module support.

%lang_package

%package devel
Summary:        Development files to build modules for ZNC
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description devel
ZNC is an IRC bouncer with many features like detaching, multiple
users, per channel playback buffer, SSL, IPv6, transparent DCC bouncing, and
C++ module support.

This package contains the development headers for developing modules for ZNC.

%package perl
Summary:        Perl support for ZNC
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}-%{release}
Requires:       perl >= 5.10

%description perl
ZNC is an IRC bouncer with many features like detaching, multiple
users, per channel playback buffer, SSL, IPv6, transparent DCC bouncing, and
C++ module support.

This package contains the Perl extension to ZNC.

%package python3
Summary:        Python support for ZNC
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}-%{release}
Requires:       python3
Provides:       %{name}-python = %{version}
Obsoletes:      %{name}-python < %{version}

%description python3
ZNC is an IRC bouncer with many features like detaching, multiple
users, per channel playback buffer, SSL, IPv6, transparent DCC bouncing, and
C++ module support.

This package contains the Python extension to ZNC.

%package tcl
Summary:        TCL support for ZNC
Group:          Productivity/Networking/IRC
Requires:       %{name} = %{version}-%{release}
Requires:       tcl

%description tcl
ZNC is an IRC bouncer with many features like detaching, multiple
users, per channel playback buffer, SSL, IPv6, transparent DCC bouncing, and
C++ module support.

This package contains the Tcl extension to ZNC.

%prep
%autosetup -p1

%build
%cmake \
  -DSYSTEMD_DIR=%{_unitdir} \
  -DWANT_TCL=1 \
  -DWANT_PERL=1 \
  -DWANT_SWIG=1 \
  -DWANT_SYSTEMD=1 \
  -DWANT_PYTHON=1 \
  -DWANT_PYTHON_VERSION=python3 \
  -Wno-dev
%cmake_build

%install
%cmake_install
install -dm 0755 %{buildroot}%{_var}/lib/%{name} \
  %{buildroot}%{_sbindir}
ln -sv %{_sbindir}/service \
  %{buildroot}%{_sbindir}/rc%{name}
%find_lang %{name} --all-name

%pre
getent group  %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || useradd -r -g %{name} -s /bin/false -c "znc irc bouncer" -d %{_var}/lib/%{name} %{name}

%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/autoattach.so
%{_libdir}/%{name}/admindebug.so
%{_libdir}/%{name}/alias.so
%{_libdir}/%{name}/autocycle.so
%{_libdir}/%{name}/autoop.so
%{_libdir}/%{name}/awaynick.so
%{_libdir}/%{name}/bouncedcc.so
%{_libdir}/%{name}/chansaver.so
%{_libdir}/%{name}/clientnotify.so
%{_libdir}/%{name}/crypt.so
%{_libdir}/%{name}/dcc.so
%{_libdir}/%{name}/fail2ban.so
%{_libdir}/%{name}/identfile.so
%{_libdir}/%{name}/imapauth.so
%{_libdir}/%{name}/keepnick.so
%{_libdir}/%{name}/kickrejoin.so
%{_libdir}/%{name}/nickserv.so
%{_libdir}/%{name}/perform.so
%{_libdir}/%{name}/raw.so
%{_libdir}/%{name}/sample.so
%{_libdir}/%{name}/savebuff.so
%{_libdir}/%{name}/schat.so
%{_libdir}/%{name}/shell.so
%{_libdir}/%{name}/simple_away.so
%{_libdir}/%{name}/stickychan.so
%{_libdir}/%{name}/watch.so
%{_libdir}/%{name}/webadmin.so
%{_libdir}/%{name}/awaystore.so
%{_libdir}/%{name}/controlpanel.so
%{_libdir}/%{name}/cyrusauth.so
%{_libdir}/%{name}/missingmotd.so
%{_libdir}/%{name}/modules_online.so
%{_libdir}/%{name}/sasl.so
%{_libdir}/%{name}/adminlog.so
%{_libdir}/%{name}/autoreply.so
%{_libdir}/%{name}/autovoice.so
%{_libdir}/%{name}/block_motd.so
%{_libdir}/%{name}/blockuser.so
%{_libdir}/%{name}/buffextras.so
%{_libdir}/%{name}/cert.so
%{_libdir}/%{name}/certauth.so
%{_libdir}/%{name}/clearbufferonmsg.so
%{_libdir}/%{name}/ctcpflood.so
%{_libdir}/%{name}/disconkick.so
%{_libdir}/%{name}/flooddetach.so
%{_libdir}/%{name}/lastseen.so
%{_libdir}/%{name}/listsockets.so
%{_libdir}/%{name}/log.so
%{_libdir}/%{name}/notes.so
%{_libdir}/%{name}/notify_connect.so
%{_libdir}/%{name}/route_replies.so
%{_libdir}/%{name}/send_raw.so
%{_libdir}/%{name}/stripcontrols.so
%{_libdir}/%{name}/samplewebapi.so
%{_libdir}/%{name}/corecaps.so
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}
%attr(750,%{name},%{name}) %{_var}/lib/%{name}

%files lang -f %{name}.lang
%{_datadir}/locale/de_DE/LC_MESSAGES/znc*
%{_datadir}/locale/es_ES/LC_MESSAGES/znc*
%{_datadir}/locale/fr_FR/LC_MESSAGES/znc*
%{_datadir}/locale/it_IT/LC_MESSAGES/znc*
%{_datadir}/locale/pt_BR/LC_MESSAGES/znc*
%{_datadir}/locale/ru_RU/LC_MESSAGES/znc*

%files perl
%{_libdir}/%{name}/modperl.so
%dir %{_libdir}/%{name}/modperl/
%{_libdir}/%{name}/modperl/ZNC.pm
%{_libdir}/%{name}/modperl/ZNC.so
%{_libdir}/%{name}/modperl/startup.pl
%{_libdir}/%{name}/perleval.pm

%files python3
%{_libdir}/%{name}/pyeval.py
%{_libdir}/%{name}/modpython.so
%dir %{_libdir}/%{name}/modpython/
%{_libdir}/%{name}/modpython/_znc_core.so
%{_libdir}/%{name}/modpython/znc.py
%{_libdir}/%{name}/modpython/znc_core.py

%files tcl
%{_libdir}/%{name}/modtcl.so

%files devel
%{_bindir}/znc-buildmod
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/znc.pc
%{_mandir}/man1/znc-buildmod.1%{?ext_man}

%changelog
