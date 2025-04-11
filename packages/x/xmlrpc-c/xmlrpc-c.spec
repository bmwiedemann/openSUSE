#
# spec file for package xmlrpc-c
#
# Copyright (c) 2025 SUSE LLC
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


%define soname_openssl 1
%define soname 3
%define soname_cpp 9
Name:           xmlrpc-c
Version:        1.60.05
Release:        0
Summary:        Library implementing XML-based Remote Procedure Calls
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            https://xmlrpc-c.sourceforge.net/
Source:         https://downloads.sourceforge.net/xmlrpc-c/xmlrpc-c-%{version}.tgz
Source9:        %{name}-rpmlintrc
Patch1:         skip-expat.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)

%description
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package devel
Summary:        Development package for xmlrpc-c
Group:          Development/Libraries/C and C++
Requires:       libxmlrpc%{soname} = %{version}
Requires:       libxmlrpc++%{soname_cpp} = %{version}
Requires:       libxmlrpc_abyss%{soname} = %{version}
Requires:       libxmlrpc_abyss++%{soname_cpp} = %{version}
Requires:       libxmlrpc_client%{soname} = %{version}
Requires:       libxmlrpc_client++%{soname_cpp} = %{version}
Requires:       libxmlrpc_cpp%{soname_cpp} = %{version}
Requires:       libxmlrpc_openssl%{soname_openssl} = %{version}
Requires:       libxmlrpc_packetsocket%{soname_cpp} = %{version}
Requires:       libxmlrpc_server%{soname} = %{version}
Requires:       libxmlrpc_server++%{soname_cpp} = %{version}
Requires:       libxmlrpc_server_abyss%{soname} = %{version}
Requires:       libxmlrpc_server_abyss++%{soname_cpp} = %{version}
Requires:       libxmlrpc_server_cgi%{soname} = %{version}
Requires:       libxmlrpc_server_cgi++%{soname_cpp} = %{version}
Requires:       libxmlrpc_server_pstream++%{soname_cpp} = %{version}
Requires:       libxmlrpc_util++%{soname_cpp} = %{version}
Requires:       libxmlrpc_util4 = %{version}
Requires:       pkgconfig(libxml-2.0)

%description devel
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

This subpackage contains libraries and header files for developing
applications that want to make use of xmlrpc-c.

%package -n libxmlrpc%{soname}
Summary:        A library implementing XML-based remote procedure calls
Group:          System/Libraries

%description -n libxmlrpc%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc++%{soname_cpp}
Summary:        Legacy C++ interface for xmlrpc-c
Group:          System/Libraries

%description -n libxmlrpc++%{soname_cpp}
libxmlrpc_cpp is the legacy C++ wrapper library.

libxmlrpc_server++, libxmlrpc_server_cgi++,
libxmlrpc_server_pstream++, libxmlrpc_packetsocket,
libxmlrpc_server_abyss++, and libxmlrpc_client++ are the more
elaborate replacements.

%package -n libxmlrpc_abyss%{soname}
Summary:        HTTP server component for xmlrpc-c
Group:          System/Libraries

%description -n libxmlrpc_abyss%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_abyss++%{soname_cpp}
Summary:        HTTP server component for xmlrpc-c
Group:          System/Libraries

%description -n libxmlrpc_abyss++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_client%{soname}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_client%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_client++%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_client++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_cpp%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_cpp%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_openssl1
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_openssl1
This xmlrpc-c component library deals with OpenSSL 3.x's locking state.

%package -n libxmlrpc_packetsocket%{soname_cpp}
Summary:        xmlrpc-c packet socket emulation on stream sockets
Group:          System/Libraries

%description -n libxmlrpc_packetsocket%{soname_cpp}
This xmlrpc-c component library contains a facility for communicating
socket-style, with defined packets like a datagram socket but with
reliable delivery like a stream socket. It's like a POSIX "sequential
packet" socket, except it is built on top of a stream socket, so it
is usable on the many systems that have stream sockets but not
sequential packet sockets.

%package -n libxmlrpc_server%{soname}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_server++%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_server_abyss%{soname}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server_abyss%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_server_abyss++%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server_abyss++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_server_cgi%{soname}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server_cgi%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_server_cgi++%{soname_cpp}
Summary:        XMLRPC interface for CGI programs
Group:          System/Libraries

%description -n libxmlrpc_server_cgi++%{soname_cpp}
This library contains the xmlrpc_c::server_cgi class, used to contain
the guts of a CGI-based XML-RPC server. It runs inside a CGI script
and gets the XML-RPC call from, and delivers the XML-RPC response to,
the CGI environment.

%package -n libxmlrpc_server_pstream++%{soname_cpp}
Summary:        Non-HTTP RPC server with XML payloads
Group:          System/Libraries

%description -n libxmlrpc_server_pstream++%{soname_cpp}
libxmlrpc_server_pstream++ provides a (non-HTTP) RPC server based on
a simple byte stream and XML-RPC XML.

%package -n libxmlrpc_util4
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_util4
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_util++%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_util++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%prep
%autosetup -p1
echo "Not using the embedded libexpat copy"
rm -rvf lib/expat

%build
## -std=gnu11 as the code decidedly does not include stdbool.h but
## includes it's own bool.h all over the place
export CFLAGS_PERSONAL="%{optflags} -std=gnu11"
%configure \
    --enable-libxml2-backend
%make_build CADD="-fPIC -DPIC" AR=ar RANLIB=ranlib --jobs 1

%check
## see comment on -std=gnu11 above
export CFLAGS_PERSONAL="%{optflags} -std=gnu11"
%make_build check CADD="-fPIC -DPIC" AR=ar RANLIB=ranlib --jobs 1

%install
%make_install AR=ar RANLIB=ranlib

# Remove static libraries
rm -fv %{buildroot}%{_libdir}/*.a

make -C examples clean
make -C examples/cpp clean

%ldconfig_scriptlets -n libxmlrpc%{soname}
%ldconfig_scriptlets -n libxmlrpc++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_abyss%{soname}
%ldconfig_scriptlets -n libxmlrpc_abyss++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_client%{soname}
%ldconfig_scriptlets -n libxmlrpc_client++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_cpp%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_openssl%{soname_openssl}
%ldconfig_scriptlets -n libxmlrpc_packetsocket%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_server%{soname}
%ldconfig_scriptlets -n libxmlrpc_server++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_server_abyss%{soname}
%ldconfig_scriptlets -n libxmlrpc_server_abyss++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_server_cgi%{soname}
%ldconfig_scriptlets -n libxmlrpc_server_cgi++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_server_pstream++%{soname_cpp}
%ldconfig_scriptlets -n libxmlrpc_util4
%ldconfig_scriptlets -n libxmlrpc_util++%{soname_cpp}

%files devel
%doc examples/
%{_bindir}/xmlrpc-c-config
%{_libdir}/*.so
%{_includedir}/XmlRpcCpp.h
%{_includedir}/xmlrpc*
%{_libdir}/pkgconfig/xmlrpc*pc

%files -n libxmlrpc%{soname}
%{_libdir}/libxmlrpc.so.%{soname}*

%files -n libxmlrpc++%{soname_cpp}
%{_libdir}/libxmlrpc++.so.%{soname_cpp}*

%files -n libxmlrpc_abyss%{soname}
%{_libdir}/libxmlrpc_abyss.so.%{soname}*

%files -n libxmlrpc_abyss++%{soname_cpp}
%{_libdir}/libxmlrpc_abyss++.so.%{soname_cpp}*

%files -n libxmlrpc_client%{soname}
%{_libdir}/libxmlrpc_client.so.%{soname}*

%files -n libxmlrpc_client++%{soname_cpp}
%{_libdir}/libxmlrpc_client++.so.%{soname_cpp}*

%files -n libxmlrpc_cpp%{soname_cpp}
%{_libdir}/libxmlrpc_cpp.so.%{soname_cpp}*

%files -n libxmlrpc_openssl%{soname_openssl}
%{_libdir}/libxmlrpc_openssl.so.%{soname_openssl}*

%files -n libxmlrpc_packetsocket%{soname_cpp}
%{_libdir}/libxmlrpc_packetsocket.so.%{soname_cpp}*

%files -n libxmlrpc_server%{soname}
%{_libdir}/libxmlrpc_server.so.%{soname}*

%files -n libxmlrpc_server++%{soname_cpp}
%{_libdir}/libxmlrpc_server++.so.%{soname_cpp}*

%files -n libxmlrpc_server_abyss%{soname}
%{_libdir}/libxmlrpc_server_abyss.so.%{soname}*

%files -n libxmlrpc_server_abyss++%{soname_cpp}
%{_libdir}/libxmlrpc_server_abyss++.so.%{soname_cpp}*

%files -n libxmlrpc_server_cgi%{soname}
%{_libdir}/libxmlrpc_server_cgi.so.%{soname}*

%files -n libxmlrpc_server_cgi++%{soname_cpp}
%{_libdir}/libxmlrpc_server_cgi++.so.%{soname_cpp}*

%files -n libxmlrpc_server_pstream++%{soname_cpp}
%{_libdir}/libxmlrpc_server_pstream++.so.%{soname_cpp}*

%files -n libxmlrpc_util4
%{_libdir}/libxmlrpc_util.so.4*

%files -n libxmlrpc_util++%{soname_cpp}
%{_libdir}/libxmlrpc_util++.so.%{soname_cpp}*

%changelog
