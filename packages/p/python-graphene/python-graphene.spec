#
# spec file for package python-graphene
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-graphene
Version:        3.0.0
Release:        0
Summary:        GraphQL Framework for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/graphql-python/graphene
Source:         https://github.com/graphql-python/graphene/archive/v%{version}.tar.gz#/graphene-%{version}.tar.gz
BuildRequires:  %{python_module aniso8601 >= 8}
BuildRequires:  %{python_module graphql-core >= 3.1.2}
BuildRequires:  %{python_module graphql-relay >= 3.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module promise}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-aniso8601 >= 8
Requires:       python-graphql-core >= 3.1.2
Requires:       python-graphql-relay >= 3.0
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Graphene is a Python library for building GraphQL schemas/types.

%prep
%setup -q -n graphene-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The example depend on snapshottest, which is a bit messy to package as of v0.5.1
# https://github.com/syrusakbary/snapshottest/pull/114

# test_objecttype_as_container_extra_args and test_objecttype_as_container_invalid_kwargs
# have slightly different output on Python 3.10, that the tests do not expect
# https://github.com/graphql-python/graphene/issues/1400
%pytest --ignore examples -k 'not (test_objecttype_as_container_extra_args or test_objecttype_as_container_invalid_kwargs)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*graphene*/

%changelog
