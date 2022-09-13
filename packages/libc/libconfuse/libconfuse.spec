#
# spec file for package libconfuse
#
# Copyright (c) 2022 SUSE LLC
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


%define library_name libconfuse2
Name:           libconfuse
Version:        3.3
Release:        0
Summary:        A configuration file parser library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.nongnu.org/confuse/
Source:         https://github.com/martinh/libconfuse/releases/download/v%{version}/confuse-%{version}.tar.xz
# PATCH-FIX_UPSTREAM
Patch0:         libconfuse-d73777c2c3566fb2647727bb56d9a2295b81669b.patch
BuildRequires:  check-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  rpm-config-SUSE >= 0.g8

%description
libConfuse is a configuration file parser library. It supports
sections and (lists of) values (strings, integers, floats, booleans
or other sections), as well as single/double-quoted strings,
environment variable expansion, functions and nested include
statements.

%package -n %{library_name}
Summary:        A configuration file parser library
Group:          System/Libraries

%description -n %{library_name}
libConfuse is a configuration file parser library. It supports
sections and (lists of) values (strings, integers, floats, booleans
or other sections), as well as single/double-quoted strings,
environment variable expansion, functions and nested include
statements.

%package devel
Summary:        The development files for libconfuse
Group:          Development/Libraries/C and C++
Requires:       %{library_name} = %{version}

%description devel
libConfuse is a configuration file parser library. It supports
sections and (lists of) values (strings, integers, floats, booleans
or other sections), as well as single/double-quoted strings,
environment variable expansion, functions and nested include
statements.

This package holds the development files for libconfuse.

%lang_package -r %{library_name}

%prep
%autosetup -n confuse-%{version} -p1

%build
%configure --enable-shared --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc

%find_lang confuse
install -Dd %{buildroot}%{_mandir}
cp -Rv doc/man/man3/ %{buildroot}%{_mandir}

# clean up unneeded files
make -C examples clean
rm -rf examples/.deps/ examples/Makefile*
rm %{buildroot}%{_libdir}/libconfuse.la

%post -n %{library_name} -p /sbin/ldconfig
%postun -n %{library_name} -p /sbin/ldconfig

%files -n %{library_name}
%license LICENSE
%doc README.md AUTHORS ChangeLog.md
%{_libdir}/libconfuse.so.*

%files devel
%doc doc/html/ doc/tutorial-html/ examples/
%{_libdir}/libconfuse.so
%{_libdir}/pkgconfig/libconfuse.pc
%{_includedir}/confuse.h
%{_mandir}/man3/*.3%{?ext_man}

%files -n %{name}-lang -f confuse.lang

%changelog
