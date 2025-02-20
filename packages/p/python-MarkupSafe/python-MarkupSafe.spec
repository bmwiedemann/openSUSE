#
# spec file for package python-MarkupSafe
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-MarkupSafe%{psuffix}
Version:        2.1.5
Release:        0
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pallets/markupsafe
Source:         https://files.pythonhosted.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base >= 3.6
%if %{with test}
BuildRequires:  %{python_module MarkupSafe >= %{version}}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
Implements a unicode subclass that supports HTML strings. This can be used to
safely encode strings for dynamically generated web pages.

%prep
%autosetup -p1 -n MarkupSafe-%{version}

# Upstream changed the Python package metadata to require Python 3.7, but the tests pass on Python 3.6.
sed -i -e '/^python_requires =/s/3\.7/3\.6/' setup.cfg

%build
%if !%{with test}
export CFLAGS="%{optflags}"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/markupsafe/_speedups.c
%endif

%if %{with test}
%check
%pytest_arch
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.rst
%doc README.rst docs/
%{python_sitearch}/markupsafe/
%{python_sitearch}/MarkupSafe-%{version}.dist-info
%endif

%changelog
