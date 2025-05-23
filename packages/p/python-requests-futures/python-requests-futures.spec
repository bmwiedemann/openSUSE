#
# spec file for package python-requests-futures
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
Name:           python-requests-futures
Version:        1.0.2
Release:        0
Summary:        Asynchronous Python HTTP Requests for Humans using Futures
License:        Apache-2.0
URL:            https://github.com/ross/requests-futures
Source:         https://files.pythonhosted.org/packages/source/r/requests-futures/requests_futures-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.6.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.31.0
BuildArch:      noarch
%python_subpackages

%description
Small add-on for the python requests_ http library. Makes use of python 3.2’s
concurrent.futures or the backport for prior versions of python.

%prep
%setup -q -n requests_futures-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests on http://httpbin.org
# %%python_exec -m unittest test_requests_futures

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/requests_futures
%{python_sitelib}/requests[_-]futures-%{version}.dist-info

%changelog
