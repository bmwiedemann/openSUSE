#
# spec file for package python-typer
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


%define plainpython python
%{?sle15_python_module_pythons}
Name:           python-typer
Version:        0.13.1
Release:        0
Summary:        Typer, build great CLIs. Easy to code. Based on Python type hints
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tiangolo/typer
Source:         https://files.pythonhosted.org/packages/source/t/typer/typer-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typer-slim}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Work around Python dependency not being auto-added as there are no modules provided
Requires:       %{plainpython}(abi) = %{python_version}
Requires:       python-click
Requires:       python-rich
Requires:       python-shellingham
Requires:       python-typer-slim >= %version
Requires:       python-typing_extensions
Requires(post): update-alternatives
Requires(postun): update-alternatives
# both packages provide /usr/bin/typer
Conflicts:      erlang
BuildArch:      noarch
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
%setup -q -n typer-%{version}
%autopatch -p1

%build
%pyproject_wheel

%install
%pyproject_install

# Remove files that were already installed by typer-slim
%python_expand rm -r %{buildroot}%{$python_sitelib}/typer

%python_clone -a %{buildroot}/%{_bindir}/typer

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# There are no tests in the python package as it only pulls dependencies

%post
%python_install_alternative typer

%postun
%python_uninstall_alternative typer

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/typer
%{python_sitelib}/typer-%{version}*-info

%changelog
