#
# spec file for package criterion
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

%define _lto_cflags %{nil}
%define sover 3

Name: criterion
Version:   2.4.1
Release:   0
Summary:   A dead-simple, yet extensible, C and C++ unit testing framework
License:   MIT
URL:  https://github.com/Snaipe/Criterion
Source:    https://github.com/Snaipe/Criterion/archive/refs/tags/v2.4.1.tar.gz#/%{name}-%{version}.tar.xz
Patch0:    fix-nanopb.patch
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libprotobuf-nanopb0
BuildRequires:  meson
BuildRequires:  nanopb-devel
BuildRequires:  debugbreak-devel
BuildRequires:  boxfort-devel
BuildRequires:  klib-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-protobuf
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(nanomsg)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(protobuf-lite)

%lang_package

%description
Criterion follows the KISS principle, while keeping the control the user would have with other frameworks:
* C99 and C++11 compatible.
* Tests are automatically registered when declared.
* Implements a xUnit framework structure.
* A default entry point is provided, no need to declare a main unless you want to do special handling.
* Test are isolated in their own process, crashes and signals can be reported and tested.
* Unified interface between C and C++: include the criterion header and it just works.
* Supports parameterized tests and theories.
* Progress and statistics can be followed in real time with report hooks.
* TAP output format can be enabled with an option.
* Runs on Linux, FreeBSD, macOS, and Windows (Compiling with MinGW GCC and Visual Studio 2015+).

%package -n lib%{name}%{sover}
Summary: Libraries needed to use Criterion
Requires: lib%{name}%{sover}-devel = %{version}

%description -n lib%{name}%{sover}
This packages contains all the libraries needed to use Criterion.

%package -n lib%{name}%{sover}-devel
Summary: Devel files for Criterion
Requires: lib%{name}%{sover} = %{version}

%description -n lib%{name}%{sover}-devel
Contains all needed devel files for Criterion.

%prep
%autosetup -n Criterion-%{version}

%build
# we disable tests because they require Cram, a no longer upstream maintained tool that's also not in openSUSE.
%meson -Dtests=false
%meson_build

%install
%meson_install
chrpath -d %{buildroot}%{_libdir}/lib%{name}.so.%{sover}*
%find_lang %{name}

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md AUTHORS ChangeLog CONTRIBUTING.md

%files -n lib%{name}%{sover}
%{_libdir}/libcriterion.so.3
%{_libdir}/libcriterion.so.3.2.0

%files -n lib%{name}%{sover}-devel
%dir %{_includedir}/criterion
%dir %{_includedir}/criterion/internal
%dir %{_includedir}/criterion/internal/assert
%dir %{_includedir}/criterion/new
%{_libdir}/libcriterion.a
%{_includedir}/criterion/abort.h
%{_includedir}/criterion/alloc.h
%{_includedir}/criterion/assert.h
%{_includedir}/criterion/criterion.h
%{_includedir}/criterion/embedded.h
%{_includedir}/criterion/event.h
%{_includedir}/criterion/hooks.h
%{_includedir}/criterion/internal/asprintf-compat.h
%{_includedir}/criterion/internal/assert.h
%{_includedir}/criterion/internal/assert/complex.h
%{_includedir}/criterion/internal/assert/exceptions.h
%{_includedir}/criterion/internal/assert/ieee.h
%{_includedir}/criterion/internal/assert/memory.h
%{_includedir}/criterion/internal/assert/op.h
%{_includedir}/criterion/internal/assert/op.hxx
%{_includedir}/criterion/internal/assert/stream.h
%{_includedir}/criterion/internal/assert/tag.h
%{_includedir}/criterion/internal/assert/tostr.h
%{_includedir}/criterion/internal/assert/types.h
%{_includedir}/criterion/internal/capabilities.h
%{_includedir}/criterion/internal/common.h
%{_includedir}/criterion/internal/deprecation.h
%{_includedir}/criterion/internal/designated-initializer-compat.h
%{_includedir}/criterion/internal/hooks.h
%{_includedir}/criterion/internal/new_asserts.h
%{_includedir}/criterion/internal/ordered-set.h
%{_includedir}/criterion/internal/parameterized.h
%{_includedir}/criterion/internal/preprocess.h
%{_includedir}/criterion/internal/redirect.h
%{_includedir}/criterion/internal/stdio_filebuf.hxx
%{_includedir}/criterion/internal/stream.hxx
%{_includedir}/criterion/internal/test.h
%{_includedir}/criterion/internal/theories.h
%{_includedir}/criterion/logging.h
%{_includedir}/criterion/new/assert.h
%{_includedir}/criterion/new/memory.h
%{_includedir}/criterion/new/stream.h
%{_includedir}/criterion/options.h
%{_includedir}/criterion/output.h
%{_includedir}/criterion/parameterized.h
%{_includedir}/criterion/redirect.h
%{_includedir}/criterion/stats.h
%{_includedir}/criterion/theories.h
%{_includedir}/criterion/types.h
%{_libdir}/libcriterion.so
%{_libdir}/pkgconfig/criterion.pc

%files lang -f %{name}.lang

%changelog
