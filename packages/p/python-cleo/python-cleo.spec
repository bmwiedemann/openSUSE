#
# spec file for package python-cleo
#
# Copyright (c) 2022 SUSE LLC
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


%define pyversion 1.0.0a5
Name:           python-cleo
Version:        1.0.0~a5
Release:        0
Summary:        Python module for creating testable command-line interfaces
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sdispater/cleo
Source:         https://github.com/sdispater/cleo/archive/%{pyversion}.tar.gz#/cleo-%{pyversion}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module crashtest >= 0.3.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pylev >= 1.3}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-crashtest >= 0.3.1
Requires:       python-pylev >= 1.3
BuildArch:      noarch
%python_subpackages

%description
Cleo allows creating testable command-line interfaces.

%prep
%setup -q -n cleo-%{pyversion}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cleo
%{python_sitelib}/cleo-%{pyversion}*info

%changelog
