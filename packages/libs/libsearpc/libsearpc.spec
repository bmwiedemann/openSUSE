#
# spec file for package libsearpc
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


%define sover   1

Name:           libsearpc
Version:        3.2.0.20200618
Release:        0
Summary:        Simple C language RPC framework based on GObject system
License:        Apache-2.0
Group:          System/Libraries
URL:            https://github.com/haiwen/libsearpc/
Source0:        %{name}-%{version}.tar.gz
Patch0:         01-fix-includes.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(python3)
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  jansson-devel
%else
BuildRequires:  pkgconfig(jansson)
%endif

%description
Searpc is a simple C language RPC framework based on GObject system. Searpc handles the serialization/deserialization part of RPC, the transport part is left to users.

The serialization/deserialization uses JSON format via json-glib library. A serialized json object is returned from server to client after executing the RPC function. Each RPC function defined in the server side should take an extra GError argument to report error.

%package  -n   %{name}%{sover}
Summary:        Library to handle the serialization/deserialization part of RPC
Group:          System/Libraries

%description  -n   %{name}%{sover}
Searpc is a simple C language RPC framework based on GObject system. Searpc handles the serialization/deserialization part of RPC, the transport part is left to users.

The serialization/deserialization uses JSON format via json-glib library. A serialized json object is returned from server to client after executing the RPC function. Each RPC function defined in the server side should take an extra GError argument to report error.

%package        devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{name}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-pysearpc
Summary:        Python files for %{name}
Group:          System/Libraries
Requires:       %{name}%{sover} = %{version}

%description    -n python3-pysearpc
The python-pysearpc package contains python files to make use of %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
./autogen.sh
%configure --disable-static
%make_build
sed -i -e 's#^prefix.*#prefix=/usr#g' libsearpc.pc
sed -i -e 's/#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' lib/searpc-codegen.py

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.opt-1.pyc" -delete -print

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license LICENSE.txt
%doc README.markdown AUTHORS
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{sover}.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libsearpc.pc
%{_bindir}/searpc-codegen.py

%files -n python3-pysearpc
%dir %{python3_sitearch}/pysearpc
%{python3_sitearch}/pysearpc/*.py
%dir %{python3_sitearch}/pysearpc/__pycache__/
%{python3_sitearch}/pysearpc/__pycache__/*.pyc

%changelog
