#
# spec file for package powdertoy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           powdertoy
Version:        94.1
Release:        0
Summary:        Physics sandbox game
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            http://powdertoy.co.uk
Source:         https://github.com/simtr/The-Powder-Toy/archive/v%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  fftw3-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  libbz2-devel
BuildRequires:  lua51-devel
BuildRequires:  python-devel
BuildRequires:  scons
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel

%description
The Powder Toy is a free physics sandbox game, which simulates
air pressure and velocity, heat, gravity and a countless number
of interactions between different substances! The game provides
you with various building materials, liquids, gases and electronic
components which can be used to construct complex machines, guns,
bombs, realistic terrains and almost anything else.

%prep
%setup -q -n The-Powder-Toy-%{version}

%build
%ifarch x86_64
scons --lin --release --64
%else
%ifarch %{ix86}
scons --lin --release --32
%else
scons --lin --release --no-sse
%endif
%endif

%install
%ifarch x86_64
install -D -m 0755 build/powder64 %{buildroot}%{_bindir}/powder
%else
install -D -m 0755 build/powder %{buildroot}%{_bindir}/powder
%endif
convert resources/icon.ico -strip resources/powder.png
install -D -m 0644 resources/icon/powder-256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/powder.png
install -D -m 0644 resources/icon/powder-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/powder.png
install -D -m 0644 resources/icon/powder-48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/powder.png
install -D -m 0644 resources/icon/powder-32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/powder.png
install -D -m 0644 resources/icon/powder-24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/powder.png
install -D -m 0644 resources/icon/powder-16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/powder.png

install -D -m 0644 resources/powder.desktop %{buildroot}%{_datadir}/applications/powder.desktop
install -D -m 0644 resources/powder.appdata.xml %{buildroot}%{_datadir}/appdata/powder.appdata.xml
install -D -m 0644 resources/powdertoy-save.xml %{buildroot}%{_datadir}/mime/packages/powdertoy-save.xml

%post
%icon_theme_cache_post
%desktop_database_post
%mime_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun

%files
%license LICENSE
%doc README.md TODO
%{_bindir}/powder
%{_datadir}/appdata/powder.appdata.xml
%{_datadir}/applications/powder.desktop
%{_datadir}/icons/hicolor/*/apps/powder.png
%{_datadir}/mime/packages/powdertoy-save.xml

%changelog
