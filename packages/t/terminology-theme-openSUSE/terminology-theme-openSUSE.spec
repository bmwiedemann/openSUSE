#
# spec file for package terminology-theme-openSUSE
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


Name:           terminology-theme-openSUSE
Version:        20220430.1.26
Release:        0
Summary:        openSUSE theme for Terminology
License:        BSD-2-Clause AND LGPL-2.1-only AND CC-BY-SA-3.0
Group:          System/X11/Terminals
URL:            https://en.opensuse.org/Portal:Enlightenment
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ImageMagick
BuildRequires:  edje
BuildRequires:  python3-base
Requires:       terminology
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       terminology-theme-dft
Conflicts:      otherproviders(terminology-theme-dft)

%description
openSUSE theme for Terminology

%prep
%setup -q

%build
./build-darkmod.sh --termpkg
cp artifacts/bin-term/openSUSE.edj ./default.edj
cp artifacts/bin-term/openSUSE.eet ./Default.eet
cp licenses-authors/* .

%install
install -m 0755 -d %{buildroot}%{_datadir}/terminology/themes
install -m 0755 -d %{buildroot}%{_datadir}/terminology/colorschemes
install -m 0644 -t %{buildroot}%{_datadir}/terminology/themes default.edj
install -m 0644 -t %{buildroot}%{_datadir}/terminology/colorschemes Default.eet

%files
%defattr(-,root,root)
%license AUTHORS COPYING
%{_datadir}/terminology

%changelog
