#
# spec file for package vifm-colors
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


Name:           vifm-colors
Version:        0.10
Release:        0
Summary:        Color themes for vifm
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/vifm/%{name}/
Source:         https://github.com/vifm/%{name}/archive/v%{version}.tar.gz
#only since 0.8 global color themes are supported
Requires:       vifm >= 0.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Color themes for vifm file manager.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/vifm/colors
cp *.vifm %{buildroot}%{_sysconfdir}/vifm/colors/
chmod 644 %{buildroot}%{_sysconfdir}/vifm/colors/*

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/vifm/
%dir %{_sysconfdir}/vifm/colors/
%config %{_sysconfdir}/vifm/colors/*

%changelog
