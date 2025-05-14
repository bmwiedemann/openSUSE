#
# spec file for package python-azure-core
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-azure-core
Version:        1.34.0
Release:        0
Summary:        Microsoft Azure Core Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure_core/azure_core-%{version}.tar.gz
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aiohttp >= 3.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-opentelemetry-api >= 1.26
Requires:       python-requests >= 2.21.0
Requires:       python-six >= 1.11.0
Requires:       (python-typing_extensions >= 4.6.0 if python-base < 3.8)
Conflicts:      python-azure-sdk <= 2.0.0
%if 0%{?sle_version} >= 150400
Obsoletes:      python3-azure-core < 1.30.0
%endif
BuildArch:      noarch

%python_subpackages

%description
The Azure Core pipeline is a re-structuring of the msrest pipeline introduced in msrest 0.6.0.
Further discussions on the msrest implementation can be found in the msrest wiki.

The Azure Core Pipeline is an implementation of chained policies as described in the
Azure SDK guidelines.

The Python implementation of the pipeline has some mechanisms specific to Python.
This is due to the fact that both synchronous and asynchronous implementations of the
pipeline must be supported independently.

%prep
%setup -q -n azure_core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/azure/core
%{python_sitelib}/azure_core-*.dist-info

%changelog
