#
# spec file for package python-pytest-attrib
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


Name:           python-pytest-attrib
Version:        0.1.3
Release:        0
Summary:        Pytest plugin to select tests based on attributes
License:        MIT
URL:            http://pypi.python.org/pypi/pytest-attrib/
Source:         https://github.com/AbdealiJK/pytest-attrib/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  %{python_module pytest >= 2.2}
# /SECTION
Requires:       python-pytest >= 2.2
BuildArch:      noarch

%python_subpackages

%description
The pytest-attrib plugin extends py.test with the ability to select tests
based on a criteria rather than just the filename or pytest.marks. For
example, you might want to run only tests that need internet connectivity,
or tests that are slow.

The pytest.mark  plugin already provides a featrure to mark tests and run
only the marked tests. This plugin also allows to run expressions on the
attributes of the class, and does not require the pytest.mark decorator.

It offers features similar to the nose plugin nose-attrib.

%prep
%autosetup -p1 -n pytest-attrib-%{version}
rm setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/pytest_attrib

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_attrib
%{python_sitelib}/pytest_attrib-%{version}.dist-info

%changelog
