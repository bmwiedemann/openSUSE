#
# spec file for package python-PySocks
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2016 LISA GmbH, Bingen, Germany.
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


%define oldpython python
%{?sle15_python_module_pythons}
Name:           python-PySocks
Version:        1.7.1
Release:        0
Summary:        A Python SOCKS client module
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Anorov/PySocks
Source:         https://files.pythonhosted.org/packages/source/P/PySocks/PySocks-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-SocksiPy = %{version}
Obsoletes:      %{oldpython}-SocksiPy < %{version}
%endif
%python_subpackages

%description
A Python SOCKS client module.

It is an actively maintained SocksiPy fork. Contains many
improvements to the original.

See https://github.com/Anorov/PySocks for more information.

%prep
%setup -q -n PySocks-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%{python_sitelib}/socks.py*
%{python_sitelib}/sockshandler.py*
%{python_sitelib}/[Pp]y[Ss]ocks-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__

%changelog
