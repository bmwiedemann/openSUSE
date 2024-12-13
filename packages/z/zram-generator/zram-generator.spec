#
# spec file for package zram-generator
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


%global _systemd_util_dir /usr/lib/systemd

Name:           zram-generator
Version:        1.2.1
Release:        0
Summary:        Systemd unit generator for zram swap devices
License:        MIT
Group:          Development/Libraries/Rust

# Upstream license specification: MIT
URL:            https://github.com/systemd/zram-generator
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz

# pregenerated man-pages to avoid dependency on ronn
Source2:        zram-generator.conf.5
Source3:        zram-generator.8

BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(systemd)

%description
This is a systemd unit generator that enables swap on zram.
(With zram, there is no physical swap device. Part of the avaialable RAM
is used to store compressed pages, essentially trading CPU cycles for memory.)

To configure and activate swap and zram devices with file-systems,  create a configuration file in /etc/systemd/zram-generator.conf. You can consult  %{_datadir}/doc/%{name}/zram-generator.conf.example for an example and a list of available settings.

%prep
%autosetup -a1 -p1 -n %{name}-%{version}
cp %{SOURCE2} man/
cp %{SOURCE3} man/

%build
export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
export LC_ALL=C.UTF-8
%{cargo_build}

%make_build SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir} SYSTEMD_SYSTEM_GENERATOR_DIR=%{_systemdgeneratordir} systemd-service

%install
%make_install SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir} SYSTEMD_SYSTEM_GENERATOR_DIR=%{_systemdgeneratordir} NOBUILD=1

%check
export SYSTEMD_UTIL_DIR=%{_systemd_util_dir}
%{cargo_test}

%files
%doc README.md
%dir %{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}/zram-generator.conf.example
%dir %{_systemdgeneratordir}
%{_systemdgeneratordir}/zram-generator
%{_unitdir}/systemd-zram-setup@.service
%{_mandir}/man8/zram-generator.8*
%{_mandir}/man5/zram-generator.conf.5*

%changelog
