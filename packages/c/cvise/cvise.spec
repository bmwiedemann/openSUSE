#
# spec file for package cvise
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


Name:           cvise
Version:        2.6.0+git.20221216.1423ed5
Release:        0
Summary:        Super-parallel Python port of the C-Reduce
License:        BSD-3-Clause
URL:            https://github.com/marxin/cvise
Source:         %{name}-%{version}.tar.xz
BuildRequires:  astyle
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  flex
%if %{suse_version} < 1550
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  indent
BuildRequires:  llvm-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-Pebble
BuildRequires:  python3-chardet
BuildRequires:  python3-psutil
BuildRequires:  python3-pytest
BuildRequires:  unifdef
Requires:       astyle
Requires:       clang
Requires:       colordiff
Requires:       indent
Requires:       llvm
Requires:       python3-Pebble
Requires:       python3-chardet
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
%if %{suse_version} < 1550
export CC=gcc-11
export CXX=g++-11
%endif
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
