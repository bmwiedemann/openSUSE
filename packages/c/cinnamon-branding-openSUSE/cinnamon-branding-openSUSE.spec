#
# spec file for package cinnamon-branding-openSUSE
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


%define mint_artwork_ver 5.3
%define cinnamon_gschemas_version %(rpm -q --queryformat '%%{VERSION}' cinnamon-gschemas)
%define libcinnamon_desktop_data_version %(rpm -q --queryformat '%%{VERSION}' libcinnamon-desktop-data)
Name:           cinnamon-branding-openSUSE
Version:        42.2
Release:        0
Summary:        openSUSE Branding of the Cinnamon Desktop Environment
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            https://en.opensuse.org/Portal:Cinnamon
Source1:        cinnamon-branding.gschema.override
Source2:        libcinnamon-desktop-branding.gschema.override.in
Source3:        http://packages.linuxmint.com/pool/main/m/mint-artwork-cinnamon/mint-artwork-cinnamon_%{mint_artwork_ver}.tar.gz
BuildRequires:  cinnamon-gschemas-branding-upstream
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme-branding-openSUSE
BuildRequires:  libcinnamon-desktop-data-branding-upstream
BuildRequires:  pkgconfig
BuildRequires:  wallpaper-branding-openSUSE
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This package provides the openSUSE look and feel for the Cinnamon
desktop environment.

%package -n cinnamon-gschemas-branding-openSUSE
Summary:        openSUSE Branding of the Cinnamon Desktop Environment
Group:          System/Libraries
Requires:       cinnamon-gschemas = %{cinnamon_gschemas_version}
Requires:       cinnamon-themes
Requires:       libgnomesu
Supplements:    packageand(cinnamon-gschemas:branding-openSUSE)
Conflicts:      otherproviders(cinnamon-gschemas-branding)
Provides:       cinnamon-gschemas-branding = %{cinnamon_gschemas_version}
# cinnamon-branding-openSUSE was last used in openSUSE Leap 42.2.
Provides:       cinnamon-branding-openSUSE = %{version}-%{release}
Obsoletes:      cinnamon-branding-openSUSE < %{version}-%{release}
%glib2_gsettings_schema_requires

%description -n cinnamon-gschemas-branding-openSUSE
This package provides the openSUSE look and feel for the Cinnamon
desktop environment.

%package -n libcinnamon-desktop-data-branding-openSUSE
Summary:        openSUSE Branding of the Cinnamon Desktop Environment
Group:          System/GUI/Other
Requires:       adwaita-icon-theme
Requires:       libcinnamon-desktop-data = %{libcinnamon_desktop_data_version}
Requires:       mate-themes
Requires:       wallpaper-branding-openSUSE
Supplements:    packageand(libcinnamon-desktop-data:branding-openSUSE)
Conflicts:      otherproviders(libcinnamon-desktop-data-branding)
Provides:       libcinnamon-desktop-data-branding = %{libcinnamon_desktop_data_version}
%glib2_gsettings_schema_requires

%description -n libcinnamon-desktop-data-branding-openSUSE
This package provides the openSUSE look and feel for the Cinnamon
desktop environment.

%prep
%setup -q -c -T
cp -f %{SOURCE1} cinnamon-branding.gschema.override
cp -f %{SOURCE2} libcinnamon-desktop-branding.gschema.override.in
%setup -q -T -D -a 3

%build
[ -f %{_datadir}/wallpapers/openSUSE-default.xml ]
sed -e 's|@@WALLPAPER_URI@@|%{_datadir}/wallpapers/openSUSE-default.xml|' \
  libcinnamon-desktop-branding.gschema.override.in > \
  libcinnamon-desktop-branding.gschema.override

%install
install -Dpm 0644 cinnamon-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/cinnamon-branding.gschema.override
install -Dpm 0644 libcinnamon-desktop-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/libcinnamon-desktop-branding.gschema.override

install -Dpm 0644 %{_datadir}/icons/hicolor/scalable/apps/distributor.svg \
  %{buildroot}%{_datadir}/cinnamon/theme/menu.svg

mkdir -p %{buildroot}%{_datadir}/sounds/cinnamon/opensuse/
install -pm 0644 \
  mint-artwork-cinnamon-%{mint_artwork_ver}%{_datadir}/mint-artwork-cinnamon/sounds/* \
  %{buildroot}%{_datadir}/sounds/cinnamon/opensuse/

%fdupes %{buildroot}%{_datadir}/

%post -n cinnamon-gschemas-branding-openSUSE
%glib2_gsettings_schema_post

%postun -n cinnamon-gschemas-branding-openSUSE
%glib2_gsettings_schema_postun

%post -n libcinnamon-desktop-data-branding-openSUSE
%glib2_gsettings_schema_post

%postun -n libcinnamon-desktop-data-branding-openSUSE
%glib2_gsettings_schema_postun

%files -n cinnamon-gschemas-branding-openSUSE
%defattr(-,root,root)
%{_datadir}/glib-2.0/schemas/cinnamon-branding.gschema.override
%dir %{_datadir}/cinnamon/
%dir %{_datadir}/cinnamon/theme/
%{_datadir}/cinnamon/theme/menu.svg
%dir %{_datadir}/sounds/cinnamon/
%{_datadir}/sounds/cinnamon/opensuse/
%exclude %{_datadir}/sounds/cinnamon/opensuse/volume.oga

%files -n libcinnamon-desktop-data-branding-openSUSE
%defattr(-,root,root)
%{_datadir}/glib-2.0/schemas/libcinnamon-desktop-branding.gschema.override
%dir %{_datadir}/sounds/cinnamon/
%dir %{_datadir}/sounds/cinnamon/opensuse/
%{_datadir}/sounds/cinnamon/opensuse/volume.oga

%changelog
