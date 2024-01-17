#
# spec file for package python-wstools
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-wstools
Version:        0.4.8
Release:        0
Summary:        WSDL parsing services package for Web Services for Python
License:        ZPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pycontribs/wstools
Source:         https://files.pythonhosted.org/packages/8d/d0/0e48ae89e4b2a9aa3a1a088782ae183dc09ca1f3545b29051c46d9efbc0f/wstools-%{version}.tar.gz
# https://github.com/pycontribs/wstools/issues/37
Patch0:         python-wstools-python-310.patch
BuildRequires:  %{python_module pbr >= 1.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 17.1}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python module for WSDL parsing services package for Web Services.

%prep
%setup -q -n wstools-%{version}
%patch0 -p1
# https://github.com/pycontribs/wstools/issues/35
sed -i 's:.pytest-runner.::' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
