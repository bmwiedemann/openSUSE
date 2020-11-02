#
# spec file for package python-cleo
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-cleo
Version:        0.8.1
Release:        0
Summary:        Python module for creating testable command-line interfaces
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sdispater/cleo
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module clikit >= 0.6.0}
BuildRequires:  %{python_module pastel >= 0.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pylev >= 1.3}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-clikit >= 0.6.0
Requires:       python-pastel >= 0.2.0
Requires:       python-pylev >= 1.3
Requires:       python-typing
BuildArch:      noarch
%python_subpackages

%description
Cleo allows creating testable command-line interfaces.

%prep
%setup -q -n cleo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/cleo
%{python_sitelib}/cleo-%{version}*info

%changelog
