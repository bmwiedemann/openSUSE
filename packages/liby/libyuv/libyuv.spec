#
# spec file for package libyuv
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libyuv
Version:        20230517+a377993
Release:        0
Summary:        YUV scaling and conversion library
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://chromium.googlesource.com/libyuv/libyuv/
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf
# from Fedora
Patch0:         Use-a-proper-so-version.patch
Patch1:         Link-against-shared-library.patch
Patch2:         Disable-static-library.patch
Patch3:         Install-missing-yuvconstants-binary.patch
Patch4:         Use-library-suffix-during-installation.patch
Patch5:         cmake-minimum-required.patch
Patch6:         convert_test-little-endian.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libjpeg)

%description
libyuv is a project for YUV image scaling and conversion. It can
convert between RGB and YUV, scale images with point/bilinear/box
filter, rotate by 90/180/270°, and offers SSE/NEON/MSA acceleration.

%package -n libyuv0
Summary:        YUV scaling and conversion library
Group:          System/Libraries

%description -n libyuv0
libyuv is a project for YUV image scaling and conversion.

%package devel
Summary:        Development files for the YUV scaling and conversion library
Group:          Development/Libraries/C and C++
Requires:       libyuv0%{_isa} = %{version}

%description devel
This package contains the development files
for the YUV scaling and conversion library.

%package tools
Summary:        Command line utilities from libyuv
Group:          Productivity/Graphics/Other

%description tools
libyuv is a project for YUV image scaling and conversion. It can
convert between RGB and YUV, scale images with point/bilinear/box
filter, rotate by 90/180/270°, and offers SSE/NEON/MSA acceleration.

This package contains the yuvconvert and yuvconstants commandline programs.

%prep
%autosetup -p1

%build
rversion=`grep --perl-regex --only-matching "(?<=LIBYUV_VERSION )[0-9]+" include/libyuv/version.h`
cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=%{_includedir}
libdir=%{_libdir}

Name:           %{name}
Description:  %{summary}
Version:        ${rversion}
Libs:  -lyuv
EOF

# Compile all unit tests, not only the default set.
export CFLAGS="%{optflags} -DENABLE_ROW_TESTS -DENABLE_FULL_TESTS"
export CXXFLAGS="$CFLAGS"

OUR_CMAKE_FLAGS=' -DCMAKE_SKIP_RPATH:BOOL=ON ' #do not put bogus runpath in installed executables
OUR_CMAKE_FLAGS+=' -DUNIT_TEST:BOOL=ON '
%cmake $OUR_CMAKE_FLAGS
%cmake_build

%install
%cmake_install
install -pDm0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%ldconfig_scriptlets -n libyuv0

%check
LD_LIBRARY_PATH=$PWD/build ./build/libyuv_unittest

%files -n libyuv0
%{_libdir}/libyuv.so.*

%files devel
%license LICENSE
%{_libdir}/libyuv.so
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/yuvconvert
%{_bindir}/yuvconstants

%changelog
