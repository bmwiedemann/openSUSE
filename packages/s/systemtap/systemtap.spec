#
# spec file for package systemtap
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


%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
Name:           systemtap
Version:        5.1
Release:        0
Summary:        Instrumentation System
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://sourceware.org/systemtap/
Source0:        https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz
Source1:        https://sourceware.org/systemtap/ftp/releases/systemtap-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        README-BEFORE-ADDING-PATCHES
Source4:        README-KEYRING
Source5:        stap-server.conf
Patch1:         systemtap-build-source-dir.patch

BuildRequires:  autoconf >= 2.71
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libavahi-devel
BuildRequires:  libcap-devel
BuildRequires:  libdw-devel
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  mozilla-nss-tools
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  sqlite-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  pkgconfig(systemd)
Requires:       %{name}-dtrace = %{version}
Requires:       %{name}-runtime = %{version}-%{release}
Recommends:     kernel-devel
Obsoletes:      systemtap-client < 1.5

%description
SystemTap is an instrumentation system for systems running Linux.
Developers can write instrumentation to collect data on the operation
of the system.

%package runtime
Summary:        Runtime environment for systemtap
Group:          Development/Tools/Debuggers

%description runtime
SystemTap is an instrumentation system for systems running Linux.
This package contains the runtime environment for systemtap programs.

%package server
Summary:        Systemtap server
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}-%{release}
# dependancies for systemtap shell scripts
Requires:       avahi
Requires:       avahi-utils
Requires:       coreutils
Requires:       mozilla-nss-tools
Requires:       unzip
Requires:       zip

%description server
SystemTap is an instrumentation system for systems running Linux.
This package contains the server component of systemtap.

%package sdt-devel
Summary:        Static probe support tools
# systemtap-headers provides the same header files
# as sdt-devel, so we must conflict.
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}-%{release}
Conflicts:      systemtap-headers

%description sdt-devel
SystemTap is an instrumentation system for systems running Linux.
This package contains the support tools for static probes.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fi
%configure \
  --disable-docs \
  --with-python3 \
  --docdir=%{_docdir}/systemtap
make %{?_smp_mflags} V=1

%install
%make_install
rm -f %{buildroot}%{_bindir}/dtrace
rm -f %{buildroot}%{_libexecdir}/systemtap/stap-server-request
# README, AUTHORS, NEWS, man3 and all examples packaged by systemtap-docs
# COPYING needs to stay in main for GPL
rm -rf %{buildroot}%{_docdir}/systemtap/
rm -rf %{buildroot}%{_datadir}/systemtap/examples
rm -rf %{buildroot}%{_mandir}/man3 %{buildroot}%{_mandir}/cs/man3
mkdir -p %{buildroot}%{_docdir}/systemtap/
cp COPYING %{buildroot}%{_docdir}/systemtap/
mkdir -p %{buildroot}%{_localstatedir}/cache/systemtap
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/stap-server.log
# config file for stap-server (/run now on tmpfs)
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}

%fdupes %{buildroot}%{_datadir}/%{name}
%python3_fix_shebang

%find_lang systemtap

%post server
# Create tmpfiles
%tmpfiles_create %{_tmpfilesdir}/stap-server.conf

%files
%{_bindir}/stap
%{_bindir}/stap-profile-annotate
%{_bindir}/stap-jupyter-container
%{_bindir}/stap-jupyter-install
%{_mandir}/man[17]/*
%{_mandir}/cs/man[17]/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/runtime
%{_datadir}/%{name}/interactive-notebook
%{_datadir}/%{name}/tapset
#packaged by systemtap-initscript in upstream
%dir %{_localstatedir}/cache/systemtap

%files runtime -f systemtap.lang
%doc %{_docdir}/systemtap
%{_bindir}/staprun
%{_bindir}/stapsh
%{_bindir}/stap-merge
%{_bindir}/stap-report
%{_bindir}/stapbpf
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/stapio
%{_libexecdir}/%{name}/stap-env
%{_libexecdir}/%{name}/stap-authorize-cert
%{_mandir}/man8/staprun.8*
%{_mandir}/man8/systemtap-service.8*
%{_mandir}/cs/man8/systemtap.8*
%{_mandir}/man8/stapsh.8*
%{_mandir}/cs/man8/stapsh.8*
%{_mandir}/man8/stapbpf.8*

%files server
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/stap-server.conf
%{_bindir}/stap-server
%{_libexecdir}/%{name}/stap-gen-cert
%{_libexecdir}/%{name}/stap-serverd
%{_libexecdir}/%{name}/stap-sign-module
%{_libexecdir}/%{name}/stap-start-server
%{_libexecdir}/%{name}/stap-stop-server
%{_mandir}/man8/stap-server.8*
%{_mandir}/cs/man8/stap-server.8*
%ghost %{_localstatedir}/log/stap-server.log
%ghost %dir %{_rundir}/stap-server

%files sdt-devel
%{_includedir}/sys/*.h

%changelog
