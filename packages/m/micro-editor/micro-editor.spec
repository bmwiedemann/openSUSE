#
# spec file for package micro-editor
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global shortcommit     04c5770
%global compiledate     Oct\ 13,\ 2025

Name:           micro-editor
Version:        2.0.15
Release:        0
License:        MIT
Summary:        Micro is a terminal-based text editor that aims to be easy to use and intuitive
URL:            https://github.com/zyedidia/micro
Group:          Productivity/Text/Editors
Source0:        micro-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        micro-editor-Makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  golang-packaging
BuildRequires:  git-core
BuildRequires:  golang(API) >= 1.15

%description
Micro is a terminal-based text editor that aims to be easy to use and intuitive,
while also taking advantage of the full capabilities of modern terminals.
It comes as one single, batteries-included, static binary with no dependencies,
and you can download and use it right now.

As the name indicates, micro aims to be somewhat of a successor to the nano editor
by being easy to install and use in a pinch, but micro also aims to be enjoyable to
use full time, whether you work in the terminal because you prefer it (like me),
or because you need to (over ssh).

%prep
%setup -q -n micro-%{version}
%setup -q -T -D -a 1 -n micro-%{version}
rm -rf vendor
tar -xf %{SOURCE1}

%build
export GOFLAGS="-mod=vendor"

%ifnarch ppc64 ppc64le
    export GOFLAGS="${GOFLAGS} -buildmode=pie"
%endif

export DATE="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%s)} --iso-8601)"
export HASH="%{shortcommit}"
export VERSION="%{version}"

make build VERSION="2.0.15" HASH="rpmbuild" DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"


%install
export GOPATH="%{_builddir}/go:$GOPATH"
mkdir -p %{buildroot}%{_bindir}
mv micro %{buildroot}%{_bindir}

%check
go test ./...

%files
%{_bindir}/micro

%changelog
