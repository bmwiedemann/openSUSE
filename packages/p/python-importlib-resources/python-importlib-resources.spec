#
# spec file for package python-importlib-resources
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


%{?sle15_python_module_pythons}
Name:           python-importlib-resources
Version:        6.5.2
Release:        0
Summary:        Read resources from Python packages
License:        Apache-2.0
URL:            https://importlib-resources.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/i/importlib_resources/importlib_resources-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module jaraco.test >= 5.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testsuite}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zipp >= 3.1.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-importlib_resources = %{version}
Obsoletes:      python-importlib_resources < %{version}
BuildArch:      noarch
%if 0%{python_version_nodots} < 310
Requires:       python-zipp >= 3.1.0
%endif
%python_subpackages

%description
importlib_resources is a library which provides for access to resources in
Python packages. It provides functionality similar to pkg_resources Basic
Resource Access API, but without all of the overhead and performance problems
of pkg_resources.

In our terminology, a resource is a file tree that is located alongside an
importable Python module. Resources can live on the file system or in a zip
file, with support for other loader classes that implement the appropriate API
for reading resources.

importlib_resources supplies a backport of importlib.resources, enabling early
access to features of future Python versions and making functionality available
for older Python versions. Users are encouraged to use the Python standard
library where suitable and fall back to this library for future compatibility.
Developers looking for detailed API descriptions should refer to the standard
library documentation.

%prep
%setup -q -n importlib_resources-%{version}

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
%{python_sitelib}/importlib_resources
%{python_sitelib}/importlib_resources-%{version}.dist-info

%changelog
