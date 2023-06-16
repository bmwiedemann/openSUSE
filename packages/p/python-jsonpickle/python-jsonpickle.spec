#
# spec file for package python-jsonpickle
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


%{?sle15_python_module_pythons}
Name:           python-jsonpickle
Version:        3.0.1
Release:        0
Summary:        Python library for serializing any arbitrary object graph into JSON
License:        BSD-3-Clause
URL:            https://github.com/jsonpickle/jsonpickle
Source:         https://files.pythonhosted.org/packages/source/j/jsonpickle/jsonpickle-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/jsonpickle/jsonpickle/commit/a24240bfdec6a9d5172c2f25e19654d23ffc61e1 Implement compatibility with pandas 2
Patch:          pandas2.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-simplejson
Suggests:       python-ujson
Suggests:       python-numpy
Suggests:       python-pandas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module gmpy2}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module ujson}
# /SECTION
%python_subpackages

%description
Python library for serializing any arbitrary object graph into JSON.
It can take almost any Python object and turn the object into JSON.
Additionally, it can reconstitute the object back into Python.

%prep
%autosetup -p1 -n jsonpickle-%{version}
sed -i 's/ --cov//' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_multindex_dataframe_roundtrip is flaky on i586
%pytest -ra -k "not test_multindex_dataframe_roundtrip"

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.rst
%{python_sitelib}/jsonpickle
%{python_sitelib}/jsonpickle-%{version}*-info

%changelog
