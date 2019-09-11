#
# spec file for package klatexformula
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


# * Library version
%define	libversion		4
%define libversionpkgsuffix	4
# * Set whether to compile with debug information or not, depending on ability to create debug packages
%define cmake_build_type "RelWithDebInfo"
%define makeinstall_target install
# * Set CMake Common compilation options
#   Note: KLF_CMAKE_DEBUG only turns on KLF's CMake debugging messages, it has no effect upon the build itself.
%define cmake_common_options -DCMAKE_SKIP_RPATH=ON -DKLF_CMAKE_DEBUG=ON -DCMAKE_INSTALL_PREFIX="/usr" -DKLF_INSTALL_LIB_DIR=%{_libdir} -DKLF_INSTALL_BIN_DIR=%{_bindir}
# ktexteditor not ported to Qt5
%define build_ktexteditorplugin 0
%if %build_ktexteditorplugin
  %define cmake_buildktexteditorplugin -DKLF_BUILD_KTEXTEDITORPLUGIN=ON
%else
  %define cmake_buildktexteditorplugin -DKLF_BUILD_KTEXTEDITORPLUGIN=OFF
%endif
# -------------------------
#
#  Package Header
#  --------------

Name:           klatexformula
Version:        4.0.0
Release:        0
Summary:        A gaphical application for generating images from LaTeX equations
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            http://klatexformula.sourceforge.net/
Source0:        http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.6.4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  gs
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  libstdc++-devel
BuildRequires:  shared-mime-info
BuildRequires:  texlive-latex
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       libklfbackend%libversionpkgsuffix = %{version}
Requires:       libklftools%libversionpkgsuffix = %{version}
Requires:       shared-mime-info
Obsoletes:      KLatexFormula < 3.2
Obsoletes:      klatexformula-plugins < 3.2.2
Provides:       KLatexFormula = %{version}
Provides:       klatexformula-plugins = %{version}
# PATCH-FIX-UPSTREAM klatexformula-4.0.0-remove-uninstall-target.patch -- fix CMake build error (picked from Debian)
Patch1:         klatexformula-%{version}-remove-uninstall-target.patch
# PATCH-FIX-UPSTREAM klatexformula-4.0.0-include_QAction.patch
Patch2:         klatexformula-4.0.0-include_QAction.patch

%description
KLatexFormula is a graphical user interface for generating images
from LaTeX equations. These images can be dragged and dropped or copied and
pasted into external applications (presentations, text documents, graphics...),
or can be saved to disk in a variety of formats (PNG, JPG, BMP, EPS, PDF, etc.).

If the "cm-unicode" LaTeX package is installed, KLatexFormula can use LaTeX's
Computer Modern Sans Serif font as a default application font.

%package -n libklfbackend%libversionpkgsuffix

Summary:        KLatexFormula backend library (Qt4)
Group:          Development/Libraries/C and C++
Requires:       gs
Requires:       texlive-latex
Provides:       libklfbackend = %{version}

%description -n libklfbackend%libversionpkgsuffix
A C++/Qt library to generate images (PNG, EPS, PDF, plus all Qt-supported image
formats) from LaTeX equations.

This library implements the base functionality of KLatexFormula. This library
is compiled for Qt 4.

See also packages klatexformula and libklfbackend-qt3.

%package -n klfbackend-devel
Summary:        Development files for the KLatexFormula backend library
Group:          Development/Libraries/C and C++
Requires:       libklfbackend = %{version}
Provides:       libklfbackend-devel = %{version}
Obsoletes:      libklfbackend-devel < 4.0.0

%description -n klfbackend-devel
A C++/Qt library to generate images (PNG, EPS, PDF, plus all Qt-supported image
formats) from LaTeX equations.

This library implements the base functionality of KLatexFormula.

This package contains the needed files for development.

See also packages klatexformula-devel and libklfbackend-qt3-devel

%package -n libklftools%libversionpkgsuffix

Summary:        KLatexFormula tool library
Group:          Development/Libraries/C and C++
Provides:       libklftools = %{version}

%description -n libklftools%libversionpkgsuffix
A C++/Qt4 library containing general-purpose GUI tools.

These tools were originially written for use by klatexformula, but they have
been promoted to a library for use in any application.

%package -n klftools-devel
Summary:        Development files for the KLatexFormula tool library
Group:          Development/Libraries/C and C++
Requires:       libklftools = %{version}
Obsoletes:      %{name}-devel < 4.0.0
Provides:       %{name}-devel = %{version}
Obsoletes:      libklftools-devel < 4.0.0
Provides:       libklftools-devel = %{version}

%description -n klftools-devel
A C++/Qt4 library containing general-purpose GUI tools.

These tools were originially written for use by klatexformula, but they have
been promoted to a library for use in any application.

This package contains the needed files for development.

%package apidoc
Summary:        API documentation for KLatexFormula
Group:          Documentation/HTML
Requires:       klatexformula = %{version}
BuildArch:      noarch

%description apidoc
KLatexFormula is a graphical user interface for generating images
from LaTeX equations.

This package contains the API documentation of the libraries libklfbackend and
libklftool which are the different components of klatexformula.

%if %build_ktexteditorplugin

%package ktexteditor-plugin
Summary:        KLatexFormula integration into KDE4's text editor
Group:          Productivity/Publishing/TeX/Frontends
Requires:       klatexformula = %{version}
%{?kde4_runtime_requires}

%description ktexteditor-plugin
KLatexFormula is a graphical user interface for generating images
from LaTeX equations.

This package contains a KLatexFormula integration plugin for KDE4's KTextEditor
interface. This makes KLatexFormula integrate into Kate, Kile, and any other
KDE4 application using KTextEditor.

%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build

%cmake -DCMAKE_BUILD_TYPE=%cmake_build_type \
       -DKLF_LIBKLFBACKEND_STATIC=OFF \
       -DKLF_LIBKLFTOOLS_STATIC=OFF \
       %cmake_common_options \
       %cmake_buildktexteditorplugin \
       -DKLF_INSTALL_RUNTIME=ON \
       -DKLF_INSTALL_DEVEL=OFF \
       -DKLF_INSTALL_KLFTOOLS_HEADERS=ON \
       -DKLF_INSTALL_KLFBACKEND_HEADERS=ON \
       -DKLF_INSTALL_KLFBACKEND_AUTO_HEADERS=ON \
       -DKLF_INCLUDE_FONTS="" \
       -DKLF_INSTALL_DESKTOP_CATEGORIES="Qt;Office;Utility;Viewer;DesktopUtility;" \
       -DKLF_INSTALL_DESKTOP_ICON="klatexformula" \
       -DKLF_INSTALL_SHARE_PIXMAPS_DIR="" \
       -DKLF_INSTALL_ICON_THEME="share/icons/hicolor" \
       -DKLF_INSTALL_RUN_POST_INSTALL=OFF \
       -DKLF_INSTALL_APIDOC_DIR="share/doc/klatexformula-api" \
       -DKLF_INSTALL_SHARE_MAN1_DIR=%{_mandir}/man1

make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

# Doxygen doc generates some duplicate files in the big lot ...
%fdupes %{buildroot}%{_datadir}/doc/klatexformula-api
# Man pages are duplicates
%fdupes -s %{buildroot}%{_mandir}

%suse_update_desktop_file klatexformula
%if %build_ktexteditorplugin
  %suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/ktexteditor_klf.desktop
  %suse_update_desktop_file %{buildroot}%{_datadir}/kde4/services/ktexteditor_klf_config.desktop
%endif

%files
%doc AUTHORS CMUFONTS_COPYING README
%license COPYING
%{_bindir}/klatexformula
%{_bindir}/klatexformula_cmdl
%{_datadir}/applications/klatexformula.desktop
%{_datadir}/icons/*/*/*/*
%{_datadir}/mime/packages/klatexformula-mime.xml
%{_mandir}/man1/klatexformula.1.gz
%{_mandir}/man1/klatexformula_cmdl.1.gz
%{_datadir}/klatexformula/

%post
update-mime-database /usr/share/mime
ldconfig

%postun
update-mime-database /usr/share/mime
ldconfig

%files -n libklfbackend%libversionpkgsuffix
%{_libdir}/libklfbackend.so.%libversion

%post -n libklfbackend%libversionpkgsuffix -p /sbin/ldconfig

%postun -n libklfbackend%libversionpkgsuffix -p /sbin/ldconfig

%files -n klfbackend-devel
%{_libdir}/libklfbackend.so
%{_includedir}/klfbackend/

%post -n klfbackend-devel -p /sbin/ldconfig

%postun -n klfbackend-devel -p /sbin/ldconfig

%files -n libklftools%libversionpkgsuffix
%{_libdir}/libklftools.so.*

%post -n libklftools%libversionpkgsuffix -p /sbin/ldconfig

%postun -n libklftools%libversionpkgsuffix -p /sbin/ldconfig

%files -n klftools-devel
%{_libdir}/libklftools.so
%{_includedir}/klftools/

%post -n klftools-devel -p /sbin/ldconfig

%postun -n klftools-devel -p /sbin/ldconfig

%files apidoc
%{_datadir}/doc/klatexformula-api

%if %build_ktexteditorplugin

%files ktexteditor-plugin
%{_libdir}/kde4/ktexteditor_klf.so
%{_datadir}/kde4/apps/ktexteditor_klf/
%{_datadir}/kde4/services/ktexteditor_klf.desktop
%{_datadir}/kde4/services/ktexteditor_klf_config.desktop
%endif

%changelog
