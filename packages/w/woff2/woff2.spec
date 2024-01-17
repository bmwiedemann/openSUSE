#
# spec file for package woff2
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


%define soname 1_0_2

Name:           woff2
Version:        1.0.2
Release:        0
Summary:        Web Open Font Format 2.0 library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/woff2
Source0:        https://github.com/google/woff2/archive/v%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM woff2-fix-overflow-when-decoding-glyf.patch -- Check for overflow when decoding glyf
Patch0:         woff2-fix-overflow-when-decoding-glyf.patch
# PATCH-FIX-OPENSUSE install-executables.patch -- Install woff tools
Patch1:         install-executables.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbrotlidec) >= 1.0
BuildRequires:  pkgconfig(libbrotlienc) >= 1.0

%description
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF
1.0 with improved compression that is achieved by using the Brotli
algorithm. The primary purpose of the WOFF2 format is to
efficiently package fonts linked to Web documents by means of CSS
@font-face rules.

%package -n     libwoff2common%{soname}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n libwoff2common%{soname}
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF
1.0 with improved compression that is achieved by using the Brotli
algorithm. The primary purpose of the WOFF2 format is to
efficiently package fonts linked to Web documents by means of CSS
@font-face rules.

This package contains the shared library for %{name}.

%package -n     libwoff2dec%{soname}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n libwoff2dec%{soname}
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF
1.0 with improved compression that is achieved by using the Brotli
algorithm. The primary purpose of the WOFF2 format is to
efficiently package fonts linked to Web documents by means of CSS
@font-face rules.

This package contains the shared library for %{name}.

%package -n     libwoff2enc%{soname}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n libwoff2enc%{soname}
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF
1.0 with improved compression that is achieved by using the Brotli
algorithm. The primary purpose of the WOFF2 format is to
efficiently package fonts linked to Web documents by means of CSS
@font-face rules.

This package contains the shared library for %{name}.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libwoff2common%{soname} = %{version}
Requires:       libwoff2dec%{soname} = %{version}
Requires:       libwoff2enc%{soname} = %{version}

%description    devel
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF
1.0 with improved compression that is achieved by using the Brotli
algorithm. The primary purpose of the WOFF2 format is to
efficiently package fonts linked to Web documents by means of CSS
@font-face rules.

This package contains development files for %{name}.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DBUILD_STATIC_LIBS=OFF \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	-DCMAKE_INSTALL_LIBDIR="%{_libdir}" \
	%{nil}
%make_build

%install
%cmake_install

%post -n libwoff2common%{soname} -p /sbin/ldconfig
%postun -n libwoff2common%{soname} -p /sbin/ldconfig

%post -n libwoff2dec%{soname} -p /sbin/ldconfig
%postun -n libwoff2dec%{soname} -p /sbin/ldconfig

%post -n libwoff2enc%{soname} -p /sbin/ldconfig
%postun -n libwoff2enc%{soname} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/woff2_*

%files -n libwoff2common%{soname}
%license LICENSE
%{_libdir}/libwoff2common.so.*

%files -n libwoff2dec%{soname}
%{_libdir}/libwoff2dec.so.*

%files -n libwoff2enc%{soname}
%{_libdir}/libwoff2enc.so.*

%files devel
%{_includedir}/woff2
%{_libdir}/libwoff2common.so
%{_libdir}/libwoff2dec.so
%{_libdir}/libwoff2enc.so
%{_libdir}/pkgconfig/libwoff2common.pc
%{_libdir}/pkgconfig/libwoff2dec.pc
%{_libdir}/pkgconfig/libwoff2enc.pc

%changelog
