#
# spec file for package python-transaction
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


%{?sle15_python_module_pythons}
Name:           python-transaction
Version:        5.0
Release:        0
Summary:        Transaction management for Python
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/transaction
Source:         https://files.pythonhosted.org/packages/source/t/transaction/transaction-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.interface
BuildArch:      noarch
# SECTION Test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
# /SECTION
%python_subpackages

%description
This package contains a generic transaction implementation for Python. It is
mainly used by the ZODB, though.

Note that the data manager API, transaction.interfaces.IDataManager, is
syntactically simple, but semantically complex. The semantics were not easy to
express in the interface. This could probably use more work. The semantics are
presented in detail through examples of a sample data manager in
transaction.tests.test_SampleDataManager.

%prep
%autosetup -p1 -n transaction-%{version}
rm -rf transaction.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%{python_sitelib}/transaction
%{python_sitelib}/transaction-%{version}.dist-info

%changelog
