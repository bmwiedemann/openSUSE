#
# spec file for package python-fake-useragent
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
Name:           python-fake-useragent
Version:        2.1.0
Release:        0
Summary:        Useragent faker package for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/fake-useragent/fake-useragent
Source:         https://github.com/fake-useragent/fake-useragent/archive/refs/tags/%{version}.tar.gz#/fake-useragent-%{version}.tar.gz
BuildRequires:  %{python_module base > 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{python_version_nodots} < 310
Requires:       python-importlib-resources > 6.0.0
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module importlib-resources >= 6.0.0 if %python-base < 3.10}
BuildRequires:  %{python_module pytest >= 7.4.0}
# /SECTION
%python_subpackages

%description
Useragent faker with real world database.

%prep
%setup -q -n fake-useragent-%{version}
rm pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# NOTE: disable "test_utils_load_pkg_resource_fallback" test case as it is
# testing using pkg_resource, which conflicts with setuptools.
# See https://github.com/pypa/setuptools/issues/4487
%pytest -k "(not test_utils_load_pkg_resource_fallback)"

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/fake_useragent
%{python_sitelib}/fake_useragent-%{version}.dist-info

%changelog
