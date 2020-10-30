#
# spec file for package cvise
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


Name:           cvise
Version:        1.8.0+git.20201029.d32ab1b
Release:        0
Summary:        Super-parallel Python port of the C-Reduce
License:        BSD-3-Clause
URL:            https://github.com/marxin/cvise
Source:         %{name}-%{version}.tar.xz
BuildRequires:  astyle
%if %{?suse_version} > 1500
BuildRequires:  clang10-devel
BuildRequires:  llvm10-devel
%else
BuildRequires:  clang9-devel
BuildRequires:  llvm9-devel
%endif
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  indent
BuildRequires:  ncurses-devel
BuildRequires:  ninja
BuildRequires:  python3-Pebble
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  unifdef
Requires:       astyle
%if %{?suse_version} > 1500
Requires:       clang10
Requires:       llvm10
%else
Requires:       clang9
Requires:       llvm9
%endif
Requires:       indent
Requires:       python3-Pebble
Requires:       python3-psutil
Requires:       unifdef

%description

C-Vise is a super-parallel Python port of the C-Reduce. The port is fully
compatible to the C-Reduce and uses the same efficient
LLVM-based C/C++ reduction tool named clang_delta.

C-Vise is a tool that takes a large C, C++ or OpenCL program that
has a property of interest (such as triggering a compiler bug) and
automatically produces a much smaller C/C++ or OpenCL program that
has the same property. It is intended for use by people who discover
and report bugs in compilers and other tools that process C/C++ or OpenCL code.

%prep
%setup -q
%autopatch -p1

%build
%define __builder ninja
%cmake -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir}
%cmake_build

%check
cd build
pytest -v .

%install
%cmake_install

%files
%license COPYING
%{_bindir}/cvise
%{_bindir}/cvise-delta
%dir %{_libexecdir}/cvise
%{_libexecdir}/cvise/clex
%{_libexecdir}/cvise/clang_delta
%{_libexecdir}/cvise/clex
%{_libexecdir}/cvise/strlex
%{_libexecdir}/cvise/topformflat
%{_datadir}/cvise

%changelog
