#
# spec file for package python-reconfigure
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


Name:           python-reconfigure
Version:        0.1.83
Release:        0
Summary:        Python ORM for config files
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/Eugeny/reconfigure
Source:         https://github.com/Eugeny/reconfigure/archive/%{version}.tar.gz#/reconfigure-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module chardet}
# /SECTION
%python_subpackages

%description
Python ORM for config files.

%prep
%autosetup -p1 -n reconfigure-%{version}

printf '[pytest]\npython_files = *_test*.py' > pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest reconfigure/tests/

%files %{python_files}
%doc README.rst
%license docs/LICENSE
%{python_sitelib}/reconfigure
%{python_sitelib}/reconfigure-%{version}*-info

%changelog
