#
# spec file for package openttd
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2007-2012 The OpenTTD developers
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


%define about OpenTTD is a reimplementation of the Microprose game "Transport Tycoon Deluxe" with lots of new features and enhancements. To play the game, you need either the original proprietary data set from the game, or install the recommend subpackages OpenGFX, OpenSFX and OpenMSX for an alternate, free set of graphics, sounds and music, respectively.
Name:           openttd
Version:        13.0
Release:        0
Summary:        A clone of Chris Sawyer's Transport Tycoon Deluxe
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://openttd.org/
Source:         https://cdn.openttd.org/openttd-releases/%{version}/%{name}-%{version}-source.tar.xz
# PATCH-FEATURE-UPSTREAM https://bugs.openttd.org/task/6490
Source2:        openttd.appdata.xml
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++ >= 8.1
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}-%{release}
Conflicts:      %{name}-dedicated
Provides:       %{name}-gui = %{version}
%if 0%{?mdkversion}
BuildRequires:  liblzma-devel
BuildRequires:  liblzo-devel
%else
BuildRequires:  lzo-devel
BuildRequires:  pkgconfig(liblzma)
%endif
%if 0%{?suse_version} || 0%{?mdkversion}
BuildRequires:  pkgconfig(freetype2)
%else
BuildRequires:  freetype-devel
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libtimidity)
BuildRequires:  pkgconfig(libxdg-basedir)
%else
BuildRequires:  desktop-file-utils
BuildRequires:  grfcodec
%endif
%if 0%{?suse_version} || 0%{?mdkversion}
Recommends:     adobe-sourcehansans-fonts
Recommends:     openttd-openmsx
Recommends:     openttd-opensfx
%endif

%description
%{about}

Use package %{name}-dedicated for systems without SDL.

%package dedicated
Summary:        OpenTTD Dedicated Server binary (without SDL)
Group:          Amusements/Games/Strategy/Other
Requires:       %{name}-data = %{version}-%{release}
Conflicts:      %{name}

%description dedicated
%{about}

This package provides the binary %{name}-dedicated without dependency of SDL.

%package data
Summary:        OpenTTD data
Group:          Amusements/Games/Strategy/Other
%if 0%{?suse_version} || 0%{?fedora} || 0%{?mdkversion} || 0%{?rhel_version} >= 600 || 0%{?centos_version} >= 600
BuildArch:      noarch
%endif
%if 0%{?suse_version} || 0%{?mdkversion}
Recommends:     openttd-opengfx >= 0.5.2
%endif

%description data
%{about}

This package provides the data files needed by %{name} or %{name}-dedicated.

%prep
%setup -q

# Remove build time references so build-compare can do its work
sed -i "s/__DATE__.*__TIME__/\"${SOURCE_DATE_EPOCH}\"/" src/rev.cpp.in

%build
%if 0%{?suse_version} <= 1500
export CXX=g++-10
%else
export CXX=g++
%endif
# first, we build the dedicated binary inside dedicated/
%define __builddir dedicated
%cmake -DCMAKE_INSTALL_BINDIR="bin" -DCMAKE_INSTALL_DATADIR="share" -DOPTION_DEDICATED:BOOL=ON
%cmake_build
cd ..

# then, we build the common gui version which we install the usual way
%define __builddir build
%cmake -DCMAKE_INSTALL_BINDIR="bin" -DCMAKE_INSTALL_DATADIR="share" -DOPTION_DEDICATED:BOOL=OFF
%cmake_build

%install
# install the game
%cmake_install INSTALL_DIR=%{buildroot}

# install the dedicated server
install -D -m0755 dedicated/openttd %{buildroot}%{_bindir}/%{name}-dedicated

mkdir -p %{buildroot}%{_datadir}/appdata
install -D -m0644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/openttd.appdata.xml

%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%endif

%post dedicated
rm -f %{_bindir}/%{name}
ln -s %{name}-dedicated %{_bindir}/%{name}

%preun dedicated
if [ "$1" -eq 0 ] ; then
    rm -f %{_bindir}/%{name}
fi

%if 0%{?suse_version} < 1500
%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata/
%{_datadir}/appdata/openttd.appdata.xml
%{_datadir}/icons/hicolor
%{_datadir}/pixmaps/%{name}.32.xpm
%{_datadir}/pixmaps/%{name}.64.xpm
%{_mandir}/man6/%{name}.6%{?ext_man}

%files dedicated
%{_bindir}/%{name}-dedicated
%{_mandir}/man6/%{name}.6%{?ext_man}

%files data
%{_datadir}/doc/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/baseset
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/ai
%{_datadir}/%{name}/game

%changelog
