#
# spec file for package python-process-tests
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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
Name:           python-process-tests
Version:        2.1.2
Release:        0
Summary:        Tools for testing processes
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-process-tests
Source:         https://files.pythonhosted.org/packages/source/p/process-tests/process-tests-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Testcase classes and assertions for testing processes.

%prep
%setup -q -n process-tests-%{version}
dos2unix LICENSE src/process_tests.egg-info/dependency_links.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/process_tests.py*
%{python_sitelib}/process_tests-%{version}-py%{python_version}.egg-info

%changelog
