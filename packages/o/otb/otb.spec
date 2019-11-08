#
# spec file for package otb
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Angelos Tzotsos <tzotsos@opensuse.org>.
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


%define tarname OTB
%define filerelease 6.6
%define libversion 6

# Enable remote module by default
%bcond_without enable_remote_module

Name:           otb
Version:        6.6.1
Release:        0
Summary:        A C++ library for remote sensing image processing
License:        Apache-2.0
Group:          Productivity/Scientific/Other
Url:            http://www.orfeo-toolbox.org
Source0:        https://www.orfeo-toolbox.org/packages/archives/OTB/%{tarname}-%{version}.tar.xz
# OTBTemporalGapFilling - http://tully.ups-tlse.fr/jordi/temporalgapfilling.git - git rev. selected by cmake file
Source10:       temporalgapfilling-4fc4a71.tar.xz
# PATCH-FIX-UPSTREAM - otb-fix_lib64_handling.patch: fix lib64 path handling
Patch0:         otb-fix_lib64_handling.patch
# PATCH-FIX-UPSTREAM - otb-fix_VERSION_file_install.patch: fix install path of VERSION
Patch1:         otb-fix_VERSION_file_install.patch
# PATCH-FIX-UPSTREAM https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb/merge_requests/625
Patch2:         otb-6.6.1-reproducible.patch
# PATCH-FIX-OPENSUSE cmake file wants to clone the GIT repo. We are offline, so patch cmake file to be able to use our tarball instead of git clone
Patch10:        fix_non_git_usage.patch
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.1.0
BuildRequires:  fdupes
BuildRequires:  xz
%if 0%{?suse_version} < 1500
# With the default gcc 4.8, the compilation fails on Leap 42.x
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  geotiff-devel
BuildRequires:  insighttoolkit-devel
BuildRequires:  libOpenThreads-devel
BuildRequires:  libcurl-devel
# does not work with GDAL3 yet (on next major update replace this and the requires for devel with gdal-devel again)
BuildRequires:  libgdal20-devel
BuildRequires:  libproj-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libsvm-devel
%if %{with enable_remote_module}
BuildRequires:  git
# GSL is needed by OTBTemporalGapFilling module
BuildRequires:  gsl-devel
%endif
BuildRequires:  glew-devel
BuildRequires:  libglfw-devel
BuildRequires:  libsvm2
BuildRequires:  libtool
BuildRequires:  muparser-devel
BuildRequires:  muparserx-devel
BuildRequires:  ossim-devel
BuildRequires:  python2-devel
BuildRequires:  qwt6-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  python2-numpy-devel
%else
BuildRequires:  python-numpy-devel
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  opencv3-devel
%else
BuildRequires:  opencv-devel < 4.0
%endif
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  swig
BuildRequires:  tinyxml-devel
Obsoletes:      OrfeoToolbox
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ORFEO Toolbox (OTB) is a library of image processing algorithms. OTB
is based on the medical image processing library ITK and offers
particular functionalities for remote sensing image processing in
general and for high spatial resolution images in particular.

This package contains the command line tools illustrating OTB features.

%package devel
Summary:        ORFEO Toolbox development files
Group:          Productivity/Scientific/Other
Requires:       boost-devel
Requires:       cmake
Requires:       gcc
Requires:       gcc-c++
Requires:       glew-devel
Requires:       insighttoolkit-devel
Requires:       lib%{name}%{libversion} = %{version}
Requires:       libOpenThreads-devel
Requires:       libcurl-devel
Requires:       libgdal20-devel
Requires:       libgeotiff-devel
Requires:       libglfw-devel
Requires:       libqt5-linguist-devel
Requires:       libqt5-qtbase-devel
Requires:       libsvm-devel
Requires:       libsvm2
Requires:       libtool
Requires:       muparser-devel
Requires:       muparserx-devel
%if 0%{?suse_version} >= 1550
Requires:       opencv3-devel
%else
Requires:       opencv-devel < 4.0
%endif
Requires:       ossim-devel
Requires:       qwt6-devel
Requires:       tinyxml-devel
Provides:       lib%{name}-devel
Obsoletes:      OrfeoToolbox-devel < %{version}
Provides:       OrfeoToolbox-devel = %{version}

%description devel
ORFEO Toolbox (OTB) is a library of image processing algorithms. OTB
is based on the medical image processing library ITK and offers
particular functionalities for remote sensing image processing in
general and for high spatial resolution images in particular.

This package contains the development files needed to build your own OTB
applications.

%package -n %{name}-bin
Summary:        ORFEO Toolbox command line applications
Group:          Productivity/Scientific/Other
Requires:       lib%{name}%{libversion} = %{version}
Obsoletes:      OrfeoToolbox < %{version}
Provides:       OrfeoToolbox = %{version}

%description -n %{name}-bin
ORFEO Toolbox (OTB) is a library of image processing algorithms. OTB
is based on the medical image processing library ITK and offers
particular functionalities for remote sensing image processing in
general and for high spatial resolution images in particular.

This package contains the command line applications illustrating OTB features.

%package -n monteverdi
Summary:        Application based on OrfeoToolbox (OTB) for remote sensing image processing
Group:          Development/Libraries
Requires:       lib%{name}%{libversion} = %{version}
Requires:       otb-qt
Obsoletes:      monteverdi < %{version}
Provides:       monteverdi = %{version}

%description -n monteverdi
Monteverdi is an image processing workshop based on the OTB library. It takes
advantage of the streaming and multi-threading capabilities of the OTB
pipeline. It also uses cool features as processing on demand and automagic
file format I/O.

%package -n lib%{name}%{libversion}
Summary:        ORFEO Toolbox shared library of image processing algorithms
Group:          System/Libraries
Obsoletes:      OrfeoToolbox

%description -n lib%{name}%{libversion}
ORFEO Toolbox (OTB) is a library of image processing algorithms. OTB
is based on the medical image processing library ITK and offers
particular functionalities for remote sensing image processing in
general and for high spatial resolution images in particular.

This package contains the shared libraries required by Monteverdi,
Monteverdi2 and the OTB applications.

%package -n %{name}-qt
Summary:        ORFEO Toolbox graphical user interface applications
Group:          System/Libraries
Requires:       lib%{name}%{libversion} = %{version}
Obsoletes:      OrfeoToolbox

%description -n %{name}-qt
ORFEO Toolbox (OTB) is a library of image processing algorithms. OTB
is based on the medical image processing library ITK and offers
particular functionalities for remote sensing image processing in
general and for high spatial resolution images in particular.

This package contains the GUI tools illustrating OTB features (using plugins
provided by otb package).

%package -n python2-%{name}
Summary:        ORFEO Toolbox Python2 API for applications
Group:          Development/Languages/Python
Requires:       lib%{name}%{libversion} = %{version}
Obsoletes:      OrfeoToolbox

%description -n python2-%{name}
ORFEO Toolbox Python 2 API for applications.

%package -n python3-%{name}
Summary:        ORFEO Toolbox Python2 API for applications
Group:          Development/Languages/Python
Requires:       lib%{name}%{libversion} = %{version}
Obsoletes:      OrfeoToolbox

%description -n python3-%{name}
ORFEO Toolbox Python 3 API for applications.

%prep
%if %{with enable_remote_module}
%setup -q -n temporalgapfilling -b 10
%endif
%setup -q -n %{tarname}-release-%{filerelease}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch10 -p0
%if %{with enable_remote_module}
mv ../temporalgapfilling/ Modules/Remote/OTBTemporalGapFilling
%endif

%build
# Disable MPI for now since OTB apps do not start easily (we must add MPI libs to LD_LIBRARY_PATH to start apps)
# # Find MPI
# if [ -f %{_libdir}/mpi/gcc/openmpi/bin/mpivars.sh ]; then
#   source %{_libdir}/mpi/gcc/openmpi/bin/mpivars.sh
# fi

%cmake  \
%if 0%{?suse_version} < 1500
  -DCMAKE_C_COMPILER=gcc-7 \
  -DCMAKE_CXX_COMPILER=g++-7 \
%endif
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_TESTING:BOOL=OFF \
  -DOTB_USE_6S:BOOL=ON \
  -DOTB_USE_CURL:BOOL=ON \
  -DOTB_USE_LIBKML:BOOL=OFF \
  -DOTB_USE_LIBSVM:BOOL=ON \
  -DOTB_USE_MAPNIK:BOOL=OFF \
  -DOTB_USE_MPI:BOOL=OFF \
  -DOTB_USE_SPTW:BOOL=ON \
  -DOTB_USE_MUPARSER:BOOL=ON \
  -DOTB_USE_MUPARSERX:BOOL=ON \
  -DOTB_USE_OPENCV:BOOL=ON \
  -DOTB_USE_OPENMP:BOOL=ON \
  -DOTB_USE_GLEW:BOOL=ON \
  -DOTB_USE_GLFW:BOOL=ON \
  -DOTB_USE_OPENGL:BOOL=ON \
  -DOTB_USE_QT:BOOL=ON \
  -DOTB_USE_QWT:BOOL=ON \
  -DQWT_INCLUDE_DIR=%{_includedir}/qt5/qwt6 \
  -DOTB_USE_SIFTFAST:BOOL=ON \
  -DOTB_WRAP_JAVA:BOOL=OFF \
  -DOTB_WRAP_PYTHON:BOOL=ON \
  -DOTB_WRAP_PYTHON3:BOOL=ON \
  -DOTB_INSTALL_LIBRARY_DIR:STRING=%{_lib} \
  -DOTB_INSTALL_PYTHON_DIR:STRING=%{_lib}/otb/python \
  -DOTB_INSTALL_PYTHON3_DIR:STRING=%{_lib}/otb/python3 \
  -DOTB_INSTALL_APP_DIR:STRING=%{_lib}/otb/applications \
%if %{with enable_remote_module}
  -DModule_OTBTemporalGapFilling:BOOL=ON \
%endif
  -DCMAKE_BUILD_TYPE:STRING=Release

make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install 

# install -d %%{buildroot}%{_sysconfdir}/ld.so.conf.d
# LDCONFIG_FILE=%%{buildroot}%{_sysconfdir}/ld.so.conf.d/otb.conf
# %%if "%%{_lib}" == "lib64"
# cat > "$LDCONFIG_FILE" <<EOF
# # Orfeo Toolbox related search paths
# /usr/lib64/otb
# EOF
# %%else
# cat > "$LDCONFIG_FILE" <<EOF
# # Orfeo Toolbox related search paths
# /usr/lib/otb
# EOF
# %%endif

# %%if "%%{_lib}" == "lib64"
# mkdir -p %%{buildroot}/usr/lib64
# mv %%{buildroot}/usr/lib/* %%{buildroot}/usr/lib64/
# %%endif

rm -rf %{buildroot}%{_datadir}/doc
rm -rf %{buildroot}%{_libexecdir}/debug
rm -rf %{buildroot}/usr/lib/*.a
# Remove spurious executable bits
chmod 0644 %{buildroot}/usr/share/applications/monteverdi.desktop
chmod 0644 %{buildroot}/usr/share/pixmaps/monteverdi.xpm

%fdupes %{buildroot}/%{_prefix}

%post -n lib%{name}%{libversion} -p /sbin/ldconfig

%postun -n lib%{name}%{libversion} -p /sbin/ldconfig

%files -n %{name}-bin
%defattr(755,root,root,755)
%{_bindir}/otbcli_*
%{_bindir}/otbcli

%files -n %{name}-qt
%defattr(755,root,root,755)
%{_bindir}/otbgui_*
%{_bindir}/otbgui
%defattr(644,root,root,755)
%dir %{_datadir}/otb
%dir %{_datadir}/otb/i18n/
%{_datadir}/otb/i18n/*

%files -n monteverdi
%defattr(755,root,root,755)
%{_bindir}/monteverdi
%{_bindir}/mapla
%{_datadir}/applications/monteverdi.desktop
%{_datadir}/icons/*
%{_datadir}/pixmaps/monteverdi*

%files -n lib%{name}%{libversion}
%defattr(644,root,root,755)
# %config %{_sysconfdir}/ld.so.conf.d/otb.conf
%dir %{_libdir}/otb/
%{_libdir}/*.so.*
%dir %{_libdir}/otb/applications/
%{_libdir}/otb/applications/otbapp_*.so
%defattr(755,root,root,755)
%{_bindir}/otbTestDriver
%{_bindir}/otbApplicationLauncherCommandLine
%{_bindir}/otbApplicationLauncherQt
%{_bindir}/otbQgisDescriptor
%dir %{_datadir}/otb
%dir %{_datadir}/otb/description
%{_datadir}/otb/description/*.txt
%{_datadir}/otb/VERSION

%files -n python2-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/otb/python/
%{_libdir}/otb/python/*

%files -n python3-%{name}
%defattr(644,root,root,755)
%dir %{_libdir}/otb/python3/
%{_libdir}/otb/python3/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/OTB-%{filerelease}/
%{_libdir}/lib*.so
%{_libdir}/cmake/

%changelog
