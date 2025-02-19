#
# spec file for package go-mod-upgrade
#
# Copyright (c) 2025 SUSE LLC
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


Name:           go-mod-upgrade
Version:        0.11.0
Release:        0
Summary:        Update outdated Go dependencies interactively
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/oligot/go-mod-upgrade
Source:         go-mod-upgrade-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.20
%{go_nostrip}

%description
Update outdated Go dependencies interactively

%prep
%autosetup -D -a 1

%build
# Temporarily use explicit build until goreleaser is packaged for openSUSE.
GOFLAGS="-buildmode=pie" GIT_TAG="v%{version}" go build -o go-mod-upgrade main.go

%check
./go-mod-upgrade --version

%install
install -Dm 755 go-mod-upgrade %{buildroot}/%{_bindir}/go-mod-upgrade

%files
%license License
%doc readme.md
%{_bindir}/go-mod-upgrade

%changelog
