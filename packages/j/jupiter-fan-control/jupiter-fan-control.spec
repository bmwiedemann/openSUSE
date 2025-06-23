#
# spec file for package jupiter-fan-control
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

Name:           jupiter-fan-control
Version:        20240523.3
Release:        0
Summary:        Steam Deck Fan Controller
License:        GPL-3.0-or-later
URL:            https://gitlab.com/evlaV/jupiter-fan-control
Source0:        jupiter-fan-control-%{version}.tar.xz
Patch0:         rpm.patch
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
Requires:       python3
Requires:       python3-PyYAML
BuildArch:      noarch

%description
SteamOS 3.0 Steam Deck Fan Controller

%prep
%autosetup -n %{name}-%{version} -p1

%build

%install
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_datadir}/jupiter-fan-control
mkdir -p %{buildroot}%{_libexecdir}/jupiter-fan-control
cp -v usr/share/jupiter-fan-control/*.yaml %{buildroot}%{_datadir}/jupiter-fan-control/
cp -v usr/share/jupiter-fan-control/*.py %{buildroot}%{_libexecdir}/jupiter-fan-control/
chmod +x %{buildroot}%{_libexecdir}/jupiter-fan-control/PID.py
cp -v usr/lib/systemd/system/jupiter-fan-control.service %{buildroot}%{_unitdir}/jupiter-fan-control.service

%pre
%systemd_pre jupiter-fan-control.service

%post
%systemd_post jupiter-fan-control.service

%preun
%systemd_preun jupiter-fan-control.service

%postun
%systemd_postun_with_restart jupiter-fan-control.service

%files
%doc README.md
%dir %{_libexecdir}/jupiter-fan-control
%{_libexecdir}/jupiter-fan-control/fancontrol.py
%{_libexecdir}/jupiter-fan-control/PID.py
%dir %{_datadir}/jupiter-fan-control
%{_datadir}/jupiter-fan-control/*.yaml
%{_unitdir}/jupiter-fan-control.service

%changelog
