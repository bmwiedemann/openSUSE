#
# spec file for package python-enzyme
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


Name:           python-enzyme
Version:        0.5.2
Release:        0
Summary:        Python video metadata parser
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/Diaoul/enzyme
Source0:        https://files.pythonhosted.org/packages/source/e/enzyme/enzyme-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Enzyme is a Python module to parse video metadata.

%prep
%autosetup -p1 -n enzyme-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests only

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/enzyme
%{python_sitelib}/enzyme-%{version}.dist-info

%changelog
