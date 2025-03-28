#
# spec file for package python-vulkan
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-vulkan
Version:        1.3.275.1
Release:        0
Summary:        Python bindings for the Vulkan API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/realitix/vulkan
Source:         https://files.pythonhosted.org/packages/source/v/vulkan/vulkan-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildRequires:  vulkan-devel
Requires:       python-cffi >= 1.10
Requires:       vulkan
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python extension which supports the Vulkan API.
It keeps the original Vulkan API and focuses on minimizing
the differences induced by the Python language.

%prep
%setup -q -n vulkan-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests available

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/vulkan
%{python_sitelib}/vulkan-%{version}.dist-info

%changelog
