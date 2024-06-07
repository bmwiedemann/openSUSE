#
# spec file for package mathgl
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


%bcond_with zypper_posttrans
%define octave_args --no-window-system --norc
%define libname libmgl

# At least python 3.8 is required; Leap <= 15.3 only has python 3.6
%if 0%{?suse_version} >= 1550
%bcond_without python
%else
%bcond_with python
%endif
%define skip_python2 1

%define libversion 8

# oct_version must be x.y.z
%define oct_version %{version}
# Octave is too recent for oS >= 1699, and swig is too old for Leap 15.x
%bcond_with    octave

# Drop doc package as it is a constant source of build pain
%bcond_with docs

%if 0%{?fedora_version}
%define _defaultdocdir %{_docdir}
%endif
Name:           mathgl
Version:        8.0.1
Release:        0
Summary:        Library for making scientific graphics
License:        GPL-3.0-only
URL:            http://mathgl.sourceforge.net
Source0:        http://downloads.sourceforge.net/mathgl/%{name}-%{version}.tar.gz
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
# PATCH-FIX-UPSTREAM mathgl-libharu2_4-compat.patch badshah400@gmail.com -- Fix compilation against libharu 2.4.x [https://sourceforge.net/p/mathgl/bugs/48/]
Patch8:         mathgl-libharu2_4-compat.patch
BuildRequires:  cmake >= 2.8.12
BuildRequires:  desktop-file-utils
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  libharu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  lua51-devel
BuildRequires:  openmpi-macros-devel
BuildRequires:  swig
BuildRequires:  sz2-devel
BuildRequires:  texlive-filesystem
BuildRequires:  wxGTK3-devel
%if %{with python}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-numpy
%endif
%if %{with octave}
BuildRequires:  octave-devel
BuildRequires:  swig >= 4.0
%endif
%if 0%{?fedora_version}
BuildRequires:  fltk-fluid
BuildRequires:  libXmu-devel
%endif
%if %{with docs}
%if 0%{?fedora_version}
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
%else
BuildRequires:  texinfo
BuildRequires:  texlive-latex
%endif
%endif
%python_subpackages

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
%openmpi_requires

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
Requires:       %{libname}-mpi%{libversion} = %{version}
Requires:       %{libname}-qt5-%{libversion} = %{version}
Requires:       %{libname}-wnd%{libversion} = %{version}
Requires:       %{libname}-wx%{libversion} = %{version}
Requires:       cmake
%if 0%{?suse_version}
%if %{with docs}
Recommends:     %{name}-doc
%endif
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

%package -n     octave-mathgl
Summary:        Octave interface for the MathGL library
Requires:       octave-cli

%description -n octave-mathgl
MathGL is a library for making scientific graphics. It provides data
plotting and handling of large data arrays, as well as window and
console modes and for embedding into other programs.

This package provides Octave interface for MathGL.

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
%autopatch -p1

# Link mgl-mpi to mgl
sed -i 's/target_link_libraries(mgl-mpi /\0 mgl /' src/CMakeLists.txt

# Correct octave-mathgl version
sed -i 's/2.0/%{oct_version}/' lang/DESCRIPTION

# convert EOL encodings, maintaining timestamps
sed -i 's/\r$//' AUTHORS README

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%setup_openmpi

%{python_expand # For all supported python flavors
export PYTHON=$python
echo "Building for $python_ providing %{$python_provides} "
%define __builddir ${PYTHON}_build
pushd .
%cmake \
      -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix}  \
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
      -Denable-python=%{?with_python:on}%{!?with_python:off} \
      -DPY3VERSION_DOTTED=%{$python_version}  \
      -Denable-json-sample=off                \
%if "%{$python_provides}" == "python3" || "$python_" == "python3_"
      -Denable-doc-html=%{?with_docs:on}%{!?with_docs:off} \
      -Denable-doc-pdf-en=%{?with_docs:on}%{!?with_docs:off} \
      -Denable-fltk=on                        \
      -Denable-glut=on                        \
      -Denable-lua=on                         \
      -Denable-mgltex=on                      \
      -Denable-octave=%{?with_octave:on}%{!?with_octave:off} \
      -Denable-octave-install=OFF             \
      -Denable-qt=on                          \
      -Denable-wx=on                          \
%else
      -Denable-doc-html=off                   \
      -Denable-doc-pdf-en=off                 \
      -Denable-fltk=off                       \
      -Denable-glut=off                       \
      -Denable-lua=off                        \
      -Denable-mgltex=off                     \
      -Denable-octave=off                     \
      -Denable-octave-install=off             \
      -Denable-qt5=off                        \
      -Denable-wx=off                         \
%endif
      %{nil}

%cmake_build
popd
}

%install
%{python_expand # For all supported python flavors
export PYTHON=$python
%define __builddir ${PYTHON}_build
%cmake_install

%if "%{$python_provides}" == "python3" || "$python_" == "python3_"
pushd %{__builddir}

%if %{with octave}
# Can not use enable-octave-install, as it ignores the buildroot
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
# Install octave-mathgl
mkdir -p %{buildroot}%{_libdir}/octave/packages
mkdir -p %{buildroot}%{_datadir}/octave/packages
octave %{octave_args} --eval \
  "pkg prefix %{buildroot}%{_datadir}/octave/packages %{buildroot}%{_libdir}/octave/packages; pkg install lang/%{name}.tar.gz"
# rm %%{buildroot}%%{_datadir}/octave/packages/*/packinfo/.autoload
# remove octave module archive
rm %{buildroot}%{_datadir}/%{name}/%{name}.tar.gz
%endif

# move mgl.cgi
install -d %{buildroot}/srv/www/cgi-bin/
mv %{buildroot}%{_prefix}/lib/cgi-bin/mgl.cgi %{buildroot}/srv/www/cgi-bin/mgl.cgi

# LaTeX package (based on TeXLive spec files)
%if %{with zypper_posttrans}
mkdir -p %{buildroot}%{_localstatedir}/adm/update-scripts
ln -sf %{_datadir}/texmf/texconfig/zypper.py \
    %{buildroot}%{_localstatedir}/adm/update-scripts/texlive-mgltex-%{version}-%{release}-zypper
%endif

%find_lang %{name}
# Copy mathgl.lang file to main dir for use with file list
cp %{name}.lang ../

popd
%endif
}

%if %{with docs}
# R-B diagnostics
# fexport.prc is nontrivial to fix, as it contains a time based UUID
# fexport.pdf is non-reproducible due to embedded fexport.prc
grep `date +'%Y'` %{buildroot}%{_docdir}/mathgl/png/fexport*.{eps,svg}
sha256sum %{buildroot}%{_docdir}/mathgl/png/fexport*.{prc,pdf,eps,svg}
%endif

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
%{_libdir}/libmgl.so.%{libversion}*

%files -n %{libname}-mpi%{libversion}
%{_libdir}/libmgl-mpi.so.%{libversion}*

%files -n %{libname}-fltk%{libversion}
%{_libdir}/libmgl-fltk.so.%{libversion}*

%files -n %{libname}-glut%{libversion}
%{_libdir}/libmgl-glut.so.%{libversion}*

%files -n %{libname}-qt5-%{libversion}
%{_libdir}/libmgl-qt5.so.%{libversion}*

%files -n %{libname}-wnd%{libversion}
%{_libdir}/libmgl-wnd.so.%{libversion}*

%files -n %{libname}-wx%{libversion}
%{_libdir}/libmgl-wx.so.%{libversion}*

%files -n %{name}-cgi
/srv/www/cgi-bin/mgl.cgi
%if %{with docs}
%{_mandir}/man1/mgl.cgi.1%{?ext_man}
%endif

%files -n %{name}-devel
%license COPYING
%doc AUTHORS ChangeLog.txt README
%{_includedir}/mgl2/
%{_libdir}/libmgl*.so
%dir %{_libdir}/cmake/mathgl
%dir %{_libdir}/cmake/mathgl2
%{_libdir}/cmake/mathgl/*.cmake
%{_libdir}/cmake/mathgl2/*.cmake

%files -n %{name}-lang -f %{name}.lang

%files -n %{name}-devel-static
%{_libdir}/*.a

%if %{with docs}
%files -n %{name}-doc
%dir %{_docdir}/mathgl
%doc %{_docdir}/mathgl/png/
%doc %{_docdir}/mathgl/udav/
%doc %{_docdir}/mathgl/*.html
%exclude %{_docdir}/mathgl/*.pdf
%doc %{_docdir}/mathgl/*.png
%exclude %{_docdir}/mathgl/mathgl_ru.html
%exclude %{_docdir}/mathgl/mgl_ru.html
# %%{_infodir}/%%{name}_en.info*.gz

%files -n %{name}-doc-pdf
%doc %{_docdir}/mathgl/*.pdf

%files -n %{name}-doc-ru
%doc %{_docdir}/mathgl/mathgl_ru.html
%doc %{_docdir}/mathgl/mgl_ru.html
%endif

%files -n %{name}-examples
%{_bindir}/mgl*example

%files -n %{name}-fonts
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/fonts/

%files -n %{name}-lua
%{_libdir}/mgl-lua.so

%if %{with octave}
%files -n octave-mathgl
%{_datadir}/octave/packages/%{name}-%{oct_version}/
%{_libdir}/octave/packages/%{name}-%{oct_version}/
%endif

%if %{with python}
%files %{python_files}
%{python_sitearch}/mathgl.py
%{python_sitearch}/_mathgl.so
%{python_sitearch}/__pycache__/*.pyc
%endif

%files -n %{name}-tex
%{_datadir}/texmf/tex/latex/mgltex/
%if %{with zypper_posttrans}
%{_localstatedir}/adm/update-scripts/texlive-mgltex-%{version}-%{release}-zypper
%endif

%files -n %{name}-tex-doc
%{_datadir}/texmf/doc/latex/mgltex/

%files -n %{name}-tools
%{_bindir}/mglconv
%{_bindir}/mglview
%{_bindir}/mgltask
%if %{with docs}
%{_mandir}/man1/mglconv.1%{?ext_man}
%{_mandir}/man1/mglview.1%{?ext_man}
%{_mandir}/man5/mgl.5%{?ext_man}
%endif

%files -n udav
%{_bindir}/udav
%{_datadir}/pixmaps/udav.png
%{_datadir}/applications/udav.desktop
%{_datadir}/mime/packages/mgl.xml
%{_datadir}/udav/
%if %{with docs}
%{_mandir}/man1/udav.1%{?ext_man}
%endif
# mgllab's .desktop file uses the same icon as udav's, so we have to bundle them in the same package
%{_bindir}/mgllab
%{_datadir}/applications/mgllab.desktop
#

%changelog
