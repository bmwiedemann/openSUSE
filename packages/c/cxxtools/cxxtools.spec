#
# spec file for package cxxtools
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


%define _lto_cflags %{nil}
%define major   10
Name:           cxxtools
Version:        3.0
Release:        0
Summary:        Collection of General-purpose C++ Classes
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://www.tntnet.org/cxxtools.html
Source0:        https://github.com/maekitalo/cxxtools/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       cxxtools-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
Cxxtools is a collection of general-purpose C++ classes.

It includes classes for:
- argument parsing
- logging
- wrappers for threading (pthreads)
- networking with tcp and udp including iostream-based classes
- std::ostream for md5-calculation
- std::ostream-hexdumper
- std::ostream, which duplicates output (like tee)
- wrappers for fork(2) and pipe(2)
- parser for ini files
- parser for property files
- policy based smartpointer
- wrappers for dlopen(2) and dlsym(2)
- fast http client
- uuencoder-std::ostream
- classes to create mime messages for sending mail with attachements or
  as html-formatted mail
- template based fast signal/slot-classes
- template for pools
- parser for http-query-parameters e.g. for cgi
- ostream-filter for counting bytes passed through it
- wrappers for atomic operations

%package -n libcxxtools%{major}
Summary:        Collection of General-purpose C++ Classes
Group:          System/Libraries

%description -n libcxxtools%{major}
Cxxtools is a collection of general-purpose C++ classes. The library
includes classes for serialization, unicode text, multi threading,
networking, rpc, http client and server, xml, logging and many more.

%package -n libcxxtools-bin%{major}
Summary:        A C++ toolbox - binary RPC package
Group:          System/Libraries

%description -n libcxxtools-bin%{major}
Cxxtools is a collection of general-purpose C++ classes. The library
includes classes for serialization, unicode text, multi threading,
networking, rpc, http client and server, xml, logging and many more.

%package -n libcxxtools-http%{major}
Summary:        A C++ toolbox - HTTP protocol implementation
Group:          System/Libraries

%description -n libcxxtools-http%{major}
Cxxtools is a collection of general-purpose C++ classes. The library
includes classes for serialization, unicode text, multi threading,
networking, rpc, http client and server, xml, logging and many more.

%package -n libcxxtools-json%{major}
Summary:        A C++ toolbox - JSON package
Group:          System/Libraries

%description -n libcxxtools-json%{major}
Cxxtools is a collection of general-purpose C++ classes. The library
includes classes for serialization, unicode text, multi threading,
networking, rpc, http client and server, xml, logging and many more.

%package -n libcxxtools-unit%{major}
Summary:        A C++ toolbox - testing library
Group:          System/Libraries

%description -n libcxxtools-unit%{major}
Cxxtools is a collection of general-purpose C++ classes. The library
includes classes for serialization, unicode text, multi threading,
networking, rpc, http client and server, xml, logging and many more.

%package -n libcxxtools-xmlrpc%{major}
Summary:        A C++ toolbox - XMLRPC package
Group:          System/Libraries

%description -n libcxxtools-xmlrpc%{major}
Cxxtools is a collection of general-purpose C++ classes. The library
includes classes for serialization, unicode text, multi threading,
networking, rpc, http client and server, xml, logging and many more.

%package devel
Summary:        Cxxtools Development Files
Group:          Development/Libraries/C and C++
Requires:       libcxxtools%{major} = %{version}
Requires:       libcxxtools-bin%{major} = %{version}
Requires:       libcxxtools-http%{major} = %{version}
Requires:       libcxxtools-json%{major} = %{version}
Requires:       libcxxtools-unit%{major} = %{version}
Requires:       libcxxtools-xmlrpc%{major} = %{version}
# various home projects does use spurious lib prefix for devel files, lets be compatible
Provides:       lib%{name}-devel = %{version}

%description devel
Cxxtools is a collection of general-purpose C++ classes.

It includes classes for:
- argument parsing
- logging
- wrappers for threading (pthreads)
- networking with tcp and udp including iostream-based classes
- std::ostream for md5-calculation
- std::ostream-hexdumper
- std::ostream, which duplicates output (like tee)
- wrappers for fork(2) and pipe(2)
- parser for ini files
- parser for property files
- policy based smartpointer
- wrappers for dlopen(2) and dlsym(2)
- fast http client
- uuencoder-std::ostream
- classes to create mime messages for sending mail with attachements or
  as html-formatted mail
- template based fast signal/slot-classes
- template for pools
- parser for http-query-parameters e.g. for cgi
- ostream-filter for counting bytes passed through it
- wrappers for atomic operations

%prep
%autosetup

%build
autoreconf -fiv
%configure \
    --disable-static \
    --with-iconvstream=yes \
%ifarch aarch64 s390x
    --with-atomictype=pthread \
%endif
    --with-pic
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}/%{_datadir}/%{name}/

%post   -n libcxxtools%{major} -p /sbin/ldconfig
%postun -n libcxxtools%{major} -p /sbin/ldconfig
%post   -n libcxxtools-bin%{major} -p /sbin/ldconfig
%postun -n libcxxtools-bin%{major} -p /sbin/ldconfig
%post   -n libcxxtools-http%{major} -p /sbin/ldconfig
%postun -n libcxxtools-http%{major} -p /sbin/ldconfig
%post   -n libcxxtools-json%{major} -p /sbin/ldconfig
%postun -n libcxxtools-json%{major} -p /sbin/ldconfig
%post   -n libcxxtools-unit%{major} -p /sbin/ldconfig
%postun -n libcxxtools-unit%{major} -p /sbin/ldconfig
%post   -n libcxxtools-xmlrpc%{major} -p /sbin/ldconfig
%postun -n libcxxtools-xmlrpc%{major} -p /sbin/ldconfig

%files -n libcxxtools%{major}
%{_libdir}/libcxxtools.so.%{major}*

%files -n libcxxtools-bin%{major}
%{_libdir}/libcxxtools-bin.so.%{major}*

%files -n libcxxtools-http%{major}
%{_libdir}/libcxxtools-http.so.%{major}*

%files -n libcxxtools-json%{major}
%{_libdir}/libcxxtools-json.so.%{major}*

%files -n libcxxtools-unit%{major}
%{_libdir}/libcxxtools-unit.so.%{major}*

%files -n libcxxtools-xmlrpc%{major}
%{_libdir}/libcxxtools-xmlrpc.so.%{major}*

%files devel
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/cxxtools-config
%{_bindir}/cxxtz
%{_bindir}/siconvert
%{_includedir}/cxxtools/
%{_libdir}/libcxxtools*.so
%{_libdir}/pkgconfig/cxxtools*.pc

%changelog
