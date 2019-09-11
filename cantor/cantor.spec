#
# spec file for package cantor
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global libMAJOR 23
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           cantor
Version:        19.08.0
Release:        0
Summary:        Worksheet GUI for mathematical software
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Mathematics
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  R-base
BuildRequires:  R-base-devel
BuildRequires:  analitza-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  help2man
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kf5-filesystem
BuildRequires:  knewstuff-devel
BuildRequires:  kparts-devel
BuildRequires:  kpty-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  libspectre-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  python3-devel
BuildRequires:  syntax-highlighting-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
Recommends:     %{name}-lang
Recommends:     maxima
Recommends:     octave
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
A frontend to several existing mathematical software such as R, Sage
and Maxima: Cantor. Cantor offers a worksheet as a nice GUI for all
those backends and is not targeted to kids but to scientists.

%package devel
Summary:        Worksheet GUI for mathematical software
Group:          Development/Libraries/KDE
Requires:       libcantorlibs%{libMAJOR} = %{version}

%description devel
A frontend to several existing mathematical software such as R, Sage
and Maxima: Cantor. Cantor offers a worksheet as a nice GUI for all
those backends and is not targeted to kids but to scientists.

%package -n libcantorlibs%{libMAJOR}
Summary:        Shared libraries for Cantor
Group:          System/Libraries

%description -n libcantorlibs%{libMAJOR}
Shared libraries for package cantor.

%lang_package

%prep
%setup -q

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
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif

%post -n libcantorlibs%{libMAJOR} -p /sbin/ldconfig
%postun -n libcantorlibs%{libMAJOR} -p /sbin/ldconfig

%files devel
%license COPYING*
%{_kf5_libdir}/libcantorlibs.so
%{_kf5_prefix}/include/cantor/
%dir %{_kf5_cmakedir}/Cantor
%{_kf5_cmakedir}/Cantor/CantorConfig.cmake
%{_kf5_cmakedir}/Cantor/CantorConfigVersion.cmake
%{_kf5_cmakedir}/Cantor/CantorTargets.cmake
%{_kf5_cmakedir}/Cantor/CantorTargets-none.cmake

%files
%doc README.md DESIGN .doc/*
%license COPYING*
%(config) %{_kf5_configdir}/*.knsrc
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/org.kde.cantor.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/cantor
%{_kf5_bindir}/cantor_python3server
%{_kf5_bindir}/cantor_python2server
%{_kf5_bindir}/cantor_rserver
%{_kf5_bindir}/cantor_scripteditor
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/*
%{_kf5_kxmlguidir}/cantor/
%{_kf5_libdir}/libcantor_config.so
%{_kf5_libdir}/libcantor_pythonbackend.so
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
%{_kf5_plugindir}/cantor/backends/cantor_nullbackend.so
%{_kf5_plugindir}/cantor/backends/cantor_octavebackend.so
%{_kf5_plugindir}/cantor/backends/cantor_python2backend.so
%{_kf5_plugindir}/cantor/backends/cantor_python3backend.so
%{_kf5_plugindir}/cantor/backends/cantor_rbackend.so
%{_kf5_plugindir}/cantor/backends/cantor_sagebackend.so
%{_kf5_plugindir}/cantor/backends/cantor_scilabbackend.so
%{_kf5_plugindir}/cantor/backends/cantor_qalculatebackend.so
%dir %{_kf5_plugindir}/cantor/panels
%{_kf5_plugindir}/cantor/panels/cantor_helppanelplugin.so
%{_kf5_plugindir}/cantor/panels/cantor_variablemanagerplugin.so
%{_kf5_plugindir}/libcantorpart.so
%{_kf5_sharedir}/cantor/

%files -n libcantorlibs%{libMAJOR}
%license COPYING*
%{_kf5_libdir}/libcantorlibs.so.*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
