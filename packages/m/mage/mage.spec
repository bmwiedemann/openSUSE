#
# spec file for package mage
#
# Copyright (c) 2021 SUSE LLC
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


Name:           mage
Version:        v1.11.0~git0.07afc7d
Release:        0
Summary:	A make-like build tool using Go
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        Apache-2.0
URL:            https://github.com/magefile/mage
Source:         mage-%{version}.tar.xz
BuildRequires:  go
BuildRequires:  golang(API) >= 1.12
BuildRequires:  golang-packaging


%description

Mage is a make-like build tool using Go. You write plain-old go functions, and Mage automatically uses them as Makefile-like runnable targets.

%prep
%setup -q

%build
if test -z "$GOPATH"; then
	GOPATH="$HOME/go"
fi
mkdir -p $GOPATH
go run bootstrap.go

%install
mkdir -p %{buildroot}%{_bindir}
if test -z "$GOPATH"; then
	GOPATH="$HOME/go"
fi
mv $GOPATH/bin/mage %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/mage

%changelog
