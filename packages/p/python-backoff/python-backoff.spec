#
# spec file for package python-backoff
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
Name:           python-backoff
Version:        1.8.0
Release:        0
Summary:        Function decoration for backoff and retry
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/litl/backoff
Source0:        https://files.pythonhosted.org/packages/source/b/backoff/backoff-%{version}.tar.gz
# https://github.com/litl/backoff/issues/75
# github repo does not have setup.py
Source1:        tests.tar.bz2
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
This module provides function decorators which can be used to wrap a
function such that it will be retried until some condition is met. It
is meant to be of use when accessing unreliable resources with the
potential for intermittent failures i.e. network resources and external
APIs. Somewhat more generally, it may also be of use for dynamically
polling resources for externally generated content.

Decorators support both regular functions for synchronous code and
`asyncio <https://docs.python.org/3/library/asyncio.html>`_'s coroutines
for asynchronous code.

%prep
%setup -q -n backoff-%{version} -a1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# will not work with python 2.7
rm -r tests/python35
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
