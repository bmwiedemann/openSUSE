#
# spec file for package python-unittest-xml-reporting
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-unittest-xml-reporting
Version:        3.0.2
Release:        0
Summary:        PyUnit-based test runner with JUnit like XML reporting
License:        LGPL-3.0-or-later
URL:            https://github.com/xmlrunner/unittest-xml-reporting
Source:         https://github.com/xmlrunner/unittest-xml-reporting/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-311.patch gh#xmlrunner/unittest-xml-reporting#274
Patch0:         python-311.patch
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-xmlrunner = %{version}
BuildArch:      noarch
%python_subpackages

%description
unittest-xml-reporting is a unittest test runner that can save test results
to XML files that can be consumed by a wide range of tools, such as build
systems, IDEs and continuous integration servers.

%prep
%autosetup -p1 -n unittest-xml-reporting-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#xmlrunner/unittest-xml-reporting#205
%pytest -k 'not test_xmlrunner_non_ascii'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/xmlrunner
%{python_sitelib}/unittest_xml_reporting-%{version}*-info

%changelog
