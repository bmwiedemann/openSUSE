#
# spec file for package git-spice
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

%define gitexecdir %{_libexecdir}/git
Name:           git-spice
Version:        0.31.2
Release:        0
Summary:        Manage stacked Git branches
License:        GPL-3.0-or-later
URL:            https://abhinav.github.io/git-spice/
Source0:        https://github.com/abhinav/git-spice/archive/refs/tags/v%{version}.tar.gz#/git-spice-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.25.0
BuildRequires:  git
BuildRequires:  make
BuildRequires:  notmuch-devel
BuildRequires:  scdoc
Requires:       git

%description
Tool for stacking Git branches. It lets you manage and navigate
stacks of branches, conveniently modify and rebase them, and
create GitHub Pull Requests or GitLab Merge Requests from them.

%prep
%autosetup -p1 -a1

%build
go build \
   -mod=vendor \
%if "%{_arch}" != "ppc64"
   -buildmode=pie
%endif

# Building of documentation is skipped, we don’t have `mise` tool
# available.

%install
install -D -m 0755 gs "%{buildroot}/%{gitexecdir}/git-spice"

%check
go test -v

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{gitexecdir}/git-spice

%changelog
