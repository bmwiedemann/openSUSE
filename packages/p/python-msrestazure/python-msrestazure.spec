#
# spec file for package python-msrestazure
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
Name:           python-msrestazure
Version:        0.6.4
Release:        0
Summary:        AutoRest swagger generator - Azure-specific module
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/msrestazure
Source:         https://files.pythonhosted.org/packages/source/m/msrestazure/msrestazure-%{version}.tar.gz
Source1:        LICENSE.md
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires:       (python-adal >= 0.6.0 with python-adal < 2.0.0)
Requires:       (python-msrest >= 0.6.0 with python-msrest < 2.0.0)
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-msrestazure < 0.6.4
%endif
BuildArch:      noarch

%python_subpackages

%description
AutoRest swagger generator Python client runtime. Azure-specific module.

%prep
%setup -q -n msrestazure-%{version}
cp %{SOURCE1} LICENSE.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files  %{python_files}
%doc README.rst
%license LICENSE.md
%{python_sitelib}/msrestazure
%{python_sitelib}/msrestazure-*.dist-info

%changelog
