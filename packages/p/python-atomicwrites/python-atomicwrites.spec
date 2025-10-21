#
# spec file for package python-atomicwrites
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%if "%{flavor}" == "doc"
%define psuffix -doc
%bcond_without doc
%else
%define psuffix %{nil}
%bcond_with doc
%endif

%{?sle15_python_module_pythons}
Name:           python-atomicwrites%{psuffix}
Version:        1.4.1
Release:        0
Summary:        Atomic file writes for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/untitaker/python-atomicwrites
Source:         https://files.pythonhosted.org/packages/source/a/atomicwrites/atomicwrites-%{version}.tar.gz
# PATCH-FIX-OPENSUSE sphinx8.patch -- daniel.garcia@suse.com
Patch0:         sphinx8.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with doc}
BuildRequires:  %{modern_python}-Sphinx
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Atomic file writes for python3.
Features that distinguish it from other similar libraries:

- Race-free assertion that the target file doesn't yet exist. This can be
  controlled with the 'overwrite' parameter.

- High-level API that wraps a very flexible class-based API.

%prep
%autosetup -p1 -n atomicwrites-%{version}
rm -rf atomicwrites.egg-info

%build
%if %{without doc}
%pyproject_wheel
%else
pushd docs
make html
rm _build/html/.buildinfo
popd
%endif

%install
%if %{without doc}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with doc}
%pytest
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%if %{without doc}
%{python_sitelib}/atomicwrites
%{python_sitelib}/atomicwrites-%{version}.dist-info
%else
%doc docs/_build/html
%endif

%changelog
