#
# spec file for package git-repo
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


Name:           git-repo
Version:        2.29
Release:        0
Summary:        The Multiple Git Repository Tool
License:        Apache-2.0
URL:            https://gerrit.googlesource.com/git-repo
Source:         %{name}-%{version}.tar.xz
# SECTION tests
BuildRequires:  git
BuildRequires:  gpg2
BuildRequires:  python3-pytest
BuildRequires:  tree
# /SECTION
Requires:       python3-base
Requires:       git
BuildArch:      noarch

%description
Repo is a tool built on top of Git. Repo helps manage many Git repositories, does the uploads to
revision control systems, and automates parts of the development  workflow. Repo is not meant to
replace Git, only to make it easier to work with Git.

%prep
%setup -q
# fix shebang
sed -i -E "s|#!/usr/bin/env python.*|#!/usr/bin/python3|" repo run_tests
# remove unnecessary document
rm -f docs/windows.md

%build
# nothing to build

%install
install -Dm755 repo %{buildroot}%{_bindir}/repo

%check
%{buildroot}%{_bindir}/repo --help
git config --global user.email "abuild@local.localdomain"
./run_tests

%files
%doc README.md docs/*.md
%{_bindir}/repo
%license LICENSE

%changelog
