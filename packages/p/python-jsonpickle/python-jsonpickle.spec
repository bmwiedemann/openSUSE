#
# spec file for package python-jsonpickle
#
# Copyright (c) 2021 SUSE LLC
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
%define modname jsonpickle
%bcond_without python2
%bcond_with ringdisabled
Name:           python-jsonpickle
Version:        2.0.0
Release:        0
Summary:        Python library for serializing any arbitrary object graph into JSON
License:        BSD-3-Clause
URL:            https://github.com/jsonpickle/jsonpickle
Source:         https://files.pythonhosted.org/packages/source/j/jsonpickle/jsonpickle-%{version}.tar.gz
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{python_version_nodots} < 38
Requires:       python-importlib_metadata
%endif
Recommends:     python-simplejson
Suggests:       python-ujson
Suggests:       python-yajl
Suggests:       python-numpy
Suggests:       python-pandas
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module ecdsa}
BuildRequires:  %{python_module pymongo}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module simplejson}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
%if ! 0%{?_with_ringdisabled}
# Test these in a normal devel project or locally, but not when staging with Ring1
BuildRequires:  %{python_module ujson}
BuildRequires:  %{python_module pandas if (%python-base without python36-base)}
BuildRequires:  %{python_module scikit-learn if (%python-base without python36-base)}
%endif
%if %{with python2}
BuildRequires:  python-enum34
BuildRequires:  python-jsonlib
%endif
# /SECTION
%ifpython2
Suggests:       python-enum34
Suggests:       python-jsonlib
%endif
%python_subpackages

%description
Python library for serializing any arbitrary object graph into JSON.
It can take almost any Python object and turn the object into JSON.
Additionally, it can reconstitute the object back into Python.

%prep
%autosetup -p1 -n %{modname}-%{version}
sed -i 's/--flake8 --black --cov//' pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
python36_ignorefiles="--ignore jsonpickle/ext/numpy.py \
                      --ignore jsonpickle/ext/pandas.py"
%pytest -ra ${$python_ignorefiles} %{?_with_ringdisabled:--ignore jsonpickle/ext/pandas.py}

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.rst
%{python_sitelib}/jsonpickle
%{python_sitelib}/jsonpickle-%{version}*-info

%changelog
