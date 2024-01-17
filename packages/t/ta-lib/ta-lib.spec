#
# spec file for package ta-lib
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ta-lib
Version:        0.4.0
Release:        0
Summary:        Technical Analysis Library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://ta-lib.org/
Source:         %{name}-%{version}-src.tar.bz2
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  libtool

%description

TA-Lib provides common functions for the technical analysis of stock/future/commodity market data.

%package -n libta_lib0
Summary:        Technical Analysis Library
Group:          Development/Libraries/C and C++
# O/P added for 12.2. Must be <= until version update.
Obsoletes:      libta0 < %{version}
Provides:       libta0 = %{version}

%description -n libta_lib0

TA-Lib provides common functions for the technical analysis of stock/future/commodity market data.

%package -n libta-devel
Summary:        Technical Analysis Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libta_lib0 = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description -n libta-devel

TA-Lib provides common functions for the technical analysis of stock/future/commodity market data.

%prep

%setup -q -n %{name}

%build

CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="%{optflags} -fno-strict-aliasing"
%if 0%{?suse_version} > 1000
CFLAGS="$CFLAGS -fstack-protector"
CXXFLAGS="$CXXFLAGS -fstack-protector"
%endif

export CFLAGS
export CXXFLAGS

autoreconf -fi

%configure --with-pic --disable-static --disable-rpath

# parallel build not supported
%make_build -j1

%install

%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libta_lib0 -p /sbin/ldconfig
%postun -n libta_lib0 -p /sbin/ldconfig

%files -n libta_lib0
%{_libdir}/libta_lib.so.0*

%files -n libta-devel
%{_bindir}/ta-lib-config
%dir %{_includedir}/ta-lib
%{_includedir}/ta-lib/*.h
%{_libdir}/libta_*.so

%changelog
