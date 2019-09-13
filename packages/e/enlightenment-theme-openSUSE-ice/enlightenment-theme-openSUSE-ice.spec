#
# spec file for package enlightenment-theme-openSUSE-ice
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           enlightenment-theme-openSUSE-ice
Version:        20161028
Release:        0
Summary:        A light openSUSE theme modified to suite the openSUSE 13.2 artwork
License:        BSD-2-Clause and LGPL-2.1 and CC-BY-SA-3.0
Group:          System/GUI/Other
Url:            https://en.opensuse.org/Portal:Enlightenment
Source:         enlightenment-theme-openSUSE-ice-%{version}.tar.xz
# for convert
BuildRequires:  ImageMagick
BuildRequires:  edje
Requires:       elementary
Provides:       enlightenment-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Ice is a light theme for enlightenment, this version has been modified to suite the artwork for openSUSE 13.2

%prep
%setup -q -n enlightenment-theme-openSUSE-ice-%{version}

%build
./build-darkmod.sh --epkg
cp enlightenment-elementary/openSUSE-ice.edj .
cp licenses-authors/* .

%install
install -m 0755 -d %{buildroot}%{_datadir}/elementary/themes
install -m 0644 -t %{buildroot}%{_datadir}/elementary/themes openSUSE-ice.edj

%files
%defattr(-,root,root)
%doc AUTHORS COPYING AUTHORS.elementary AUTHORS.enlightenment COPYING.images COPYING.lgpl
%{_datadir}/elementary

%changelog
