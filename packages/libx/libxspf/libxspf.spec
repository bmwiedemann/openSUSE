#
# spec file for package libxspf
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libxspf
Version:        1.2.0
Release:        0
# doxygen
Summary:        Provides XSPF playlist reading and writing support
License:        BSD-3-Clause and LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://libspiff.sourceforge.net/
Source:         http://downloads.xiph.org/releases/xspf/%{name}-%{version}.tar.bz2
Patch0:         libxspf-1.1.0-gcc44.patch
Patch1:         libxspf-gcc47.patch
Patch2:         libxspf-automake.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  liburiparser-devel >= 0.7.5
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libxspf the replacement for libSpiff brings XSPF playlist reading and
 writing support to your C++ application. Both version 0 and 1 are
supported. libxspf uses Expat for XML parsing and CppTest for unit
testing. libxspf is the official reference implementation for XSPF
of the Xiph.Org Foundation. Features :-
* Full conformance to the XSPF specification
* Cross-platform (Unix, Windows, Mac OS X, ...)
* Read and write XSPF files
* XSPF-0 and XSPF-1 support
* Unicode support
* Full support for XSPF extensions
* Full support for XML namespaces
* Fast (XML parsing is done by Expat)
* Uses unit testing
* Liberal license: New BSD license

%package -n 	libxspf4
Summary:        Provides XSPF playlist reading and writing support
Group:          Development/Libraries/C and C++

%description -n libxspf4
libxspf brings XSPF playlist reading and writing support to your C++
application. Both version 0 and 1 are supported. libxspf uses Expat
for XML parsing and CppTest for unit testing. libxspf is the official
reference implementation for XSPF of the Xiph.Org Foundation. Features
* Full conformance to the XSPF specification
* Cross-platform (Unix, Windows, Mac OS X, ...)
* Read and write XSPF files
* XSPF-0 and XSPF-1 support
* Unicode support
* Full support for XSPF extensions
* Full support for XML namespaces
* Fast (XML parsing is done by Expat)
* Uses unit testing
* Liberal license: New BSD license

%package -n libxspf-devel
Summary:        Brings XSPF playlist read and write support to C++ apps
Group:          Development/Libraries/C and C++
Requires:       libexpat-devel
Requires:       libstdc++-devel
Requires:       libxspf4 = %{version}

%description -n libxspf-devel
libxspf brings XSPF playlist reading and writing support to your C++
application. Both version 0 and 1 are supported. libxspf uses Expat
for XML parsing and CppTest for unit testing. libxspf is the official
reference implementation for XSPF of the Xiph.Org Foundation. Features

* Full conformance to the XSPF specification

* Cross-platform (Unix, Windows, Mac OS X, ...)

* Read and write XSPF files

* XSPF-0 and XSPF-1 support

* Unicode support

* Full support for XSPF extensions

* Full support for XML namespaces

* Fast (XML parsing is done by Expat)

* Uses unit testing

* Liberal license: New BSD license

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fiv
%configure  \
  --disable-test \
  --enable-static=no \
  --with-pic
#  --enable-doc
make %{?_smp_mflags}

# This section no longer works without libcpptest and can be enabled when the package is available
# %check
# make %{?_smp_mflags} check

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libxspf4 -p /sbin/ldconfig

%postun -n libxspf4 -p /sbin/ldconfig

%files -n libxspf4
%defattr(-,root,root)
%{_libdir}/libxspf.so.4*

%files -n libxspf-devel
%defattr(-,root,root)
%{_bindir}/xspf_check
%{_bindir}/xspf_strip
%dir %{_includedir}/xspf
%dir %{_includedir}/xspf/ProjectOpus
%{_includedir}/xspf/ProjectOpus/*.h
%{_includedir}/xspf/*.h
%{_libdir}/libxspf.so
%{_libdir}/pkgconfig/xspf.pc

%changelog
