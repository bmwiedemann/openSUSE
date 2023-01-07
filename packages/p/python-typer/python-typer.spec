#
# spec file for package python-typer
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
Name:           python-typer
Version:        0.7.0
Release:        0
Summary:        Typer, build great CLIs. Easy to code. Based on Python type hints
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tiangolo/typer
Source:         https://files.pythonhosted.org/packages/source/t/typer/typer-%{version}.tar.gz
Patch0:         run-subprocesses-with-correct-python.patch
Patch1:         set-proper-pythonpath-for-tutorial-script-tests.patch
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module shellingham}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 7.1
Recommends:     python-colorama
Recommends:     python-rich
Recommends:     python-shellingham
BuildArch:      noarch
%python_subpackages

%description
Typer is a library for building CLI applications based on Python 3.6+ type hints.

Based on type hints, Typer enables great editor support and completion for developers.
With automatic help and completion, Typer makes CLIs easy to use for users.

This package provides the Typer Python package required to build and run Typer-based CLI applications.

%prep
%setup -q -n typer-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the completion tests fail as build runs in sh which is not supported
%pytest -k 'not test_show_completion and not test_install_completion'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
