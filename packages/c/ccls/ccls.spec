#
# spec file for package ccls
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


Name:           ccls
Version:        0.20201025
Release:        0
Summary:        C/C++/ObjC language server
# main package is Apache 2.0
# bundled dependencies are Boost (macro_map) and CC0 (siphash)
License:        Apache-2.0 AND CC0-1.0 AND BSL-1.0
Group:          Development/Tools/IDE
URL:            https://github.com/MaskRay/ccls
Source0:        %{URL}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  clang-devel >= 7.0
BuildRequires:  cmake >= 3.8
BuildRequires:  llvm-devel >= 7.0
BuildRequires:  rapidjson-devel
BuildRequires:  zlib-devel
Requires:       clang >= 5.0
Requires:       llvm >= 7.0
Provides:       bundled(macro_map)
Provides:       bundled(siphash)
# ccls hardcodes the paths to clang's resource dir and we thus must ensure that
# it is always shipped with the same clang version that was used to build it
%{requires_eq clang}
# gcc > 7.0 is called gcc7- in Leap 15.2
%if 0%{?sle_version} == 150200
BuildRequires:  gcc7-c++ >= 7.2
%else
BuildRequires:  gcc-c++ >= 7.2
%endif

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
%autosetup -p1
rm -rf third_party/rapidjson

%build
pushd .
%cmake -DUSE_SYSTEM_RAPIDJSON=ON -DCLANG_LINK_CLANG_DYLIB=on

# ccls currently consumes ~1GB of memory during compilation per thread
%make_build
popd

%install
%make_install -C build

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog
