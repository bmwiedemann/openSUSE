#
# spec file for package terminology-theme-dark
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


%define theme_name Dark

Name:           terminology-theme-dark
Version:        20220216.1.26
Release:        0
Summary:        Old default theme for Terminology
License:        BSD-2-Clause AND LGPL-2.1-only AND CC-BY-SA-3.0
URL:            https://en.opensuse.org/Portal:Enlightenment
Source:         terminology-theme-%{theme_name}-%{version}.tar.xz
BuildRequires:  ImageMagick
BuildRequires:  edje
BuildRequires:  python3-base
Requires:       terminology
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       terminology-theme

%description
Old default theme for Terminology

%prep
%setup -q -n terminology-theme-%{theme_name}-%{version}

%build
./build-darkmod.sh --termpkg
cp licenses-authors/* .

%install
install -m 0755 -d %{buildroot}%{_datadir}/terminology/themes
install -m 0644 -t %{buildroot}%{_datadir}/terminology/themes artifacts/bin-term/Dark.edj
install -m 0755 -d %{buildroot}%{_datadir}/terminology/colorschemes
install -m 0644 -t %{buildroot}%{_datadir}/terminology/colorschemes artifacts/bin-term/Dark.eet

%files
%defattr(-,root,root)
%license AUTHORS COPYING
%{_datadir}/terminology

%changelog
