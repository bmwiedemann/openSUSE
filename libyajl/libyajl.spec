#
# spec file for package libyajl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 2
Name:           libyajl
Version:        2.1.0
Release:        0
Summary:        Yet Another JSON Library
License:        ISC
Group:          System/Libraries
Url:            http://lloyd.github.com/yajl/
Source0:        https://github.com/lloyd/yajl/archive/%{version}.tar.gz
Source1:        baselibs.conf
Source2:        json_reformat.1
Source3:        json_verify.1
Source99:       %{name}-rpmlintrc
Patch1:         libyajl-optflags.patch
Patch2:         libyajl-lib_suffix.patch
Patch3:         libyajl-pkgconfig.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a
small validating JSON generator.

%package -n %{name}%{sover}
Summary:        Yet Another JSON Library
Group:          System/Libraries

%description -n %{name}%{sover}
YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a
small validating JSON generator.

%package -n %{name}-devel
Summary:        Yet Another JSON Library (Development Environment)
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description -n %{name}-devel
YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a
small validating JSON generator.

This package provides the necessary environment for compiling and linking
against %{name}.

%package -n %{name}-devel-static
Summary:        Yet Another JSON Library (Static Library)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description -n %{name}-devel-static
YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a
small validating JSON generator.

This package provides the necessary environment for linking statically
against %{name}.

%package -n yajl
Summary:        Yet Another JSON Library Tools
Group:          Productivity/Text/Utilities
Requires:       %{name}%{sover} = %{version}

%description -n yajl
YAJL is a small event-driven (SAX-style) JSON parser written in ANSI C, and a
small validating JSON generator.

This package provides a few command-line utilities for processing JSON files.

%prep
%autosetup -p1 -n yajl-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m644 %{SOURCE2} %{SOURCE3} %{buildroot}/%{_mandir}/man1

%check
make %{?_smp_mflags} test

%post   -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%license COPYING
%{_libdir}/libyajl.so.%{sover}
%{_libdir}/libyajl.so.%{sover}.*

%files -n %{name}-devel
%defattr(-,root,root)
%doc README TODO
%{_includedir}/yajl
%{_libdir}/libyajl.so
%{_libdir}/pkgconfig/yajl.pc

%files -n %{name}-devel-static
%defattr(-,root,root)
%{_libdir}/libyajl_s.a

%files -n yajl
%defattr(-,root,root)
%{_mandir}/man1/json_reformat.1*
%{_mandir}/man1/json_verify.1*
%{_bindir}/json_reformat
%{_bindir}/json_verify

%changelog
