#
# spec file for package python-wstools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-wstools
Version:        0.4.8
Release:        0
Summary:        WSDL parsing services package for Web Services for Python
License:        ZPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pycontribs/wstools
Source:         https://files.pythonhosted.org/packages/8d/d0/0e48ae89e4b2a9aa3a1a088782ae183dc09ca1f3545b29051c46d9efbc0f/wstools-%{version}.tar.gz
BuildRequires:  %{python_module pbr} >= 1.10
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools} >= 17.1
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python module for WSDL parsing services package for Web Services.

%prep
%setup -q -n wstools-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
