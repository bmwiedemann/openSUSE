#
# spec file for package stellarium
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_with     Qt5
%else
%bcond_without  Qt5
%endif

Name:           stellarium
Version:        25.2
Release:        0
Summary:        Astronomical Sky Simulator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://stellarium.org/
Source0:        https://github.com/Stellarium/stellarium/releases/download/v%{version}/stellarium-%{version}.tar.xz
Source1:        https://github.com/Stellarium/stellarium/releases/download/v%{version}/stellarium-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.16.0
%if 0%{?suse_version} <= 1600
BuildRequires:  cmake(FastFloat)
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 7
BuildRequires:  hicolor-icon-theme
BuildRequires:  libnova-devel
BuildRequires:  libxkbcommon-devel >= 0.5.0
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libindi) >= 2.0.0
BuildRequires:  pkgconfig(md4c)
BuildRequires:  pkgconfig(nlopt)
BuildRequires:  pkgconfig(zlib)
%if %{with Qt5}
BuildRequires:  libQt5Core-private-headers-devel >= 5.9.0
BuildRequires:  libQt5Gui-private-headers-devel >= 5.9.0
BuildRequires:  libqt5-qtpaths
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
%else
BuildRequires:  qt6-core-private-devel >= 6.2.0
BuildRequires:  qt6-gui-private-devel >= 6.2.0
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6Widgets)
%ifarch aarch64 x86_64 riscv64
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
%endif
Requires:       qt6-multimedia
%endif
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(Qgpsmm)
BuildRequires:  pkgconfig(libgps)
%endif

%description
Stellarium is a software to render 3D photo-realistic skies in real
time, similar to what can be observed with human eyes through
binoculars or a small telescope.

%prep
%autosetup -p1

%build
# Require at least 4000 MB of memory per job
%limit_build -m 4000
export QT_HASH_SEED=0
%cmake	-DCMAKE_BUILD_TYPE=Release \
	-DCPM_USE_LOCAL_PACKAGES=yes \
	-DBUILD_SHARED_LIBS=OFF \
	-DENABLE_SHOWMYSKY=OFF \
	-DENABLE_XLSX=OFF
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_datadir}/%{name}/data/script_internet_update
%fdupes %{buildroot}%{_datadir}
# remove all zero size files
find %{buildroot}%{_datadir}/%{name}/skycultures -type f -size 0 -delete

#%%find_lang %%{name}
#%%find_lang %%{name}-skycultures
#cat %%{name}-skycultures.lang >> %%{name}.lang

%files
%defattr(-,root,root,755)
%license COPYING
%doc CREDITS.md ChangeLog README.md
%dir %{_datadir}/icons/hicolor/512x512/
%dir %{_datadir}/icons/hicolor/512x512/apps/
%{_bindir}/%{name}
%{_datadir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
