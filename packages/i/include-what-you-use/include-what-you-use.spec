#
# spec file for package include-what-you-use
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Aaron Puchert.
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


%define _llvm_version 21

Name:           include-what-you-use
Version:        0.25
Release:        0
Summary:        A tool to analyze #includes in C and C++ source files
License:        NCSA
Group:          Development/Languages/C and C++
URL:            https://include-what-you-use.org/
Source0:        https://include-what-you-use.org/downloads/%{name}-%{version}.src.tar.gz
Patch1:         fix-shebang.patch
Patch2:         iwyu_include_picker.patch
BuildRequires:  c++_compiler
BuildRequires:  clang%{_llvm_version}-devel
BuildRequires:  cmake
BuildRequires:  libstdc++-devel
BuildRequires:  llvm%{_llvm_version}-devel
%if %{suse_version} > 1500
BuildRequires:  python3-base
%else
BuildRequires:  python311-base
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
"Include what you use" means this: for every symbol (type, function,
variable, or macro) that you use in foo.cc (or foo.cpp), either foo.cc
or foo.h should include a .h file that exports the declaration of that
symbol. The include-what-you-use program is a tool to analyze includes
of source files to find include-what-you-use violations, and suggest
fixes for them.

The main goal of include-what-you-use is to remove superfluous includes.
It does this both by figuring out what includes are not actually needed
for this file (for both .cc and .h files), and replacing includes with
forward declarations when possible.

%package tools
Summary:        Additional tools to use %{name} effectively
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description tools
This package contains additional scripts for using %{name} as automated
refactoring tool.

%prep
%autosetup -p1 -n %{name}
sed -i s#lib/#lib\${LLVM_LIBDIR_SUFFIX}/#g CMakeLists.txt

%build
%cmake -DIWYU_LLVM_ROOT_PATH=%{_libdir} \
    -DCMAKE_SKIP_RPATH:BOOL=ON \
%if %{suse_version} <= 1500
    -DPython3_EXECUTABLE=%{_bindir}/python3.11 \
%endif
    ..
%cmake_build

%install
%cmake_install

%check
%global exclude_tests no-test-should-match-this

%ifarch %arm
%global exclude_tests %exclude_tests|cxx.test_badinc
%endif

# Fails with older versions of libstdc++ (at least <= 7, maybe more) with error
# "type 'const std::hash<IndirectClass>' does not provide a call operator".
# Fails with newer versions of libstc++ with error "static assertion failed due
# to requirement 'is_copy_constructible<std::hash<IndirectClass>>::value': hash
# function must be copy constructible".
%if %{pkg_vcmp libstdc++-devel <= 7} || %{pkg_vcmp libstdc++-devel >= 15}
%global exclude_tests %exclude_tests|cxx.test_precomputed_tpl_args(|_cpp14)
%endif

%{ctest '-E' '^(%exclude_tests)$'}

%files
%license LICENSE.TXT
%doc docs/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{_datadir}/%{name}/

%files tools
%{_bindir}/*.py

%changelog
