#
# spec file for package python-coconut
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python2 1
Name:           python-coconut
Version:        1.4.0
Release:        0
Summary:        A functional programming language that compiles to Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/evhub/coconut
Source:         https://files.pythonhosted.org/packages/source/c/coconut/coconut-%{version}.tar.gz
BuildRequires:  %{python_module Pygments >= 2.2}
BuildRequires:  %{python_module prompt_toolkit >= 2}
BuildRequires:  %{python_module pyparsing >= 2.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cPyparsing >= 2.2.0.1.1}
BuildRequires:  %{python_module jupyter >= 1}
BuildRequires:  %{python_module jupyter_console >= 5.2}
BuildRequires:  %{python_module ipykernel >= 4.6}
BuildRequires:  %{python_module ipython >= 5.4}
BuildRequires:  %{python_module mypy >= 0.540}
BuildRequires:  %{python_module psutil >= 5}
BuildRequires:  %{python_module pytest >= 3}
BuildRequires:  %{python_module requests >= 2}
BuildRequires:  %{python_module watchdog >= 0.8}
# /SECTION
Requires:       python-Pygments >= 2.2
Requires:       python-pyparsing >= 2.2
Requires:       python-six
Recommends:     python-cPyparsing >= 2.2.0.1.1
Recommends:     python-jupyter >= 1
Recommends:     python-jupyter_console >= 5.2
Recommends:     python-ipykernel >= 4.6
Recommends:     python-ipython >= 5.4
Recommends:     python-mypy >= 0.540
Requires:       python-prompt_toolkit >= 2
Recommends:     python-psutil >= 5
Recommends:     python-requests >= 2
Recommends:     python-watchdog >= 0.8
Conflicts:      python2-coconut <= 1.4.0
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
%setup -q -n coconut-%{version}
find . -type f -exec sed -i 's/\r$//' {} +
find . -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} +

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/

%files %{python_files}
%doc README.rst CONTRIBUTING.md DOCS.md FAQ.md HELP.md
%license LICENSE.txt
%{_bindir}/coconut-py3*
%{_bindir}/coconut
%{_bindir}/coconut-v1*
%{_bindir}/coconut-release*
%{_bindir}/coconut-run
%{python_sitelib}/coconut/
%{python_sitelib}/coconut-%{version}-py*.egg-info

%changelog
