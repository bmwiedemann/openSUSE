#
# spec file for package python-nornir
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
%define skip_python2 1
Name:           python-nornir
Version:        2.3.0
Release:        0
Summary:        Network automation framework written in Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nornir-automation/nornir
#Source:         https://files.pythonhosted.org/packages/source/n/nornir/nornir-%%{version}.tar.gz
Source:         https://github.com/nornir-automation/nornir/archive/v%{version}.tar.gz#/nornir-%{version}.tar.gz
# FIXME: Use the setup.py from pypi
Source1:        setup.py
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2
Requires:       python-colorama >= 0.4.1
Requires:       python-mypy_extensions >= 0.4.1
Requires:       python-napalm >= 2
Requires:       python-ncclient >= 0.6.4
Requires:       python-netmiko >= 2.3.3
Requires:       python-paramiko >= 2.1.1
Requires:       python-pydantic >= 0.18.2
Requires:       python-requests >= 2
Requires:       python-ruamel.yaml >= 0.15.85
Requires:       python-typing_extensions >= 3.7
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.4.1}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module mypy_extensions >= 0.4.1}
BuildRequires:  %{python_module napalm >= 2}
BuildRequires:  %{python_module pydantic >= 0.18.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module ruamel.yaml >= 0.15.85}
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
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
