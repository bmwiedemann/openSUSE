#
# spec file for package brickd
#
# Copyright (c) 2024 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           brickd
Version:        2.4.6
Release:        0
Summary:        Tinkerforce Brick Daemon
License:        GPL-2.0-only
Group:          System/Daemons
URL:            https://www.tinkerforge.com
Source0:        https://github.com/Tinkerforge/brickd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/Tinkerforge/daemonlib/archive/brickd-%{version}.tar.gz#/daemonlib-%{name}-%{version}.tar.gz
Source2:        brickd-rpmlintrc
Patch0:         harden_brickd-resume.service.patch
Patch1:         harden_brickd.service.patch
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(systemd)
Suggests:       logrotate

%description
Brick Daemon is a small bridge between the USB port of Bricks and
the TCP/IP socket connection to the language binding APIs.

%prep
%setup -q -a 1
mv daemonlib-%{name}-%{version} src/daemonlib
%autopatch -p1

%build
pushd src/brickd
%make_build WITH_SYSTEMD=yes WITH_BRICKLET=no RPM_OPT_FLAGS+=-D_GNU_SOURCE
popd

%install
pushd src/brickd
%make_install WITH_BRICKLET=no
popd
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-resume

%check

%pre
%service_add_pre brickd-resume.service brickd.service

%post
%service_add_post brickd-resume.service brickd.service

%preun
%service_del_preun brickd-resume.service brickd.service

%postun
%service_del_postun brickd-resume.service brickd.service

%files -n %{name}
%doc src/changelog README.rst
%{_bindir}/*
%{_mandir}/man*/%{name}.*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-resume.service
%{_sbindir}/rc%{name}
%{_sbindir}/rc%{name}-resume

%changelog
