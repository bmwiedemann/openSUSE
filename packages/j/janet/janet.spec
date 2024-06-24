#
# spec file for package janet
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


%global somajor 1
%global sominor 35
%global revision 0
%global libname libjanet%{somajor}_%{sominor}

Name:           janet
Version:        %{somajor}.%{sominor}.%{revision}
Release:        0
Summary:        Lisp-like functional and imperative programming language
License:        MIT
URL:            https://janet-lang.org
Source0:        https://github.com/janet-lang/janet/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja

%description
Janet is a functional and imperative programming language.  The entire
language (core library, interpreter, compiler, assembler, PEG) is less
than 2MB.  Janet scripting can be added to an application by embedding a
single C source file and a single header.

%package -n %{libname}
Summary:        Library for the lisp-like functional and imperative programming language
Group:          System/Libraries

%description -n %{libname}
This contains the library for Janet—a functional and imperative programming language.

%package devel
Summary:        Headers for embedding Janet scripting
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description devel
Janet is a functional and imperative programming language.  Janet scripting
can be added to an application by embedding a single C source file and a
single header.

This package contains the development files for the Janet programming language.

%package devel-static
Summary:        Headers for embedding Janet scripting
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-devel = %{version}

%description devel-static
Janet is a functional and imperative programming language.  Janet scripting
can be added to an application by embedding a single C source file and a
single header.

This package contains the development files for the Janet programming language.
It contains static libraries for -static linking which is highly discouraged.

%prep
%autosetup

%build
export CFLAGS="%optflags -ffat-lto-objects"
%meson -Ddefault_library=both
%meson_build

%install
export CFLAGS="%optflags -ffat-lto-objects"
%meson_install

# Remove useless keep file
rm %{buildroot}%{_libdir}/janet/.keep

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/janet
%dir %{_libdir}/janet/
%{_mandir}/man1/janet.1%{?ext_man}
%license LICENSE
%doc *.md

%files devel
%dir %{_libdir}/janet
%dir %{_includedir}/janet

%if 0%{?suse_version} > 1600 || 0%{?sle_version} == 150500 && 0%{?is_opensuse}
%{_includedir}/janet.h
%endif

%{_includedir}/janet/*
%{_libdir}/pkgconfig/janet.pc
%{_libdir}/libjanet.so

%files devel-static
%{_libdir}/libjanet.a

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{somajor}*

%changelog
