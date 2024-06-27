#
# spec file for package endless-sky
#
# Copyright (c) 2024 SUSE LLC
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


%define lname   io.github.endless_sky.endless_sky
Name:           endless-sky
Version:        0.10.8
Release:        0
Summary:        Space exploration, trading, and combat game
License:        CC-BY-3.0 AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND GPL-3.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://endless-sky.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE endless-sky-fix-data-path.patch -- Fix installation path of data
Patch0:         endless-sky-fix-data-path.patch 
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg8-devel
BuildRequires:  libmad-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)

%description
Explore other star systems. Earn money by trading, carrying passengers,
or completing missions. Use your earnings to buy a better ship or to
upgrade the weapons and engines on your current one. Blow up pirates.
Take sides in a civil war. Or leave human space behind and hope to
find some friendly aliens whose culture is more civilized than your own...

%prep
%autosetup -p1

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden"
%else
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden -Wno-error=dangling-reference"
%endif
export CFLAGS="%{optflags} -fvisibility=hidden"
scons

%install
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden"
%else
export CXXFLAGS="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden -Wno-error=dangling-reference"
%endif
export CFLAGS="%{optflags} -fvisibility=hidden"
scons install PREFIX=%{_prefix} DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{_prefix}/games/endless-sky %{buildroot}%{_bindir}/endless-sky

%fdupes %{buildroot}

%files
%license license.txt
%doc README.md changelog copyright
%{_bindir}/endless-sky
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{lname}.desktop
%{_mandir}/man6/*
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{lname}.appdata.xml

%changelog
