#
# spec file for package python-tenacity
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
%bcond_without  python2
Name:           python-tenacity
Version:        6.3.1
Release:        0
Summary:        Python module for retrying code until it succeeeds
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/jd/tenacity
Source:         https://files.pythonhosted.org/packages/source/t/tenacity/tenacity-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module typeguard}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
Recommends:     python-tornado
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python2-futures >= 3.0
BuildRequires:  python2-monotonic >= 0.6
%endif
%ifpython2
Requires:       python-futures >= 3.0
Requires:       python-monotonic >= 0.6
%endif
%python_subpackages

%description
Tenacity is a general-purpose retrying library, written in Python, to simplify
the task of adding retry behavior to just about anything.
It originates from a fork of `Retrying`_
Features
--------
- Generic Decorator API
- Specify stop condition (i.e. limit by number of attempts)
- Specify wait condition (i.e. exponential backoff sleeping between attempts)
- Customize retrying on Exceptions
- Customize retrying on expected returned result

%prep
%setup -q -n tenacity-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --ignore tenacity/tests/test_asyncio.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
