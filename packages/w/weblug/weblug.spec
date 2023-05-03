#
# spec file for package weblug
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


Name:           weblug
Version:        0.3
Release:        0
Summary:        Simple webhook receiver program
License:        MIT
URL:            https://codeberg.org/grisu48/weblug
Source:         weblug-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  go1.18
%{go_nostrip}
%{systemd_ordering}

%description
Simple webhook receiver program

%prep
%autosetup -D -a 1

%build
make all GOARGS="-mod vendor -buildmode pie"

%install
install -Dm 755 weblug %{buildroot}/%{_bindir}/weblug
# systemd unit
install -Dpm0644 weblug.service %{buildroot}%{_unitdir}/weblug.service
# configuration file (/etc/weblug.yml)
mkdir -p %{buildroot}%{_sysconfdir}
install -m 600 weblug.yml %{buildroot}%{_sysconfdir}/weblug.yml
# man page
install -Dm 644 doc/weblug.8 %{buildroot}/%{_mandir}/man8/weblug.8

%pre
%service_add_pre weblug.service

%preun
%service_del_preun weblug.service

%post
%service_add_post weblug.service

%postun
%service_del_postun weblug.service

%files
%doc README.md
%license LICENSE
%{_bindir}/weblug
%{_unitdir}/weblug.service
%config %{_sysconfdir}/weblug.yml
%{_mandir}/man8/weblug.8%{?ext_man}

%changelog
