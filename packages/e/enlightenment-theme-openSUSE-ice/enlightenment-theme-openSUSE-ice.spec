#
# spec file for package enlightenment-theme-openSUSE-ice
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


%define icon_theme_name openSUSE-e-X-Ice

Name:           enlightenment-theme-openSUSE-ice
Version:        20200529
Release:        0
Summary:        A light openSUSE theme modified to suite the openSUSE 13.2 artwork
License:        BSD-2-Clause AND LGPL-2.1-only AND CC-BY-SA-3.0
Group:          System/GUI/Other
URL:            https://en.opensuse.org/Portal:Enlightenment
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

%package -n openSUSE-e-X-Ice-Icons
Summary:        FDO Icon theme to go with openSUSE Enlightenment Theme
License:        GPL-3.0-only
Group:          System/GUI/Other

%description -n openSUSE-e-X-Ice-Icons
An FDO Icon theme that matches the one used by the openSUSE Enlightenment
theme

%prep
%setup -q -n enlightenment-theme-openSUSE-ice-%{version}

%build
./build-darkmod.sh --epkg
cp build/e/openSUSE-ice.edj .
cp licenses-authors/* .
cp build/icons/openSUSE-ice-icons/README README.icons

%install
install -m 0755 -d %{buildroot}%{_datadir}/elementary/themes
install -m 0644 -t %{buildroot}%{_datadir}/elementary/themes openSUSE-ice.edj

install -m 0755 -d %{buildroot}%{_datadir}/icons/%{icon_theme_name}
install -m 0644 -t %{buildroot}%{_datadir}/icons/%{icon_theme_name} build/icons/openSUSE-ice-icons/index.theme

pushd build/icons/openSUSE-ice-icons
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

%files -n openSUSE-e-X-Ice-Icons
%license README.icons
%{_datadir}/icons/%{icon_theme_name}

%changelog
