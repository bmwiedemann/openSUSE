#
# spec file for package gh
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


Name:           gh
Version:        1.4.0
Release:        0
Summary:        The official CLI for GitHub
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://cli.github.com/
Source0:        https://github.com/cli/cli/archive/v%{version}.tar.gz#/gh-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.13
Requires:       git

%description
Official CLI client for GitHub written in Go

%prep
%setup -q -n cli-%{version}
%setup -q -T -D -n cli-%{version} -a 1

%build
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw -ldflags=-linkmode=external"
%make_build GH_VERSION="v%{version}" bin/gh manpages

%install
install -D -m 0755 bin/gh %{buildroot}%{_bindir}/gh
install -d %{buildroot}%{_mandir}/man1/
cp share/man/man1/* %{buildroot}%{_mandir}/man1

%files
%doc README.md
%license LICENSE
%{_bindir}/gh
%{_mandir}/man1/*

%changelog
