#
# spec file for package python-backoff
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-backoff
Version:        2.2.1
Release:        0
Summary:        Function decoration for backoff and retry
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/litl/backoff
Source0:        https://files.pythonhosted.org/packages/source/b/backoff/backoff-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
# /SECTION
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
%setup -q -n backoff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/backoff
%{python_sitelib}/backoff-%{version}.dist-info

%changelog
