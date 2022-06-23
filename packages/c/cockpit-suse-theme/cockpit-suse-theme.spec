#
# spec file for package cockpit-suse-theme
#
# Copyright (c) 2022 SUSE LLC
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


Name:           cockpit-suse-theme
Version:        0.1
Release:        0
Summary:        A Cockpit green-ish theme
Source:         %{name}-%{version}.tar.xz
Url:            https://github.com/dgdavid/cockpit-suse-theme
License:        MIT

Requires:       cockpit-ws
BuildRequires:  cockpit-ws
BuildArch:      noarch

%description
A package holding needed resources for changing Cockpit styling to match the
SUSE look&feel by using the workaround described at
https://github.com/cockpit-project/cockpit/pull/17437

Intended changes only take effect when using a Cockpit version patched for
loading the CSS overrides file in each HTML page.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/cockpit/branding/default
cp src/css-overrides.css %{buildroot}%{_datadir}/cockpit/branding/default
cp src/fonts.css %{buildroot}%{_datadir}/cockpit/branding/default
cp -a src/fonts %{buildroot}%{_datadir}/cockpit/branding/default

%files
%dir %{_datadir}/cockpit
%{_datadir}/cockpit/branding/default/*

%changelog
