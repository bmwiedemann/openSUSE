#
# spec file for package python-requests-futures
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         short_name requests-futures
Name:           python-%{short_name}
Version:        1.0.0
Release:        0
Summary:        Asynchronous Python HTTP Requests for Humans using Futures
License:        Apache-2.0
URL:            https://github.com/ross/%{short_name}
Source:         https://files.pythonhosted.org/packages/source/r/%{short_name}/%{short_name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.6.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 1.2.0
BuildArch:      noarch
%ifpython2
Requires:       python-futures >= 2.1.3
%endif
%python_subpackages

%description
Small add-on for the python requests_ http library. Makes use of python 3.2’s
concurrent.futures or the backport for prior versions of python.

%prep
%setup -q -n %{short_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online tests on http://httpbin.org
# %%python_exec -m unittest test_requests_futures

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
