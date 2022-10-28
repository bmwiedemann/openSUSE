#
# spec file for package libyuv
#
# Copyright (c) 2022 SUSE LLC
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
Version:        20220920+f9fda6e
Release:        0
Summary:        YUV scaling and conversion library
License:        BSD-3-Clause
Group:          Productivity/Multimedia/Other
URL:            https://chromium.googlesource.com/libyuv/libyuv/
Source0:        %{name}-%{version}.tar.xz
Source99:       baselibs.conf
# from Fedora
Patch0:         Use-a-proper-so-version.patch
Patch1:         Link-against-shared-library.patch
Patch2:         Disable-static-library.patch
Patch3:         Don-t-install-conversion-tool.patch
Patch4:         Use-library-suffix-during-installation.patch
Patch5:         Link-main-library-against-libjpeg.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libjpeg)

%description
libyuv is an open source project that includes YUV scaling and conversion functionality.
- Scale YUV to prepare content for compression, with point, bilinear or box filter.
- Convert to YUV from webcam formats for compression.
- Convert to RGB formats for rendering/effects.
- Rotate by 90/180/270 degrees to adjust for mobile devices in portrait mode.
- Optimized for SSSE3/AVX2 on x86/x64.
- Optimized for Neon on Arm.
- Optimized for MSA on Mips.

%package -n libyuv0
Summary:        YUV scaling and conversion library
Group:          System/Libraries

%description -n libyuv0
libyuv is an open source project that includes YUV scaling and conversion functionality.

%package devel
Summary:        Development files for the YUV scaling and conversion library
Group:          Development/Libraries/C and C++
Requires:       libyuv0 = %{version}

%description devel
This package contains the development files
for the YUV scaling and conversion library

%prep
%autosetup -p1

%build
rversion=`grep --perl-regex --only-matching "(?<=LIBYUV_VERSION )[0-9]+" include/libyuv/version.h`
cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=\${prefix}
includedir=%{_includedir}
libdir=%{_libdir}

Name:  %{name}
Description:  %{summary}
Version:  ${rversion}
Libs:  -lyuv
EOF

%cmake
%cmake_build

%install
%cmake_install
install -Dm0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%ldconfig_scriptlets -n libyuv0

%files -n libyuv0
%{_libdir}/libyuv.so.*

%files devel
%license LICENSE
%{_libdir}/libyuv.so
%{_includedir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
