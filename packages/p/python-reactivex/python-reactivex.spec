#
# spec file for package python-reactivex
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


%{?sle15_python_module_pythons}
Name:           python-reactivex
Version:        4.1.0
Release:        0
Summary:        ReactiveX (Rx) for Python
License:        MIT
URL:            https://reactivex.io
# SourceRepository: https://github.com/ReactiveX/RxPY
Source:         https://github.com/ReactiveX/RxPY/archive/refs/tags/v%{version}.tar.gz#/reactivex-%{version}-gh.tar.gz
#PATCH-FIX-OPENSUSE fix-python314-test.patch
Patch0:         fix-python314-test.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing-extensions >= 4.1.1
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions >= 4.1.1}
# /SECTION
%python_subpackages

%description
A library for composing asynchronous and event-based programs using observable
collections and query operator functions in Python

%prep
%autosetup -p1 -n RxPY-%{version}
# https://github.com/ReactiveX/RxPY/blob/master/.github/workflows/python-publish.yml
echo "__version__ = \"%{version}\"" > reactivex/_version.py
sed -i 's/version = "0.0.0" # NOTE: will be updated by publish script/version = "%{version}"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# -n 1: async errors on parallel build
%pytest -n 1

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/reactivex
%{python_sitelib}/reactivex-%{version}.dist-info

%changelog
