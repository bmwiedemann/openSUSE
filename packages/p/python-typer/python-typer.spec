#
# spec file for package python-typer
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 SUSE LLC and contributors
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


%define plainpython python
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-typer
Version:        0.20.0
Release:        0
Summary:        Typer, build great CLIs. Easy to code. Based on Python type hints
License:        MIT
URL:            https://github.com/tiangolo/typer
Source:         https://files.pythonhosted.org/packages/source/t/typer/typer-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich}
BuildRequires:  %{python_module shellingham}
BuildRequires:  %{python_module typer-slim >= %{version}}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Work around Python dependency not being auto-added as there are no modules provided
Requires:       %{plainpython}(abi) = %{python_version}
Requires:       python-click
Requires:       python-rich
Requires:       python-shellingham
Requires:       python-typer-slim >= %{version}
Requires:       python-typing_extensions
# both packages provide /usr/bin/typer
Conflicts:      erlang
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Typer is a library for building CLI applications based on Python 3.6+ type hints.

Based on type hints, Typer enables great editor support and completion for developers.
With automatic help and completion, Typer makes CLIs easy to use for users.

This package provides the Typer Python package and ensures all dependencies required
for full functionality are provided. In addition, it provides the command "typer"
which allows users to run scripts not using typer with the same command line comfort
as those that do.

%prep
%autosetup -p1 -n typer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# Remove files that were already installed by typer-slim
%python_expand rm -r %{buildroot}%{$python_sitelib}/typer

%python_clone -a %{buildroot}/%{_bindir}/typer

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Broken with click 8.2.0:
# - test_enum/test_tutorial003
# - test_script_completion_run and test_completion_show_invalid_shell
# - test_invalid_score stumbles over linebreaks in the output
%pytest -k 'not ((test_enum and test_tutorial003) or test_script_completion_run or test_completion_show_invalid_shell or test_invalid_score)'

%post
%python_install_alternative typer

%postun
%python_uninstall_alternative typer

%pre
%python_libalternatives_reset_alternative typer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/typer
%{python_sitelib}/typer-%{version}.dist-info

%changelog
