#
# spec file for package dbus-1-devel-doc
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
# Temporary code to disable service restart on update sflees@suse.de boo#1020301
%global _backup %{_sysconfdir}/sysconfig/services.rpmbak.%{name}-%{version}-%{release}
%bcond_without selinux
Name:           dbus-1-devel-doc
Version:        1.14.6
Release:        0
Summary:        Developer documentation package for D-Bus
License:        AFL-2.1 OR GPL-2.0-or-later
URL:            https://dbus.freedesktop.org/
Source0:        https://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.xz
Source1:        https://dbus.freedesktop.org/releases/dbus/%{_name}-%{version}.tar.xz.asc
Source2:        dbus-1.keyring
Source3:        baselibs.conf
Source4:        dbus-1.desktop

# PATCH-FEATURE-OPENSUSE feature-suse-log-deny.patch
Patch0:         feature-suse-log-deny.patch
# PATCH-FIX-OPENSUSE coolo@suse.de -- force a feature configure won't accept without x11 in buildrequires
Patch1:         feature-suse-do-autolaunch.patch
# PATCH-FEATURE-OPENSUSE sflees@suse.de, users shouldn't be allowed to start / stop the dbus service.
Patch2:         feature-suse-refuse-manual-start-stop.patch

BuildRequires:  doxygen
BuildRequires:  libexpat-devel >= 2.1.0
BuildRequires:  xmlto
Requires:       dbus-1 = %{version}
BuildArch:      noarch

%description
D-Bus is a message bus system, a simple way for applications to talk to
one another. D-BUS supplies both a system daemon and a
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
    --disable-asserts \
    --libexecdir=%{_libexecdir}/dbus-1 \
    --runstatedir=%{_rundir} \
    --enable-doxygen-docs \
    --with-console-auth-dir=/run/dbus/at_console/ \
    --with-system-pid-file=/run/dbus/pid \
    --with-system-socket=/run/dbus/system_bus_socket \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-systemduserunitdir=%{_userunitdir} \
    --without-x

doxygen -u
%make_build -C doc

%install
%make_install -C doc

# Remove manpages for commandline tools (shipped in main package)
rm -Rf %{buildroot}/%{_mandir}/man1/*
rmdir -p --ignore-fail-on-non-empty %{buildroot}/%{_mandir}/man1

# Remove DTDs and xml catalog (shipped in devel subpackage)
rm -Rf %{buildroot}/%{_datadir}/xml/dbus-1/*dtd
rm -Rf %{buildroot}/%{_datadir}/xml/dbus-1/*.xml
rmdir -p --ignore-fail-on-non-empty %{buildroot}/%{_datadir}/xml/dbus-1

mkdir -p %{buildroot}/%{_datadir}/susehelp/meta/Development/Libraries/
install -m 0644 %{SOURCE4} \
    %{buildroot}/%{_datadir}/susehelp/meta/Development/Libraries/dbus-1.desktop
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
mkdir -p %{buildroot}/lib/dbus-1/system-services

mkdir -p %{buildroot}%{_datadir}/doc/dbus/examples/
install -m 0644 tools/GetAllMatchRules.py %{buildroot}%{_datadir}/doc/dbus/examples/
install -m 0644 bus/example-*-stats.conf %{buildroot}%{_datadir}/doc/dbus/examples/

%files
%dir %{_datadir}/doc/dbus
%dir %{_datadir}/doc/dbus/examples
%{_datadir}/doc/dbus/api/
%doc %{_datadir}/doc/dbus/dbus-faq.html
%doc %{_datadir}/doc/dbus/dbus-specification.html
%doc %{_datadir}/doc/dbus/dbus-test-plan.html
%doc %{_datadir}/doc/dbus/dbus-tutorial.html
%doc %{_datadir}/doc/dbus/diagram.*
%doc %{_datadir}/doc/dbus/system-activation.txt
%doc %{_datadir}/doc/dbus/dbus-cleanup-sockets.1.html
%doc %{_datadir}/doc/dbus/dbus-daemon.1.html
%doc %{_datadir}/doc/dbus/dbus-launch.1.html
%doc %{_datadir}/doc/dbus/dbus-run-session.1.html
%doc %{_datadir}/doc/dbus/dbus-monitor.1.html
%doc %{_datadir}/doc/dbus/dbus-send.1.html
%doc %{_datadir}/doc/dbus/dbus-uuidgen.1.html
%doc %{_datadir}/doc/dbus/dbus.devhelp2
%doc %{_datadir}/doc/dbus/dbus-test-tool.1.html
%doc %{_datadir}/doc/dbus/dbus-update-activation-environment.1.html
%doc %{_datadir}/doc/dbus/examples/GetAllMatchRules.py
%doc %{_datadir}/doc/dbus/examples/example-session-disable-stats.conf
%doc %{_datadir}/doc/dbus/examples/example-system-enable-stats.conf
%doc doc/*.txt doc/file-boilerplate.c doc/TODO
%{_datadir}/susehelp

%changelog
