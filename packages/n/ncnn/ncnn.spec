#
# spec file for package ncnn
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Hillwood Yang <hillwood@opensuse.org>
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


%define  sover  1
Name:           ncnn
Version:        20250916
Release:        0
Summary:        A high-performance neural network inference framework
License:        BSD-2-Clause AND BSD-3-Clause AND Zlib
Group:          Development/Tools/Other
URL:            https://github.com/Tencent/ncnn
Source:         https://github.com/Tencent/ncnn/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glslang-nonstd-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(glslang)
BuildRequires:  cmake(SPIRV-Tools-opt)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(protobuf)

%description
ncnn is a high-performance neural network inference computing framework
optimized for mobile platforms. ncnn is deeply considerate about deployment and
uses on mobile phones from the beginning of design. ncnn does not have third
party dependencies. It is cross-platform, and runs faster than all known open
source frameworks on mobile phone cpu. Developers can easily deploy deep
learning algorithm models to the mobile platform by using efficient ncnn
implementation, create intelligent APPs, and bring the artificial intelligence
to your fingertips. ncnn is currently being used in many Tencent applications,
such as QQ, Qzone, WeChat, Pitu and so on.

%package -n lib%{name}%{sover}
Summary:        NCNN library
Group:          System/Libraries

%description -n lib%{name}%{sover}
The package contains the library for ncnn.

%package devel
Summary:        Development tools for ncnn
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The ncnn-devel package contains the header files for ncnn.

%prep
%autosetup -p1

%build
%cmake -DNCNN_BUILD_EXAMPLES=ON \
       -DNCNN_VULKAN=ON \
       -DNCNN_SYSTEM_GLSLANG=ON \
       -DNCNN_SHARED_LIB=ON \
       -DNCNN_ENABLE_LTO=ON
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%doc README.md CONTRIBUTING.md
%license LICENSE.txt
%{_bindir}/*

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}
%{_includedir}/%{name}

%changelog
