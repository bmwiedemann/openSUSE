#
# spec file for package labwc-themes
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           labwc-themes
Version:        0.1.0
Release:        0
Summary:        Server-Side Decoration themes for labwc
License:        CC-BY-SA-4.0
URL:            https://github.com/labwc/labwc-themes
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  meson
Requires:       labwc

%description
A collection of Server-Side Decoration (SSD) themes for labwc, 
designed to complement popular desktop themes and icon sets.

%prep
%autosetup

%build
%meson

%install
%meson_install

%fdupes %{buildroot}%{_datadir}/themes/

%files
%license LICENSE
%{_datadir}/themes/lab*/

%changelog
