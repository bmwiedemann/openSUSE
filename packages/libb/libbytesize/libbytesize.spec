#
# spec file for package libbytesize
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


%define somajor 1
%define libname %{name}%{somajor}
Name:           libbytesize
Version:        2.8
Release:        0
Summary:        A library for working with sizes in bytes
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/storaged-project/libbytesize
Source:         https://github.com/storaged-project/libbytesize/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gtk-doc
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(libpcre2-8)

%description
The LibBytesize is a C library that facilitates work with sizes in
bytes, be it parsing the input from users or producing a human-readable
representation of a size in bytes. This library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n %{libname}
Summary:        A library for working with sizes in bytes
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{libname}
The LibBytesize is a C library that facilitates work with sizes in
bytes, be it parsing the input from users or producing a human-readable
representation of a size in bytes. This library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n bscalc
Summary:        A utility for working with sizes in bytes
Group:          System/Libraries
Requires:       %{libname} = %{version}
BuildArch:      noarch

%description -n bscalc
The LibBytesize is a C library that facilitates work with sizes in
bytes, be it parsing the input from users or producing a human-readable
representation of a size in bytes. This library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package devel
Summary:        Development files for LibBytesize
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package contains header files and pkg-config files needed for development
with the LibBytesize library.

%package -n python3-%{name}
Summary:        Python 3 bindings for LibBytesize
Group:          Development/Libraries/Python
Requires:       %{libname} = %{version}
Requires:       python3-six

%description -n python3-%{name}
This package contains Python 3 bindings for LibBytesize making the use of
the library from Python 3 easier and more convenient.

%lang_package

%prep
%autosetup

%build
%configure \
    --disable-static \
    --with-python3 \
    --with-gtk-doc
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n bscalc
%license LICENSE
%doc README.md
%{_bindir}/bscalc
%{_mandir}/man1/bscalc.1*

%files -n %{libname}
%{_libdir}/%{name}.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/%{name}.so
%dir %{_includedir}/bytesize
%{_includedir}/bytesize/bs_size.h
%{_libdir}/pkgconfig/bytesize.pc

%files -n python3-%{name}
%dir %{python3_sitearch}/bytesize
%{python3_sitearch}/bytesize/*

%files lang -f %{name}.lang

%changelog
