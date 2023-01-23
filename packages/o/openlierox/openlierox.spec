#
# spec file for package openlierox
#
# Copyright (c) 2023 SUSE LLC
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


Name:           openlierox
Version:        0.58_rc5
Release:        0
Summary:        A real-time, excessive clone of Worms
License:        LGPL-2.0-or-later
Group:          Amusements/Games/Other
URL:            http://www.openlierox.net/
Source:         http://downloads.sourceforge.net/%{name}/OpenLieroX_%{version}.src.tar.bz2
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gd-devel
BuildRequires:  hawknl-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel
BuildRequires:  libzip-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(sdl)
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++ >= 11
%endif
# for people who try to install this using upstream capitalization
Provides:       OpenLieroX = %{version}-%{release}

%description
Based on Liero gameplay, OpenLierox is an extremely addictive realtime worms
shoot-em-up backed by an active gamers community. Dozens of levels and mods
are available to provide endless gaming pleasure.

%prep
%autosetup -n OpenLieroX

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-11"
export CXX="g++-11"
%endif

%cmake -DDEBUG=OFF -DBREAKPAD=OFF -DSYSTEM_DATA_DIR=%{_datadir} -DHAWKNL_BUILTIN=ON
%make_build

%install
install -m 755 -d %{buildroot}%{_datadir}/openlierox/
cp -r share/gamedir/* %{buildroot}%{_datadir}/openlierox/
find %{buildroot}%{_datadir}/openlierox/ -type f -exec chmod 0644 \{\} +

install -m 755 -d %{buildroot}%{_bindir}
install -m 755 build/bin/openlierox %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 644 share/OpenLieroX.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/OpenLieroX.svg

mkdir -p %{buildroot}%{_datadir}/applications
install -p -m 644 share/openlierox-openlierox.desktop %{buildroot}%{_datadir}/applications/openlierox.desktop

mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 644 share/openlierox.appdata.xml %{buildroot}%{_datadir}/appdata/openlierox.appdata.xml

%fdupes %{buildroot}%{_datadir}

%files
%{_bindir}/openlierox
%{_datadir}/openlierox
%{_datadir}/icons/hicolor/scalable/apps/OpenLieroX.svg
%{_datadir}/applications/openlierox.desktop
%{_datadir}/appdata/openlierox.appdata.xml

%changelog
