#
# spec file for package dbus-1
#
# Copyright (c) 2023 SUSE LLC
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


%define with_systemd 1
%define _name   dbus
%define _libname libdbus-1-3
%bcond_without selinux
Name:           dbus-1
Version:        1.14.6
Release:        0
Summary:        D-Bus Message Bus System
License:        AFL-2.1 OR GPL-2.0-or-later
URL:            https://dbus.freedesktop.org/
Source0:        https://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.xz
Source1:        https://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.xz.asc
Source2:        dbus-1.keyring
Source3:        baselibs.conf
Source4:        dbus-1.desktop
Source5:        messagebus.conf
# PATCH-FEATURE-OPENSUSE feature-suse-log-deny.patch
Patch0:         feature-suse-log-deny.patch
# PATCH-FIX-OPENSUSE coolo@suse.de -- force a feature configure won't accept without x11 in buildrequires
Patch1:         feature-suse-do-autolaunch.patch
# PATCH-FEATURE-OPENSUSE sflees@suse.de, users shouldn't be allowed to start / stop the dbus service.
Patch2:         feature-suse-refuse-manual-start-stop.patch
BuildRequires:  alts
BuildRequires:  audit-devel
BuildRequires:  cmake
BuildRequires:  libcap-ng-devel
BuildRequires:  libexpat-devel >= 2.1.0
BuildRequires:  permissions
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libsystemd) >= 209
Requires:       alts
Requires(post): %{_libname} = %{version}
Requires(post): diffutils
Requires(pre):  permissions
Provides:       dbus-launch = %{version}
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif
Requires:       dbus-1-common >= %{version}
# Later this should move to Recommends
Requires:       dbus-1-tools >= %{version}
# Later on change this to just dbus-broker
Requires:       dbus-service >= %{version}
Recommends:     dbus-1-daemon >= %{version}

%package -n %{_libname}
Summary:        Library package for D-Bus
Requires:       dbus-1-common >= %{version}

%package common
Summary:        D-BUS message bus configuration
BuildArch:      noarch
%sysusers_requires

%package daemon
Summary:        D-Bus message bus daemon
Provides:       dbus-1:%{_bindir}/dbus-daemon
Provides:       dbus-service = %{version}

%package devel
Summary:        Developer package for D-Bus
Requires:       %{_libname} = %{version}
Requires:       dbus-1 = %{version}
Requires:       glibc-devel

%package tools
Summary:        Tools that go along with dbus
Provides:       dbus-1:%{_bindir}/dbus-monitor

%description
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%description -n %{_libname}
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%description common
D-Bus is a message bus system, The dbus-common package provides the configuration and setup files for D-Bus
implementations to provide a System and User Message Bus.

%description daemon
D-Bus is a message bus system, This package contains the original
dbus-daemon to make it easier to switch to dbus-broker

%description devel
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

%description tools
D-Bus is a message bus system, these are some of the tools that go along
with it.

%prep
%setup -q -n %{_name}-%{version}
%autopatch -p1

%build
echo 'HTML_TIMESTAMP=NO' >> Doxyfile.in
# We use -fpie/-pie for the whole build; this is the recommended way to harden
# the build upstream, see discussion in fdo#46570
export CFLAGS="%{optflags} -fno-strict-aliasing -fPIC -fpie"
export LDFLAGS="-pie"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
export V=1
%configure \
    --disable-static \
    --disable-asserts \
    --runstatedir=%{_rundir} \
    --libexecdir=%{_libexecdir}/dbus-1 \
    --enable-inotify \
    --disable-doxygen-docs \
%if %{with selinux}
    --enable-selinux \
%endif
    --enable-systemd \
    --enable-user-session \
    --enable-libaudit \
    --with-console-auth-dir=/run/dbus/at_console/ \
    --with-system-pid-file=/run/dbus/pid \
    --with-system-socket=/run/dbus/system_bus_socket \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-systemduserunitdir=%{_userunitdir} \
    --without-x
%make_build
# The original dbus sysusers config does not create our account,
# overwrite it with our user definition
cp %{SOURCE5} bus/sysusers.d/dbus.conf
%sysusers_generate_pre %{SOURCE5} messagebus dbus.conf

%check
%make_build check

%install
%make_install

# dbus-launch, too
mv -f %{buildroot}/%{_bindir}/dbus-launch %{buildroot}%{_bindir}/dbus-launch.nox11
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service  %{buildroot}/%{_sbindir}/rcdbus
install -d %{buildroot}/run/dbus
mkdir -p %{buildroot}/%{_libdir}/pkgconfig

for i in %{_sysconfdir}/dbus-1/session.d %{_sysconfdir}/dbus-1/system.d \
       %{_datadir}/dbus-1/interfaces %{_datadir}/dbus-1/services \
       %{_datadir}/dbus-1/system.d %{_datadir}/dbus-1/system-services; do
  mkdir -p %{buildroot}$i
done

mkdir -p %{buildroot}%{_localstatedir}/lib/dbus

# create entries for libalternatives
ln -sf %{_bindir}/alts %{buildroot}%{_bindir}/dbus-launch
mkdir -p %{buildroot}%{_datadir}/libalternatives/dbus-launch
cat > %{buildroot}%{_datadir}/libalternatives/dbus-launch/10.conf <<EOF
binary=%{_bindir}/dbus-launch.nox11
group=dbus-launch
EOF

find %{buildroot} -type f -name "*.la" -delete -print

rm -Rf %{buildroot}%{_datadir}/doc/dbus

%verifyscript -n dbus-1
%verify_permissions -e %{_libexecdir}/dbus-1/dbus-daemon-launch-helper

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig

%pre
%service_add_pre dbus.service
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
    %{_sbindir}/update-alternatives --remove dbus-launch %{_bindir}/dbus-launch.nox11
fi

%post
/sbin/ldconfig
%set_permissions %{_libexecdir}/dbus-1/dbus-daemon-launch-helper
%service_add_post dbus.service

%preun
%service_del_preun dbus.service

%postun
%service_del_postun_without_restart dbus.service

%pre common -f messagebus.pre
%service_add_pre dbus.socket

%post common
if [ -e %{_localstatedir}/lib/dbus/machine-id -a -e %{_sysconfdir}/machine-id ]; then
  cmp -s %{_localstatedir}/lib/dbus/machine-id %{_sysconfdir}/machine-id > /dev/null
  if [ $? ]; then
    rm -f %{_localstatedir}/lib/dbus/machine-id
  fi
fi
if [ ! -L %{_localstatedir}/lib/dbus/machine-id ]; then
  mkdir -p %{_localstatedir}/lib/dbus/
  ln -s %{_sysconfdir}/machine-id %{_localstatedir}/lib/dbus/machine-id
fi
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/dbus.conf
%service_add_post dbus.socket

%preun common
%service_del_preun dbus.socket

%postun common
%service_del_postun_without_restart dbus.socket

%files
%dir %{_libexecdir}/dbus-1/
%license COPYING
%doc AUTHORS NEWS README

# See doc/system-activation.txt in source tarball for the rationale
# behind these permissions
%attr(4750,root,messagebus) %verify(not mode) %{_libexecdir}/dbus-1/dbus-daemon-launch-helper
%{_unitdir}/dbus.service
%{_sbindir}/rcdbus
%dir %{_unitdir}/multi-user.target.wants
%{_unitdir}/multi-user.target.wants/dbus.service
%{_userunitdir}/dbus.service
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/dbus-launch
%{_datadir}/libalternatives/dbus-launch/10.conf
%{_bindir}/dbus-launch.nox11
%{_bindir}/dbus-launch
%{_mandir}/man1/dbus-launch.1%{?ext_man}

%files -n %{_libname}
%{_libdir}/libdbus-1.so.*

%files common
%dir %{_localstatedir}/lib/dbus
%ghost /run/dbus
%ghost %{_localstatedir}/lib/dbus/machine-id
%config(noreplace) %{_sysconfdir}/dbus-1/session.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.conf
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/session.d
%dir %{_sysconfdir}/dbus-1/system.d
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/interfaces
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/dbus-1/system.d
%dir %{_datadir}/dbus-1/system-services
%dir %{_userunitdir}/sockets.target.wants
%{_userunitdir}/sockets.target.wants/dbus.socket
%dir %{_unitdir}/sockets.target.wants
%{_unitdir}/sockets.target.wants/dbus.socket
%{_prefix}/lib/sysusers.d/dbus.conf
%{_prefix}/lib/tmpfiles.d/dbus.conf
%{_datadir}/dbus-1/session.conf
%{_datadir}/dbus-1/system.conf
%{_unitdir}/dbus.socket
%{_userunitdir}/dbus.socket

%files daemon
%{_bindir}/dbus-cleanup-sockets
%{_bindir}/dbus-daemon
%{_bindir}/dbus-run-session
%{_bindir}/dbus-test-tool
%{_mandir}/man1/dbus-cleanup-sockets.1%{?ext_man}
%{_mandir}/man1/dbus-daemon.1%{?ext_man}
%{_mandir}/man1/dbus-run-session.1%{?ext_man}
%{_mandir}/man1/dbus-test-tool.1%{?ext_man}

%files devel
%{_includedir}/*
%{_libdir}/libdbus-1.so
%dir %{_libdir}/dbus-1.0
%{_libdir}/dbus-1.0/include
%{_libdir}/pkgconfig/dbus-1.pc
%{_libdir}/cmake/DBus1
%{_datadir}/xml/dbus-1

%files tools
%{_bindir}/dbus-monitor
%{_bindir}/dbus-send
%{_bindir}/dbus-update-activation-environment
%{_bindir}/dbus-uuidgen
%{_mandir}/man1/dbus-monitor.1%{?ext_man}
%{_mandir}/man1/dbus-send.1%{?ext_man}
%{_mandir}/man1/dbus-update-activation-environment.1%{?ext_man}
%{_mandir}/man1/dbus-uuidgen.1%{?ext_man}

%changelog
