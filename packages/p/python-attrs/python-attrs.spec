#
# spec file
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%global skip_python36 1
Name:           python-attrs%{psuffix}
Version:        22.2.0
Release:        0
Summary:        Attributes without boilerplate
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hynek/attrs/
Source:         https://files.pythonhosted.org/packages/source/a/attrs/attrs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Pympler}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
%endif
%python_subpackages

%description
attrs is an MIT-licensed Python package with class decorators that ease the
chores of implementing the most common attribute-related object protocols.

You just specify the attributes to work with and attrs gives you:
  - a nice human-readable __repr__,
  - a complete set of comparison methods,
  - an initializer,
  - and much more

without writing dull boilerplate code again and again.

This gives you the power to use actual classes with actual types in your code
instead of confusing tuples or confusingly behaving namedtuples.

So put down that type-less data structures and welcome some class into your
life!

python-attrs is the successor to python-characterstic

%prep
%setup -q -n attrs-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitelib}/attr*
%{python_sitelib}/attrs-%{version}-py*.egg-info
%endif

%changelog
