#
# spec file for package naev
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


Name:           naev
Version:        0.7.0
Release:        0
Summary:        2D action RPG space game
License:        GPL-3.0
Group:          Amusements/Games/Action/Other
Url:            http://naev.org/
Source0:        http://downloads.sourceforge.net/naev/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        http://downloads.sourceforge.net/naev/%{name}-%{version}/%{name}-%{version}-ndata.zip
BuildRequires:  SDL2-devel
BuildRequires:  freetype2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libSDL2_mixer-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  lua51-devel
BuildRequires:  openal-soft-devel
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
Requires:       %{name}-data = %{version}

%description
Naev is a 2D space trading and combat game, in a similar vein to Escape Velocity.

Naev is played from a top-down perspective, featuring fast-paced combat, many ships,
a large variety of equipment and a large galaxy to explore. The game is
open-ended, letting you proceed at your own pace.

%package data
Summary:        Data files for Naev
Group:          Amusements/Games/Action/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
This package contains the universal data for Naev, a 2D action RPG space game.

%prep
%setup -q

%build
%configure --with-ndata-path=%{_datadir}/%{name}/ndata-%{version}.zip --enable-lua=shared --disable-shave --enable-debug=no

make %{?_smp_mflags}

%install
%make_install

install -D -m 0644 extras/logos/logo16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/naev.png
install -D -m 0644 extras/logos/logo32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/naev.png
install -D -m 0644 extras/logos/logo64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/naev.png
install -D -m 0644 extras/logos/logo128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/naev.png

%suse_update_desktop_file %{name}

mkdir -p %{buildroot}%{_datadir}/naev
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/naev/ndata-%{version}.zip

# Already packaged by the doc macro
rm -fr %{buildroot}%{_datadir}/doc

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README TODO
%doc %{_mandir}/man6/*
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*x*/apps/naev.png

%files data
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
