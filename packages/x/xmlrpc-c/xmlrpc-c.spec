#
# spec file for package xmlrpc-c
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


%define soname 3
%define soname_cpp 9
Name:           xmlrpc-c
Version:        1.59.03
Release:        0
Summary:        Library implementing XML-based Remote Procedure Calls
License:        BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            https://xmlrpc-c.sourceforge.net/
Source:         https://sourceforge.net/projects/xmlrpc-c/files/Xmlrpc-c%{20}Super%{20}Stable/%{version}/xmlrpc-c-%{version}.tgz
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
Summary:        A library implementing XML-based remote procedure calls
Group:          System/Libraries

%description -n libxmlrpc++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_abyss%{soname}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_abyss%{soname}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_abyss++%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
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

%package -n libxmlrpc_packetsocket%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_packetsocket%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

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
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server_cgi++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

%package -n libxmlrpc_server_pstream++%{soname_cpp}
Summary:        Library implementing XML-based Remote Procedure Calls
Group:          System/Libraries

%description -n libxmlrpc_server_pstream++%{soname_cpp}
XML-RPC is a lightweight RPC protocol based on XML and HTTP. This
package is used by XML-RPC clients and servers written in C and C++.

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
export CFLAGS_PERSONAL="%{optflags}"
%configure \
    --enable-libxml2-backend
%make_build CADD="-fPIC -DPIC" AR=ar RANLIB=ranlib --jobs 1

%check
%make_build check CADD="-fPIC -DPIC" AR=ar RANLIB=ranlib --jobs 1

%install
%make_install AR=ar RANLIB=ranlib

# Remove static libraries
rm -f %{buildroot}%{_libdir}/*.a

make -C examples clean
make -C examples/cpp clean

%post -n libxmlrpc%{soname} -p /sbin/ldconfig
%post -n libxmlrpc++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_abyss%{soname} -p /sbin/ldconfig
%post -n libxmlrpc_abyss++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_client%{soname} -p /sbin/ldconfig
%post -n libxmlrpc_client++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_cpp%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_packetsocket%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_server%{soname} -p /sbin/ldconfig
%post -n libxmlrpc_server++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_server_abyss%{soname} -p /sbin/ldconfig
%post -n libxmlrpc_server_abyss++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_server_cgi%{soname} -p /sbin/ldconfig
%post -n libxmlrpc_server_cgi++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_server_pstream++%{soname_cpp} -p /sbin/ldconfig
%post -n libxmlrpc_util4 -p /sbin/ldconfig
%post -n libxmlrpc_util++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc%{soname} -p /sbin/ldconfig
%postun -n libxmlrpc++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_abyss%{soname} -p /sbin/ldconfig
%postun -n libxmlrpc_abyss++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_client%{soname} -p /sbin/ldconfig
%postun -n libxmlrpc_client++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_cpp%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_packetsocket%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_server%{soname} -p /sbin/ldconfig
%postun -n libxmlrpc_server++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_server_abyss%{soname} -p /sbin/ldconfig
%postun -n libxmlrpc_server_abyss++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_server_cgi%{soname} -p /sbin/ldconfig
%postun -n libxmlrpc_server_cgi++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_server_pstream++%{soname_cpp} -p /sbin/ldconfig
%postun -n libxmlrpc_util4 -p /sbin/ldconfig
%postun -n libxmlrpc_util++%{soname_cpp} -p /sbin/ldconfig

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
