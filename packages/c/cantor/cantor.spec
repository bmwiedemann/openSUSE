#
# spec file for package cantor
#
# Copyright (c) 2022 SUSE LLC
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


%global libMAJOR 28
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           cantor
Version:        22.12.0
Release:        0
Summary:        Worksheet GUI for mathematical software
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/cantor
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  R-base
BuildRequires:  R-base-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  help2man
BuildRequires:  kf5-filesystem
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libspectre-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  shared-mime-info
BuildRequires:  xz
BuildRequires:  cmake(Analitza5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(luajit)
Recommends:     maxima
Recommends:     octave
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
# Only build on archs where Qt5WebEngine is available
ExcludeArch:    ppc ppc64 ppc64le s390 s390x

%description
A frontend to several existing mathematical software such as R, Sage
and Maxima: Cantor. Cantor offers a worksheet as a nice GUI for all
those backends and is not targeted to kids but to scientists.

%package devel
Summary:        Worksheet GUI for mathematical software
Requires:       libcantorlibs%{libMAJOR} = %{version}
Requires:       libpoppler-qt5-devel
Requires:       libspectre-devel
Requires:       cmake(KF5Archive)
Requires:       cmake(KF5Completion)
Requires:       cmake(KF5Config)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5IconThemes)
Requires:       cmake(KF5KIO)
Requires:       cmake(KF5XmlGui)
Requires:       cmake(Qt5Svg)
Requires:       cmake(Qt5Xml)

%description devel
A frontend to several existing mathematical software such as R, Sage
and Maxima: Cantor. Cantor offers a worksheet as a nice GUI for all
those backends and is not targeted to kids but to scientists.

%package -n libcantorlibs%{libMAJOR}
Summary:        Shared libraries for Cantor

%description -n libcantorlibs%{libMAJOR}
Shared libraries for package cantor.

%lang_package

%prep
%autosetup -p1

mkdir .doc
cd src/backends
for d in *
do ! ln -T "${d}/DESIGN" "../../.doc/${d}"
done

%build
export RPM_OPT_FLAGS="%{optflags}"
%ifarch ppc ppc64
export RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
  # Julia uses <> instead of "" in some files, so it has to be a system include
  # export RPM_OPT_FLAGS="%{optflags} -isystem %{_includedir}/julia -isystem $PWD/src/lib/test -isystem %{_includedir}/qt5/QtTest"
  export CFLAGS="%{optflags}"
  export CXXFLAGS="%{optflags}"
  %cmake_kf5 -d build
  %cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -n libcantorlibs%{libMAJOR} -p /sbin/ldconfig
%postun -n libcantorlibs%{libMAJOR} -p /sbin/ldconfig

%files devel
%dir %{_kf5_cmakedir}/Cantor
%{_kf5_cmakedir}/Cantor/CantorConfig.cmake
%{_kf5_cmakedir}/Cantor/CantorConfigVersion.cmake
%{_kf5_cmakedir}/Cantor/CantorTargets-none.cmake
%{_kf5_cmakedir}/Cantor/CantorTargets.cmake
%{_kf5_libdir}/libcantorlibs.so
%{_kf5_prefix}/include/cantor/

%files
%doc README.md DESIGN .doc/*
%{_kf5_knsrcfilesdir}/*.knsrc
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.cantor.desktop
%{_kf5_appstreamdir}/org.kde.cantor.appdata.xml
%{_kf5_bindir}/cantor
%{_kf5_bindir}/cantor_pythonserver
%{_kf5_bindir}/cantor_rserver
%{_kf5_bindir}/cantor_scripteditor
%{_kf5_configkcfgdir}/*backend.kcfg
%{_kf5_configkcfgdir}/cantor.kcfg
%{_kf5_configkcfgdir}/cantor_libs.kcfg
%{_kf5_configkcfgdir}/rserver.kcfg
%{_kf5_configkcfgdir}/octavebackend.kcfg.in
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_kxmlguidir}/cantor/
%{_kf5_libdir}/libcantor_config.so
%{_kf5_libdir}/cantor_pythonbackend.so
%dir %{_kf5_plugindir}/cantor
%dir %{_kf5_plugindir}/cantor/assistants
%{_kf5_plugindir}/cantor/assistants/cantor_advancedplotassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_creatematrixassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_differentiateassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_eigenvaluesassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_eigenvectorsassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_importpackageassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_integrateassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_invertmatrixassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_plot2dassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_plot3dassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_runscriptassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_solveassistant.so
%{_kf5_plugindir}/cantor/assistants/cantor_qalculateplotassistant.so
%dir %{_kf5_plugindir}/cantor/backends
%{_kf5_plugindir}/cantor/backends/cantor_kalgebrabackend.so
%{_kf5_plugindir}/cantor/backends/cantor_maximabackend.so
%{_kf5_plugindir}/cantor/backends/cantor_octavebackend.so
%{_kf5_plugindir}/cantor/backends/cantor_pythonbackend.so
%{_kf5_plugindir}/cantor/backends/cantor_rbackend.so
%{_kf5_plugindir}/cantor/backends/cantor_sagebackend.so
%{_kf5_plugindir}/cantor/backends/cantor_scilabbackend.so
%{_kf5_plugindir}/cantor/backends/cantor_qalculatebackend.so
%{_kf5_plugindir}/cantor/backends/cantor_luabackend.so
%dir %{_kf5_plugindir}/cantor/panels
%{_kf5_plugindir}/cantor/panels/cantor_helppanelplugin.so
%{_kf5_plugindir}/cantor/panels/cantor_variablemanagerplugin.so
%{_kf5_plugindir}/cantor/panels/cantor_filebrowserpanelplugin.so
%{_kf5_plugindir}/cantor/panels/cantor_tocpanelplugin.so
%{_kf5_plugindir}/cantor/panels/cantor_documentationpanelplugin.so

%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_plugindir}/kf5/parts/cantorpart.so
%{_kf5_sharedir}/cantor/
%{_kf5_sharedir}/mime/packages/cantor.xml

%files -n libcantorlibs%{libMAJOR}
%license LICENSES/*
%{_kf5_libdir}/libcantorlibs.so.*

%files lang -f %{name}.lang

%changelog
