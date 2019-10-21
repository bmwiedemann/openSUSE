#
# spec file for package brickd
#
# Copyright (c) 2019 Frank Kunz
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.


Name:           brickd
Version:        2.4.0
Release:        0
Summary:        Tinkerforce Brick Daemon
License:        GPL-2.0-only
Group:          System/Daemons
Url:            http://www.tinkerforge.com
Source0:        https://github.com/Tinkerforge/brickd/archive/v2.4.0.tar.gz
Source1:        https://github.com/Tinkerforge/daemonlib/archive/brickd-2.4.0.tar.gz
# backport from upstream
Patch0:         0001-Makefile-Support-DESTDIR-variable.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-use-RPM_OPT_FLAGS-in-rpm-package-builds.patch
Patch2:         0001-systemd-unit-files-are-always-in-prefix-lib-systemd.patch
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(systemd)
Suggests:       logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Brick Daemon is a small bridge between the USB port of Bricks and
the TCP/IP socket connection to the language binding APIs.

%prep
%setup -q -a 1 -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
mv daemonlib-%{name}-%{version} src/daemonlib

%build
pushd src/brickd
make %{?_smp_mflags} WITH_SYSTEMD=yes
popd

%install
pushd src/brickd
make install DESTDIR=%{buildroot}
popd
mkdir -p %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}-resume

%pre
%service_add_pre brickd-resume.service brickd.service

%post
%service_add_post brickd-resume.service brickd.service

%preun
%service_del_preun brickd-resume.service brickd.service

%postun
%service_del_postun brickd-resume.service brickd.service

%files -n %{name}
%defattr(-,root,root)
%doc src/changelog README.rst
%{_bindir}/*
%{_mandir}/man*/%{name}.*
%config(noreplace) /etc/%{name}.conf
%config /etc/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-resume.service
%{_sbindir}/rc%{name}
%{_sbindir}/rc%{name}-resume

%changelog
