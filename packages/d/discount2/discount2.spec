#
# spec file for package markdown2
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


%define shlib libmarkdown2
Name:           discount2
Version:        2.2.7d
Release:        0
Summary:        Markdown markup language as implemented in Discount 2.x
License:        BSD-3-Clause
URL:            https://github.com/Orc/discount
Source:         https://github.com/Orc/discount/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE discount2-disable_ldconfig.patch badshah400@gmail.com -- Disable ldconfig from make install, post(un) scriptlets are the right place do this
Patch0:         discount2-disable_ldconfig.patch
BuildRequires:  gcc

%description
Discount is a C language implementation of the Markdown markup language. This
package provides series 2.x of the libmarkdown library to allow apps that have
not yet migrated to the version 3 API to be compiled.

%package -n %{shlib}
Summary:        Shared library for Discount markdown library

%description -n %{shlib}
Discount is a C language implementation of the Markdown markup language.

This package provides the shared library for Discount markdown library 2.x.

%package -n %{shlib}-devel
Summary:        Headers and sources for developing apps against discount markdown 2.x
Requires:       %{shlib} = %{version}
Conflicts:      libmarkdown-devel >= 3.0

%description -n %{shlib}-devel
Discount is a C language implementation of the Markdown markup language.

This package provides the headers and sources needed to develop apps against
libmarkdown 2.x.

%prep
%autosetup -n discount-%{version}

%build
CFLAGS="%{optflags}" ./configure.sh \
  --cxx-binding	\
  --shared \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --pkg-config \
  %{nil}
%make_build

%install
%make_install

# Delete binary as we only intend to provide the library for apps to build against
rm -fr %{buildroot}%{_bindir}/*

%check
%make_build test

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYRIGHT
%{_libdir}/*.so.*

%files -n %{shlib}-devel
%license COPYRIGHT
%doc README
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
