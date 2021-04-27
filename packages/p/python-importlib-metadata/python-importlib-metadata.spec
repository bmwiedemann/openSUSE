#
# spec file for package python-importlib-metadata-test
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-importlib-metadata%{psuffix}
Version:        3.7.2
Release:        0
Summary:        Read metadata from Python packages
License:        Apache-2.0
URL:            http://importlib-metadata.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/i/importlib_metadata/importlib_metadata-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zipp >= 0.5
%if %{python_version_nodots} < 38
Requires:       python-typing_extensions >= 3.6.4
%endif
Provides:       python-importlib_metadata = %{version}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module importlib_resources >= 1.3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyfakefs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zipp >= 0.5}
BuildRequires:  (python3-typing_extensions  >= 3.6.4 if python3-base < 3.8)
BuildRequires:  (python36-typing_extensions  >= 3.6.4 if python36-base)
%endif
%python_subpackages

%description
importlib_metadata is a library which provides an API for accessing an installed
package’s metadata (see PEP 566), such as its entry points or its top-level
name. This functionality intends to replace most uses of pkg_resources entry
point API and metadata API. Along with importlib.resources in Python 3.7 and
newer (backported as importlib_resources for older versions of Python), this can
eliminate the need to use the older and less efficient pkg_resources package.

importlib_metadata is a backport of Python 3.8’s standard library
importlib.metadata module for Python 2.7, and 3.4 through 3.7. Users of Python
3.8 and beyond are encouraged to use the standard library module. When imported
on Python 3.8 and later, importlib_metadata replaces the DistributionFinder
behavior from the stdlib, but leaves the API in tact. Developers looking for
detailed API descriptions should refer to the Python 3.8 standard library
documentation.

%prep
%setup -q -n importlib_metadata-%{version}
# don't import from sourcedir during testing
sed -i -e 's/norecursedirs.*/& importlib_metadata/' pytest.ini

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/importlib_metadata
%{python_sitelib}/importlib_metadata-%{version}*-info
%endif

%changelog
