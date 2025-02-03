#
# spec file for package python-nornir
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           python-nornir
Version:        3.5.0
Release:        0
Summary:        Network automation framework written in Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nornir-automation/nornir
Source:         https://github.com/nornir-automation/nornir/archive/v%{version}.tar.gz#/nornir-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ruamel.yaml >= 0.17
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml >= 0.17}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Nornir is a pure Python network automation framework intented to be used
directly from Python.
While most automation frameworks use their own Domain Specific Language (DSL)
which you use to describe what you want to have done, Nornir lets you control
everything from Python.
What Nornir brings to the table is that it takes care of dealing with your
inventory and manages the job of dispatching the tasks you want to run against
your nodes and devices. The framework provides a very simple way to write
plugins if you aren't happy with the ones we ship.

%prep
%setup -q -n nornir-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --ignore tests/core/test_registered_plugins.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/nornir*

%changelog
