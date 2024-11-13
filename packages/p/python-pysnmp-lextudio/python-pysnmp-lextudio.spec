#
# spec file for package python-pysnmp-lextudio
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-pysnmp-lextudio
Version:        6.3.0
Release:        0
Summary:        A pure-Python implementation of v1/v2c/v3 SNMP engine
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lextudio/pysnmp
Source:         https://files.pythonhosted.org/packages/source/p/pysnmp-lextudio/pysnmp_lextudio-%{version}.tar.gz
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module coloredlogs}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module orjson}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyasn1 >= 0.4.8
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pysnmp = %{version}
Conflicts:      otherproviders(python-pysnmp)
BuildArch:      noarch
%python_subpackages

%description
This is a pure-Python, open source and free implementation of v1/v2c/v3 SNMP engine

%prep
%setup -q -n pysnmp_lextudio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.rst
%doc README.md
%{python_sitelib}/pysnmp
%{python_sitelib}/pysnmp_lextudio-%{version}.dist-info

%changelog
