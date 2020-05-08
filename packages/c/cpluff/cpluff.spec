#
# spec file for package cpluff
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


%define sover 0

Name:           cpluff
Version:        0.2.0
Release:        0
Summary:        A plug-in framework for C
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/jlehtine/c-pluff
Source0:        %{name}-%{version}.tar.xz
Patch0:         cpluff.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(expat)

%description
C-Pluff is a plug-in framework for C programs. It has been strongly inspired by
the Java plug-in framework in Eclipse. C-Pluff focuses on providing core
services for plug-in interaction and plug-in management. It aims to be platform
neutral and supports dynamic changes to plug-in configuration without stopping
the whole application or framework.

%package     -n lib%{name}%{sover}
Summary:        A plug-in framework for C
Group:          System/Libraries

%description -n lib%{name}%{sover}
C-Pluff is a plug-in framework for C programs.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description -n lib%{name}-devel
This package contains libraries and header files for
developing applications that use lib%{name}.

%package     -n lib%{name}xx%{sover}
Summary:        A plug-in framework for C++
Group:          System/Libraries

%description -n lib%{name}xx%{sover}
C-Pluff is a plug-in framework for C++ programs.

%package -n lib%{name}xx-devel
Summary:        Development files for lib%{name}xx
Group:          Development/Libraries/C and C++
Requires:       lib%{name}xx%{sover} = %{version}

%description -n lib%{name}xx-devel
This package contains libraries and header files for
developing applications that use lib%{name}xx.

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
	--enable-cpluffxx \
	--disable-nls \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc

%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig
%post   -n lib%{name}xx%{sover} -p /sbin/ldconfig
%postun -n lib%{name}xx%{sover} -p /sbin/ldconfig

%files
%doc README.txt
%{_bindir}/*

%files -n lib%{name}%{sover}
%license COPYRIGHT.txt
%{_libdir}/lib%{name}.so.%{sover}*

%files -n lib%{name}xx%{sover}
%license COPYRIGHT.txt
%{_libdir}/lib%{name}xx.so.%{sover}*

%files -n lib%{name}-devel
%{_includedir}/cpluff.h
%{_includedir}/cpluffdef.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc

%files -n lib%{name}xx-devel
%{_includedir}/cpluffxx
%{_includedir}/cpluffxx.h
%{_libdir}/lib%{name}xx.so
%{_libdir}/pkgconfig/lib%{name}xx.pc

%changelog
