#
# spec file for package gn
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


Name:           gn
Version:        0.1807
Release:        0
Summary:        A meta-build system that generates build files for Ninja
License:        BSD-3-Clause
URL:            https://gn.googlesource.com/
Source:         https://dev.gentoo.org/~floppym/dist/%{name}-%{version}.tar.xz
Patch0:         gn-flags.patch
Patch1:         gn-always-python3.patch
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python3-base
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%endif

%description
GN is a meta-build system that generates build files for Ninja.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CC=gcc
export CXX=g++
export AR=ar
%if 0%{?suse_version} < 1500
export CC=gcc-7
export CXX=g++-7
%endif
export CXXFLAGS="%{optflags}"
# bootstrap
python3 build/gen.py \
  --no-strip \
  --no-last-commit-position \
  --no-static-libstdc++
PV=%{version}
cat >out/last_commit_position.h <<-EOF
	#ifndef OUT_LAST_COMMIT_POSITION_H_
	#define OUT_LAST_COMMIT_POSITION_H_
	#define LAST_COMMIT_POSITION_NUM ${PV##0.}
	#define LAST_COMMIT_POSITION "${PV}"
	#endif  // OUT_LAST_COMMIT_POSITION_H_
EOF
%ninja_build -C out gn

%check
%ninja_build -C out gn_unittests
./out/gn_unittests

%install
install -Dm 0755 out/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
