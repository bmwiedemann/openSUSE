#
# spec file for package re2
#
# Copyright (c) 2020 SUSE LLC
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


%global longver 2020-10-01
%global shortver %(echo %{longver}|sed 's|-||g')
%define libname libre2-8
Name:           re2
Version:        %{shortver}
Release:        0
Summary:        C++ fast alternative to backtracking RE engines
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/google/re2/
Source0:        https://github.com/google/re2/archive/%{longver}.tar.gz#/%{name}-%{longver}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g. back references and generalized assertions).

%package -n %{libname}
Summary:        C++ fast alternative to backtracking RE engines
Group:          System/Libraries

%description -n %{libname}
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g. back references and generalized assertions).

%package        devel
Summary:        C++ header files and library symbolic links for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-%{longver}

%build
%if %{do_profiling}
  %make_build CXXFLAGS="%{optflags} %{cflags_profile_generate}"
  %make_build CXXFLAGS="%{optflags} %{cflags_profile_generate}" LDFLAGS="-lgcov" benchlog
  %make_build clean
  %make_build CXXFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CXXFLAGS="%{optflags}"
%endif

%install
%make_install includedir=%{_includedir} libdir=%{_libdir}

# Suppress the static library
find %{buildroot} -name 'lib%{name}.a' -delete

%check
# Tests fail on all 32 bit architectures
%if %{__isa_bits} == 64
%make_build test CXXFLAGS="%{optflags}"
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc AUTHORS CONTRIBUTORS README
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
