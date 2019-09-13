#
# spec file for package openEMS
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


Name:           openEMS
%define octpkg  openems
Version:        0.0.35
Release:        0
Summary:        Electromagnetic field solver using the EC-FDTD method
License:        GPL-3.0-only
Group:          Productivity/Scientific/Physics
Url:            http://openems.de
# source - openEMS component only, not openEMS-Project
Source0:        https://github.com/thliebig/%{name}/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM openEMS-vtk.patch -- Fix linking for VTK >= 6.3
Patch1:         0001-Fix-linking-for-VTK-6.3.patch
# PATCH-FIX-OPENSUSE openEMS-octave-openEMS-load.patch -- Fix openEMS.sh load
Patch2:         0002-Fix-openEMS.sh-load.patch
# PATCH-FIX-OPENSUSE openEMS-octave-nf2ff-load.patch -- Fix nf2ff load
Patch3:         0003-Fix-nf2ff-load.patch
# PATCH-FIX-OPENSUSE openEMS-readme-octave-package.patch -- Add correct instruction about Octave and MATLAB packages
Patch4:         0004-Add-correct-instruction-about-Octave-and-MATLAB-pack.patch
# PATCH-FIX-UPSTREAM openEMS-hdf5.patch -- Fix build with HDF5
Patch5:         0005-Fix-build-with-HDF5.patch
# PATCH-FIX-UPSTREAM openEMS-no-return.patch
Patch6:         0006-Add-missing-return-statement.patch
# PATCH-FIX-OPENSUSE 0001-Fix-build-error-due-to-ambigous-overload-of-isnan-is.patch -- Fix ambigous isnan/std::isnan
Patch7:         0001-Fix-build-error-due-to-ambigous-overload-of-isnan-is.patch
# PATCH-FIX-OPENSUSE 0001-Guard-xmmintrin.h-include-so-it-is-only-used-when-ne.patch -- Only include xmmintrin.h on x86
Patch8:         0001-Guard-xmmintrin.h-include-so-it-is-only-used-when-ne.patch

BuildRequires:  CSXCAD-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
%if %{suse_version} >= 1500
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  octave-devel
BuildRequires:  tinyxml-devel
BuildRequires:  vtk-devel
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(fparser)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Electromagnetic field solver using the EC-FDTD method.

%package -n     libnf2ff0
Summary:        Near-field to far-field transformation library
Group:          System/Libraries

%description -n libnf2ff0
Near-field to far-field transformation library.

%package -n     libopenEMS0
Summary:        Electromagnetic field solver library
Group:          System/Libraries

%description -n libopenEMS0
Electromagnetic field solver using the EC-FDTD method library.

%package        devel
Summary:        openEMS development files
Group:          Development/Libraries/C and C++
Requires:       libnf2ff0 = %{version}
Requires:       libopenEMS0 = %{version}

%description    devel
This package contains libraries for developing applications
that use %{name}.

%package -n     octave-%{name}
Summary:        Octave interface for openEMS
Group:          Productivity/Scientific/Physics
Requires:       %{name} = %{version}
Requires:       AppCSXCAD
Requires:       octave-CSXCAD
Requires:       octave-cli

%description -n octave-%{name}
Electromagnetic field solver using the EC-FDTD method.

This package provides Octave interface for openEMS.

%package -n     %{name}-matlab
Summary:        MATLAB interface for openEMS
Group:          Productivity/Scientific/Physics
Requires:       %{name} = %{version}
Requires:       AppCSXCAD
Requires:       CSXCAD-matlab

%description -n %{name}-matlab
Electromagnetic field solver using the EC-FDTD method.

This package provides MATLAB interface for openEMS.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

echo "Name: %{octpkg}" >> DESCRIPTION
echo "Version: %{version}" >> DESCRIPTION
echo "Date: 2015-10-10" >> DESCRIPTION
echo "Author: Thorsten Liebig" >> DESCRIPTION
echo "Maintainer: Thorsten Liebig" >> DESCRIPTION
echo "Title: Electromagnetic field solver using the EC-FDTD method" >> DESCRIPTION
echo "Description: Electromagnetic field solver using the EC-FDTD method." >> DESCRIPTION
echo "Categories: openEMS" >> DESCRIPTION
echo "Depends: csxcad" >> DESCRIPTION
echo "Autoload: yes" >> DESCRIPTION

cat > Makefile-octave << 'EOF'
MKOCTFILE := mkoctfile

all: h5readatt_octave.oct

%.oct: %.cc
	$(MKOCTFILE) -lhdf5 -DH5_USE_16_API -s $<

clean: ; rm *.o *.oct
EOF

rm matlab/setup.m

mkdir octave_build
cp -r matlab octave_build
pushd octave_build/matlab
    mkdir src
    mv *.cc src/
    mv ../../Makefile-octave src/Makefile
    mkdir inst
    mv *.m inst/
    mv {private,examples,Tutorials} inst/
    cp ../../COPYING .
    mv ../../DESCRIPTION .
    cd ..
    %octave_pkg_src
popd

%build
%ifarch %ix86
# Required for XMM intrinsics
export CFLAGS="%{optflags} -msse"
export CXXFLAGS="%{optflags} -msse"
%endif
%ifnarch %ix86 x86_64
# Always handle subnormals according to IEEE754 (gradual underflow),
# as the code for enabling Flush-To-Zero is x86 specific. This may have
# a performance impact, arch specific code for non-x86 should be used.
export CXXFLAGS="%{optflags} -DSSE_CORRECT_DENORMALS"
%endif
%cmake

%make_jobs

cd ..
pushd octave_build
    %octave_pkg_build
popd

%install
%cmake_install

pushd octave_build
    %octave_pkg_install
popd

%post -n libnf2ff0 -p /sbin/ldconfig

%postun -n libnf2ff0 -p /sbin/ldconfig

%post -n libopenEMS0 -p /sbin/ldconfig

%postun -n libopenEMS0 -p /sbin/ldconfig

%post -n octave-%{name}
%octave --eval "pkg rebuild -auto %{octpkg}"

%postun -n octave-%{name}
%octave --eval "pkg rebuild"

%files
%license COPYING
%doc NEWS README
%{_bindir}/*

%files -n libnf2ff0
%{_libdir}/libnf2ff.so.*

%files -n libopenEMS0
%{_libdir}/libopenEMS.so.*

%files devel
%dir %{_prefix}/include/%{name}
%{_prefix}/include/%{name}/*
%{_libdir}/libnf2ff.so
%{_libdir}/libopenEMS.so

%files -n octave-%{name}
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%files -n %{name}-matlab
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/matlab/

%changelog
