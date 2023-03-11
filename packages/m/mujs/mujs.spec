#
# spec file for package mujs
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


Name:           mujs
Version:        1.3.2
Release:        0
Summary:        An embeddable Javascript interpreter
License:        AGPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://mujs.com
Source0:        https://mujs.com/downloads/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif

%description
MuJS is a lightweight Javascript interpreter designed for embedding in other software to extend them with scripting capabilities.

%package devel
Summary:        MuJS development files
Group:          Development/Languages/C and C++
Provides:       %{name}-static = %{version}

%description devel
This package provides the MuJS static library.

%prep
%autosetup -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%make_build debug CFLAGS="%{optflags} -fPIC"

%install
%make_install prefix="%{_prefix}" libdir="%{_libdir}" CFLAGS="%{optflags} -fPIC"

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}

%files devel
%license COPYING
%doc AUTHORS README
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.a

%changelog
