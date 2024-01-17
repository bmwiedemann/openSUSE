#
# spec file for package librcc
#
# Copyright (c) 2023 SUSE LLC
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


%define major   0
Name:           librcc
Version:        0.2.13
Release:        0
Summary:        Russian Character Set Conversion Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://rusxmms.sourceforge.net
Source:         https://github.com/RusXMMS/librcc/archive/refs/tags/librcc-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  aspell-devel
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(libguess)
BuildRequires:  pkgconfig(librcd)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Provides the possibility to automatically convert considered
encodings to and from UTF-8. A lot of languages are supported, not
just the Russian one. The library is part of the rusxmms patch.

%package -n %{name}%{major}
Summary:        Russian Character Set Conversion Library
Group:          System/Libraries
Requires:       rcc-runtime
Supplements:    (unzip and aspell)

%description -n %{name}%{major}
Provides the possibility to automatically convert considered
encodings to and from UTF-8. A lot of languages are supported, not
just the Russian one. The library is part of the rusxmms patch.

%package devel
Summary:        Development files for librcc, a charset conversion library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{major} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of librcc.

%package -n rcc-runtime
Summary:        LibRCC Runtime Environment
Group:          System/Libraries

%description -n rcc-runtime
Runtime environment for the LibRCC package.

%prep
%setup -q -n librcc-librcc-%{version}

%build
./autogen.sh
%configure \
    --disable-static \
    --enable-force-system-iconv
%make_build

%install
%make_install
install -Dm 0644 examples/rcc.xml %{buildroot}%{_sysconfdir}/rcc.xml
rm -f %{buildroot}%{_libdir}/{*.la,rcc/engines/*.la}
rm -rf %{_builddir}/%{name}-%{version}/examples/{.deps,Makefile,*~}

%post -n %{name}%{major} -p /sbin/ldconfig
%postun -n %{name}%{major} -p /sbin/ldconfig

%files -n %{name}%{major}
%license COPYING
%{_libdir}/librcc.so.*
%{_libdir}/librccui.so.*

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README docs examples
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n rcc-runtime
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/rcc/
%config(noreplace) %{_sysconfdir}/rcc.xml

%changelog
