#
# spec file for package octave
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


%define apiver  v53
# Required for RC builds, in this case version contains ~rc, src_ver -rc
%define pkg_ver 5.1.0
%define src_ver %{pkg_ver}

# Use native graphics or gnuplot
%bcond_without native_graphics

# Build GUI
%if 0%{?suse_version} == 1315 && 0%{?is_opensuse} == 0
%bcond_with gui
%else
%bcond_without gui
%endif

# Use Qt5 GUI
%if 0%{?suse_version} == 1315 && 0%{?is_opensuse} == 1
%bcond_with qt5gui
%else
%bcond_without qt5gui
%endif

# JIT compilation
%bcond_with jit

# JAVA support
%bcond_without java

# Image processing library
# Default variant - GraphicsMagick
%if 0%{?suse_version} == 1315 && 0%{?is_opensuse} == 0
%bcond_without imagemagick
%else
%bcond_with imagemagick
%endif

# Sound IO
%bcond_without sound

# Build documentation
%if 0%{?suse_version} == 1315
%bcond_with doc
%else
%bcond_without doc
%endif

# Allow building without openBLAS, e.g. for architectures
# like RISC-V where openBLAS is not available
%bcond_without openblas

%if %{with openblas}
%define blas_library openblas
%else
%define blas_library blas
%endif

Name:           octave
Version:        %{pkg_ver}
Release:        0
Summary:        A High Level Programming Language
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://www.octave.org/
Source:         https://ftp.gnu.org/gnu/octave/%{name}-%{src_ver}.tar.lz
Source2:        octave.pc.in
Source3:        octave.macros
# PATCH-FIX-OPENSUSE
Patch0:         octave_tools_pie.patch
# PATCH-FIX-UPSTREAM
Patch1:         octave-bug-55029-fix_pause_and_kbhit_with_glibc_2_28.patch
Patch2:         octave-bug-56533-Cursor_misplaced_when_entering_newline_in_editor_with_tabs_indentation-part1.patch
Patch3:         octave-bug-56533-Cursor_misplaced_when_entering_newline_in_editor_with_tabs_indentation-part2.patch
BuildRequires:  arpack-ng-devel
# Required for Patch0
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
#
BuildRequires:  %{blas_library}-devel
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  fftw3-threads-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  glpk-devel
BuildRequires:  gmp-devel
BuildRequires:  gperf
BuildRequires:  hdf5-devel
BuildRequires:  lapack-devel
BuildRequires:  memory-constraints
%if %{with imagemagick}
BuildRequires:  pkgconfig(ImageMagick++)
%else
BuildRequires:  pkgconfig(GraphicsMagick++)
%endif
BuildRequires:  lzip
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  qhull-devel
BuildRequires:  qrupdate-devel
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel
BuildRequires:  termcap
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(zlib)
# Documentation build requires
%if %{with doc}
BuildRequires:  gnuplot
BuildRequires:  texinfo
BuildRequires:  texlive-dvips
BuildRequires:  texlive-latex
%endif
# GUI build requires
%if %{with gui}
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%if %{with qt5gui}
BuildRequires:  libqscintilla_qt5-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qttools
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
# boo#1095605
Requires:       libQt5Sql5-sqlite
%else
BuildRequires:  libqt4-devel
BuildRequires:  libqt4-devel-doc
BuildRequires:  qscintilla-devel
%endif
Obsoletes:      octave-gui < 4.0
Provides:       octave-gui = %{version}
%endif
# Sound IO build requires
%if %{with sound}
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile)
%endif
# JAVA functions build requires
%if %{with java}
BuildRequires:  java-devel
%endif
# JIT build requires
%if %{with jit}
BuildRequires:  llvm-devel
%endif
# Native graphics build requires
%if %{with native_graphics}
BuildRequires:  Mesa-devel
BuildRequires:  fltk-devel
BuildRequires:  gl2ps-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glu)
%else
Requires:       gnuplot
%endif
# Tests build requires
BuildRequires:  unzip
BuildRequires:  zip
Requires:       octave-cli = %{version}
Requires(pre):  update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Octave is a high level programming language. It is designed for the
solution of numeric problems.
%if %{with gui}

This package contains the graphical user interface.
%endif

%package        cli
Summary:        Command-line user interface for Octave
Group:          Productivity/Scientific/Math
Requires:       makeinfo
Requires(pre):  update-alternatives
%if %{with native_graphics}
Recommends:     epstool
Recommends:     pstoedit
# transfig requires texlive installation now
# Recommends:     transfig
%endif
Recommends:     octave-doc = %{version}

%description    cli
Octave is a high level programming language. It is designed for the
solution of numeric problems.

This package contains the command-line user interface.

%package        devel
Summary:        Development files for Octave
Group:          Development/Languages/Other
Requires:       %{blas_library}-devel
Requires:       %{name}-cli = %{version}
Requires:       fftw3-devel
Requires:       fftw3-threads-devel
Requires:       gcc-c++
Requires:       gcc-fortran
Requires:       hdf5-devel
Requires:       make

%description    devel
Octave is a high level programming language. It is designed for the
solution of numeric problems.

This package contains all necessary include files and libraries needed
to develop applications using Octave.

%package        doc
Summary:        Documentation for Octave
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
Octave is a high level programming language. It is designed for the
solution of numeric problems.

This package contains documentation for Octave.

%prep
%setup -q -n %{name}-%{src_ver}
%if 0%{?suse_version} > 1315
# autoconf in Leap 42.x is to old, so we just build without -pie there
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%endif

# define octave_blas macros
sed -i 's/OCTAVE_BLAS_LIBRARY_NAME/%{blas_library}/g' %{SOURCE3}

%build
%limit_build -m 700

%if 0%{?suse_version} > 1315
# rebuild makefiles after Patch0
autoreconf -i -s -f
%endif
%if 0%{?suse_version} > 1500
export QCOLLECTIONGENERATOR=qhelpgenerator-qt5
%endif
%configure \
  --libexecdir=%{_libdir} \
  %{?with_gui: --with-qt} \
  %{!?with_gui: --without-qt} \
  %{?with_jit: --enable-jit} \
  %{!?with_java: --disable-java} \
  --with-blas=%{blas_library} \
  --enable-openmp

make %{?_smp_mflags}

# .pc file
cp %{SOURCE2} octave.pc
sed -i 's:@VERSION@:%{src_ver}:' octave.pc
sed -i 's:@LIB@:%{_lib}:' octave.pc

%install
%make_install
# see bnc#557340
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo %{_libdir}/%{name}/%{src_ver} > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf
rm %{buildroot}/%{_libdir}/%{name}/%{src_ver}/*.la
# local rc file into /etc
mkdir %{buildroot}/%{_sysconfdir}/%{name}
mv %{buildroot}/%{_datadir}/%{name}/site/m/startup/octaverc %{buildroot}/%{_sysconfdir}/%{name}
ln -s %{_sysconfdir}/%{name}/octaverc %{buildroot}/%{_datadir}/%{name}/site/m/startup/octaverc
#
mkdir -p %{buildroot}/%{_libdir}/%{name}/packages
mkdir -p %{buildroot}/%{_datadir}/%{name}/packages
# .pc file
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cp octave.pc %{buildroot}/%{_libdir}/pkgconfig
# gui related fixes
%if %{without gui}
rm -rf %{buildroot}/%{_datadir}/icons/hicolor/
rm -rf %{buildroot}/%{_datadir}/metainfo/
rm -rf %{buildroot}/%{_datadir}/applications/
%endif
# rpm macros
install -Dm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/rpm/macros.octave
# increase stack size set by the JVM, affects the whole octave process
echo "-Xss8m" >  %{buildroot}/%{_datadir}/%{name}/%{src_ver}/m/java/java.opts

%check
# Increase stack limits. OpenBLAS tests are run after some JVM test, and OpenBLAS
# dgetrf is quite memory hungry, see https://github.com/xianyi/OpenBLAS/issues/246
echo "-Xss8m" >  scripts/java/java.opts
make check

%post
/sbin/ldconfig
%if %{with gui}
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
/sbin/ldconfig
%if %{with gui}
%desktop_database_postun
%icon_theme_cache_postun
%endif

%post cli
/sbin/ldconfig
%install_info --info-dir=%{_infodir} %{_infodir}/octave.info.gz

%postun cli
/sbin/ldconfig
%install_info_delete --info-dir=%{_infodir} %{_infodir}/octave.info.gz

%files
%license COPYING
%doc AUTHORS BUGS NEWS
%doc README ChangeLog
%if %{with gui}
%{_libdir}/%{name}/%{src_ver}/exec/*-*-linux-gnu*/octave-gui
%{_libdir}/%{name}/%{src_ver}/exec/*-*-linux-gnu*/octave-svgconvert
%{_libdir}/%{name}/%{src_ver}/liboctgui.so.*
%{_datadir}/%{name}/%{src_ver}/locale/
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/*.desktop
%if 0%{?suse_version} <= 1315
%dir %{_datadir}/metainfo/
%endif
%{_datadir}/icons/hicolor/*/apps/octave.*
%endif

%files cli
%{_bindir}/octave
%{_bindir}/octave-%{src_ver}
%{_bindir}/octave-cli
%{_bindir}/octave-cli-%{src_ver}
%if %{with doc}
%{_mandir}/man1/octave.1.gz
%{_mandir}/man1/octave-cli.1.gz
%endif
%{_bindir}/octave-config
%{_bindir}/octave-config-%{src_ver}
%if %{with doc}
%{_mandir}/man1/octave-config.1.gz
%{_infodir}/*.gz
%endif
%config %{_sysconfdir}/ld.so.conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/octaverc
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/%{src_ver}
%dir %{_libdir}/%{name}/packages
%dir %{_datadir}/%{name}/packages
%dir %{_sysconfdir}/%{name}
%{_libdir}/%{name}/%{src_ver}/oct
%{_libdir}/%{name}/%{src_ver}/liboctave.so.*
%{_libdir}/%{name}/%{src_ver}/liboctinterp.so.*
%if %{with gui}
%dir %{_libdir}/%{name}/%{src_ver}/exec/
%dir %{_libdir}/%{name}/%{src_ver}/exec/*-*-linux-gnu*/
%exclude %{_datadir}/%{name}/%{src_ver}/locale/
%endif
%{_datadir}/octave/
%{_libdir}/%{name}/site

%files devel
%{_bindir}/mkoctfile
%{_bindir}/mkoctfile-%{src_ver}
%if %{with doc}
%{_mandir}/man1/mkoctfile.1.gz
%endif
%{_includedir}/*
%{_libdir}/%{name}/%{src_ver}/lib*.so
%{_libdir}/%{name}/api-%{apiver}
%{_libdir}/pkgconfig/octave.pc
%{_libdir}/pkgconfig/octinterp.pc
%config %{_sysconfdir}/rpm/macros.octave

%files doc
%doc doc/interpreter/octave.pdf
%doc doc/liboctave/liboctave.pdf
%doc doc/refcard/refcard-a4.pdf
%doc doc/refcard/refcard-legal.pdf

%changelog
