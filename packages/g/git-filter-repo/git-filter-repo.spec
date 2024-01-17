#
# spec file for package git-filter-repo
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1

%global gitexecdir %{_libexecdir}/git

Name:           git-filter-repo
Version:        2.38.0
Release:        0
Summary:        Quickly rewrite git repository history (git-filter-branch replacement)
License:        GPL-2.0-only OR MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/newren/git-filter-repo
Source0:        https://github.com/newren/git-filter-repo/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  %{python_module devel}
BuildRequires:  git-core
Requires:       git-core

%description
git filter-repo is a versatile tool for rewriting history, which includes
capabilities not found anywhere else. It roughly falls into the same space of
tool as git filter-branch but without the capitulation-inducing poor
performance, with far more capabilities, and with a design that scales
usability-wise beyond trivial rewriting cases.

%prep
%autosetup -p1

# Change shebang in all relevant files in this directory and all subdirectories
find -type f -exec sed -i '1s=^#!%{_bindir}/\(python\|env python\)[23]\?=#!%{_bindir}/python3=' {} +

%build

%install
install -d -m 0755 %{buildroot}%{gitexecdir}
install -m 0755 git-filter-repo %{buildroot}%{gitexecdir}/git-filter-repo

install -d -m 0755 %{buildroot}%{python_sitelib}
ln -sf %{gitexecdir}/git-filter-repo %{buildroot}%{python_sitelib}/git_filter_repo.py

install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 Documentation/man1/git-filter-repo.1 %{buildroot}%{_mandir}/man1/git-filter-repo.1

%files
%license COPYING COPYING.gpl COPYING.mit
%doc README.md contrib/filter-repo-demos
%{gitexecdir}/git-filter-repo
%{python_sitelib}/git_filter_repo.py
%{_mandir}/man1/git-filter-repo.1*

%changelog
