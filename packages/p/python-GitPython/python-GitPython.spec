#
# spec file for package python-GitPython
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-GitPython
Version:        3.1.12.1610074031.f653af66
Release:        0
Summary:        Python Git Library
License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/GitPython
Source:         GitPython-%{version}.tar.xz
Patch0:         test-skips.patch
Patch1:         test_blocking_lock_file-extra-time.patch
BuildRequires:  %{python_module ddt >= 1.1.1}
BuildRequires:  %{python_module gitdb >= 4.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module smmap >= 3.0.1}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-gitdb >= 4.0.1
BuildArch:      noarch
%python_subpackages

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model read and write access to your git repository.
Access repository information conveniently, alter the index directly, handle
remotes, or go down to low-level object database access with big-files support.

With the new object database abstraction added in 0.3, its even possible to
implement your own storage mechanisms, the currently available implementations
are 'cgit' and pure python, which is the default.

%prep
%setup -q -n GitPython-%{version}
echo y | ./init-tests-after-clone.sh
%autopatch -p1
# do not pull in extra deps
sed -i -e '/tox/d' -e '/flake8/d' -e '/coverage/d' test-requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# While SKIP_GITHUB is fine, the two tests skipped with SKIP_LOCALHOST
# should work as the test runner sets up a git daemon.
export SKIP_GITHUB=true
export SKIP_LOCALHOST=true
export TRAVIS=true

export LANG=en_US.UTF-8
export GIT_PYTHON_TEST_GIT_REPO_BASE=${PWD}

git config --global user.email "you@example.com"
git config --global user.name "Your Name"

%pytest -k 'not test_installation' test 

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.md doc/source/*.rst
%dir %{python_sitelib}/git
%{python_sitelib}/git/*
%{python_sitelib}/GitPython*

%changelog
