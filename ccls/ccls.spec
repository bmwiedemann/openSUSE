#
# spec file for package ccls
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ccls
Version:        0.20190314
Release:        0
Summary:        C/C++/ObjC language server
# main package is Apache 2.0
# bundled dependencies are Boost (macro_map) and CC0 (siphash)
License:        Apache-2.0 AND CC0-1.0 AND BSL-1.0
Group:          Development/Tools/IDE

URL:            https://github.com/MaskRay/ccls
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz
# FIXME: drop this on the next upstream release
# PATCH-FIX-UPSTREAM 0001-Only-add-include-directories-for-LLVM-clang-rapidjso.patch
# This fixes compilation failures with libstdc++ from gcc9
Patch0:         0001-Only-add-include-directories-for-LLVM-clang-rapidjso.patch

BuildRequires:  clang-devel >= 5.0
BuildRequires:  cmake >= 3.8
BuildRequires:  gcc-c++ >= 7.2
BuildRequires:  llvm-devel >= 7.0
BuildRequires:  rapidjson-devel
BuildRequires:  zlib-devel

BuildRequires:  memory-constraints

Requires:       clang >= 5.0
Requires:       llvm >= 7.0

Provides:       bundled(macro_map)
Provides:       bundled(siphash)

%description
ccls, which originates from cquery, is a C/C++/Objective-C language server.

- code completion (with both signature help and snippets)
- definition/references, and other cross references
- cross reference extensions: $ccls/call $ccls/inheritance $ccls/member
  $ccls/vars ...
- formatting
- hierarchies: call (caller/callee) hierarchy, inheritance (base/derived)
  hierarchy, member hierarchy
- symbol rename
- document symbols and approximate search of workspace symbol
- hover information
- diagnostics and code actions (clang FixIts)
- semantic highlighting and preprocessor skipped regions
- semantic navigation: $ccls/navigate


%prep
%autosetup
rm -rf third_party/rapidjson

%build
pushd .
%cmake -DUSE_SYSTEM_RAPIDJSON=ON

# ccls currently consumes ~1GB of memory during compilation per thread
%limit_build -m 1500
make %{?_smp_mflags}
popd

%install
%make_install -C build

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
