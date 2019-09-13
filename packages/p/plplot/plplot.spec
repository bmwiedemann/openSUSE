#
# spec file for package plplot
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} <= 1320
%define lua_version 5.2
%else
%define lua_version 5.3
%endif

%define tk_enabled 1

# SECTION Disable octave bindings for all versions until compilation against octave 4.4 is fixed
%define octave_enabled 0
# /SECTION

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

Name:           plplot
Version:        5.15.0
Release:        0
Summary:        Software package for creating scientific plots
# Main license is LGPL-2.1+, but Octave bindings are licensed as GPL-2.0+
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            http://plplot.sourceforge.net/
Source0:        http://download.sf.net/plplot/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM plplot-5.9.9-ada-pic.patch idoenmez@suse.de -- Compile Ada code with -fPIC
Patch1:         plplot-5.9.9-ada-pic.patch
BuildRequires:  cmake >= 3.13.2
BuildRequires:  fdupes
BuildRequires:  freefont
BuildRequires:  gcc-ada
BuildRequires:  gcc-fortran >= 6
BuildRequires:  itcl-devel
BuildRequires:  itk
BuildRequires:  java-devel
BuildRequires:  lapack-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  qhull-devel
BuildRequires:  shapelib
BuildRequires:  swig
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangoft2)
# Required for enabling tk driverand in the %%check section, currently disabled
BuildRequires:  hdf5-devel
%if %{?octave_enabled}
BuildRequires:  octave-devel
%endif
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  xorg-x11-server
BuildRequires:  perl(XML::DOM)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lasi)
BuildRequires:  pkgconfig(lua)

Requires:       libtool
Requires:       python3-numpy
Recommends:     %{name}-doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       %{csironn_shlib} = %{version}
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

%post devel
/sbin/install-info %{_infodir}/plplotdoc.info %{_infodir}/dir

%preun devel
/sbin/install-info --delete %{_infodir}/plplotdoc.info %{_infodir}/dir

%files devel
%license COPYING.LIB Copyright
%doc AUTHORS FAQ README README.release
%{_bindir}/pltek
%{_infodir}/plplotdoc.info*
%{_mandir}/man1/pltek.1.gz
%{_includedir}/plplot/
%exclude %{_includedir}/plplot/plstream.h
%{_libdir}/libcsirocsa.so
%{_libdir}/libcsironn.so
%{_libdir}/libplplot.so
%{_libdir}/libqsastime.so
%{_libdir}/pkgconfig/plplot.pc
%dir %{_libdir}/cmake/plplot
%{_libdir}/cmake/plplot/export_cairo.cmake
%{_libdir}/cmake/plplot/export_cairo-release.cmake
%{_libdir}/cmake/plplot/export_csirocsa.cmake
%{_libdir}/cmake/plplot/export_csirocsa-release.cmake
%{_libdir}/cmake/plplot/export_csironn.cmake
%{_libdir}/cmake/plplot/export_csironn-release.cmake
%{_libdir}/cmake/plplot/export_mem.cmake
%{_libdir}/cmake/plplot/export_mem-release.cmake
%{_libdir}/cmake/plplot/export_ntk.cmake
%{_libdir}/cmake/plplot/export_ntk-release.cmake
%{_libdir}/cmake/plplot/export_null.cmake
%{_libdir}/cmake/plplot/export_null-release.cmake
%{_libdir}/cmake/plplot/export_plfortrandemolib.cmake
%{_libdir}/cmake/plplot/export_plfortrandemolib-release.cmake
%{_libdir}/cmake/plplot/export_plplotada.cmake
%{_libdir}/cmake/plplot/export_plplotada-release.cmake
%{_libdir}/cmake/plplot/export_plplotc.cmake
%{_libdir}/cmake/plplot/export_plplot.cmake
%{_libdir}/cmake/plplot/export_plplotc-release.cmake
%{_libdir}/cmake/plplot/export_plplotcxx.cmake
%{_libdir}/cmake/plplot/export_plplotcxx-release.cmake
%{_libdir}/cmake/plplot/export_plplotfortran.cmake
%{_libdir}/cmake/plplot/export_plplotfortran-release.cmake
%{_libdir}/cmake/plplot/export_plplotjavac_wrap.cmake
%{_libdir}/cmake/plplot/export_plplotjavac_wrap-release.cmake
%{_libdir}/cmake/plplot/export_plplotluac.cmake
%{_libdir}/cmake/plplot/export_plplotluac-release.cmake
%{_libdir}/cmake/plplot/export_plplot_pyqt5.cmake
%{_libdir}/cmake/plplot/export_plplot_pyqt5-release.cmake
%{_libdir}/cmake/plplot/export_plplotqt.cmake
%{_libdir}/cmake/plplot/export_plplotqt-release.cmake
%{_libdir}/cmake/plplot/export_plplot-release.cmake
%{_libdir}/cmake/plplot/export_plplottcltk.cmake
%{_libdir}/cmake/plplot/export_plplottcltk_Main.cmake
%{_libdir}/cmake/plplot/export_plplottcltk_Main-release.cmake
%{_libdir}/cmake/plplot/export_plplottcltk-release.cmake
%{_libdir}/cmake/plplot/export_plplotwxwidgets.cmake
%{_libdir}/cmake/plplot/export_plplotwxwidgets-release.cmake
%{_libdir}/cmake/plplot/export_plserver.cmake
%{_libdir}/cmake/plplot/export_plserver-release.cmake
%{_libdir}/cmake/plplot/export_pltcl.cmake
%{_libdir}/cmake/plplot/export_pltcl-release.cmake
%{_libdir}/cmake/plplot/export_pltek.cmake
%{_libdir}/cmake/plplot/export_pltek-release.cmake
%{_libdir}/cmake/plplot/export_Pltk_init.cmake
%{_libdir}/cmake/plplot/export_Pltk_init-release.cmake
%{_libdir}/cmake/plplot/export_ps.cmake
%{_libdir}/cmake/plplot/export_ps-release.cmake
%{_libdir}/cmake/plplot/export_psttf.cmake
%{_libdir}/cmake/plplot/export_psttf-release.cmake
%{_libdir}/cmake/plplot/export_qsastime.cmake
%{_libdir}/cmake/plplot/export_qsastime-release.cmake
%{_libdir}/cmake/plplot/export_qt.cmake
%{_libdir}/cmake/plplot/export_qt-release.cmake
%{_libdir}/cmake/plplot/export_svg.cmake
%{_libdir}/cmake/plplot/export_svg-release.cmake
%{_libdir}/cmake/plplot/export_tclmatrix.cmake
%{_libdir}/cmake/plplot/export_tclmatrix-release.cmake
%{_libdir}/cmake/plplot/export_tk.cmake
%{_libdir}/cmake/plplot/export_tk-release.cmake
%{_libdir}/cmake/plplot/export_tkwin.cmake
%{_libdir}/cmake/plplot/export_tkwin-release.cmake
%{_libdir}/cmake/plplot/export_wxPLViewer.cmake
%{_libdir}/cmake/plplot/export_wxPLViewer-release.cmake
%{_libdir}/cmake/plplot/export_wxwidgets.cmake
%{_libdir}/cmake/plplot/export_wxwidgets-release.cmake
%{_libdir}/cmake/plplot/export_xfig.cmake
%{_libdir}/cmake/plplot/export_xfig-release.cmake
%{_libdir}/cmake/plplot/export_xwin.cmake
%{_libdir}/cmake/plplot/export_xwin-release.cmake
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

##########################################################################

%package doc
##########################################################################
Summary:        Documentation for PLplot and its bindings
License:        LGPL-2.1-or-later
Group:          Documentation/Other

%description doc
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the documentation for PLplot and its associated
modules.

%files doc
%dir %{_docdir}/%{name}-doc
%{_docdir}/%{name}-doc/*
##########################################################################

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
%{_datadir}/ada/adainclude/plplotada/
%{_datadir}/plplot%{version}/examples/ada/
%{_datadir}/plplot%{version}/examples/test_ada.sh
##########################################################################

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
%{_datadir}/plplot%{version}/examples/octave/
%{_datadir}/plplot%{version}/examples/test_octave.sh
%endif
##########################################################################

%package python3-qt
##########################################################################
Summary:        PLplot functions for scientific plotting with python-qt4
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
Requires:       %{name}-common = %{version}
Requires:       python3-qt5

%description python3-qt
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot functions required for scientific
plotting with python-qt.

%files python3-qt
%{python3_sitearch}/plplot_pyqt5.so
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
Requires:       libqt4-devel
Requires:       pkgconfig
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
%{_libdir}/pkgconfig/plplot-tcl*.pc
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
%{python3_sitearch}/Plframe.py*
%{python3_sitearch}/TclSup.py*
%{python3_sitearch}/*Pltk_init.*
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

%package -n python3-%{name}
##########################################################################
Summary:        PLplot functions for scientific plotting with Python
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       %{name}-common = %{version}
Provides:       python-%{name}

%description -n python3-%{name}
PLplot is a library of functions that are useful for making scientific
plots.

This package provides the PLplot's Python binding.

%files -n python3-%{name}
%{python3_sitearch}/_plplotc.so
%{python3_sitearch}/plplot.py*
%{python3_sitearch}/plplotc.py*
%{python3_sitearch}/_plplotc.so
%{python3_sitearch}/plplot.py*
%{python3_sitearch}/plplotc.py*
%{_datadir}/plplot%{version}/examples/python/
%{_datadir}/plplot%{version}/examples/test_python.sh
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
##########################################################################

%prep
%setup -q
%patch1 -p1

for file in NEWS README.release
do
  iconv -f ISO-8859-1 -t UTF-8 $file > ${file}.tmp
  touch -r $file ${file}.tmp
  mv ${file}.tmp $file
done

%build
export CFLAGS="%{optflags} -DUSE_INTERP_RESULT -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
export FFLAGS="%{optflags}"
export LDFLAGS="-fPIC"

mkdir builddir && pushd builddir

# X-server and $DISPLAY required to enable tk bindings
export DISPLAY=%{X_display}
Xvfb -noreset %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 5
cmake \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \\\
        -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \\\
        -DCMAKE_BUILD_TYPE:STRING=Release \\\
        -DPL_FREETYPE_FONT_PATH:PATH="%{_datadir}/fonts/truetype" \\\
        -DUSE_RPATH:BOOL=OFF \\\
        -DENABLE_ada:BOOL=ON \\\
%if 0%{?octave_enabled}
        -DENABLE_octave:BOOL=ON \\\
        -DTRY_OCTAVE4=ON \\\
%else
        -DENABLE_octave:BOOL=OFF \\\
%endif
        -DENABLE_d:BOOL=ON \\\
        -DENABLE_itcl:BOOL=ON \\\
%if 0%{?tk_enabled} > 1320
        -DENABLE_itk:BOOL=OFF \\\
        -DENABLE_tk:BOOL=OFF \\\
%else
        -DENABLE_itk:BOOL=ON \\\
        -DENABLE_tk:BOOL=ON \\\
%endif
        -DENABLE_ocaml:BOOL=ON \\\
        -DPLD_aqt:BOOL=ON \\\
        -DPLD_plmeta:BOOL=OFF \\\
        -DPLD_svg:BOOL=ON \\\
        -DPLD_wxwidgets:BOOL=ON \\\
        -DBUILD_DOC:BOOL=OFF \\\
        -DPREBUILT_DOC:BOOL=ON \\\
        -DJAVAWRAPPER_DIR:PATH="%{_libdir}/plplot%{version}" \\\
        -DBUILD_TEST:BOOL=ON  \\\
        -DENABLE_lua:BOOL=ON \\\
        -DPLPLOT_USE_QT5:BOOL=ON \\\
        ..

make %{?_smp_mflags}
popd

%install
pushd builddir
%make_install DESTDIR=%{buildroot}
popd

# Fix up tclIndex files so they are the same on all builds
for file in %{buildroot}%{_datadir}/plplot%{version}/examples/*/tclIndex
do
   grep '^[# ]' ${file} > tclIndex.hd
   grep -v '^[# ]' ${file} | sort > tclIndex
   cat tclIndex.hd tclIndex > ${file}
done
rm -rf %{buildroot}%{_datadir}/plplot%{version}/examples/cmake/modules/Platform

#Remove unnecessary examples that trigger build errors or warnings
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/cmake/modules/export_plplot-release.cmake
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/test_octave_interactive.sh
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/tk/*.in
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/tcl/*.in
rm -f %{buildroot}%{_datadir}/%{name}%{version}/examples/tk/tk01

#Remove cmake files for the examples since they don't work anyway due to presence of rpath
rm -f %{buildroot}%{_datadir}/plplot%{version}/examples/CMakeLists.txt
rm -fr %{buildroot}%{_datadir}/plplot%{version}/examples/cmake

#Move doc files to appropriate location
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}-doc

%if %{tk_enabled}
#Grant executable permissions to example tk binaries with valid shebang
chmod +x %{buildroot}%{_datadir}/%{name}%{version}/examples/tk/tk03
%endif

#Remove a fortran static library
rm %{buildroot}%{_libdir}/libplfortrandemolib*.a

#Fix python hashbangs for examples (/usr/bin/env python -> /usr/bin/python)
sed -i "1{s/\/usr\/bin\/env python/\/usr\/bin\/python/;}" %{buildroot}%{_datadir}/%{name}%{version}/examples/python/x*
sed -i "1{s/\/usr\/bin\/env python/\/usr\/bin\/python/;}" %{buildroot}%{_datadir}/%{name}%{version}/examples/python/*.py
sed -i "1{s/\/usr\/bin\/env python/\/usr\/bin\/python/;}" %{buildroot}%{_datadir}/%{name}%{version}/examples/python/pytkdemo

%fdupes %{buildroot}%{_datadir}/

%check
pushd builddir
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
sleep 5
# Octave tests fail, known issue with tests
# Qt tests fail on Xvfb
ctest -V -E "octave|qt" %{?_smp_mflags}
popd

%changelog
