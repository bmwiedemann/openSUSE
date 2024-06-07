#
# spec file for package usbguard
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


%global _hardened_build 1
%define lname libusbguard1
Name:           usbguard
Version:        1.1.3
Release:        0
Summary:        A tool for implementing USB device usage policy
## Not installed
# src/ThirdParty/Catch: Boost Software License - Version 1.0
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://usbguard.github.io
Source0:        https://github.com/USBGuard/usbguard/releases/download/usbguard-%{version}/usbguard-%{version}.tar.gz
Source1:        https://github.com/USBGuard/usbguard/releases/download/usbguard-%{version}/usbguard-%{version}.tar.gz.sum.asc
Source2:        usbguard.keyring
Source3:        usbguard-daemon.conf
Source4:        usbguard-rpmlintrc
Patch0:         usbguard-pthread.patch
BuildRequires:  asciidoc
BuildRequires:  audit-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion-devel
BuildRequires:  dbus-1-glib-devel
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libcap-ng-devel
BuildRequires:  libqb-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
#BuildRequires:  spdlog-static
BuildRequires:  protobuf-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
%{?systemd_requires}

%description
The USBGuard software framework helps to protect your computer against rogue USB
devices by implementing basic whitelisting/blacklisting capabilities based on
USB device attributes.

%package -n %{lname}
Summary:        Library for implementing USB device usage policy
Group:          System/Libraries
Obsoletes:      libusbguard0 < %{version}

%description -n %{lname}
The USBGuard software framework helps to protect your computer against rogue USB
devices by implementing basic whitelisting/blacklisting capabilities based on
USB device attributes.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        tools
Summary:        USBGuard Tools
Group:          System/Management
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains optional tools from the USBGuard
software framework.

%prep
%autosetup -p1 -n usbguard-%{version}

%build
%if 0%{?suse_version} == 1500
export CXX=g++-10
# gcc10 has no gcc10-PIE yet, enforce manually (see boo#1195628 for progress)
export CPPFLAGS='-fPIE'
export LDFLAGS='-pie'
%endif
mkdir -p ./m4
autoreconf -fiv

%configure \
    --disable-silent-rules \
    --with-bundled-catch \
    --with-bundled-pegtl \
    --enable-systemd \
    --with-dbus \
    --disable-static

make %{?_smp_mflags}

%check
# while we specify --with-bundled-catch, it is not there :(
# make check

%install
%make_install INSTALL="install -p"
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rcusbguard

# Install configuration
mkdir -p %{buildroot}%{_sysconfdir}/usbguard
install -p -m 600 %{SOURCE3} %{buildroot}%{_sysconfdir}/usbguard/usbguard-daemon.conf

# zsh completion, currently needs manual intervention
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -p -m 644 scripts/usbguard-zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_usbguard

# turn off system call filtering in Leap 15.X, as it interferes with daemon start up (boo#1173750)
%if 0%{?suse_version} == 1500 && 0%{?is_opensuse}
  sed -i '/^SystemCallFilter=@system-service/d' %{buildroot}%{_unitdir}/usbguard.service
%endif

# Cleanup
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -delete

%preun
%service_del_preun usbguard.service usbguard-dbus.service

%post
%service_add_post usbguard.service usbguard-dbus.service

%postun
%service_del_postun usbguard.service usbguard-dbus.service

%pre
%service_add_pre usbguard.service usbguard-dbus.service

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc README.adoc CHANGELOG.md
%license LICENSE
%{_sbindir}/usbguard-daemon
%dir %{_localstatedir}/log/usbguard
%dir %{_sysconfdir}/usbguard
%{_sbindir}/rcusbguard
%{_sbindir}/usbguard-dbus
%dir %{_sysconfdir}/usbguard/IPCAccessControl.d
%config(noreplace) %attr(0600,-,-) %{_sysconfdir}/usbguard/usbguard-daemon.conf
%config(noreplace) %attr(0600,-,-) %{_sysconfdir}/usbguard/rules.conf
%{_unitdir}/usbguard.service
%{_unitdir}/usbguard-dbus.service
%{_mandir}/man8/usbguard-daemon.8%{?ext_man}
%{_mandir}/man8/usbguard-dbus.8%{?ext_man}
%{_mandir}/man5/usbguard-daemon.conf.5%{?ext_man}
%{_mandir}/man5/usbguard-rules.conf.5%{?ext_man}
%{_datadir}/bash-completion/completions/usbguard
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_usbguard
%{_datadir}/dbus-1/system-services/org.usbguard1.service
%{_datadir}/dbus-1/system.d/org.usbguard1.conf
%{_datadir}/polkit-1/actions/org.usbguard1.policy

%files -n %{lname}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/usbguard
%{_bindir}/usbguard-rule-parser
%{_mandir}/man1/usbguard.1%{?ext_man}

%changelog
