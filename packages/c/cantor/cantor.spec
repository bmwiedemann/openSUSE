#
# spec file for package cantor
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


%global libMAJOR 28
%define kf6_version 6.6.0
%define qt6_version 6.6.0

%ifarch x86_64 %{x86_64} aarch64 riscv64
%define with_qtwebengine 1
%endif

# luajit isn't available on ppc64le and riscv64
%ifarch %{ix86} x86_64 %{x86_64} %{arm} aarch64 s390x
%define with_luajit 1
%endif

%bcond_without analitza
%bcond_without released
Name:           cantor
Version:        24.12.2
Release:        0
Summary:        Worksheet GUI for mathematical software
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/cantor
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  R-base
BuildRequires:  R-base-devel
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
# julia-devel is unresolvable in factory
# BuildRequires:  julia-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libspectre-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  shared-mime-info
%if %{with analitza}
BuildRequires:  cmake(Analitza6)
%endif
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuffCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
%if 0%{?with_qtwebengine}
BuildRequires:  cmake(Qt6Help) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
%if 0%{?with_luajit}
BuildRequires:  pkgconfig(luajit)
%endif
BuildRequires:  pkgconfig(poppler-qt6)
Recommends:     maxima
Recommends:     octave
Obsoletes:      cantor5 < %{version}
Provides:       cantor5 = %{version}

%description
A frontend to several existing mathematical software such as R, Sage
and Maxima: Cantor. Cantor offers a worksheet as a nice GUI for all
those backends and is not targeted to kids but to scientists.

%package devel
Summary:        Worksheet GUI for mathematical software
Requires:       libcantorlibs%{libMAJOR} = %{version}
Requires:       pkgconfig(poppler-qt6)
Requires:       libspectre-devel
Requires:       cmake(KF6Archive) >= %{kf6_version}
Requires:       cmake(KF6Completion) >= %{kf6_version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6IconThemes) >= %{kf6_version}
Requires:       cmake(KF6KIO) >= %{kf6_version}
Requires:       cmake(KF6XmlGui) >= %{kf6_version}
Requires:       cmake(Qt6Svg) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

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
pushd src/backends
for d in R maxima sage; do
  ln -T "${d}/DESIGN" "../../.doc/${d}"
done
popd

%build
# Julia uses <> instead of "" in some files, so it has to be a system include
# export RPM_OPT_FLAGS="%%{optflags} -isystem %%{_includedir}/julia -isystem $PWD/src/lib/test -isystem %%{_includedir}/qt6/QtTest"
# export CFLAGS="%%{optflags}"
# export CXXFLAGS="%%{optflags}"

%cmake_kf6 \
%if !0%{?with_qtwebengine}
  -DENABLE_EMBEDDED_DOCUMENTATION:BOOL=FALSE
%endif
%{nil}

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets -n libcantorlibs%{libMAJOR}

%files
%doc README.md DESIGN .doc/*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.cantor.desktop
%{_kf6_appstreamdir}/org.kde.cantor.appdata.xml
%{_kf6_bindir}/cantor
%{_kf6_bindir}/cantor_pythonserver
%{_kf6_bindir}/cantor_rserver
%{_kf6_bindir}/cantor_scripteditor
%{_kf6_configkcfgdir}/*backend.kcfg
%{_kf6_configkcfgdir}/cantor.kcfg
%{_kf6_configkcfgdir}/cantor_libs.kcfg
%{_kf6_configkcfgdir}/octavebackend.kcfg.in
%{_kf6_configkcfgdir}/rserver.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/*
%{_kf6_knsrcfilesdir}/*.knsrc
%{_kf6_libdir}/cantor_pythonbackend.so
%{_kf6_libdir}/libcantor_config.so
%dir %{_kf6_plugindir}/cantor_plugins
%dir %{_kf6_plugindir}/cantor_plugins/assistants
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_advancedplotassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_creatematrixassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_differentiateassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_eigenvaluesassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_eigenvectorsassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_importpackageassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_integrateassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_invertmatrixassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_plot2dassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_plot3dassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_qalculateplotassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_runscriptassistant.so
%{_kf6_plugindir}/cantor_plugins/assistants/cantor_solveassistant.so
%dir %{_kf6_plugindir}/cantor_plugins/backends
%if %{with analitza}
%{_kf6_plugindir}/cantor_plugins/backends/cantor_kalgebrabackend.so
%endif
%if 0%{?with_luajit}
%{_kf6_plugindir}/cantor_plugins/backends/cantor_luabackend.so
%endif
%{_kf6_plugindir}/cantor_plugins/backends/cantor_maximabackend.so
%{_kf6_plugindir}/cantor_plugins/backends/cantor_octavebackend.so
%{_kf6_plugindir}/cantor_plugins/backends/cantor_pythonbackend.so
%{_kf6_plugindir}/cantor_plugins/backends/cantor_qalculatebackend.so
%{_kf6_plugindir}/cantor_plugins/backends/cantor_rbackend.so
%{_kf6_plugindir}/cantor_plugins/backends/cantor_sagebackend.so
%{_kf6_plugindir}/cantor_plugins/backends/cantor_scilabbackend.so
%dir %{_kf6_plugindir}/cantor_plugins/panels
%if 0%{?with_qtwebengine}
%{_kf6_plugindir}/cantor_plugins/panels/cantor_documentationpanelplugin.so
%endif
%{_kf6_plugindir}/cantor_plugins/panels/cantor_filebrowserpanelplugin.so
%{_kf6_plugindir}/cantor_plugins/panels/cantor_helppanelplugin.so
%{_kf6_plugindir}/cantor_plugins/panels/cantor_tocpanelplugin.so
%{_kf6_plugindir}/cantor_plugins/panels/cantor_variablemanagerplugin.so
%{_kf6_plugindir}/kf6/parts/cantorpart.so
%{_kf6_sharedir}/cantor/
%{_kf6_sharedir}/mime/packages/cantor.xml

%files -n libcantorlibs%{libMAJOR}
%license LICENSES/*
%{_kf6_libdir}/libcantorlibs.so.*

%files devel
%{_kf6_cmakedir}/Cantor
%{_kf6_libdir}/libcantorlibs.so
%{_includedir}/cantor/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
