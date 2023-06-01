#
# spec file for package janet
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


%global somajor 1
%global sominor 28
%global libname libjanet%{somajor}_%{sominor}

Name:           janet
Version:        %{somajor}.%{sominor}.0
Release:        0
Summary:        Lisp-like functional and imperative programming language
License:        MIT
URL:            https://janet-lang.org
Source0:        https://github.com/janet-lang/janet/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  ninja

%description
Janet is a functional and imperative programming language.
It runs on Windows, Linux, macOS, BSDs, and should run on other systems with some porting.
The entire language (core library, interpreter, compiler, assembler, PEG) is less than 1MB.
You can also add Janet scripting to an application by embedding a single C source file and a single header.

%package -n %{libname}
Summary:        Lisp-like functional and imperative programming language
Group:          System/Libraries

%description -n %{libname}
Janet is a functional and imperative programming language.
It runs on Windows, Linux, macOS, BSDs, and should run on other systems with some porting.
The entire language (core library, interpreter, compiler, assembler, PEG) is less than 1MB.
You can also add Janet scripting to an application by embedding a single C source file and a single header.

%package devel
Summary:        Lisp-like functional and imperative programming language
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description devel
Janet is a functional and imperative programming language.
It runs on Windows, Linux, macOS, BSDs, and should run on other systems with some porting.
The entire language (core library, interpreter, compiler, assembler, PEG) is less than 1MB.
You can also add Janet scripting to an application by embedding a single C source file and a single header.

%prep
%setup -q

%build
export CFLAGS="%optflags -ffat-lto-objects"
%meson -Ddefault_library=shared 
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
%{_includedir}/janet.h
%{_includedir}/janet/janet.h
%{_libdir}/pkgconfig/janet.pc
%{_libdir}/libjanet.so

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{somajor}*

%changelog
