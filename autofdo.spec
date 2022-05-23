#
# spec file for package autofdo
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


Name:           autofdo
Version:        0.18
Release:        0
Summary:        A tool to convert perf.data profile to AutoFDO profile
License:        Apache-2.0
URL:            https://github.com/google/autofdo
Source:         https://github.com/google/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         llvm11-fix.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libunwind-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version} > 1320
BuildRequires:  clang13-devel
BuildRequires:  llvm13-devel
%endif

%description
This package contains a tool to convert perf.data profile to AutoFDO
profile that can be used by GCC and LLVM.

Each compiler is supported by a different tool. For GCC, use
'create_gcov'. For LLVM, use 'create_llvm_prof'. The two tools
have compatible command line flags. However, the outputs are
incompatible. You cannot use the profile generated for GCC in
LLVM and vice-versa.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/create_gcov
%{_bindir}/dump_gcov
%{_bindir}/sample_merger
%{_bindir}/profile_merger
%{_bindir}/profile_diff
%{_bindir}/profile_update
%{_bindir}/create_llvm_prof

%changelog
