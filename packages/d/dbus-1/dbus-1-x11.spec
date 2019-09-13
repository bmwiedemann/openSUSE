#
# spec file for package dbus-1-x11
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   dbus
%define _libname libdbus-1-3
%if 0%{?suse_version} <= 1320
%define _userunitdir %{_prefix}/lib/systemd/user
%endif
%bcond_without selinux
Name:           dbus-1-x11
Version:        1.12.12
Release:        0
Summary:        D-Bus Message Bus System
License:        GPL-2.0-or-later OR AFL-2.1
Group:          System/Daemons
URL:            http://dbus.freedesktop.org/
Source0:        http://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.gz
Source2:        dbus-1.desktop
Source3:        dbus_at_console.ck
Source4:        baselibs.conf
Patch0:         feature-suse-log-deny.patch
# PATCH-FIX-OPENSUSE coolo@suse.de -- force a feature configure won't accept without x11 in buildrequires
Patch1:         feature-suse-do-autolaunch.patch
# Patch-Feature-opensuse sflees@suse.de, users shouldn't be allowed to start / stop the dbus service.
Patch2:         feature-suse-refuse-manual-start-stop.patch
# PATCH-FIX-UPSTREAM
Patch3:         dbus-no-ax-check.patch
# PATCH-FIX-UPSTREAM tchvatal@suse.com -- work with new autoconf-archive
Patch4:         dbus-new-autoconf-archive.patch
BuildRequires:  autoconf-archive
BuildRequires:  libcap-ng-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(x11)
Requires(post): update-alternatives
Requires(preun): update-alternatives
Supplements:    packageand(dbus-1:libX11-6)
Provides:       dbus-launch
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif

%description
D-Bus contains some tools that require Xlib to be installed, those are
in this separate package so server systems need not install X.

%prep
%setup -q -n %{_name}-%{version}
%autopatch -p1

%build
echo 'HTML_TIMESTAMP=NO' >> Doxyfile.in
autoreconf -fi
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
    --with-x
make %{?_smp_mflags}

%install
tdir=$(mktemp -d)
make DESTDIR=$tdir install
mkdir -p %{buildroot}/%{_bindir}
mv $tdir/%{_bindir}/dbus-launch %{buildroot}/%{_bindir}/dbus-launch.x11
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/dbus-launch %{buildroot}%{_bindir}/dbus-launch

%post
%{_sbindir}/update-alternatives --install %{_bindir}/dbus-launch dbus-launch %{_bindir}/dbus-launch.x11 20

%preun
if [ "$1" = 0 ] ; then
  %{_sbindir}/update-alternatives --remove dbus-launch %{_bindir}/dbus-launch.x11
fi

%files
%ghost %{_sysconfdir}/alternatives/dbus-launch
%{_bindir}/dbus-launch
%{_bindir}/dbus-launch.x11

%changelog
