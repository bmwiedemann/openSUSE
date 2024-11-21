#
# spec file for package python-typer-slim
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2021 Matthias Bach <marix@marix.org>
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
Name:           python-typer-slim
Version:        0.13.1
Release:        0
Summary:        Typer, build great CLIs. Easy to code. Based on Python type hints
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tiangolo/typer
Source:         https://files.pythonhosted.org/packages/source/t/typer_slim/typer_slim-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
Patch1:         set-proper-pythonpath-for-tutorial-script-tests.patch
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module shellingham}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 8.0.0
Requires:       python-typing_extensions >= 3.7.4.3
Suggests:       python-rich
Suggests:       python-shellingham
Obsoletes:      python-typer < 0.12.0
BuildArch:      noarch
%python_subpackages

%description
Typer is a library for building CLI applications based on Python 3.7+ type hints.

Based on type hints, Typer enables great editor support and completion for developers.
With automatic help and completion, Typer makes CLIs easy to use for users.

This package provides the Typer Python package required to build and run Typer-based CLI applications.

%prep
%setup -q -n typer_slim-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# The typer command is only meant to be provided by the full typer
# package. It's unclear why it shows up here.
%python_expand rm -rf %{buildroot}/%{_bindir}/typer

%check
# the completion tests fail as build runs in sh which is not supported
%pytest -k 'not test_show_completion and not test_install_completion'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/typer
%{python_sitelib}/typer_slim-%{version}*-info

%changelog
