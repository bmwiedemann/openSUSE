#
# spec file for package wbxml2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# set libname
%define libname libwbxml2-1

Name:           wbxml2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  pkg-config
BuildRequires:  popt-devel
BuildRequires:  zlib-devel
Url:            http://libwbxml.opensync.org/
Summary:        WBXML parser and compiler library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Version:        0.11.6
Release:        0
Source:         libwbxml-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
wbxml2 is a library that includes a WBXML (Wireless Binary XML)
parser and a WBXML compiler. Unlike wbxml, it uses expat instead of
libxml2. WBXML contains a library and its associated tools to parse,
ecode and handle WBXML documents.

%package -n %{libname}
Summary:        WBXML parser and compiler library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{libname}
wbxml2 is a library that includes a WBXML (Wireless Binary XML)
parser and a WBXML compiler. Unlike wbxml, it uses expat instead of
libxml2. WBXML contains a library and its associated tools to parse,
ecode and handle WBXML documents. The WBXML format is a binary
representation of XML defined by the Wap Forum.

%package -n wbxml2-tools
Summary:        Tools for libwbxml2
License:        GPL-2.0-or-later
Group:          Productivity/Other
Requires:       %{libname} = %{version} 
# package was called wbxml2 in openSUSE < 11.2
Provides:       wbxml2 = %{version}
Obsoletes:      wbxml2 < %{version}

%description -n wbxml2-tools 
wbxml2 is a library that includes a WBXML (Wireless Binary XML)
parser and a WBXML compiler. Unlike wbxml, it uses expat instead of
libxml2. WBXML contains a library and its associated tools to parse,
ecode and handle WBXML documents.

%package -n libwbxml2-devel
Summary:        WBXML parser and compiler library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version} glibc-devel libexpat-devel 

%description -n libwbxml2-devel 
wbxml2 is a library that includes a WBXML (Wireless Binary XML)
parser and a WBXML compiler. Unlike wbxml, it uses expat instead of
libxml2. WBXML contains a library and its associated tools to parse,
ecode and handle WBXML documents.

%prep
%setup -q -n libwbxml-%{version}

%build
mkdir build
pushd build
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
cmake \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DENABLE_INSTALL_DOC:BOOL=OFF \
%if %{_lib} == lib64
        -DLIB_SUFFIX=64 \
%endif
         %{_builddir}/libwbxml-%{version}
make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd build
%makeinstall
popd

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n  %{libname}
%defattr(-, root, root)
%doc BUGS COPYING ChangeLog GNU-LGPL INSTALL README RELEASE References THANKS TODO
%{_libdir}/libwbxml2.so.1*

%files -n libwbxml2-devel
%defattr(-,root,root)
%{_datadir}/cmake/Modules/FindLibWbxml2.cmake
%{_libdir}/pkgconfig/libwbxml2.pc
%{_libdir}/libwbxml2.so
%{_includedir}/libwbxml*

%files -n wbxml2-tools
%defattr(-,root,root)
%{_bindir}/wbxml2xml
%{_bindir}/xml2wbxml

%changelog
