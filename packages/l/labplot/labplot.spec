#
# spec file for package labplot
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


%define kf6_version 6.0
%define qt6_version 6.2.2

Name:           labplot
Version:        2.11.1git.20250114T013234~18418c36
Release:        0
Summary:        Data Visualization and Analysis software
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/labplot/
Source0:        %{name}-%{version}.tar.xz
# SECTION TODO
# TODO: Uncomment when a new release with cantor fixes is available
# Source1:        https://download.kde.org/stable/labplot/%%{name}-%%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/sgerlach@key1.asc?ref_type=heads
# Source2:        labplot.keyring
# /SECTION
# PATCH-FIX-OPENSUSE
Patch0:         0001-Fix-finding-liborigin-on-openSUSE.patch
BuildRequires:  bison
BuildRequires:  hdf5-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libixion-devel
BuildRequires:  liborcus-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(Cantor) >= 24.11.70
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuffCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
# Not detected correctly upstream
# BuildRequires:  cmake(KF6UserFeedback) >= %%{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Mqtt) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6SerialPort) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcerf)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libmarkdown)
BuildRequires:  pkgconfig(liborigin)
BuildRequires:  pkgconfig(matio)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(poppler-qt6) >= 0.62.0
BuildRequires:  pkgconfig(zlib)
Requires:       qt6-sql-sqlite >= %{qt6_version}
Provides:       labplot-kf5 = %{version}
Obsoletes:      labplot-kf5 < %{version}
Obsoletes:      labplot-kf5-lang < %{version}

%description
LabPlot provides an easy way to create, manage and edit plots. It allows you to
produce plots based on data from a spreadsheet or on data imported from external
files. Plots can be exported to several pixmap and vector graphic formats.

%lang_package

%prep
%autosetup -p1

%build
# oom issues with lto
%global _lto_cflags %{nil}

# ECM sets '-Werror=undef', which causes a build error because of libixion-0.18/ixion/env.hpp:39
# ('#if _WIN32'), we need to remove it from build flags (Cf. sr#1237616)
sed -i 's#-pedantic#-pedantic -Wno-error=undef#' CMakeLists.txt

%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DQT_VERSION_MAJOR:STRING=6 \
  -DENABLE_REPRODUCIBLE:BOOL=TRUE \
  -DENABLE_TESTS:BOOL=FALSE \
  -DENABLE_COMPILER_OPTIMIZATION:BOOL=FALSE \
  -DENABLE_READSTAT:BOOL=FALSE \
  -DENABLE_SDK:BOOL=FALSE \
  -DENABLE_CANTOR:BOOL=TRUE

%kf6_build

%install
%kf6_install

# Remove exotic resolutions
for res in 44 150 310; do
  rm -r %{buildroot}%{_kf6_iconsdir}/hicolor/${res}x${res}
done

%find_lang %{name} --all-name --with-html --with-man

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc ChangeLog README.md
%doc %lang(en) %{_kf6_htmldir}/en/labplot/
%{_kf6_applicationsdir}/org.kde.labplot.desktop
%{_kf6_appstreamdir}/org.kde.labplot.appdata.xml
%{_kf6_bindir}/labplot
%{_kf6_iconsdir}/hicolor/*/apps/*labplot*
%{_kf6_mandir}/man1/labplot.1%{?ext_man}
%{_kf6_sharedir}/labplot/
%{_kf6_sharedir}/mime/packages/labplot.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/labplot

%changelog
