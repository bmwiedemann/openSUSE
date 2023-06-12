#
# spec file for package python-overrides
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


Name:           python-overrides
Version:        7.3.1
Release:        0
Summary:        A decorator to automatically detect mismatch when overriding a method
License:        Apache-2.0
URL:            https://github.com/mkorpela/overrides
Source:         https://files.pythonhosted.org/packages/source/o/overrides/overrides-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A decorator @override that verifies that a method that should override
an inherited method actually does it.

Copies the docstring of the inherited method to the overridden method.

Since signature validation and docstring inheritance are performed on
class creation and not on class instantiation, this library significantly
improves the safety and experience of creating class hierarchies in Python
without significantly impacting performance.
See https://stackoverflow.com/q/1167617 for the initial inspiration for
this library.

%prep
%autosetup -p1 -n overrides-%{version}

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
%{python_sitelib}/overrides
%{python_sitelib}/overrides-%{version}.dist-info

%changelog
