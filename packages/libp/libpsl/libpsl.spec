#
# spec file for package libpsl
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2015 rpm@cicku.me
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


%define somajor 5
Name:           libpsl
Version:        0.21.2
Release:        0
Summary:        C library for the Publix Suffix List
License:        BSD-3-Clause AND MIT AND MPL-2.0
Group:          Development/Libraries/C and C++
URL:            https://rockdaboot.github.io/libpsl
Source:         https://github.com/rockdaboot/libpsl/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1000:     baselibs.conf
BuildRequires:  libidn2-devel >= 0.14
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  publicsuffix
BuildRequires:  python3-base

%description
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

HTTP user agents can use it to avoid privacy-leaking "supercookies" and "super
domain" certificates. It is also use do highlight domain parts in a user interface
and sorting domain lists by site.

%package -n %{name}%{somajor}
Summary:        C library for the Publix Suffix List
# The libary code is MIT, with built-in data from publicsuffix
License:        MIT AND MPL-2.0
Group:          System/Libraries
Recommends:     publicsuffix

%description -n %{name}%{somajor}
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

HTTP user agents can use it to avoid privacy-leaking "supercookies" and "super
domain" certificates. It is also use do highlight domain parts in a user interface
and sorting domain lists by site.

%package        devel
Summary:        Development files for %{name}
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       %{name}%{somajor} = %{version}

%description    devel
libpsl is a C library to handle the Public Suffix List. A "public suffix" is a
domain name under which Internet users can directly register own names.

HTTP user agents can use it to avoid privacy-leaking "supercookies" and "super
domain" certificates. It is also use do highlight domain parts in a user interface
and sorting domain lists by site.

This package contains libraries and header files.
Developer documentation is in %{_docdir}/libpsl-devel/html .

%package -n     psl
Summary:        Commandline utility to explore the Public Suffix List
License:        MIT
Group:          Productivity/Networking/Other

%description -n psl
This package contains a commandline utility to explore the Public Suffix List,
for example it checks if domains are public suffixes, checks if cookie-domain
is acceptable for domains and so on.

HTTP user agents can use it to avoid privacy-leaking "supercookies" and "super
domain" certificates. It is also use do highlight domain parts in a user interface
and sorting domain lists by site.

%prep
%setup -q
# fix env shebang to call py3 directly
sed -i -e "1s|#!.*|#!%{_bindir}/python3|" src/psl-make-dafsa

%build
# default is libicu, but this just too heavy dependency. This library is part of the
# minimal system as curl uses it - but libidn2 is already used by curl directly, while
# icu is not
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-psl-file=%{_datadir}/publicsuffix/public_suffix_list.dat \
	--with-psl-distfile=%{_datadir}/publicsuffix/public_suffix_list.dafsa
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# in psl-make-dafsa package to break build cycle
make DESTDIR=%{buildroot} install-man
rm %{buildroot}%{_mandir}/man1/psl-make-dafsa.1

%check
%make_build check || (cat tests/test-suite.log; exit 42)

%post -n %{name}%{somajor} -p /sbin/ldconfig
%postun -n %{name}%{somajor} -p /sbin/ldconfig

%files -n %{name}%{somajor}
%license COPYING
%{_libdir}/libpsl.so.%{somajor}*

%files devel
%license COPYING
%doc AUTHORS NEWS
%doc docs/libpsl/html
%{_includedir}/libpsl.h
%{_libdir}/libpsl.so
%{_libdir}/pkgconfig/libpsl.pc

%files -n psl
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/psl
%{_mandir}/man1/psl.1%{?ext_man}

%changelog
