#
# spec file for package gn
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


Name:           gn
Version:        0.1544
Release:        0
Summary:        A meta-build system that generates build files for Ninja
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://gn.googlesource.com/
Source:         https://dev.gentoo.org/~floppym/dist/%{name}-%{version}.tar.gz
Patch0:         gn-flags.patch
# PATCH-FIX-UPSTREAM: https://bugs.chromium.org/p/gn/issues/detail?id=6
Patch1:         gn-add_missing_arm_files.patch
BuildRequires:  gcc-c++
%if 0%{suse_version} < 1500
BuildRequires:  gcc7-c++
%endif
BuildRequires:  ninja
BuildRequires:  python2-base

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
%if 0%{suse_version} < 1500
export CC=gcc-7
export CXX=g++-7
%endif
export CXXFLAGS="%{optflags}"
# bootstrap
python2 build/gen.py --no-last-commit-position
cat >out/last_commit_position.h <<-EOF
	#ifndef OUT_LAST_COMMIT_POSITION_H_
	#define OUT_LAST_COMMIT_POSITION_H_
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
