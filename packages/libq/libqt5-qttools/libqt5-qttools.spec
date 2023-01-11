#
# spec file for package libqt5-qttools
#
# Copyright (c) 2020 SUSE LLC
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


%define qt5_snapshot 1
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qttools-everywhere-src-%{version}
%if 0%{?suse_version} >= 1330
%bcond_without qdoc
%else
# Needs clang >= 3.9.0
%bcond_with qdoc
%endif
Name:           libqt5-qttools
Version:        5.15.8+kde1
Release:        0
Summary:        Qt 5 QtTools Module
# Legal:
# most src/ subfolders are GPL-3.0-only WITH Qt-GPL-exception-1.0, except:
# qtpaths is BSD-3-Clause
# qdoc is GPL-3.0-only WITH Qt-GPL-exception-1.0 + (LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)) == GPL-3.0-only
# src/shared contains BSD-3-Clause and LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later) files. The
# 'GPL-3.0-only WITH Qt-GPL-exception-1.0' files in this folder are only used on Windows.
License:        (LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)) AND GPL-3.0-only WITH Qt-GPL-exception-1.0
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
Source11:       designer5.desktop
Source12:       linguist5.desktop
Source13:       assistant5.desktop
Source14:       qdbusviewer5.desktop
Source99:       libqt5-qttools-rpmlintrc
%if %{with qdoc}
BuildRequires:  clang-devel >= 3.9.0
%endif
BuildRequires:  fdupes
BuildRequires:  libqt5-qtbase-devel >= %{real_version}
BuildRequires:  libqt5-qtbase-private-headers-devel >= %{real_version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{real_version}
BuildRequires:  libxslt-devel
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  update-desktop-files
BuildRequires:  xz
Requires:       %{name}-qhelpgenerator = %{version}
# help files are SQLite databases, so assistant/qhelpgenerator need the SQLite plugin
Requires:       libQt5Sql5-sqlite >= %{real_version}
Requires:       libqt5-qdbus = %{version}
Requires:       libqt5-qtpaths = %{version}
%requires_ge    libQt5DBus5
Recommends:     libqt5-linguist
Recommends:     libqt5-qtdoc-qch >= %{version}

%description
The QtTools modules contains some tools mostly useful for application development.

Included are QtAssistant (help browser), QtDesigner (GUI design), QDbusViewer
and several more.

%prep
%autosetup -p1 -n %{tar_version}

%package devel
Summary:        Development files for the Qt5 Tools library
Group:          Development/Libraries/X11
Requires:       %{name}-qhelpgenerator = %{version}
Requires:       libQt5Designer5 = %{version}
Requires:       libQt5DesignerComponents5 = %{version}
Requires:       libQt5Help5 = %{version}
Requires:       libqt5-linguist-devel = %{version}
Requires:       libxslt-devel
Requires:       pkgconfig(Qt5Xml) >= %{real_version}
Recommends:     %{name} = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
You need this package if you want to compile programs with qttools.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 Tools library
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qttools that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 tools examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qttools module.

%package example-plugins
Summary:        Example plugins for Qt5 Designer
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Recommends:     %{name}-examples

%description example-plugins
Example plugins for Qt5 Designer, e.g. a TicTacToe and a World Clock widget.

%package -n libQt5Designer5
Summary:        Qt 5 Designer Library
Group:          Development/Libraries/X11
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
%requires_ge    libQt5Widgets5
%requires_ge    libQt5Xml5

%description -n libQt5Designer5
The Qt 5 Designer library.

%package -n libQt5DesignerComponents5
Summary:        Qt 5 Designer Components Library
Group:          Development/Libraries/X11
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
Requires:       libQt5Designer5 = %{version}

%description -n libQt5DesignerComponents5
The Qt 5 Designer Components library.

%package -n libQt5Help5
Summary:        Qt 5 Help Library
Group:          Development/Libraries/X11
%requires_ge    libQt5Network5
%requires_ge    libQt5Sql5
%requires_ge    libQt5Widgets5

%description -n libQt5Help5
The Qt 5 Help library.

%package qhelpgenerator
Summary:        Generator for Qt5 Help files (qch)
Group:          Development/Libraries/X11
# help files are SQLite databases, so assistant/qhelpgenerator need the SQLite plugin
Requires:       libQt5Sql5-sqlite >= %{real_version}

%description qhelpgenerator
Binaries for generating .qch help catalogs.

%package -n libqt5-linguist
Summary:        Qt 5 Linguist Tools
Group:          Development/Libraries/X11
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
%requires_ge    libQt5PrintSupport5
%requires_ge    libQt5Widgets5
%requires_ge    libQt5Xml5

%description -n libqt5-linguist
The Qt 5 Linguist Tools.

%package -n libqt5-linguist-devel
Summary:        Development files for the Qt 5 Linguist tools
Group:          Development/Libraries/X11
Requires:       libqt5-linguist = %{version}
Requires:       pkgconfig(Qt5Core) >= %{real_version}

%description -n libqt5-linguist-devel
The Qt 5 Linguist Tools - development files.

%package -n libqt5-qdbus
Summary:        Command line client for communication over D-Bus
Group:          Development/Libraries/X11
License:        GPL-3.0-only WITH Qt-GPL-exception-1.0
Conflicts:      %{name} < %{version}

%description -n libqt5-qdbus
Command line client for communication over D-Bus.

%package -n libqt5-qtpaths
Summary:        Command line client to QStandardPaths
Group:          Development/Libraries/X11
License:        BSD-3-Clause
Conflicts:      %{name} < %{version}

%description -n libqt5-qtpaths
Command line client to QStandardPaths.

%package doc
Summary:        Qt 5 tool used by Qt Developers to generate documentation
Group:          Development/Libraries/C and C++
License:        GPL-3.0-only
Provides:       libqt5-qtbase-doc = %{version}
Obsoletes:      libqt5-qtbase-doc < %{version}
# qdoc hardcodes clang include paths: boo#1109367, QTBUG-70687
%global _clang_major_version %(printf %{pkg_version clang-devel} | cut -d. -f1)

%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%requires_eq libclang%{_clang_major_version}
%else
%requires_eq clang%{_clang_major_version}
%endif

%description doc
Qt 5 tool used by Qt Developers to generate documentation for software projects.

%post -p /sbin/ldconfig
%post -n libQt5Designer5 -p /sbin/ldconfig
%post -n libQt5DesignerComponents5 -p /sbin/ldconfig
%post -n libQt5Help5 -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%postun -n libQt5Designer5 -p /sbin/ldconfig
%postun -n libQt5DesignerComponents5 -p /sbin/ldconfig
%postun -n libQt5Help5 -p /sbin/ldconfig

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install
find %{buildroot}%{_libdir} -type f -name '*pc' -print -exec sed -i -e "s, -L%{buildroot}/?\S+,,g" -e "s,^moc_location=.*,moc_location=%{_libqt5_bindir}/moc," -e "s,uic_location=.*,uic_location=%{_libqt5_bindir}/uic," {} +
%fdupes -s %{buildroot}%{_libqt5_includedir}

# kill .la files
find %{buildroot}%{_libdir} -type f -name "*.la" -delete -print

# Link all the binaries with -qt5 suffix to %%{_bindir}
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_libqt5_bindir}
for i in * ; do
  case "${i}" in
   assistant|designer|lconvert|linguist|lrelease|lupdate|pixeltool|qcollectiongenerator|qdbus|qdbusviewer|qdoc|qhelpgenerator)
      ln -s %{_libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}-qt5
      ;;
   *)
      # No conflict with Qt4, so keep the original name for compatibility
      ln -s %{_libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}
      ln -s %{_libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}-qt5
      ;;
  esac
done
popd

# Do not add dependencies on the implementation of the abstract Designer plugin
# interface provided by the plugins, QTCREATORBUG-22886
rm %{buildroot}%{_libqt5_libdir}/cmake/Qt5Designer/Qt5Designer_*Plugin.cmake

install -D -m644 %{SOURCE11} %{buildroot}%{_datadir}/applications/designer5.desktop
install -D -m644 %{SOURCE12} %{buildroot}%{_datadir}/applications/linguist5.desktop
install -D -m644 %{SOURCE13} %{buildroot}%{_datadir}/applications/assistant5.desktop
install -D -m644 %{SOURCE14} %{buildroot}%{_datadir}/applications/qdbusviewer5.desktop

install -D -m644 src/assistant/assistant/images/assistant.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/assistant5.png
install -D -m644 src/assistant/assistant/images/assistant-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/assistant5.png
install -D -m644 src/linguist/linguist/images/icons/linguist-32-32.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/linguist5.png
install -D -m644 src/linguist/linguist/images/icons/linguist-128-32.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/linguist5.png
install -D -m644 src/designer/src/designer/images/designer.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/designer5.png
install -D -m644 src/qdbus/qdbusviewer/images/qdbusviewer.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/qdbusviewer5.png
install -D -m644 src/qdbus/qdbusviewer/images/qdbusviewer-128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/qdbusviewer5.png

%files
%license LICENSE.*
%{_bindir}/assistant*
%{_bindir}/designer*
%{_bindir}/pixeltool*
%{_bindir}/qdbusviewer*
%{_bindir}/qtdiag*
%{_bindir}/qtplugininfo*
%{_bindir}/qtattributionsscanner*
%{_bindir}/qdistancefieldgenerator*
%{_libqt5_bindir}/assistant*
%{_libqt5_bindir}/designer*
%{_libqt5_bindir}/pixeltool*
%{_libqt5_bindir}/qdbusviewer*
%{_libqt5_bindir}/qtdiag*
%{_libqt5_bindir}/qtplugininfo*
%{_libqt5_bindir}/qtattributionsscanner*
%{_libqt5_bindir}/qdistancefieldgenerator
%{_datadir}/applications/assistant5.desktop
%{_datadir}/applications/designer5.desktop
%{_datadir}/applications/qdbusviewer5.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/assistant5.png
%{_datadir}/icons/hicolor/*/apps/designer5.png
%{_datadir}/icons/hicolor/*/apps/qdbusviewer5.png
%dir %{_libqt5_libdir}/qt5/plugins/designer
%{_libqt5_libdir}/qt5/plugins/designer/libqquickwidget.so
# CMake target for some of the binaries in this package. Own the dir to not require CMake
%dir %{_libqt5_libdir}/cmake/
%{_libqt5_libdir}/cmake/Qt5AttributionsScannerTools/

%files -n libqt5-linguist
%license LICENSE.*
%{_bindir}/lconvert*
%{_bindir}/linguist*
%{_bindir}/lprodump*
%{_bindir}/lrelease*
%{_bindir}/lupdate*
%{_libqt5_bindir}/lconvert*
%{_libqt5_bindir}/linguist*
%{_libqt5_bindir}/lprodump*
%{_libqt5_bindir}/lrelease*
%{_libqt5_bindir}/lupdate*
%{_datadir}/applications/linguist5.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/linguist5.png

%files -n libQt5Designer5
%license LICENSE.*
%{_libqt5_libdir}/libQt5Designer.so.*

%files -n libQt5DesignerComponents5
%license LICENSE.*
%{_libqt5_libdir}/libQt5DesignerComponents.so.*

%files -n libQt5Help5
%license LICENSE.*
%{_libqt5_libdir}/libQt5Help.so.*

%files -n libqt5-linguist-devel
%license LICENSE.*
%{_libqt5_libdir}/cmake/Qt5LinguistTools/
%{_datadir}/qt5/phrasebooks

%files -n libqt5-qdbus
%license LICENSE.*
%{_bindir}/qdbus-qt5
%{_libqt5_bindir}/qdbus

%files -n libqt5-qtpaths
%license LICENSE.*
%{_bindir}/qtpaths*
%{_libqt5_bindir}/qtpaths

%if %{with qdoc}
%files doc
%license LICENSE.*
%{_bindir}/qdoc*
%{_libqt5_bindir}/qdoc*
# CMake target for some of the binaries in this package. Own the dir to not require CMake
%dir %{_libqt5_libdir}/cmake/
%{_libqt5_libdir}/cmake/Qt5DocTools/
%endif

%files qhelpgenerator
%license LICENSE.*
%{_bindir}/qhelpgenerator*
%{_bindir}/qcollectiongenerator*
%{_libqt5_bindir}/qhelpgenerator*
%{_libqt5_bindir}/qcollectiongenerator*

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/QtDesigner/%{so_version}
%{_libqt5_includedir}/QtDesignerComponents/%{so_version}
%{_libqt5_includedir}/QtHelp/%{so_version}
%{_libqt5_includedir}/QtUiTools/%{so_version}

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/QtDesigner/%{so_version}
%{_libqt5_includedir}/QtDesigner
%exclude %{_libqt5_includedir}/QtDesignerComponents/%{so_version}
%{_libqt5_includedir}/QtDesignerComponents
%exclude %{_libqt5_includedir}/QtHelp/%{so_version}
%{_libqt5_includedir}/QtHelp
%exclude %{_libqt5_includedir}/QtUiTools/%{so_version}
%{_libqt5_includedir}/QtUiTools
%{_libqt5_includedir}/QtUiPlugin
%{_libqt5_libdir}/cmake/Qt5Designer/
%{_libqt5_libdir}/cmake/Qt5DesignerComponents/
%{_libqt5_libdir}/cmake/Qt5Help/
%{_libqt5_libdir}/cmake/Qt5UiTools/
%{_libqt5_libdir}/cmake/Qt5UiPlugin/
%{_libqt5_libdir}/libQt5*.prl
%{_libqt5_libdir}/libQt5*.so
%{_libqt5_libdir}/libQt5*.a
%{_libqt5_libdir}/pkgconfig/Qt5*.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_*.pri
%dir %{_datadir}/qt5

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%files example-plugins
%license LICENSE.*
%{_libqt5_libdir}/qt5/plugins/designer
%exclude %{_libqt5_libdir}/qt5/plugins/designer/libqquickwidget.so

%changelog
