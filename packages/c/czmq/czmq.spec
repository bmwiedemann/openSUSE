#
# spec file for package czmq
#
# Copyright (c) 2020 SUSE LLC
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


%define lib_name libczmq4
Name:           czmq
Version:        4.2.0
Release:        0
Summary:        High-level C binding for ZeroMQ
License:        MPL-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/zeromq/czmq
Source0:        https://github.com/zeromq/czmq/releases/download/v%{version}/czmq-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(libzmq) > 4.1
# documentation
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildRequires:  xz

%description
CZMQ is a higher-level binding for the ZeroMQ core API.
This package contains key creation utility zmakecert.

%package -n %{lib_name}
Summary:        Shared library of %{name}
Group:          Development/Languages/C and C++

%description -n %{lib_name}
CZMQ is a higher-level binding for the ZeroMQ core API.

* It wraps the ZeroMQ core API in semantics that lead to shorter,
  more readable applications.
* It hides, as far as possible, the differences between different
  versions of ZeroMQ (2.x, 3.x, 4.x).
* It provides a space for development of more sophisticated API
  semantics.
* It wraps the ZeroMQ security features with high-level tools and
  APIs.
* It is the basis for other language bindings built on top of CZMQ.

%package devel
Summary:        Devel files for %{name}
Group:          Development/Languages/C and C++
Requires:       %{lib_name} = %{version}

%description devel
CZMQ is a higher-level binding for the ZeroMQ core API.

This subpackage contains libraries, header files, and pkgconfig and
cmake descriptions for developing applications that want to make use
of CZMQ.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

rm -f %{buildroot}/%{_bindir}/*.gsl
rm -f %{buildroot}/%{_libdir}/*.la

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/zmakecert
%{_mandir}/man1/zmakecert.1.gz

%files -n %{lib_name}
%{_libdir}/libczmq.so.*

%files devel
%license LICENSE
%doc AUTHORS CONTRIBUTING.md NEWS README.md README.txt
%{_includedir}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_mandir}/man3/z*.3.gz
%{_mandir}/man7/%{name}.7.gz
%dir %{_datadir}/zproject
%{_datadir}/zproject/%{name}

%changelog
