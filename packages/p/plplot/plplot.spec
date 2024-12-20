#
# spec file for package plplot
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


%define lua_version 5.3

%bcond_with    ocaml_camlidl
%define tk_enabled 1

# SECTION swig is patched on TW to support octave 6, but not on any Leaps
%if 0%{?suse_version} >= 1550
#
# No qhull/octave on arch, ppc
%ifarch %ix86 x86_64
# Octave 8+ unsupported
%define octave_enabled 0
%else
%define octave_enabled 0
%endif
#
%else
%define octave_enabled 0
%endif
# /SECTION

%bcond_without qhull

# FIXME Doesn't build with fPIC (it seems)
%define ada_enabled 0

%define X_display ":98"

%define ada_shlib libplplotada4
%define c_shlib libplplot17
%define cxx_shlib libplplotcxx15
%define csirocsa_shlib libcsirocsa0
%define csironn_shlib libcsironn0
%define fort_shlib libplplotfortran0
%define qsastime_shlib libqsastime0
%define qt_shlib libplplotqt2
%define wx_shlib libplplotwxwidgets1
# DONT SPLIT OUT plplot-tcltk-libs INTO INDIVIDUAL SHARED LIBS AS THEY ARE ALL REQUIRED TOGETHER AND THEIR SO NUMBERING CHANGE IN-STEP WITH EACH OTHER

%define skip_python312 1

Name:           plplot
Version:        5.15.0
Release:        0
Summary:        Software package for creating scientific plots
# Main license is LGPL-2.1+, but Octave bindings are licensed as GPL-2.0+
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Scientific/Other
URL:            http://plplot.sourceforge.net/
Source0:        http://download.sf.net/plplot/%{name}-%{version}.tar.gz
Patch0:         plplot-ocaml.patch
# PATCH-FIX-UPSTREAM plplot-5.9.9-ada-pic.patch idoenmez@suse.de -- Compile Ada code with -fPIC
Patch1:         plplot-5.9.9-ada-pic.patch
# PATCH-FIX-UPSTREAM plplot-include-QPainterPath.patch badshah400@gmail.com -- Include QPainterPath header when building Qt modules, needed for Qt >= 5.15.0; patch from upstream
Patch2:         plplot-include-QPainterPath.patch
# PATCH-FIX-UPSTREAM plplot-drop-FindLua-cmake-module.patch badshah400@gmail.com -- Drop in-house FindLua.cmake module, which is severely dated, to use cmake's own module and fix building for lua >= 5.4; patch taken from upstream.
Patch3:         plplot-drop-FindLua-cmake-module.patch
# PATCH-FIX-UPSTREAM https://sourceforge.net/p/plplot/bugs/196/ -- Use reentrant libqhull_r
Patch4:         0001-Use-reentrant-libqhull_r-instead-of-deprecated-libqh.patch
# PATCH-FIX-UPSTREAM support-python3-pythondemos.patch Use print function, so the script works with Python 3
Patch5:         support-python3-pythondemos.patch
# PATCH-FIX-UPSTREAM plplot-libharu-version-check.patch badshah400@gmail.com -- Include correct header for libharu version checks
Patch6:         plplot-libharu-version-check.patch
# PATCH-FIX-UPSTREAM plplot-pkgconfig-includedir.patch badshah400@gmail.com -- Fix includedir in pkgconfig files
Patch7:         plplot-pkgconfig-includedir.patch
# PATCH-FIX-UPSTREAM plplot-numpy-2.0-compat.patch gh#PLplot/PLplot#10 badshah400@gmail.com -- Make plplot compilation compatible with numpy >= 2.0
Patch8:         plplot-numpy-2.0-compat.patch
# PATCH-FIX-SUSE
Patch9:         plplot-reproducible-jar-mtime.patch
# List based on build_ada in gcc.spec
ExclusiveArch:  %ix86 x86_64 ppc ppc64 ppc64le s390 s390x ia64 aarch64 riscv64
BuildRequires:  cmake >= 3.13.2
BuildRequires:  fdupes
BuildRequires:  freefont
%if 0%{?ada_enabled}
BuildRequires:  gcc-ada
%endif
BuildRequires:  gcc-fortran >= 6
BuildRequires:  itcl-devel
BuildRequires:  itk
BuildRequires:  java-devel
BuildRequires:  lapack-devel
BuildRequires:  libharu-devel >= 2.3.0
BuildRequires:  libtool
BuildRequires:  ncurses-devel
%if %{with ocaml_camlidl}
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocamlfind(camlidl)
BuildRequires:  ocamlfind(findlib)
%endif
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module sip4-devel if %python-base < 3.11}
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if %{with qhull}
BuildRequires:  qhull-devel
%endif
BuildRequires:  swig
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(shapelib)
# Required for enabling tk driverand in the %%check section, currently disabled
BuildRequires:  hdf5-devel
%if %{?octave_enabled}
BuildRequires:  octave-devel
%endif
BuildRequires:  wxGTK3-devel >= 3.1
BuildRequires:  xorg-x11-server
BuildRequires:  perl(XML::DOM)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lasi)
BuildRequires:  pkgconfig(lua)
Requires:       libtool
Requires:       python-numpy
Recommends:     %{name}-doc = %{version}
%define python_subpackage_only 1
%python_subpackages

%description
PLplot is a library of functions that are useful for making scientific
plots.

PLplot can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

The PLplot library can be used to create standard x-y plots, semilog
plots, log-log plots, contour plots, 3D surface plots, mesh plots, bar
charts and pie charts. Multiple graphs (of the same or different sizes)
may be placed on a single page with multiple lines in each graph.

A variety of output file devices such as Postscript, png, jpeg, LaTeX
and others, as well as interactive devices such as xwin, tk, xterm and
Tektronics devices are supported. New devices can be easily added by
writing a small number of device dependent routines.

There are almost 2000 characters in the extended character set. This
includes four different fonts, the Greek alphabet and a host of
mathematical, musical, and other symbols. Some devices supports its own
way of dealing with text, such as the Postscript and LaTeX drivers, or
the png and jpeg drivers that uses the Freetype library.

This package provides the shared libraries for PLplot.

%package common
##########################################################################
Summary:        Files for development with PLplot
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Visualization/Graph
Provides:       %{name} = %{version}
Obsoletes:      %{name} < 5.12.0

%description common
PLplot is a library of functions that are useful for making scientific
plots.

PLplot can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

This package provides some common files shared between the different
PLplot interfaces.

%files common
%dir %{_libdir}/plplot%{version}
%dir %{_libdir}/plplot%{version}/drivers
%dir %{_datadir}/plplot%{version}
%{_libdir}/plplot%{version}/drivers/null.driver_info
%{_libdir}/plplot%{version}/drivers/null.so
%{_libdir}/plplot%{version}/drivers/mem.driver_info
%{_libdir}/plplot%{version}/drivers/mem.so
%{_datadir}/plplot%{version}/*.shp
%{_datadir}/plplot%{version}/*.shx
%{_datadir}/plplot%{version}/ss/
%{_datadir}/plplot%{version}/*.fnt
%{_datadir}/plplot%{version}/*.pal
%dir %{_datadir}/plplot%{version}/examples
%{_datadir}/plplot%{version}/examples/Chloe.pgm
%{_datadir}/plplot%{version}/examples/README.Chloe
##########################################################################

%package devel
##########################################################################
Summary:        Files for development with PLplot
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{c_shlib} = %{version}
Requires:       %{csirocsa_shlib} = %{version}
%if %{with qhull}
Requires:       %{csironn_shlib} = %{version}
%endif
Requires:       %{qsastime_shlib} = %{version}
Requires:       gcc-c++
Requires:       pkgconfig
Requires:       plplot-common = %{version}
Requires:       pkgconfig(freetype2)
Provides:       %{name} = %{version}
Obsoletes:      %{name} < 5.12.0

%description devel
PLplot is a library of functions that are useful for making scientific
plots.

PLplot can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

This package provides the files necessary for development with PLplot
in C.

%files devel -f %{_builddir}/%{name}.filelist.ocaml
%license COPYING.LIB Copyright
%doc AUTHORS FAQ README README.release
%{_bindir}/pltek
%{_infodir}/plplotdoc.info*
%{_mandir}/man1/pltek.1.gz
%{_includedir}/plplot/
%exclude %{_includedir}/plplot/plstream.h
%{_libdir}/libcsirocsa.so
%{_libdir}/libplplot.so
%{_libdir}/libqsastime.so
%{_libdir}/pkgconfig/plplot.pc
%dir %{_libdir}/cmake/plplot
%{_libdir}/cmake/plplot/export_csirocsa.cmake
%{_libdir}/cmake/plplot/export_csirocsa-*.cmake
%if %{with qhull}
%{_libdir}/libcsironn.so
%{_libdir}/cmake/plplot/export_csironn.cmake
%{_libdir}/cmake/plplot/export_csironn-*.cmake
%endif
%{_libdir}/cmake/plplot/export_mem.cmake
%{_libdir}/cmake/plplot/export_mem-*.cmake
%{_libdir}/cmake/plplot/export_null.cmake
%{_libdir}/cmake/plplot/export_null-*.cmake
%{_libdir}/cmake/plplot/export_plplot.cmake
%{_libdir}/cmake/plplot/export_plplot-*.cmake
%{_libdir}/cmake/plplot/export_plplotc.cmake
%{_libdir}/cmake/plplot/export_plplotc-*.cmake
%{_libdir}/cmake/plplot/export_plserver.cmake
%{_libdir}/cmake/plplot/export_plserver-*.cmake
%{_libdir}/cmake/plplot/export_pltek.cmake
%{_libdir}/cmake/plplot/export_pltek-*.cmake
%{_libdir}/cmake/plplot/export_qsastime.cmake
%{_libdir}/cmake/plplot/export_qsastime-*.cmake
%{_libdir}/cmake/plplot/plplotConfig.cmake
%{_libdir}/cmake/plplot/plplot_exports.cmake
%{_mandir}/man3/pl*.3*
# PLMETA DRIVER DISABLED
#%%{_bindir}/plm2gif
#%%{_bindir}/plpr
#%%{_bindir}/plrender
#%%{_mandir}/man1/plm2gif.1.gz
#%%{_mandir}/man1/plpr.1.gz
#%%{_mandir}/man1/plrender.1.gz
#%%{_datadir}/plplot%%{version}/examples/test_plrender.sh
#%%{_libdir}/plplot%%{version}/drivers/plmeta.driver_info
#%%{_libdir}/plplot%%{version}/drivers/plmeta.so
%dir %{_datadir}/plplot%{version}/examples
%dir %{_datadir}/plplot%{version}/examples/plplot_test
%{_datadir}/plplot%{version}/examples/CTestConfig.cmake
%{_datadir}/plplot%{version}/examples/CTestCustom.cmake.in
%{_datadir}/plplot%{version}/examples/plplot-test.sh
%{_datadir}/plplot%{version}/examples/plplot-test-interactive.sh
%{_datadir}/plplot%{version}/examples/c/
%{_datadir}/plplot%{version}/examples/c++/
%{_datadir}/plplot%{version}/examples/Makefile
%{_datadir}/plplot%{version}/examples/plplot_test/CMakeLists.txt
%{_datadir}/plplot%{version}/examples/test_c.sh
%{_datadir}/plplot%{version}/examples/test_c_interactive.sh
%{_datadir}/plplot%{version}/examples/test_cxx.sh
%{_datadir}/plplot%{version}/examples/test_diff.sh
%if %{with ocaml_camlidl}
%{_libdir}/pkgconfig/plplot-ocaml.pc
%{_datadir}/plplot%{version}/examples/ocaml
%{_datadir}/plplot%{version}/examples/test_ocaml.sh
%endif

##########################################################################

%package doc
##########################################################################
Summary:        Documentation for PLplot and its bindings
License:        LGPL-2.1-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description doc
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the documentation for PLplot and its associated
modules.

%files doc
%dir %{_docdir}/%{name}-doc
%{_docdir}/%{name}-doc/*
##########################################################################

%if 0%{?ada_enabled}
%package -n %{ada_shlib}
##########################################################################
Summary:        Shared libraries for PLplot's Ada bindings
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{ada_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared libraries necessary for using PLplot
with Ada.

%post -n %{ada_shlib} -p /sbin/ldconfig

%postun -n %{ada_shlib} -p /sbin/ldconfig

%files -n %{ada_shlib}
%{_libdir}/libplplotada.so.*
##########################################################################

%package -n %{name}ada-devel
##########################################################################
Summary:        Ada bindings for development with PLplot
License:        LGPL-2.1-or-later
Group:          Development/Languages/Other
Requires:       %{ada_shlib} = %{version}
Requires:       %{name}-common = %{version}
Requires:       gcc-ada
Requires:       pkgconfig
Provides:       %{name}-ada-devel = %{version}
Obsoletes:      %{name}-ada-devel < 5.12.0

%description -n %{name}ada-devel
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the files necessary for using PLplot in Ada.

%files -n %{name}ada-devel
%dir %{_libdir}/ada
%dir %{_libdir}/ada/adalib
%dir %{_datadir}/ada
%dir %{_datadir}/ada/adainclude
%{_libdir}/libplplotada.so
%{_libdir}/ada/adalib/plplotada/
%{_libdir}/pkgconfig/plplot-ada.pc
%{_libdir}/cmake/plplot/export_plplotada.cmake
%{_libdir}/cmake/plplot/export_plplotada-*.cmake
%{_datadir}/ada/adainclude/plplotada/
%{_datadir}/plplot%{version}/examples/ada/
%{_datadir}/plplot%{version}/examples/test_ada.sh
##########################################################################
%endif

%package -n %{fort_shlib}
##########################################################################
Summary:        Shared libraries for PLplot's Fortran bindings
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{fort_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared libraries necessary for using PLplot
with Fortran.

%post -n %{fort_shlib} -p /sbin/ldconfig

%postun -n %{fort_shlib} -p /sbin/ldconfig

%files -n %{fort_shlib}
%{_libdir}/libplplotfortran.so.*
##########################################################################

%package -n %{name}fortran-devel
##########################################################################
Summary:        Fortran bindings for development with PLplot
License:        LGPL-2.1-or-later
Group:          Development/Languages/Fortran
Requires:       %{fort_shlib} = %{version}
Requires:       %{name}-common = %{version}
Requires:       gcc-fortran
Requires:       pkgconfig
Obsoletes:      %{name}f95-devel < 5.13.0
Provides:       %{name}f95-devel = %{version}
Obsoletes:      %{name}-fortran-devel < 5.12.0
Provides:       %{name}-fortran-devel = %{version}

%description -n %{name}fortran-devel
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the files necessary for using PLplot in Fortran.

%files -n %{name}fortran-devel
%dir %{_libdir}/fortran
%dir %{_libdir}/fortran/modules
%{_libdir}/fortran/modules/plplot/
%{_libdir}/libplplotfortran.so
%{_libdir}/pkgconfig/plplot-fortran.pc
%{_libdir}/cmake/plplot/export_plfortrandemolib.cmake
%{_libdir}/cmake/plplot/export_plfortrandemolib-*.cmake
%{_libdir}/cmake/plplot/export_plplotfortran.cmake
%{_libdir}/cmake/plplot/export_plplotfortran-*.cmake
%{_datadir}/plplot%{version}/examples/fortran/
%{_datadir}/plplot%{version}/examples/test_fortran.sh
##########################################################################

%package java
##########################################################################
Summary:        PLplot functions for scientific plotting with Java
License:        LGPL-2.1-or-later
Group:          Productivity/Scientific/Other
Requires:       %{name}-common = %{version}
Requires:       java

%description java
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with Java.

%files java
%{_libdir}/plplot%{version}/libplplotjavac_wrap.so
%{_libdir}/cmake/plplot/export_plplotjavac_wrap.cmake
%{_libdir}/cmake/plplot/export_plplotjavac_wrap-*.cmake
%{_datadir}/java/plplot.jar
%{_datadir}/plplot%{version}/examples/java/
%{_datadir}/plplot%{version}/examples/test_java.sh
##########################################################################

%package lua
##########################################################################
Summary:        PLplot functions for scientific plotting with Lua
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}
Requires:       lua

%description lua
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with Lua.

%files lua
%{_libdir}/lua/plplot/
%{_libdir}/cmake/plplot/export_plplotluac.cmake
%{_libdir}/cmake/plplot/export_plplotluac-*.cmake
%{_datadir}/plplot%{version}/examples/lua/
%{_datadir}/plplot%{version}/examples/test_lua.sh
##########################################################################

%package octave
##########################################################################
Summary:        PLplot functions for scientific plotting with Octave
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}
Requires:       octave

%description octave
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with Octave.

%if 0%{?octave_enabled}
%files octave
%{_datadir}/%{name}_octave/
%{_datadir}/octave/site/m/PLplot/
%{_libdir}/octave/site/oct/*/plplot_octave.oct
%{_libdir}/cmake/plplot/export_plplot_octave-*.cmake
%{_libdir}/cmake/plplot/export_plplot_octave.cmake
%{_datadir}/plplot%{version}/examples/octave/
%{_datadir}/plplot%{version}/examples/test_octave.sh
%endif
##########################################################################

%if "%{python_flavor}" != "python311"
%package -n python-plplot-pyqt5
##########################################################################
Summary:        PLplot functions for scientific plotting with python-qt5
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
Requires:       %{name}-common = %{version}
Requires:       python-qt5
# Python 3.10 is the last version of Python with sip4 support
%if "%{python_flavor}" == "python3" || "%{python_flavor}" == "python310"
Obsoletes:      plplot-python3-qt < %{version}-%{release}
Provides:       plplot-python3-qt = %{version}-%{release}
Recommends:     plplot-pyqt5-cmake
%endif

%description -n python-plplot-pyqt5
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with python-qt.

%files %{python_files plplot-pyqt5}
%{python_sitearch}/plplot_pyqt5.so
%endif
##########################################################################

%package -n plplot-pyqt5-cmake
##########################################################################
Summary:        PLplot functions for scientific plotting with python-qt5
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
Requires:       python3-plplot-pyqt5

%description -n plplot-pyqt5-cmake
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the cmake files optionally required for building
cmake based projects with plplot-pyqt5.

%if ("%{python_flavor}" == "python3" || "%{python_provides}" == "python3") && "%{python_flavor}" != "python311"
%files -n plplot-pyqt5-cmake
%{_libdir}/cmake/plplot/export_plplot_pyqt5.cmake
%{_libdir}/cmake/plplot/export_plplot_pyqt5-*.cmake
%endif
##########################################################################

%package -n %{qt_shlib}
##########################################################################
Summary:        PLplot functions for scientific plotting with Qt
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{qt_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with Qt.

%post -n %{qt_shlib} -p /sbin/ldconfig

%postun -n %{qt_shlib} -p /sbin/ldconfig

%files -n %{qt_shlib}
%{_libdir}/libplplotqt.so.*
##########################################################################

%package -n %{name}qt-devel
##########################################################################
Summary:        PLplot functions for scientific plotting with qt
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       %{qt_shlib} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5Gui)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5Widgets)
Provides:       %{name}-qt-devel = %{version}
Obsoletes:      %{name}-qt-devel < 5.12.0
Requires:       %{name}-common = %{version}

%description -n %{name}qt-devel
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the development files for using PLplot
with Qt.

%files -n %{name}qt-devel
%{_libdir}/libplplotqt.so
%{_libdir}/pkgconfig/plplot-qt.pc
%{_libdir}/plplot%{version}/drivers/qt.driver_info
%{_libdir}/plplot%{version}/drivers/qt.so
%{_libdir}/cmake/plplot/export_plplotqt.cmake
%{_libdir}/cmake/plplot/export_plplotqt-*.cmake
%{_libdir}/cmake/plplot/export_qt.cmake
%{_libdir}/cmake/plplot/export_qt-*.cmake
##########################################################################

%package tcltk-libs
##########################################################################
Summary:        PLplot functions for scientific plotting with Tcl/Tk
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       %{name}-tcltk = %{version}
Obsoletes:      %{name}-tcltk < 5.12.0

%description tcltk-libs
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with Tcl/Tk.

%post tcltk-libs -p /sbin/ldconfig

%postun tcltk-libs -p /sbin/ldconfig

%files tcltk-libs
%{_libdir}/libplplottcltk*.so.*
%{_libdir}/libtclmatrix.so.*
##########################################################################

%package tcltk-devel
##########################################################################
Summary:        PLplot functions for scientific plotting with Tcl/Tk
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       %{name}-common = %{version}
Requires:       %{name}-tcltk-libs = %{version}
Requires:       itcl-devel
Requires:       itk
Requires:       pkgconfig
Requires:       tcl-devel
Requires:       tk-devel

%description tcltk-devel
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the development files for using PLplot with Tcl/Tk.

%files tcltk-devel
%{_bindir}/pltcl
%{_libdir}/libplplottcltk*.so
%{_libdir}/libtclmatrix.so
%{_libdir}/cmake/plplot/export_pltcl.cmake
%{_libdir}/cmake/plplot/export_pltcl-*.cmake
%{_libdir}/pkgconfig/plplot-tcl*.pc
%{_libdir}/cmake/plplot/export_tclmatrix.cmake
%{_libdir}/cmake/plplot/export_tclmatrix-*.cmake
%{_datadir}/plplot%{version}/examples/test_tcl.sh
%{_datadir}/plplot%{version}/examples/tcl/
%{_datadir}/plplot%{version}/pkgIndex.tcl
%{_datadir}/plplot%{version}/tcl/
%{_mandir}/man1/plserver.1.gz
%{_mandir}/man1/pltcl.1.gz

%if %{tk_enabled}
%{_bindir}/plserver
%{_datadir}/plplot%{version}/examples/tk/
%{_libdir}/plplot%{version}/drivers/tk.driver_info
%{_libdir}/plplot%{version}/drivers/tk.so
%{_libdir}/plplot%{version}/drivers/tkwin.driver_info
%{_libdir}/plplot%{version}/drivers/tkwin.so
%{_libdir}/cmake/plplot/export_tk.cmake
%{_libdir}/cmake/plplot/export_tk-*.cmake
%{_libdir}/cmake/plplot/export_tkwin.cmake
%{_libdir}/cmake/plplot/export_tkwin-*.cmake
%{_libdir}/cmake/plplot/export_plplottcltk.cmake
%{_libdir}/cmake/plplot/export_plplottcltk_Main.cmake
%{_libdir}/cmake/plplot/export_plplottcltk_Main-*.cmake
%{_libdir}/cmake/plplot/export_plplottcltk-*.cmake
%{_libdir}/cmake/plplot/export_Pltk_init.cmake
%{_libdir}/cmake/plplot/export_Pltk_init-*.cmake
%{python_sitearch}/Plframe.py*
%{python_sitearch}/TclSup.py*
%{python_sitearch}/*Pltk_init.*
%endif

##########################################################################

%package -n %{wx_shlib}
##########################################################################
Summary:        PLplot functions for scientific plotting with wxWidgets
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{wx_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with wxWidgets.

%post -n %{wx_shlib} -p /sbin/ldconfig

%postun -n %{wx_shlib} -p /sbin/ldconfig

%files -n %{wx_shlib}
%{_libdir}/libplplotwxwidgets.so.*
##########################################################################

%package wxwidgets
##########################################################################
Summary:        PLplot plot viewer built on wxWidgets
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Visualization/Graph
Requires:       %{name}-common = %{version}
Requires:       %{wx_shlib} = %{version}

%description wxwidgets
PLplot is a library of functions that are useful for making scientific
plots.

This package provides a PLplot viewer built using the wxWidgets GUI API.

%files wxwidgets
%{_bindir}/wxPLViewer
%{_libdir}/cmake/plplot/export_wxPLViewer.cmake
%{_libdir}/cmake/plplot/export_wxPLViewer-*.cmake
##########################################################################

%package -n %{name}wxwidgets-devel
##########################################################################
Summary:        PLplot bindings for development with wxWidgets
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       %{wx_shlib} = %{version}
Requires:       pkgconfig
Requires:       wxWidgets-devel
Provides:       %{name}-wxwidgets-devel = %{version}
Obsoletes:      %{name}-wxwidgets-devel < 5.12.0
Requires:       %{name}-common = %{version}

%description -n %{name}wxwidgets-devel
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with wxWidgets.

%files -n %{name}wxwidgets-devel
%{_libdir}/libplplotwxwidgets.so
%{_libdir}/pkgconfig/plplot-wxwidgets.pc
%{_libdir}/plplot%{version}/drivers/wxwidgets.driver_info
%{_libdir}/plplot%{version}/drivers/wxwidgets.so
%{_libdir}/cmake/plplot/export_plplotwxwidgets.cmake
%{_libdir}/cmake/plplot/export_plplotwxwidgets-*.cmake
%{_libdir}/cmake/plplot/export_wxwidgets.cmake
%{_libdir}/cmake/plplot/export_wxwidgets-*.cmake
##########################################################################

%package -n %{c_shlib}
##########################################################################
Summary:        PLplot functions for scientific plotting with C
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{c_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared lib for PLplot's C binding.

%post -n %{c_shlib} -p /sbin/ldconfig

%postun -n %{c_shlib} -p /sbin/ldconfig

%files -n %{c_shlib}
%{_libdir}/libplplot.so.*
##########################################################################

%package -n %{cxx_shlib}
##########################################################################
Summary:        PLplot functions for scientific plotting with C++
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{cxx_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared lib for PLplot's C++ binding.

%post -n %{cxx_shlib} -p /sbin/ldconfig

%postun -n %{cxx_shlib} -p /sbin/ldconfig

%files -n %{cxx_shlib}
%{_libdir}/libplplotcxx.so.*
##########################################################################

%package -n plplotcxx-devel
##########################################################################
Summary:        PLplot functions for scientific plotting with C++
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{cxx_shlib} = %{version}
Requires:       %{name}-common = %{version}

%description -n plplotcxx-devel
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared lib for PLplot's C++ binding.

%files -n plplotcxx-devel
%{_libdir}/libplplotcxx.so
%{_libdir}/pkgconfig/plplot-c++.pc
%{_libdir}/cmake/plplot/export_plplotcxx.cmake
%{_libdir}/cmake/plplot/export_plplotcxx-*.cmake
%{_includedir}/plplot/plstream.h
##########################################################################

%package -n %{csirocsa_shlib}
##########################################################################
Summary:        PLplot csirocsa component
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{csirocsa_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared lib for PLplot's csirocsa.

%post -n %{csirocsa_shlib} -p /sbin/ldconfig

%postun -n %{csirocsa_shlib} -p /sbin/ldconfig

%files -n %{csirocsa_shlib}
%{_libdir}/libcsirocsa.so.*
##########################################################################

%if %{with qhull}
%package -n %{csironn_shlib}
##########################################################################
Summary:        PLplot csironn component
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{csironn_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared lib for PLplot's csironn.

%post -n %{csironn_shlib} -p /sbin/ldconfig

%postun -n %{csironn_shlib} -p /sbin/ldconfig

%files -n %{csironn_shlib}
%{_libdir}/libcsironn.so.*
%endif
##########################################################################

%package -n %{qsastime_shlib}
##########################################################################
Summary:        PLplot qsatime component
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{qsastime_shlib}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the shared lib for PLplot's qsatime.

%post -n %{qsastime_shlib} -p /sbin/ldconfig

%postun -n %{qsastime_shlib} -p /sbin/ldconfig

%files -n %{qsastime_shlib}
%{_libdir}/libqsastime.so.*
##########################################################################

%package -n python-%{name}
##########################################################################
Summary:        PLplot functions for scientific plotting with Python
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-common = %{version}
Requires:       python-base
Requires:       python-numpy
# For update from the last python3-plplot package built against python3.10
%if "%{python_flavor}" == "python310"
Conflicts:      python3-%{name} < %{version}-%{release}
%endif
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Obsoletes:      python3-%{name} < %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
%endif

%description -n python-%{name}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot's Python binding.

%files %{python_files %{name}}
%{python_sitearch}/_plplotc.so
%{python_sitearch}/plplot.py
%{python_sitearch}/plplotc.py
%{_datadir}/plplot%{version}/examples/python%{python_version}/
%{_datadir}/plplot%{version}/examples/test_python%{python_version}.sh
##########################################################################

%package driver-cairo
##########################################################################
Summary:        PLplot driver using the cairo backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-cairo
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the cairo driver for plotting using PLplot.

%files driver-cairo
%{_libdir}/plplot%{version}/drivers/cairo.driver_info
%{_libdir}/plplot%{version}/drivers/cairo.so
%{_libdir}/cmake/plplot/export_cairo.cmake
%{_libdir}/cmake/plplot/export_cairo-*.cmake
##########################################################################

%package driver-ntk
##########################################################################
Summary:        PLplot driver using the ntk backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-ntk
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the ntk driver for plotting using PLplot.

%files driver-ntk
%{_libdir}/plplot%{version}/drivers/ntk.driver_info
%{_libdir}/plplot%{version}/drivers/ntk.so
%{_libdir}/cmake/plplot/export_ntk.cmake
%{_libdir}/cmake/plplot/export_ntk-*.cmake
##########################################################################

%package driver-pdf
##########################################################################
Summary:        PLplot driver using the pdf backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-pdf
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the pdf driver for plotting using PLplot.

%files driver-pdf
%{_libdir}/plplot%{version}/drivers/pdf.driver_info
%{_libdir}/plplot%{version}/drivers/pdf.so
%{_libdir}/cmake/plplot/export_pdf.cmake
%{_libdir}/cmake/plplot/export_pdf-*.cmake
##########################################################################

%package driver-ps
##########################################################################
Summary:        PLplot driver using the ps backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-ps
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the ps driver for plotting using PLplot.

%files driver-ps
%{_libdir}/plplot%{version}/drivers/ps.driver_info
%{_libdir}/plplot%{version}/drivers/ps.so
%{_libdir}/cmake/plplot/export_ps.cmake
%{_libdir}/cmake/plplot/export_ps-*.cmake
##########################################################################

%package driver-psttf
##########################################################################
Summary:        PLplot driver using the psttf backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-psttf
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the psttf driver for plotting using PLplot.

%files driver-psttf
%{_libdir}/plplot%{version}/drivers/psttf.driver_info
%{_libdir}/plplot%{version}/drivers/psttf.so
%{_libdir}/cmake/plplot/export_psttf.cmake
%{_libdir}/cmake/plplot/export_psttf-*.cmake
##########################################################################

%package driver-svg
##########################################################################
Summary:        PLplot driver using the SVG backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-svg
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the SVG driver for plotting using PLplot.

%files driver-svg
%{_libdir}/plplot%{version}/drivers/svg.driver_info
%{_libdir}/plplot%{version}/drivers/svg.so
%{_libdir}/cmake/plplot/export_svg.cmake
%{_libdir}/cmake/plplot/export_svg-*.cmake
##########################################################################

%package driver-xfig
##########################################################################
Summary:        PLplot driver using the xfig backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-xfig
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the xfig driver for plotting using PLplot.

%files driver-xfig
%{_libdir}/plplot%{version}/drivers/xfig.driver_info
%{_libdir}/plplot%{version}/drivers/xfig.so
%{_libdir}/cmake/plplot/export_xfig.cmake
%{_libdir}/cmake/plplot/export_xfig-*.cmake
##########################################################################

%package driver-xwin
##########################################################################
Summary:        PLplot driver using the xwin backend
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       plplot-common = %{version}

%description driver-xwin
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the xwin driver for plotting using PLplot.

%files driver-xwin
%{_libdir}/plplot%{version}/drivers/xwin.driver_info
%{_libdir}/plplot%{version}/drivers/xwin.so
%{_libdir}/cmake/plplot/export_xwin.cmake
%{_libdir}/cmake/plplot/export_xwin-*.cmake
##########################################################################

%prep
%setup
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
# The "--date" option was added into jar in OpenJDK 17
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
%patch -P 9 -p1
%endif

%build
for file in NEWS README.release
do
  iconv -f ISO-8859-1 -t UTF-8 $file > ${file}.tmp
  touch -r $file ${file}.tmp
  mv ${file}.tmp $file
done

export CFLAGS="%{optflags} -DUSE_INTERP_RESULT -fno-strict-aliasing"
# c++14 needs to use explicitly to avoid issues with GCC 11
export CXXFLAGS="%{optflags} -std=c++14 -fno-strict-aliasing"
export FFLAGS="%{optflags}"
export LDFLAGS="-fPIC"

# X-server and $DISPLAY required to enable tk bindings
export DISPLAY=%{X_display}
Xvfb -noreset %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 5
%{python_expand #Set the $python var
# Define cmake common opts
export CMAKE_COMMON_OPTS="-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
-DDOC_DIR:PATH=%{_docdir}/%{name}-doc \
-DCMAKE_INSTALL_MANDIR:PATH=%{_mandir} \
-DCMAKE_INSTALL_INFODIR:PATH=%{_infodir} \
-DENABLE_compiler_diagnostics=ON \
-DPL_FREETYPE_FONT_PATH:PATH=\"%{_datadir}/fonts/truetype\" \
-DUSE_RPATH:BOOL=OFF \
-DCMAKE_SKIP_RPATH:BOOL=OFF \
-DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
-DBUILD_DOC:BOOL=OFF \
-DBUILD_TEST:BOOL=ON  \
-DENABLE_python:BOOL=ON \
-DENABLE_qt:BOOL=ON \
-DPLPLOT_PYTHON_EXACT_VERSION=%{$python_version} \
-DPLPLOT_USE_QT5:BOOL=ON \
-DPLD_pdfcairo:BOOL=ON \
-DPLD_pngcairo:BOOL=ON \
-DPLD_pscairo:BOOL=ON \
-DPLD_epscairo:BOOL=ON \
-DPLD_svgcairo:BOOL=ON \
-DPLD_epsqt:BOOL=OFF \
-DPLD_pdfqt:BOOL=ON \
-DPLD_bmpqt:BOOL=ON \
-DPLD_jpgqt:BOOL=ON \
-DPLD_pngqt:BOOL=ON \
-DPLD_ppmqt:BOOL=ON \
-DPLD_tiffqt:BOOL=ON \
-DPLD_svgqt:BOOL=ON \
-DPLD_pdf:BOOL=ON \
-DPLD_ps:BOOL=ON \
-DPLD_psc:BOOL=ON \
-DPLD_psttf:BOOL=ON \
-DPLD_psttfc:BOOL=ON \
-DPLD_qtwidget:BOOL=ON \
-DPLD_svg:BOOL=ON \
-DPLD_xfig:BOOL=ON \
-DPLD_xcairo:BOOL=ON \
-DPLD_extcairo:BOOL=ON \
-DPLD_extqt:BOOL=ON \
-DPLD_wxpng:BOOL=OFF \
-DPLD_wxwidgets:BOOL=ON
"

mkdir ../$python
cp -pr ./* ../$python
pushd ../$python
if [ ${python_flavor} = python311 ]; then
  export CMAKE_COMMON_OPTS="${CMAKE_COMMON_OPTS} -DENABLE_pyqt5:BOOL=OFF"
else
  export CMAKE_COMMON_OPTS="${CMAKE_COMMON_OPTS} -DENABLE_pyqt5:BOOL=ON"
fi
%cmake ${CMAKE_COMMON_OPTS} \
%if "$python_" == "python3_" || "%{$python_provides}" == "python3"
        -DENABLE_ada:BOOL=%{?ada_enabled:ON}%{!?ada_enabled:OFF} \
        -DENABLE_cxx:BOOL=ON \
        -DENABLE_d:BOOL=OFF \
        -DENABLE_fortran:BOOL=ON \
        -DENABLE_itcl:BOOL=ON \
        -DENABLE_itk:BOOL=%{?tk_enabled:ON}%{!?tk_enabled:OFF} \
        -DENABLE_java:BOOL=ON \
        -DENABLE_lua:BOOL=ON \
        -DENABLE_ocaml:BOOL=%{?with_ocaml_camlidl:ON}%{!?with_ocaml_camlidl:OFF} \
        -DENABLE_octave:BOOL=%{?octave_enabled:ON}%{!?octave_enabled:OFF} \
        -DENABLE_tcl:BOOL=ON \
        -DENABLE_tk:BOOL=%{?tk_enabled:ON}%{!?tk_enabled:OFF} \
        -DENABLE_wxwidgets:BOOL=ON \
        -DPREBUILT_DOC:BOOL=ON \
				-DJAVAWRAPPER_DIR:PATH="%{_libdir}/plplot%{version}" \
        -DTRY_OCTAVE4=ON
%else
        -DDEFAULT_NO_BINDINGS:BOOL=ON \
        -DPREBUILT_DOC:BOOL=OFF
%endif

%cmake_build
popd
}

%install
%{python_expand pushd ../$python
%cmake_install
> %{_builddir}/%{name}.filelist.ocaml
%if %{with ocaml_camlidl}
: creating '%{name}.files' and '%{name}.files.devel'
%ocaml_create_file_list
mv %{name}.files.devel %{_builddir}/%{name}.filelist.ocaml
%endif

%if "$python_" == "python3_" || "%{$python_provides}" == "python3"
# Fix up tclIndex files so they are the same on all builds
for file in %{buildroot}%{_datadir}/plplot%{version}/examples/*/tclIndex
do
   grep '^[# ]' ${file} > tclIndex.hd
   grep -v '^[# ]' ${file} | sort > tclIndex
   cat tclIndex.hd tclIndex > ${file}
done
rm -rf %{buildroot}%{_datadir}/plplot%{version}/examples/cmake/modules/Platform

#Remove unnecessary examples that trigger build errors or warnings
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/cmake/modules/export_plplot-*.cmake
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/test_octave_interactive.sh
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/tk/*.in
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/tcl/*.in
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/tk/tk01

#Remove cmake files for the examples since they don't work anyway due to presence of rpath
rm -f %{buildroot}%{_datadir}/plplot%{version}/examples/CMakeLists.txt
rm -fr %{buildroot}%{_datadir}/plplot%{version}/examples/cmake

%if %{tk_enabled}
#Grant executable permissions to example tk binaries with valid shebang
chmod +x %{buildroot}%{_datadir}/%{name}%{version}/examples/tk/tk03
%endif

#Remove a fortran static library
rm %{buildroot}%{_libdir}/libplfortrandemolib*.a

sed -i "1{s@/usr/bin/env python@%{_bindir}/python%{$python_bin_suffix}@;}" %{buildroot}%{_datadir}/%{name}%{version}/examples/python/pytkdemo
%endif

#Fix python hashbangs for examples (/usr/bin/env python -> /usr/bin/pythonX.Y)
sed -i "1{s@/usr/bin/env python@%{_bindir}/python%{$python_bin_suffix}@;}" %{buildroot}%{_datadir}/%{name}%{version}/examples/python/x*
sed -i "1{s@/usr/bin/env python@%{_bindir}/python%{$python_bin_suffix}@;}" %{buildroot}%{_datadir}/%{name}%{version}/examples/python/*.py

# Move examples to versioned python dirs
mv %{buildroot}%{_datadir}/plplot%{version}/examples/python \
   %{buildroot}%{_datadir}/plplot%{version}/examples/python%{$python_version}
mv %{buildroot}%{_datadir}/plplot%{version}/examples/test_python.sh \
   %{buildroot}%{_datadir}/plplot%{version}/examples/test_python%{$python_version}.sh

# Only keep for primary flavour
if [ "${python_flavor}" != "python3" ] && [ "%{$python_provides}" != "python3" ]
then
  rm %{buildroot}%{_libdir}/cmake/plplot/export_plplot_pyqt5*.cmake
fi

%fdupes %{buildroot}%{_datadir}/
popd
}

%check
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 5
%{python_expand pushd ../$python
cd %__builddir
# Octave tests fail, known issue with tests
# Qt tests fail on Xvfb
# Avoid fontconfig warnings about un-writable cache dirs by setting HOME to pwd
export HOME=.
ctest -V -E "octave|qt" %{?_smp_mflags}
popd
}

%changelog
