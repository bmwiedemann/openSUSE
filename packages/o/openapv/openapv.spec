#
# spec file for package openapv
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         sover 2
%define         sname oapv
Name:           openapv
Version:        0.2.1.1
Release:        0
Summary:        Open Advanced Professional Video Codec
License:        BSD-3-Clause
URL:            https://github.com/AcademySoftwareFoundation/openapv
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         remove-opensuse-release-requirement.patch
BuildRequires:  cmake
%if 0%{suse_version} < 1600
BuildRequires:  gcc13
%endif
ExcludeArch:    %{ix86}

%description
The APV codec is a professional video codec, which was developed in response to
the need for professional level high quality video recording and post
production. The primary purpose of the APV codec is for use in professional
video recording and editing workflows for various types of content.

APV codec utilizes technologies known to be over 20 years to achieve a royalty
free codec. APV builds a video codec using only conventional coding
technologies, which consist of traditional methods published between the early
1980s and the end of the 1990s.

The APV codec standard has the following features:
- Perceptually lossless video quality, which is close to raw video quality
- Low complexity and high throughput intra frame only coding without pixel domain prediction
- Support for high bit-rate range up to a few Gbps for 2K, 4K and 8K
  resolution content, enabled by a lightweight entropy coding scheme
- Frame tiling for immersive content and for enabling parallel encoding and decoding
- Support for various chroma sampling formats from 4:2:2 to 4:4:4, and bit-depths from 10 to 16
- Support for multiple decoding and re-encoding without severe visual quality degradation
- Support multi-view video and auxiliary video like depth, alpha, and preview
- Support various metadata including HDR10/10+ and user-definded format

%package devel
Summary:        Development files for %{name}
Requires:       lib%{sname}%{sover} = %{version}-%{release}

%description devel
%{summary}.

%package -n lib%{sname}%{sover}
Summary:        Library files for %{name}

%description -n lib%{sname}%{sover}
%{summary}.

%prep
%autosetup -p1

%build
test -x "$(type -p gcc-13)" && export CC="$_"
%cmake
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.a" -exec rm {} +

%check
%ctest

%ldconfig_scriptlets -n lib%{sname}%{sover}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{sname}_app_dec
%{_bindir}/%{sname}_app_enc

%files devel
%{_includedir}/%{sname}
%{_libdir}/lib%{sname}.so
%{_libdir}/pkgconfig/%{sname}.pc

%files -n lib%{sname}%{sover}
%{_libdir}/lib%{sname}.so.*

%changelog
