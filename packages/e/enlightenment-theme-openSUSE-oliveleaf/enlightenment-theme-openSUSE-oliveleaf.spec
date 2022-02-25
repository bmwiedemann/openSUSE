#
# spec file for package enlightenment-theme-openSUSE-oliveleaf
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

%define icon_theme_name openSUSE-e-X-Oliveleaf

Name:           enlightenment-theme-openSUSE-oliveleaf
Version:        20220219.1.26
Release:        0
Summary:        Enlightenment theme from openSUSE 13.1
License:        BSD-2-Clause and LGPL-2.1 and CC-BY-SA-3.0
Group:          System/GUI/Other
Url:            https://en.opensuse.org/Portal:Enlightenment
Source:         enlightenment-theme-openSUSE-Oliveleaf-%{version}.tar.xz
# for convert
BuildRequires:  ImageMagick
BuildRequires:  efl
BuildRequires:  fdupes
Provides:       enlightenment-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a darker theme for enlightenment, it was the default for openSUSE 13.1

%package -n openSUSE-e-X-Oliveleaf-Icons
Summary:        FDO Icon theme to go with openSUSE Enlightenment Theme
License:        GPL-3.0-only
Group:          System/GUI/Other

%description -n openSUSE-e-X-Oliveleaf-Icons
An FDO Icon theme that matches the one used by the openSUSE Enlightenment
theme

%prep
%setup -q -n enlightenment-theme-openSUSE-Oliveleaf-%{version}

%build
./build-darkmod.sh --epkg
cp build/e/openSUSE-Oliveleaf.edj .
cp licenses-authors/* .
cp build/icons/openSUSE-Oliveleaf-icons/README README.icons

%install
install -m 0755 -d %{buildroot}%{_datadir}/elementary/themes
install -m 0644 -t %{buildroot}%{_datadir}/elementary/themes openSUSE-Oliveleaf.edj

install -m 0755 -d %{buildroot}%{_datadir}/icons/%{icon_theme_name}
install -m 0644 -t %{buildroot}%{_datadir}/icons/%{icon_theme_name} build/icons/openSUSE-Oliveleaf-icons/index.theme

pushd build/icons/openSUSE-Oliveleaf-icons
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

%fdupes %{buildroot}%{_datadir}/icons/%{icon_theme_name}

%files
%defattr(-,root,root)
%license AUTHORS COPYING AUTHORS.elementary AUTHORS.enlightenment COPYING.images COPYING.lgpl
%{_datadir}/elementary

%files -n openSUSE-e-X-Oliveleaf-Icons
%license README.icons
%{_datadir}/icons/%{icon_theme_name}

%changelog
