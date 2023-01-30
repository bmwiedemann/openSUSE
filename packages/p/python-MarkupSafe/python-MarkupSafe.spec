#
# spec file for package python-MarkupSafe
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


%define oldpython python
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_without test
Name:           python-MarkupSafe
Version:        2.1.2
Release:        0
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/pallets/markupsafe
Source:         https://files.pythonhosted.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base >= 3.6
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%ifpython2
Provides:       %{oldpython}-markupsafe = %{version}
Obsoletes:      %{oldpython}-markupsafe < %{version}
%endif
%python_subpackages

%description
Implements a unicode subclass that supports HTML strings. This can be used to
safely encode strings for dynamically generated web pages.

%prep
%setup -q -n MarkupSafe-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/markupsafe/_speedups.c
# Upstream changed the Python package metadata to require Python 3.7, but the tests pass on Python 3.6.
%if %python_version_nodots == 36
%python_expand sed 's/Requires-Python: >=3.7/Requires-Python: >=3.6/' -i %{buildroot}%{python_sitearch}/MarkupSafe-%{version}-py3.6.egg-info/PKG-INFO
%endif

%if %{with test}
%check
%pytest_arch
%endif

%files %{python_files}
%license LICENSE.rst
%doc README.rst docs/
%{python_sitearch}/markupsafe/
%{python_sitearch}/MarkupSafe-%{version}-py*.egg-info

%changelog
