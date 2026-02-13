#
# spec file for package python-cli-helpers
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


Name:           python-cli-helpers
Version:        2.7.0
Release:        0
Summary:        Helpers for building command-line apps
License:        BSD-3-Clause
URL:            https://github.com/dbcli/cli_helpers
Source:         https://files.pythonhosted.org/packages/source/c/cli_helpers/cli_helpers-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-configobj >= 5.0.5
Requires:       python-tabulate >= 0.9.0
# install_requires lists tabulate[widechars]
Requires:       python-wcwidth
Suggests:       python-Pygments >= 2.4
BuildArch:      noarch
# SECTION test requirements
# Package dependencies
BuildRequires:  %{python_module Pygments >= 2.4}
BuildRequires:  %{python_module configobj >= 5.0.5}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module tabulate >= 0.8.2}
BuildRequires:  %{python_module wcwidth}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst AUTHORS CHANGELOG docs
%{python_sitelib}/cli[-_]helpers
%{python_sitelib}/cli[-_]helpers-%{version}.dist-info

%changelog
