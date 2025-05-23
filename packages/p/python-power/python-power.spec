#
# spec file for package python-power
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


Name:           python-power
Version:        1.4
Release:        0
Summary:        System power status information in Python
License:        MIT
URL:            https://github.com/Kentzo/Power
Source:         https://files.pythonhosted.org/packages/source/p/power/power-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python module that allows you to get power and battery status of the system.

%prep
%setup -q -n power-%{version}
rm power/darwin.py power/freebsd.py power/win32.py
mkdir tests
mv power/tests.py tests/

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests.py can be run directly, but those tests expect user to alter power state during tests
cd tests
%pyunittest tests

%files %{python_files}
%{python_sitelib}/power/
%{python_sitelib}/power-%{version}.dist-info

%changelog
