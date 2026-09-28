#
# spec file for package emulationstation-de
#
# Copyright (c) 2026 SUSE LLC
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


Name:           emulationstation-de
Version:        3.4.1
Release:        0
Summary:        Gaming frontend
License:        MIT
Group:          System/Emulators/Other
URL:            https://es-de.org
Source0:        https://gitlab.com/es-de/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  Mesa-libGL-devel
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  libcurl-devel
BuildRequires:  freetype2-devel
BuildRequires:  freeimage-devel
BuildRequires:  gettext-runtime
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pugixml-devel
BuildRequires:  alsa-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libgit2-devel
BuildRequires:  bluez-devel
BuildRequires:  libpoppler-devel
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  libicu-devel
BuildRequires:  fdupes

%description
ES-DE is a frontend for browsing and launching games from your multi-platform collection.

%prep
%autosetup -n emulationstation-de-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

> %{_builddir}/es-de.lang

for mo in %{buildroot}%{_datadir}/es-de/resources/locale/*/LC_MESSAGES/*.mo; do
    lang="$(basename "$(dirname "$(dirname "$mo")")")"
    echo "%%lang($lang) ${mo#%{buildroot}}" >> %{_builddir}/es-de.lang
done

%fdupes %{buildroot}%{_datadir}

%check
# No testsuite available upstream; nothing to run in OBS.

%files -f %{_builddir}/es-de.lang
%doc README.md
%{_bindir}/es-de
%{_bindir}/es-pdf-convert
%{_mandir}/man6/es-de.6%{ext_man}

%dir %{_datadir}/es-de
%license %{_datadir}/es-de/LICENSE
%{_datadir}/es-de/licenses/
%{_datadir}/es-de/themes/
%{_datadir}/es-de/resources/

%{_datadir}/applications/org.es_de.frontend.desktop
%{_datadir}/pixmaps/org.es_de.frontend.svg
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/*/apps/org.es_de.frontend.*
%{_datadir}/metainfo/org.es_de.frontend.appdata.xml

%changelog
