#
# spec file for package dbus-1
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.12.20
Release:        0
Summary:        D-Bus Message Bus System
License:        GPL-2.0-or-later OR AFL-2.1
URL:            https://dbus.freedesktop.org/
Source0:        http://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.gz
Source1:        http://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.gz.asc
Source2:        dbus-1.keyring
Source3:        baselibs.conf
Source4:        dbus-1.desktop
Source5:        messagebus.conf
Patch0:         feature-suse-log-deny.patch
# PATCH-FIX-OPENSUSE coolo@suse.de -- force a feature configure won't accept without x11 in buildrequires
Patch1:         feature-suse-do-autolaunch.patch
# Patch-Feature-opensuse sflees@suse.de, users shouldn't be allowed to start / stop the dbus service.
Patch2:         feature-suse-refuse-manual-start-stop.patch
BuildRequires:  audit-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libexpat-devel >= 2.1.0
BuildRequires:  permissions
BuildRequires:  pkgconfig
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libsystemd) >= 209
Requires(post): %{_libname} = %{version}
Requires(post): update-alternatives
Requires(post): diffutils
Requires(pre):  permissions
Requires(preun): update-alternatives
Provides:       dbus-launch
%sysusers_requires
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif

%package -n %{_libname}
Summary:        Library package for D-Bus

%package devel
Summary:        Developer package for D-Bus
Requires:       %{_libname} = %{version}
Requires:       dbus-1 = %{version}
Requires:       glibc-devel

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

%description devel
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-Bus supplies both a system daemon and a
per-user-login-session daemon. Also, the message bus is built on top of
a general one-to-one message passing framework, which can be used by
any two apps to communicate directly (without going through the message
bus daemon).

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
%sysusers_generate_pre %{SOURCE5} messagebus

%check
%make_build check

%install
%make_install

mkdir -p %{buildroot}/lib/dbus-1/system-services
# dbus-launch, too
mv -f %{buildroot}/%{_bindir}/dbus-launch %{buildroot}%{_bindir}/dbus-launch.nox11
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service  %{buildroot}/%{_sbindir}/rcdbus
install -d %{buildroot}/run/dbus
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
mkdir -p %{buildroot}/lib/dbus-1/system-services

for i in %{_sysconfdir}/dbus-1/session.d %{_sysconfdir}/dbus-1/system.d \
       %{_datadir}/dbus-1/interfaces %{_datadir}/dbus-1/services \
       %{_datadir}/dbus-1/system.d %{_datadir}/dbus-1/system-services; do
  mkdir -p %{buildroot}$i
done

mkdir -p %{buildroot}%{_localstatedir}/lib/dbus

%if !0%{?usrmerged}
# Link the binaries that were in /bin back to /bin for compat (maybe remove for SLE-16)
# Currently required to make upower work together with systemd
mkdir -p %{buildroot}/bin

ln -sf /%{_bindir}/dbus-cleanup-sockets %{buildroot}/bin/dbus-cleanup-sockets
ln -sf /%{_bindir}/dbus-daemon %{buildroot}/bin/dbus-daemon
ln -sf /%{_bindir}/dbus-monitor %{buildroot}/bin/dbus-monitor
ln -sf /%{_bindir}/dbus-send %{buildroot}/bin/dbus-send
ln -sf /%{_bindir}/dbus-test-tool %{buildroot}/bin/dbus-test-tool
ln -sf /%{_bindir}/dbus-update-activation-environment %{buildroot}/bin/dbus-update-activation-environment
ln -sf /%{_bindir}/dbus-uuidgen %{buildroot}/bin/dbus-uuidgen
%endif

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/dbus-launch %{buildroot}%{_bindir}/dbus-launch

find %{buildroot} -type f -name "*.la" -delete -print

rm -Rf %{buildroot}%{_datadir}/doc/dbus

%verifyscript -n dbus-1
%verify_permissions -e %{_libexecdir}/dbus-1/dbus-daemon-launch-helper

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig
%pre -f messagebus.pre
%service_add_pre dbus.service dbus.socket

%post
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

/sbin/ldconfig
%set_permissions %{_libexecdir}/dbus-1/dbus-daemon-launch-helper
%{_sbindir}/update-alternatives --install %{_bindir}/dbus-launch dbus-launch %{_bindir}/dbus-launch.nox11 10
%service_add_post dbus.service dbus.socket
%tmpfiles_create %{_prefix}/lib/tmpfiles.d/dbus.conf

%preun
if [ "$1" = 0 ] ; then
  %{_sbindir}/update-alternatives --remove dbus-launch %{_bindir}/dbus-launch.nox11
fi
%service_del_preun dbus.service dbus.socket

%postun
%service_del_postun_without_restart dbus.service dbus.socket

%files
%dir %{_localstatedir}/lib/dbus
%dir /lib/dbus-1
%dir /lib/dbus-1/system-services
%dir %{_libexecdir}/dbus-1/
%license COPYING
%doc AUTHORS NEWS README
%config(noreplace) %{_sysconfdir}/dbus-1/session.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.conf
%{_datadir}/dbus-1/session.conf
%{_datadir}/dbus-1/system.conf
%{_bindir}/dbus-cleanup-sockets
%{_bindir}/dbus-daemon
%{_bindir}/dbus-monitor
%{_bindir}/dbus-run-session
%{_bindir}/dbus-send
%{_bindir}/dbus-test-tool
%{_bindir}/dbus-update-activation-environment
%{_bindir}/dbus-uuidgen
%if !0%{?usrmerged}
/bin/dbus-cleanup-sockets
/bin/dbus-daemon
/bin/dbus-monitor
/bin/dbus-send
/bin/dbus-test-tool
/bin/dbus-update-activation-environment
/bin/dbus-uuidgen
%endif
%{_mandir}/man1/dbus-cleanup-sockets.1%{?ext_man}
%{_mandir}/man1/dbus-daemon.1%{?ext_man}
%{_mandir}/man1/dbus-monitor.1%{?ext_man}
%{_mandir}/man1/dbus-run-session.1%{?ext_man}
%{_mandir}/man1/dbus-send.1%{?ext_man}
%{_mandir}/man1/dbus-test-tool.1%{?ext_man}
%{_mandir}/man1/dbus-update-activation-environment.1%{?ext_man}
%{_mandir}/man1/dbus-uuidgen.1%{?ext_man}
%{_mandir}/man1/dbus-launch.1%{?ext_man}
%{_sbindir}/rcdbus
# See doc/system-activation.txt in source tarball for the rationale
# behind these permissions
%attr(4750,root,messagebus) %verify(not mode) %{_libexecdir}/dbus-1/dbus-daemon-launch-helper
%ghost /run/dbus
%ghost %{_localstatedir}/lib/dbus/machine-id
%{_prefix}/lib/sysusers.d/dbus.conf
%{_prefix}/lib/tmpfiles.d/dbus.conf
%{_unitdir}/dbus.service
%{_unitdir}/dbus.socket
# %%dir %%{_unitdir}/dbus.target.wants
# %%{_unitdir}/dbus.target.wants/dbus.socket
%dir %{_unitdir}/multi-user.target.wants
%{_unitdir}/multi-user.target.wants/dbus.service
%dir %{_unitdir}/sockets.target.wants
%{_unitdir}/sockets.target.wants/dbus.socket
%{_userunitdir}/dbus.service
%{_userunitdir}/dbus.socket
%dir %{_userunitdir}/sockets.target.wants
%{_userunitdir}/sockets.target.wants/dbus.socket
%ghost %{_sysconfdir}/alternatives/dbus-launch
%{_bindir}/dbus-launch.nox11
%{_bindir}/dbus-launch

%files -n %{_libname}
%{_libdir}/libdbus-1.so.*
# Own those directories in the library instead of dbus-1, since dbus users
# often ship files there
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/session.d
%dir %{_sysconfdir}/dbus-1/system.d
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/interfaces
%dir %{_datadir}/dbus-1/services
%dir %{_datadir}/dbus-1/system.d
%dir %{_datadir}/dbus-1/system-services

%files devel
%{_includedir}/*
%{_libdir}/libdbus-1.so
%dir %{_libdir}/dbus-1.0
%{_libdir}/dbus-1.0/include
%{_libdir}/pkgconfig/dbus-1.pc
%{_libdir}/cmake/
%{_datadir}/xml/dbus-1

%changelog
