#
# spec file for package python-openapi-core
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
Name:           python-openapi-core
Version:        0.12.0
Release:        0
Summary:        Adds client-side and server-side support for the oas3
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/p1c2u/openapi-core
Source:         https://github.com/p1c2u/openapi-core/archive/%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module lazy-object-proxy}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module openapi-spec-validator}
BuildRequires:  %{python_module pytest < 5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module strict-rfc3339}
BuildRequires:  fdupes
BuildRequires:  python-backports.functools_lru_cache
BuildRequires:  python-backports.functools_partialmethod
BuildRequires:  python-enum34
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-isodate
Requires:       python-lazy-object-proxy
Requires:       python-openapi-spec-validator
Requires:       python-six
Requires:       python-strict-rfc3339
BuildArch:      noarch
%ifpython2
Requires:       python-backports.functools_lru_cache
Requires:       python-backports.functools_partialmethod
Requires:       python-enum34
%endif
%python_subpackages

%description
Openapi-core is a Python library that adds client-side
and server-side support for the OpenAPI Specification
v3.0.0.

%prep
%setup -q -n openapi-core-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest tests/unit

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
