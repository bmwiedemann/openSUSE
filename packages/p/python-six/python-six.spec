#
# spec file for package python-six
#
# Copyright (c) 2020 SUSE LLC
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
# This is not only because of dependency of testsuite, but mostly
# because of cyclical dependencies between six and Sphinx.
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif
Name:           python-six%{psuffix}
Version:        1.15.0
Release:        0
Summary:        Python 2 and 3 compatibility utilities
License:        MIT
Group:          Development/Libraries/Python
URL:            http://pypi.python.org/pypi/six/
Source:         https://files.pythonhosted.org/packages/source/s/six/six-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  python3-Sphinx
%endif
%python_subpackages

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python
versions with the goal of writing Python code that is compatible on
both Python versions. See the documentation for more information on
what is provided.

%package -n python-six-doc
Summary:        Documentation files for %{name}
Group:          Documentation/HTML
Provides:       %{python_module six-doc = %{version}}

%description -n python-six-doc
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python
versions with the goal of writing Python code that is compatible on
both Python versions.

This package provides documentation for %{name}.

%prep
%setup -q -n six-%{version}

%build
%python_build
%if %{with test}
cd documentation && make html && rm _build/html/.buildinfo
%endif

%install
%if ! %{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# add the setuptools egg-info directory
%{python_expand rm %{buildroot}%{$python_sitelib}/six-%{version}-py%{$python_version}.egg-info
mkdir -p %{buildroot}%{$python_sitelib}/six-%{version}-py%{$python_version}.egg-info/
cp six.egg-info/* %{buildroot}%{$python_sitelib}/six-%{version}-py%{$python_version}.egg-info/
}
%endif

%check
%if %{with test}
%pytest test_six.py
%endif

%pre
# handle distutils (file) to setuptools transition (directory)
if [ -f %{python_sitelib}/six-*-py%{python_version}.egg-info ]; then
    rm -vf %{python_sitelib}/six-*-py%{python_version}.egg-info
fi

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst CHANGES
%{python_sitelib}/six.py*
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/six-%{version}-py*.egg-info
%else
%files -n python-six-doc
%license LICENSE
%doc documentation/_build/html
%endif

%changelog
