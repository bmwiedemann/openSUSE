#
# spec file for package python-clikit
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-clikit
Version:        0.6.2
Release:        0
Summary:        Helper to build testable command line interfaces
License:        MIT
URL:            https://github.com/sdispater/clikit
Source:         %{URL}/archive/%{version}.tar.gz#/clikit-%{version}.tar.gz
BuildRequires:  %{python_module crashtest}
BuildRequires:  %{python_module pastel >= 0.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pylev >= 1.3}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-mock >= 2.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-crashtest
Requires:       python-pastel >= 0.2.0
Requires:       python-pylev >= 1.3
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34 >= 1.1
%endif
%ifpython2
Requires:       python-enum34 >= 1.1
%endif
%python_subpackages

%description
CliKit is a group of utilities to build beautiful and testable
command line interfaces.

%prep
%setup -q -n clikit-%{version}

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
%{python_sitelib}/clikit
%{python_sitelib}/clikit-%{version}.dist-info

%changelog
