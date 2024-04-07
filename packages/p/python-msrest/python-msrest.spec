#
# spec file for package python-msrest
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
Name:           python-msrest
Version:        0.7.1
Release:        0
Summary:        AutoRest swagger generator Python client runtime
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/msrest
Source:         https://files.pythonhosted.org/packages/source/m/msrest/msrest-%{version}.zip
Source1:        LICENSE.md
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-azure-core >= 1.24.0
Requires:       python-certifi >= 2017.4.17
Requires:       python-isodate >= 0.6.0
Requires:       python-requests-oauthlib >= 0.5.0
Requires:       (python-requests >= 2.16 with python-requests < 3.00)
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-msrest < 0.7.1
%endif
BuildArch:      noarch

%python_subpackages

%description
AutoRest swagger generator Python client runtime
Swagger is a powerful open source framework: http://swagger.io

%prep
%setup -q -n msrest-%{version}
cp %{SOURCE1} LICENSE.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.md
%{python_sitelib}/msrest
%{python_sitelib}/msrest-%{version}*-info

%changelog
