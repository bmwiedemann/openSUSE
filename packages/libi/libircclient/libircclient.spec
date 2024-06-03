#
# spec file for package libircclient
#
# Copyright (c) 2024 SUSE LLC
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


%define soname 1
Name:           libircclient
Version:        1.10
Release:        0
Summary:        Library implementing client-server IRC protocol
License:        LGPL-2.0-or-later
Group:          System/Libraries
URL:            http://libircclient.sourceforge.net/
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE  libircclient-memory-overflow.diff
Patch0:         libircclient-memory-overflow.diff
# PATCH-FIX-UPSTREAM libircclient-cipher-suite.patch bnc#857151
Patch1:         libircclient-cipher-suite.diff
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1500
BuildRequires:  python3-Sphinx
BuildRequires:  python3-Sphinx-latex
%else
BuildRequires:  python-Sphinx
BuildRequires:  python-Sphinx-latex
%endif
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)

%description
It is designed to be small, fast, portable and compatible to RFC standards and most IRC clients.

%package -n %{name}%{soname}
Summary:        Library implementing client-server IRC protocol
Group:          Development/Libraries/C and C++

%description -n %{name}%{soname}
It is designed to be small, fast, portable and compatible to RFC standards and most IRC clients.

%package -n %{name}-devel
Summary:        Header files and libraries for compiling against libircclient
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description -n %{name}-devel
It is designed to be small, fast, portable and compatible to RFC standards and most IRC clients.

%package -n %{name}-doc
Summary:        Documentation for libircclient
Group:          Development/Libraries/C and C++

%description -n %{name}-doc
It is designed to be small, fast, portable and compatible to RFC standards and most IRC clients.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%configure --enable-ipv6 --enable-openssl --enable-shared
make %{?_smp_mflags}
cd doc
make html

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p "%{buildroot}/%{_mandir}/man1";
install -pm0644 man/libircclient.1 "%{buildroot}/%{_mandir}/man1/";

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%doc Changelog README THANKS
%license LICENSE
%{_libdir}/libircclient.so.%{soname}

%files -n %{name}-devel
%{_includedir}/*
%{_libdir}/libircclient.so
%{_mandir}/man1/*

%files -n %{name}-doc
%doc doc/_build/html examples/*.cpp examples/*.c

%changelog
