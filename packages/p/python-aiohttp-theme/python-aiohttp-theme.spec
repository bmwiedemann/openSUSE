#
# spec file for package python-aiohttp-theme
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
Name:           python-aiohttp-theme
Version:        0.1.7
Release:        0
Summary:        A configurable sidebar-enabled Sphinx theme
License:        BSD-3-Clause
URL:            https://github.com/aio-libs/aiohttp-theme
Source:         https://files.pythonhosted.org/packages/source/a/aiohttp_theme/aiohttp_theme-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A configurable sidebar-enabled Sphinx theme used by aiohttp

%prep
%setup -q -n aiohttp_theme-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/aiohttp_theme
%{python_sitelib}/aiohttp_theme-%{version}.dist-info

%changelog
