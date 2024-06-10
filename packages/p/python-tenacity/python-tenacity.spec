#
# spec file for package python-tenacity
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-tenacity
Version:        8.3.0
Release:        0
Summary:        Python module for retrying code until it succeeeds
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/jd/tenacity
Source:         https://files.pythonhosted.org/packages/source/t/tenacity/tenacity-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module typeguard}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-tornado
BuildArch:      noarch
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --ignore tenacity/tests/test_asyncio.py -k 'not test_retry_type_annotations'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tenacity
%{python_sitelib}/tenacity-%{version}.dist-info

%changelog
