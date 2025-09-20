#
# spec file for package python-pycares
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


%{?sle15_python_module_pythons}
Name:           python-pycares
Version:        4.11.0
Release:        0
Summary:        Python interface for c-ares
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/saghul/pycares
Source0:        https://files.pythonhosted.org/packages/source/p/pycares/pycares-%{version}.tar.gz
Source99:       python-pycares.rpmlintrc
# PATCH-FIX-UPSTREAM cleanup_tests.patch bsc#[0-9]+ mcepl@suse.com
# Make the test suite slightly more normal
Patch0:         cleanup_tests.patch
BuildRequires:  %{python_module cffi}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  c-ares-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
Requires:       python-cffi
Recommends:     python-idna
%python_subpackages

%description
pycares is a Python module which provides an interface to
c-ares. c-ares is a C library that performs DNS requests and name
resolutions asynchronously

%prep
%autosetup -p1 -n pycares-%{version}

%build
export PYCARES_USE_SYSTEM_LIB=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Test suite is broken anywhere else outside of the upstream CI,
# and upstream doesn't care.
# %%pyunittest_arch -v tests.tests

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitearch}/pycares
%{python_sitearch}/pycares-%{version}*-info

%changelog
