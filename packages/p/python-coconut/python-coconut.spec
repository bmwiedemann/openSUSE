#
# spec file for package python-coconut
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


%bcond_with tests

# coconut is a programming language, not a python module
%define pythons python3
Name:           python-coconut
Version:        3.2.0
Release:        0
Summary:        A functional programming language that compiles to Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/evhub/coconut
Source:         https://files.pythonhosted.org/packages/source/c/coconut/coconut-%{version}.tar.gz
BuildRequires:  %{python_module Pygments >= 2.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-Pygments
Requires:       python-anyio
Requires:       python-async_generator
Requires:       python-cPyparsing >= 2.4.7.2.4.0
Requires:       python-prompt_toolkit >= 3
Requires:       python-psutil
Requires:       python-setuptools
Requires:       python-typing_extensions
Recommends:     python-jupyter
Recommends:     python-papermill
%if %{with tests}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module async_generator}
BuildRequires:  %{python_module cPyparsing >= 2.4.7.2.4.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module prompt_toolkit >= 3}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module typing_extensions}
%endif
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Coconut is a functional programming language that compiles to
Python. Since all valid Python is valid Coconut, using Coconut will
only extend and enhance what is already capable of in Python.

Coconut enhances the repertoire of Python programmers to include
tools for functional programming. Coconut code runs the same on any
Python version.

%prep
%autosetup -p1 -n coconut-%{version}
find . -type f -exec sed -i 's/\r$//' {} +
find . -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/
# a hint how to package it welcome
rm %{buildroot}/usr/share/jupyter/kernels/coconut/kernel.json
%fdupes %{buildroot}%{_bindir}

%check
%if %{with tests}
donttest="test_find_packages"
%pytest --strict-markers -s -k "not $donttest" ./coconut/tests
%endif

%files %{python_files}
%doc README.rst CONTRIBUTING.md DOCS.md FAQ.md HELP.md
%license LICENSE.txt
%{_bindir}/coconut-py3*
%{_bindir}/coconut
%{_bindir}/coconut-v3*
%{_bindir}/coconut-release*
%{_bindir}/coconut-run
%{python_sitelib}/_coconut/
%{python_sitelib}/__coconut__/
%{python_sitelib}/coconut/
%{python_sitelib}/coconut-%{version}.dist-info

%changelog
