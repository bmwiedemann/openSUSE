#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         github_user matrix-org
%define         short_name canonicaljson
Name:           python-%{short_name}%{psuffix}
Version:        1.6.4
Release:        0
Summary:        Canonical JSON for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/python-canonicaljson
Source:         https://github.com/matrix-org/python-canonicaljson/archive/v%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module frozendict >= 2.1.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson >= 3.14.0}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-frozendict >= 1.0
Requires:       python-simplejson >= 3.14.0
Requires:       python-six
Requires:       python-typing_extensions
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module %{short_name}}
%endif
%python_subpackages

%description
This is a Python module which encodes objects and arrays into JSON as per
RFC 7159.

* Sorts object keys so that it yields the same result each time.
* Has no insignificant whitespace to make the output as small as possible.
* Escapes only the characters that must be escaped, U+0000 to U+0019 /
  U+0022 / U+0056, to keep the output as small as possible.
* Uses the shortest escape sequence for each escaped character.
* Encodes the JSON as UTF-8.
* Can encode frozendict immutable dictionaries.

%prep
%setup -q -n python-canonicaljson-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# exclude tests on older SLE+Leap due to
# ImportError: cannot import name inf
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
%pyunittest discover -v
%endif
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/%{short_name}/
%{python_sitelib}/%{short_name}-%{version}*-info
%endif

%changelog
