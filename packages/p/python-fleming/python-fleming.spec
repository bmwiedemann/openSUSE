#
# spec file for package python-fleming
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


Name:           python-fleming
Version:        0.7.0
Release:        0
Summary:        Manipulate datetime objects relative to time zones
License:        MIT
URL:            https://github.com/ambitioninc/fleming
Source:         https://github.com/ambitioninc/fleming/archive/%{version}.tar.gz#/fleming-%{version}.tar.gz
Patch0:         use-assertequal.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.2
Requires:       python-pytz >= 2013.9
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.2}
BuildRequires:  %{python_module pytz >= 2013.9}
# /SECTION
%python_subpackages

%description
Python helpers for manipulating datetime objects relative to time zones.

%prep
%autosetup -p1 -n fleming-%{version}
mv fleming/tests/ .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/fleming_tests.py

%files %{python_files}
%doc README.rst docs/release_notes.rst
%license LICENSE.rst
%{python_sitelib}/fleming
%{python_sitelib}/fleming-%{version}.dist-info

%changelog
