#
# spec file for package aeon-check
#
# Copyright (c) 2025 SUSE LLC
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


Name:           aeon-check
Version:        1.0.3
Release:        0
Summary:        Aeon Check and Repair Tool
License:        MIT
URL:            https://github.com/AeonDesktop/aeon-check
Source:         %{name}-%{version}.tar.xz
BuildArch:      noarch

%description
Automatically checks and repairs known issues in Aeon installations at boot

%prep
%autosetup

%build

%install
install -D -m 700 aeon-check %{buildroot}%{_sbindir}/aeon-check
install -D -m 644 aeon-check.service %{buildroot}%{_unitdir}/aeon-check.service

%pre
%systemd_pre aeon-check.service

%post
%systemd_post aeon-check.service

%preun
%systemd_preun aeon-check.service

%postun
%systemd_postun aeon-check.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/aeon-check
%{_unitdir}/aeon-check.service

%changelog
