#
# spec file for package python-varlink
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


Name:           python-varlink
Version:        31.0.0
Release:        0
Summary:        Python implementation of the Varlink protocol
License:        Apache-2.0
URL:            https://github.com/varlink/python
Source:         https://files.pythonhosted.org/packages/source/v/varlink/varlink-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A varlink implementation for Python.

Varlink is an interface description format and protocol that
makes services accessible to both humans and machines.

%prep
%setup -q -n varlink-%{version}
# py3 only syntax
rm varlink/tests/test_mocks.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/varlink
%{python_sitelib}/varlink-%{version}.dist-info

%changelog
