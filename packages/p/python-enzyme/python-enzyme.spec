#
# spec file for package python-enzyme
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-enzyme
Version:        0.4.1
Release:        0
Summary:        Python video metadata parser
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Diaoul/enzyme
Source0:        https://files.pythonhosted.org/packages/source/e/enzyme/enzyme-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Enzyme is a Python module to parse video metadata.

%prep
%setup -q -n enzyme-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests only

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/enzyme
%{python_sitelib}/enzyme-%{version}-py%{py_ver}.egg-info

%changelog
