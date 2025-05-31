#
# spec file for package python-kismet-rest
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
%define pkg_version 2019.5.2
Name:           python-kismet-rest
Version:        2019.05.02
Release:        0
Summary:        Python wrapper for the Kismet REST interface
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://www.kismetwireless.net
Source:         https://github.com/kismetwireless/python-kismet-rest/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
#BuildRequires:  %%{python_module requests}
#BuildRequires:  %%{python_module pytest}
# /SECTION
%python_subpackages

%description
Simplified Python API for the Kismet REST interface.

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are disabled for now since those need a docker environment for testing
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/kismet[-_]rest
%{python_sitelib}/kismet[-_]rest-%{pkg_version}*-info

%changelog
