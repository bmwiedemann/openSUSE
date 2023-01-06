#
# spec file for package python-azure-core
#
# Copyright (c) 2023 SUSE LLC
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
%if 0%{?suse_version} >= 1500
%define skip_python2 1
%endif
Name:           python-azure-core
Version:        1.26.2
Release:        0
Summary:        Microsoft Azure Core Library for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         https://files.pythonhosted.org/packages/source/a/azure-core/azure-core-%{version}.zip
Source1:        LICENSE.txt
BuildRequires:  %{python_module azure-nspkg >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-aiohttp >= 3.0
Requires:       python-azure-nspkg >= 3.0.0
Requires:       python-requests >= 2.18.4
Requires:       python-typing_extensions >= 4.0.1
Conflicts:      python-azure-sdk <= 2.0.0

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
%setup -q -n azure-core-%{version}

%build
install -m 644 %{SOURCE1} %{_builddir}/azure-core-%{version}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%{python_expand # delete common files
rm -rf %{buildroot}%{$python_sitelib}/azure/__init__.*
rm -rf %{buildroot}%{$python_sitelib}/azure/__pycache__
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/azure/core
%{python_sitelib}/azure_core-*.egg-info

%changelog
