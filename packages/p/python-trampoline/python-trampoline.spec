#
# spec file for package python-trampoline
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# PyPI ships only a wheel (no sdist). Upstream has no git tags; pin the
# commit that bumped version to 0.1.2. The tree contains trampoline/
# (setup.py packages=['trampoline']); trampoline/__init__.py matches
# the PyPI wheel byte-for-byte.
%global git_commit 1d98f39c3015594e2ac8ed48dccc2f393b4dd82b
%{?sle15_python_module_pythons}
Name:           python-trampoline
Version:        0.1.2
Release:        0
Summary:        Simple and tiny yield-based trampoline implementation
License:        MIT
URL:            https://gitlab.com/ferreum/trampoline
Source:         https://gitlab.com/ferreum/trampoline/-/archive/%{git_commit}/trampoline-%{git_commit}.tar.gz#/trampoline-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A tiny yield-based trampoline for Python. Recursive functions can recurse
virtually infinitely by yielding generator calls instead of calling
themselves directly.

%prep
%autosetup -p1 -n trampoline-%{git_commit}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test_trampoline.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/trampoline
%{python_sitelib}/trampoline-%{version}.dist-info

%changelog
