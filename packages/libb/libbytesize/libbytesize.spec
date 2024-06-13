#
# spec file for package libbytesize
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


%define soversion 1

Name:           libbytesize
Version:        2.10
Release:        0
Summary:        A library for working with sizes in bytes
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/storaged-project/libbytesize
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/raw/%{version}/NEWS.rst

BuildRequires:  gcc
BuildRequires:  gmp-devel
BuildRequires:  gtk-doc
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(libpcre2-8)

%description
The LibBytesize is a C library that facilitates work with sizes in
bytes, be it parsing the input from users or producing a human-readable
representation of a size in bytes. This library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n libbytesize%{soversion}
Summary:        A library for working with sizes in bytes
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libbytesize%{soversion}
The LibBytesize is a C library that facilitates work with sizes in
bytes, be it parsing the input from users or producing a human-readable
representation of a size in bytes. This library takes localization into
account. It also provides support for sizes bigger than MAXUINT64.

%package -n bscalc
Summary:        A libbytesize tool
Group:          System/Libraries
Requires:       libbytesize%{soversion} = %{version}
BuildArch:      noarch

%description -n bscalc
This package solely contains the bscalc tool.

%package devel
Summary:        Development files for LibBytesize
Group:          Development/Libraries/C and C++
Requires:       libbytesize%{soversion} = %{version}

%description devel
This package contains header files and pkg-config files needed for development
with the LibBytesize library.

%package -n python3-bytesize
Summary:        Python 3 bindings for LibBytesize
Group:          Development/Libraries/Python
Requires:       libbytesize%{soversion} = %{version}

%description -n python3-bytesize
This package contains Python 3 bindings for LibBytesize making the use of
the library from Python 3 easier and more convenient.

%lang_package

%prep
%autosetup -p1
# Place NEWS.rst in the source tree for %%doc'ing it later.
install -m 644 -t . %{SOURCE1}

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
%python3_fix_shebang

%post -n libbytesize%{soversion} -p /sbin/ldconfig
%postun -n libbytesize%{soversion} -p /sbin/ldconfig

%files -n bscalc
%license LICENSE
%doc NEWS.rst README.md
%{_bindir}/bscalc
%{_mandir}/man1/bscalc.1*

%files -n libbytesize%{soversion}
%{_libdir}/%{name}.so.*

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}
%{_libdir}/%{name}.so
%dir %{_includedir}/bytesize
%{_includedir}/bytesize/bs_size.h
%{_libdir}/pkgconfig/bytesize.pc

%files -n python3-bytesize
%dir %{python3_sitearch}/bytesize
%{python3_sitearch}/bytesize/*

%files lang -f %{name}.lang

%changelog
