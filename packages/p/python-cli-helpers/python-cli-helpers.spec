#
# spec file for package python-cli-helpers
#
# Copyright (c) 2023 SUSE LLC
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
%bcond_without python2
Name:           python-cli-helpers
Version:        2.3.0
Release:        0
Summary:        Helpers for building command-line apps
License:        BSD-3-Clause
URL:            https://github.com/dbcli/cli_helpers
Source:         https://files.pythonhosted.org/packages/source/c/cli_helpers/cli_helpers-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments >= 2.4
Requires:       python-configobj >= 5.0.5
Requires:       python-tabulate >= 0.8.2
Requires:       python-terminaltables >= 3.0.0
Requires:       python-wcwidth
BuildArch:      noarch
# SECTION test requirements
# Package dependencies
BuildRequires:  %{python_module Pygments >= 2.4}
BuildRequires:  %{python_module configobj >= 5.0.5}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module tabulate >= 0.8.2}
BuildRequires:  %{python_module terminaltables >= 3.0.0}
BuildRequires:  %{python_module wcwidth}
%if %{with python2}
BuildRequires:  python2-backports.csv >= 1.0.0
%endif
# /SECTION
%ifpython2
Requires:       python2-backports.csv >= 1.0.0
%endif
%python_subpackages

%description
CLI Helpers is a Python package for performing common tasks when
building command-line apps. It's a helper library for command-line interfaces.

Libraries like Click <http://click.pocoo.org/5/> and Python Prompt
Toolkit <https://python-prompt-toolkit.readthedocs.io/en/latest/> are
tools that help to create quality apps. CLI Helpers complements these
libraries by wrapping up common tasks in interfaces.

CLI Helpers is not focused on applications' design patterns or
frameworks -- it can be used it on its own or in combination with
other libraries.

%prep
%setup -q -n cli_helpers-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst AUTHORS CHANGELOG docs
%{python_sitelib}/*

%changelog
