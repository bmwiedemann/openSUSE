#
# spec file for package python-jupyter_protocol
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-jupyter-protocol
Version:        0.1.1
Release:        0
License:        BSD-3-Clause
Summary:        Jupyter protocol implementation
Url:            https://jupyter.org
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/j/jupyter-protocol/jupyter_protocol-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module jupyter_core}
BuildRequires:  %{python_module python-dateutil >= 2.1}
BuildRequires:  %{python_module pyzmq >= 13}
BuildRequires:  %{python_module traitlets}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module ipykernel}
BuildRequires:  %{python_module mock}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jupyter_core
Requires:       python-python-dateutil >= 2.1
Requires:       python-pyzmq >= 13
Requires:       python-traitlets
BuildArch:      noarch

%python_subpackages

%description
Jupyter protocol implementation.

%prep
%setup -q -n jupyter_protocol-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/jupyter_protocol/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license COPYING.md
%{python_sitelib}/*

%changelog
