#
# spec file for package gosec
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


Name:           gosec
Version:        2.14.0
Release:        0
Summary:        Golang security checker
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/securego/gosec
Source:         gosec-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16
BuildRequires:  golang-packaging
%{go_nostrip}

%description
Inspects source code for security problems by scanning the go abstract syntax tree.

%prep
%autosetup -D -a 1

%build
# Native linux build includes version tags but currently works only on x86_64
%ifarch x86_64
GOFLAGS="-buildmode=pie" GIT_TAG="v%{version}" make build-linux
%else
GOFLAGS="-buildmode=pie" GIT_TAG="v%{version}" make build
%endif

%check
# check if binary is working
./gosec --version
make sec
# Not yet working because it wants to pull the latest ginkgo version from GitHub
#make test

%install
install -Dm 755 gosec %{buildroot}/%{_bindir}/gosec

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/gosec

%changelog
