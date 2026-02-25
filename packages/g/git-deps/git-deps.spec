#
# spec file for package git-deps
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


%define skip_python2 1
Name:           git-deps
Version:        1.1.0+git.1696898573.89d51e8
Release:        0
Summary:        Tool to analyze git deps
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://github.com/aspiers/git-deps
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM dont-use-st-markdown.patch gh#aspiers/git-deps!118 mcepl@suse.com
# update syntax to the current levels and eliminate (almost) setup.py
Patch0:         dont-use-st-markdown.patch
# PATCH-FIX-UPSTREAM pygit2-1.15.0.patch gh#aspiers/git-deps!129 mcepl@suse.com
# make compatible with pygit2 1.15.0
Patch1:         pygit2-1.15.0.patch
# PATCH-FIX-UPSTREAM no-pkg-resources.patch gh#aspiers/git-deps!131 mcepl@suse.com
# Don't depend on pkg_resources
Patch2:         no-pkg-resources.patch
# PATCH-FIX-UPSTREAM pygit2-1.16.0.patch gh#aspiers/git-deps!132 mcepl@suse.com
# Upgrade pygit2 to 1.16 and fix bugs, test pass on macos
Patch3:         pygit2-1.16.0.patch
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-pygit2
# Because of version = attr: package.__version__
BuildRequires:  python3-setuptools >= 46.4.0
BuildRequires:  python3-wheel
BuildRequires:  python3-pytest
# BuildRequires:  python3-certifi
Requires:       python3-pygit2
# for html subpackage
Requires:       python3-Flask
#Requires:       nodejs-browserify # broken/missing
Requires:       npm
Requires:       git
BuildArch:      noarch

%description
Tool to analyze git dependencies

file bugs at https://github.com/aspiers/git-deps/issues

%package html
Summary:        Tool to analyze git deps - HTML parts
Group:          Development/Tools/Version Control

%description html
Documentation for git-deps.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%python3_fix_shebang
%fdupes %{buildroot}%{python3_sitelib}

%check
# Test doesn't work with tarball, requires .git/ directory with full history
# # because of gh#libgit2/pygit2$1311
# export PYTEST_ADDOPTS="--ignore tests/test_GitUtils.py"
# %%python3_pytest

%files
%license LICENSE.txt
%doc AUTHORS.rst CONTRIBUTING.md CHANGES.rst README.md USAGE.md
%doc HISTORY.md USE-CASES.md
%{_bindir}/git-deps
# %%{_bindir}/git-fixup
%{_bindir}/gitfile-handler
%{_datadir}/git_deps
%{python3_sitelib}/git_deps
%{python3_sitelib}/git_deps-1.1.0*-info

%files html
%doc docs

%changelog
