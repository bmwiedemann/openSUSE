#
# spec file for package enlightenment-theme-openSUSE
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define icon-theme-name openSUSE-e-X-Neon

Name:           enlightenment-theme-openSUSE-neon
Version:        20200101
Release:        0
Summary:        openSUSE theme for Enlightenment
License:        BSD-2-Clause and LGPL-2.1 and CC-BY-SA-3.0
Group:          System/GUI/Other
Url:            https://en.opensuse.org/Portal:Enlightenment
Source:         enlightenment-theme-openSUSE-Neon-%{version}.tar.xz
BuildRequires:  edje
# for convert
BuildRequires:  ImageMagick
Requires:       elementary
Provides:       enlightenment-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# At recomendation of DimStar, add obsoletes but not Provides, this way people being
#  auto upgraded by the enlightenment pattern will be upgraded without any issues and
#  people who have manually installed e17 will be able to keep it
Obsoletes:      e-theme-openSUSE
Obsoletes:      e17-theme-openSUSE

%description
openSUSE, theme for Enlightenment

%package -n openSUSE-e-X-Neon-Icons
Summary:        FDO Icon theme to go with openSUSE Enlightenment Theme
License:        GPL-3.0-only
Group:          System/GUI/Other

%description -n openSUSE-e-X-Neon-Icons
An FDO Icon theme that matches the one used by the openSUSE Enlightenment
theme

%prep
%setup -q -n enlightenment-theme-openSUSE-Neon-%{version}

%build
./build-darkmod.sh --epkg
cp enlightenment-elementary/openSUSE-Neon.edj .
cp licenses-authors/* .
cp openSUSE-Neon-icons/README README.icons

%install
install -m 0755 -d %{buildroot}%{_datadir}/elementary/themes
install -m 0644 -t %{buildroot}%{_datadir}/elementary/themes openSUSE-Neon.edj
install -m 0755 -d %{buildroot}%{_datadir}/icons/%{icon_theme_name}
install -m 0644 -t %{buildroot}%{_datadir}/icons/%{icon_theme_name} openSUSE-Neon-icons/index.theme

pushd openSUSE-Neon-icons
for d in */ ; do
    install -m 0755 -d %{buildroot}%{_datadir}/icons/%{icon_theme_name}/$d
    for in in $d/*/ ; do
      install -m 0755 -d %{buildroot}%{_datadir}/icons/%{icon_theme_name}/$in
      for ind in $in/*.png ; do
        if [ -f "$ind" ]; then
          install -m 0644 -t %{buildroot}%{_datadir}/icons/%{icon_theme_name}/$in "$ind"
        fi
      done
      for ind in $in/*.svg ; do
        if [ -f "$ind" ]; then
          install -m 0644 -t %{buildroot}%{_datadir}/icons/%{icon_theme_name}/$in "$ind"
        fi
      done
    done
done
popd

%files
%defattr(-,root,root)
%doc AUTHORS COPYING AUTHORS.elementary AUTHORS.enlightenment COPYING.images COPYING.lgpl
%{_datadir}/elementary

%files -n openSUSE-e-X-Neon-Icons
%license README.icons
%{_datadir}/icons/%{icon_theme_name}

%changelog
