#
# spec file for package openhtj2k
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


Name:           openhtj2k
Version:        0.3.1
Release:        0
Summary:        An open source implementation of ITU-T Rec.814 | ISO 15444-15 (a.k.a. HTJ2K)
License:        BSD-3-Clause
URL:            https://github.com/osamu620/OpenHTJ2K
Source:         https://github.com/osamu620/OpenHTJ2K/archive/refs/tags/v%{version}.tar.gz
Patch0:         openhtj2k-0.3.0-tiff.patch
BuildRequires:  cmake >= 3.14
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtiff-4)

%description
OpenHTJ2K is an open source implementation of ITU-T Rec.814 | ISO/IEC 15444-15 (a.k.a. JPEG 2000 Part 15, High-Throughput JPEG 2000; HTJ2K).

%package -n openhtj2k-devel
Summary:        Development files for openhtj2k
Group:          Productivity/Graphics/Convertors
Requires:       libopenhtj2k0 = %{version}

%description -n openhtj2k-devel
This package contains openhtj2k, an implementation of ITU-T Rec.814 | ISO 15444-15 (a.k.a. HTJ2K).

%package -n libopenhtj2k0
Summary:        An open source implementation of ITU-T Rec.814 | ISO 15444-15 (a.k.a. HTJ2K)
Group:          System/Libraries

%description -n libopenhtj2k0
OpenHTJ2K is an open source implementation of ITU-T Rec.814 | ISO/IEC 15444-15 (a.k.a. JPEG 2000 Part 15, High-Throughput JPEG 2000; HTJ2K).

%prep
%autosetup -n OpenHTJ2K-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%cmake_install

%post -n libopenhtj2k0 -p /sbin/ldconfig
%postun -n libopenhtj2k0 -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/open_htj2k_dec
%{_bindir}/open_htj2k_enc

%files -n openhtj2k-devel
%dir %{_includedir}/open_htj2k
%dir %{_includedir}/open_htj2k/interface
%{_includedir}/open_htj2k/interface/decoder.hpp
%{_includedir}/open_htj2k/interface/encoder.hpp
%{_libdir}/libopen_htj2k_R.so
%{_libdir}/pkgconfig/open_htj2k.pc

%files -n libopenhtj2k0
%{_libdir}/libopen_htj2k_R.so.*

%changelog
