#
# spec file for package powdertoy
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


Name:           powdertoy
Version:        93.3
Release:        0
Summary:        Physics sandbox game
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            http://powdertoy.co.uk
Source:         https://github.com/simtr/The-Powder-Toy/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM powdertoy-93.3-fix-mimeinfo.patch -- Fix syntax problems
Patch0:         powdertoy-93.3-fix-mimeinfo.patch
BuildRequires:  ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
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
%patch0 -p1

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
convert resources/powder.ico -strip resources/powder.png
install -D -m 0644 resources/powder-0.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/powder.png
install -D -m 0644 resources/powder-1.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/powder.png
install -D -m 0644 resources/powder-2.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/powder.png
install -D -m 0644 resources/powder-3.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/powder.png
install -D -m 0644 resources/powder-4.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/powder.png

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
