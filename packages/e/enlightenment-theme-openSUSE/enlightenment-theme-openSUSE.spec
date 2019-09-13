#
# spec file for package enlightenment-theme-openSUSE
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           enlightenment-theme-openSUSE
Version:        20180511
Release:        0
Summary:        openSUSE theme for Enlightenment
License:        BSD-2-Clause AND LGPL-2.1-only AND CC-BY-SA-3.0
Group:          System/GUI/Other
Url:            https://en.opensuse.org/Portal:Enlightenment
Source:         enlightenment-theme-openSUSE-%{version}.tar.xz
BuildRequires:  edje
# for convert
BuildRequires:  ImageMagick
Requires:       elementary
Provides:       enlightenment-theme
Provides:       enlightenment-theme-dft
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Conflicts:      otherproviders(enlightenment-theme-dft)
# At recomendation of DimStar, add obsoletes but not Provides, this way people being
#  auto upgraded by the enlightenment pattern will be upgraded without any issues and
#  people who have manually installed e17 will be able to keep it
Obsoletes:      e-theme-openSUSE
Obsoletes:      e17-theme-openSUSE

%description
openSUSE, theme for Enlightenment

%prep
%setup -q
#%setup -q -n enlightenment-theme-openSUSE-%{Version}

%build
./build-darkmod.sh --epkg
cp enlightenment-elementary/openSUSE.edj ./default.edj
cp licenses-authors/* .

%install
install -m 0755 -d %{buildroot}%{_datadir}/elementary/themes
install -m 0644 -t %{buildroot}%{_datadir}/elementary/themes default.edj

%files
%defattr(-,root,root)
%doc AUTHORS COPYING AUTHORS.elementary AUTHORS.enlightenment COPYING.images COPYING.lgpl
%{_datadir}/elementary

%changelog
