#
# spec file for package git-credential-oauth
#
# Copyright (c) 2024 SUSE LLC
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


Name:           git-credential-oauth
Version:        0.13.4
Release:        0
Summary:        Git credential helper that authenticates to GitHub and other forges using OAuth
License:        Apache-2.0
Group:          Development/Tools/Version Control
URL:            https://github.com/hickford/git-credential-oauth
Source0:        https://github.com/hickford/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API)
Requires:       git-core

%description
A Git credential helper that securely authenticates to GitHub, GitLab, BitBucket and Gerrit using OAuth.
The first time you authenticate, the helper opens a browser window to the host. Subsequent authentication
within storage lifetime is non interactive.

%prep
%autosetup -p1 -a1

%build
go build \
    -mod=vendor \
    -buildmode=pie \

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%check

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
