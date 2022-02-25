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


%define icon_theme_name openSUSE-e-X-Dark
%define theme_name Dark

Name:           enlightenment-theme-dark
Version:        20220216.1.26
Release:        0
Summary:        The old default theme for enlightenment
License:        BSD-2-Clause AND LGPL-2.1-only AND CC-BY-SA-3.0
URL:            https://en.opensuse.org/Portal:Enlightenment
Source:         enlightenment-theme-%{theme_name}-%{version}.tar.xz
# for convert
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  efl
Provides:       enlightenment-theme
Recommends:     openSUSE-e-X-Dark-Icons
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The old default theme for enlightenment, for most of the 2010 Era.

%package -n openSUSE-e-X-Dark-Icons
Summary:        FDO Icon theme to go with Dark Enlightenment Theme
License:        GPL-3.0-only

%description -n openSUSE-e-X-Dark-Icons
An FDO Icon theme that matches the one used by the Dark Enlightenment
theme

%prep
%setup -q -n enlightenment-theme-%{theme_name}-%{version}

%build
./build-darkmod.sh --epkg
cp licenses-authors/* .
cp build/icons/Dark-icons/README README.icons

%install
install -m 0755 -d %{buildroot}%{_datadir}/elementary/themes
install -m 0644 -t %{buildroot}%{_datadir}/elementary/themes artifacts/bin-e/Dark.edj

install -m 0755 -d %{buildroot}%{_datadir}/icons/%{icon_theme_name}
install -m 0644 -t %{buildroot}%{_datadir}/icons/%{icon_theme_name} build/icons/%{theme_name}-icons/index.theme

pushd build/icons/%{theme_name}-icons
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

%files -n openSUSE-e-X-Dark-Icons
%license README.icons
%{_datadir}/icons/%{icon_theme_name}

%changelog
