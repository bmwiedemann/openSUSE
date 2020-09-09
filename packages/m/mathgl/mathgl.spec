#
# spec file for package mathgl
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


%define octave_args --no-window-system --norc
%define libname libmgl
%if 0%{?suse_version} >= 1550
%define omp_ver 1
%else
%define omp_ver %{nil}
%endif
# NO PYTHON3 SUPPORT FROM UPSTREAM
%if 0%{?suse_version} > 1500
%bcond_with python
%else
%bcond_without python
%endif
# oct_version must be x.y.z
%define oct_version %{version}
%define somajor 7.5.0
%define libversion 7_5_0

# NOT COMPATIBLE WITH OCTAVE IN LEAP 15.1, 15.2
%if 0%{?suse_version} <= 1500
%bcond_with octave
%else
%bcond_without octave
%endif

%if 0%{?fedora_version}
%define _defaultdocdir %{_docdir}
%endif
Name:           mathgl
Version:        2.4.4
Release:        0
Summary:        Library for making scientific graphics
License:        GPL-3.0-only
URL:            http://mathgl.sourceforge.net
Source0:        http://downloads.sourceforge.net/mathgl/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM mathgl-fix-python-module-path.patch -- Make python modules install arch-depended
Patch1:         mathgl-fix-python-module-path.patch
# PATCH-FEATURE-UPSTREAM mathgl-examples-install.patch -- Enable examples install
Patch2:         mathgl-examples-install.patch
# PATCH-FIX-OPENSUSE mathgl-doc-path.patch -- Locate documentation to right place
Patch3:         mathgl-doc-path.patch
# PATCH-FIX-OPENSUSE udav-help-path.patch -- fix path to documentation directory
Patch4:         udav-help-path.patch
# PATCH-FIX-OPENSUSE mathgl-texmf-dir.patch -- set correct path to texmf directory
Patch5:         mathgl-texmf-dir.patch
# PATCH-FIX-OPENSUSE mathgl-no-default-qt.patch -- do not set a default qt
Patch7:         mathgl-no-default-qt.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  libQt5WebKit5-devel
BuildRequires:  libQt5WebKitWidgets-devel
BuildRequires:  libharu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  lua51-devel
BuildRequires:  openmpi%{omp_ver}-devel
BuildRequires:  swig
BuildRequires:  sz2-devel
BuildRequires:  texinfo
BuildRequires:  texlive-filesystem
BuildRequires:  texlive-latex
BuildRequires:  wxWidgets-devel >= 3
%if %{with python}
BuildRequires:  python-devel
BuildRequires:  python-numpy-devel
%endif
%if %{with octave}
BuildRequires:  octave-devel
%endif
%if 0%{?fedora_version}
BuildRequires:  fltk-fluid
BuildRequires:  libXmu-devel
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
%endif

%description
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs. MathGL
integrates into FLTK, Qt and OpenGL applications.

%package -n     %{libname}%{libversion}
Summary:        Library for making scientific graphics
Requires:       %{name}-fonts >= %{version}
Provides:       %{name} = %{version}

%description -n %{libname}%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package -n     %{libname}-mpi%{libversion}
Summary:        MathGL library with MPI support

%description -n %{libname}-mpi%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package -n     %{libname}-fltk%{libversion}
Summary:        MathGL FLTK widget library

%description -n %{libname}-fltk%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package -n     %{libname}-glut%{libversion}
Summary:        MathGL window library

%description -n %{libname}-glut%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package -n     %{libname}-qt5-%{libversion}
Summary:        MathGL Qt5 widget library
Provides:       %{libname}-qt4-%{libversion} = %{version}
Obsoletes:      %{libname}-qt4-%{libversion} < %{version}

%description -n %{libname}-qt5-%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package -n     %{libname}-wnd%{libversion}
Summary:        MathGL window library

%description -n %{libname}-wnd%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package -n     %{libname}-wx%{libversion}
Summary:        MathGL wxWidgets library

%description -n %{libname}-wx%{libversion}
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

%package        cgi
Summary:        MathGL CGI binary

%description    cgi
This package contains the MathGL binary for parsing CGI scripts.

%package        devel
Summary:        Libraries and header files for the MathGL library
Requires:       %{libname}%{libversion} = %{version}
Requires:       %{libname}-fltk%{libversion} = %{version}
Requires:       %{libname}-glut%{libversion} = %{version}
Requires:       %{libname}-qt5-%{libversion} = %{version}
Requires:       %{libname}-wnd%{libversion} = %{version}
Requires:       %{libname}-wx%{libversion} = %{version}
Requires:       cmake
%if 0%{?suse_version}
Recommends:     %{name}-doc
%endif

%description    devel
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package contains libraries and header files for developing
applications that use MathGL.

%package        devel-static
Summary:        Static libraries for MathGL
Requires:       mathgl-devel = %{version}

%description    devel-static
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package contains static libraries for developing applications
that use MathGL.

%package        doc
Summary:        Documentation for MathGL
BuildArch:      noarch

%description    doc
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides the documentation for MathGL in HTML format.

%package        doc-pdf
Summary:        Documentation for MathGL
BuildArch:      noarch

%description    doc-pdf
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides the documentation for MathGL in PDF format.

%package        doc-ru
Summary:        Russian documentation for MathGL
Requires:       mathgl-doc = %{version}
Provides:       locale(mathgl-doc:ru)
BuildArch:      noarch

%description    doc-ru
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides Russian documentation for MathGL.

%package        examples
Summary:        Examples for %{name} library

%description    examples
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package contains examples of using MathGL.

%package        fonts
Summary:        Fonts for the MathGL library
BuildArch:      noarch

%description    fonts
This package contains command fonts for MathGL library.

%package        lua
Summary:        Lua interface for the MathGL library

%description    lua
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides lua interface for MathGL.

%if %{with octave}
%package -n     octave-mathgl
Summary:        Octave interface for the MathGL library
Requires:       octave-cli

%description -n octave-mathgl
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides Octave interface for MathGL.
%endif

%package -n     python-mathgl
Summary:        Libraries and header files for the MathGL library
Requires:       python-base

%description -n python-mathgl
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides the python bindings for MathGL.

%package        tex
Summary:        MathGL scripts for LaTeX documents
Requires:       mathgl-tools >= %{version}
Requires(post): coreutils
Requires(posttrans): texlive
Requires(postun): coreutils
Requires(postun): texlive
Requires(pre):  texlive
Recommends:     mathgl-tex-doc = %{version}
Provides:       tex(mgltex.sty)
BuildArch:      noarch

%description    tex
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package allows to use MathGL scripts in LaTeX documents.

%package        tex-doc
Summary:        Documentation for mglTeX
Conflicts:      texlive-mgltex-doc
BuildArch:      noarch

%description    tex-doc
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides documentation for mglTeX.

%package        tools
Summary:        Command line tools for the MathGL library

%description    tools
This package contains command line tools for making scientific graphics.

%package -n     udav
Summary:        Data handling and plotting tool

%description -n udav
UDAV is a program for data array visualization using the MathGL
library. It support a wide spectrum of graphics, a simple script
language and visual data handling and editing. It has a window
interface for data viewing, changing and plotting. It can also
execute MGL scripts, set up, rotate graphics, and so on.

%lang_package

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1

# Correct octave-mathgl version
sed -i 's/2.0/%{oct_version}/' lang/DESCRIPTION

# Correct location of numpy/arrayobject.h header file
numpy_h=%{python_sitearch}/numpy/core/include/numpy/arrayobject.h
sed -i "s|<numpy/arrayobject.h>|\"${numpy_h}\"|" lang/numpy.i

# convert EOL encodings, maintaining timestames
sed -i 's/\r$//' AUTHORS README

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
if [ -f %{_libdir}/mpi/gcc/openmpi%{omp_ver}/bin/mpivars.sh ]; then
  source %{_libdir}/mpi/gcc/openmpi%{omp_ver}/bin/mpivars.sh
fi

# cmake macros don't work
cmake \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}   \
      -DMathGL_INSTALL_LIB_DIR:PATH=%{_lib}   \
      -DMathGL_INSTALL_CMAKE_DIR:PATH=%{_libdir}/cmake/mathgl   \
      -DTEXMFDIR:PATH=%{_datadir}/texmf/      \
      -DCMAKE_C_FLAGS="%{optflags}"	      \
      -DCMAKE_CXX_FLAGS="%{optflags}"	      \
      -Denable-double=on                      \
      -Denable-mpi=on                         \
      -Denable-pthread=off                    \
      -Denable-openmp=on                      \
      -Denable-ltdl=on                        \
      -Denable-gsl=on                         \
      -Denable-jpeg=on                        \
      -Denable-png=on                         \
      -Denable-zlib=on                        \
      -Denable-pdf=on                         \
      -Denable-gif=on                         \
      -Denable-hdf5=on                        \
      -Denable-opengl=on                      \
      -Denable-glut=on                        \
      -Denable-fltk=on                        \
      -Denable-wx=on                          \
      -Denable-qt5=on                         \
      -Denable-python=%{?with_python:on}%{!?with_python:off} \
      -Denable-lua=on                         \
      -Denable-octave=%{?with_octave:on}%{!?with_octave:off} \
      -Denable-octave-install=off             \
      -Denable-mgltex=on                      \
      -Denable-json-sample=off                \
      -Denable-doc-html=on                    \
      -Denable-doc-pdf-en=on                  \
      .

%make_build

%install
%make_install

%if %{with octave}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
# # Install octave-mathgl
mkdir -p %{buildroot}%{_libdir}/octave/packages
mkdir -p %{buildroot}%{_datadir}/octave/packages
octave %{octave_args} --eval "pkg prefix %{buildroot}%{_datadir}/octave/packages %{buildroot}%{_libdir}/octave/packages; pkg install lang/%{name}.tar.gz"
# rm %%{buildroot}%%{_datadir}/octave/packages/*/packinfo/.autoload
# remove octave module archive
rm %{buildroot}%{_datadir}/%{name}/%{name}.tar.gz
%endif

# Install docs
install -m 644 texinfo/{classes.pdf,mgl_en.pdf} %{buildroot}%{_docdir}/%{name}/

# move mgl.cgi
install -d %{buildroot}/srv/www/cgi-bin/
mv %{buildroot}%{_prefix}/lib/cgi-bin/mgl.cgi %{buildroot}/srv/www/cgi-bin/mgl.cgi

# LaTeX package (based on TeXLive spec files)
mkdir -p %{buildroot}%{_localstatedir}/adm/update-scripts
ln -sf %{_datadir}/texmf/texconfig/zypper.py \
    %{buildroot}%{_localstatedir}/adm/update-scripts/texlive-mgltex-%{version}-%{release}-zypper

%find_lang %{name}

# %%post doc
# %%install_info --info-dir=%%{_infodir} %%{_infodir}/%%{name}_en.info.gz
# %%install_info --info-dir=%%{_infodir} %%{_infodir}/%%{name}_en.info-1.gz
# %%install_info --info-dir=%%{_infodir} %%{_infodir}/%%{name}_en.info-2.gz
#
# %%postun doc
# %%install_info_delete --info-dir=%%_infodir %%{_infodir}/%%{name}_en.info.gz
# %%install_info_delete --info-dir=%%_infodir %%{_infodir}/%%{name}_en.info-1.gz
# %%install_info_delete --info-dir=%%_infodir %%{_infodir}/%%{name}_en.info-2.gz

%post -n %{libname}%{libversion} -p /sbin/ldconfig
%postun -n %{libname}%{libversion} -p /sbin/ldconfig
%post -n %{libname}-mpi%{libversion} -p /sbin/ldconfig
%postun -n %{libname}-mpi%{libversion} -p /sbin/ldconfig
%post -n %{libname}-fltk%{libversion} -p /sbin/ldconfig
%postun -n %{libname}-fltk%{libversion} -p /sbin/ldconfig
%post -n %{libname}-glut%{libversion} -p /sbin/ldconfig
%postun -n %{libname}-glut%{libversion} -p /sbin/ldconfig
%post -n %{libname}-qt5-%{libversion} -p /sbin/ldconfig
%postun -n %{libname}-qt5-%{libversion} -p /sbin/ldconfig
%post -n %{libname}-wnd%{libversion} -p /sbin/ldconfig
%postun -n %{libname}-wnd%{libversion} -p /sbin/ldconfig
%post -n %{libname}-wx%{libversion} -p /sbin/ldconfig
%postun -n %{libname}-wx%{libversion} -p /sbin/ldconfig

%if %{with octave}
%post -n octave-mathgl
octave -qf %{octave_args} --eval "pkg rebuild -auto mathgl"

%postun -n octave-mathgl
octave -qf %{octave_args} --eval "pkg rebuild"
%endif

%post tex
mkdir -p %{_localstatedir}/run/texlive
> %{_localstatedir}/run/texlive/run-mktexlsr
> %{_localstatedir}/run/texlive/run-update

%postun tex
if test $1 = 0; then
    %{_bindir}/mktexlsr 2> /dev/null || :
    exit 0
fi
mkdir -p %{_localstatedir}/run/texlive
> %{_localstatedir}/run/texlive/run-mktexlsr
> %{_localstatedir}/run/texlive/run-update

%posttrans tex
test -f %{_localstatedir}/run/texlive/run-update || exit 0
test -z "$ZYPP_IS_RUNNING" || exit 0
VERBOSE=false %{_datadir}/texmf/texconfig/update || :
rm -f %{_localstatedir}/run/texlive/run-update

%files -n %{libname}%{libversion}
%{_libdir}/libmgl.so.%{somajor}*

%files -n %{libname}-mpi%{libversion}
%{_libdir}/libmgl-mpi.so.%{somajor}*

%files -n %{libname}-fltk%{libversion}
%{_libdir}/libmgl-fltk.so.%{somajor}*

%files -n %{libname}-glut%{libversion}
%{_libdir}/libmgl-glut.so.%{somajor}*

%files -n %{libname}-qt5-%{libversion}
%{_libdir}/libmgl-qt5.so.%{somajor}*

%files -n %{libname}-wnd%{libversion}
%{_libdir}/libmgl-wnd.so.%{somajor}*

%files -n %{libname}-wx%{libversion}
%{_libdir}/libmgl-wx.so.%{somajor}*

%files cgi
/srv/www/cgi-bin/mgl.cgi
%{_mandir}/man1/mgl.cgi.1%{?ext_man}

%files devel
%license COPYING
%doc AUTHORS ChangeLog.txt README
%{_includedir}/mgl2/
%{_libdir}/libmgl*.so
%dir %{_libdir}/cmake/mathgl
%dir %{_libdir}/cmake/mathgl2
%{_libdir}/cmake/mathgl/*.cmake
%{_libdir}/cmake/mathgl2/*.cmake

%files lang -f %{name}.lang

%files devel-static
%{_libdir}/*.a

%files doc
%dir %{_docdir}/mathgl
%doc %{_docdir}/mathgl/png/
%doc %{_docdir}/mathgl/udav/
%doc %{_docdir}/mathgl/*.html
%exclude %{_docdir}/mathgl/*.pdf
%doc %{_docdir}/mathgl/*.png
%exclude %{_docdir}/mathgl/mathgl_ru.html
%exclude %{_docdir}/mathgl/mgl_ru.html
# %%{_infodir}/%%{name}_en.info*.gz

%files doc-pdf
%doc %{_docdir}/mathgl/*.pdf

%files doc-ru
%doc %{_docdir}/mathgl/mathgl_ru.html
%doc %{_docdir}/mathgl/mgl_ru.html

%files examples
%{_bindir}/mgl*example

%files fonts
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fonts/

%files lua
%{_libdir}/mgl-lua.so

%if %{with octave}
%files -n octave-mathgl
%{_datadir}/octave/packages/%{name}-%{oct_version}/
%{_libdir}/octave/packages/%{name}-%{oct_version}/
%endif

%if %{with python}
%files -n python-mathgl
%{python2_sitearch}/*
%endif

%files tex
%{_datadir}/texmf/tex/latex/mgltex/
%{_localstatedir}/adm/update-scripts/texlive-mgltex-%{version}-%{release}-zypper

%files tex-doc
%{_datadir}/texmf/doc/latex/mgltex/

%files tools
%{_bindir}/mglconv
%{_bindir}/mglview
%{_bindir}/mgltask
%{_mandir}/man1/mglconv.1%{?ext_man}
%{_mandir}/man1/mglview.1%{?ext_man}
%{_mandir}/man5/mgl.5%{?ext_man}

%files -n udav
%{_bindir}/udav
%{_datadir}/pixmaps/udav.png
%{_datadir}/applications/udav.desktop
%{_datadir}/mime/packages/mgl.xml
%{_datadir}/udav/
%{_mandir}/man1/udav.1%{?ext_man}
# mgllab's .desktop file uses the same icon as udav's, so we have to bundle them in the same package
%{_bindir}/mgllab
%{_datadir}/applications/mgllab.desktop
#

%changelog
