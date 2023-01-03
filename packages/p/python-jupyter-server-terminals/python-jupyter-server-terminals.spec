#
# spec file for package python-jupyter-server-terminals
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-jupyter-server-terminals%{psuffix}
Version:        0.4.3
Release:        0
Summary:        A Jupyter Server Extension Providing Terminals
License:        BSD-3-Clause
URL:            https://github.com/jupyter-server/jupyter_server_terminals
Source:         https://files.pythonhosted.org/packages/source/j/jupyter_server_terminals/jupyter_server_terminals-0.4.3.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  jupyter-rpm-macros
Requires:       python-terminado >= 0.8.3
Requires:       jupyter-server-terminals = %{version}
Provides:       python-jupyter_server_terminals = %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module jupyter-server-terminals = %{version}}
BuildRequires:  %{python_module jupyter-server >= 2}
BuildRequires:  %{python_module pytest >= 7.0}
BuildRequires:  %{python_module pytest-jupyter-server >= 0.5.3}
BuildRequires:  %{python_module pytest-timeout}
%endif
%python_subpackages

%description
A Jupyter Server Extension Providing Terminals.

%package -n jupyter-server-terminals
Summary: Jupyter Server Extension registration for python*-jupyter-server-terminals
# Any flavor is okay
Requires: (%(echo "%{python_module jupyter-server-terminals = %{version}@or@}" | sed "s/@or@/ or /g" | sed 's/ or\s*$//'))

%description -n jupyter-server-terminals
A Jupyter Server Extension Providing Terminals.
This package provides the jupyter server registration

%prep
%setup -q -n jupyter_server_terminals-%{version}
sed -i 's/--color=yes//' pyproject.toml

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%jupyter_move_config
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/jupyter_server_terminals
%{python_sitelib}/jupyter_server_terminals-%{version}.dist-info

%files -n jupyter-server-terminals
%license LICENSE
%_jupyter_config %_jupyter_server_confdir/jupyter_server_terminals.json
%endif

%changelog
