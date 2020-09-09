#
# spec file for package python-canonicaljson
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.4.0
Release:        0
Summary:        Canonical JSON for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/python-canonicaljson
Source:         https://github.com/matrix-org/python-canonicaljson/archive/v%{version}.tar.gz
BuildRequires:  %{python_module frozendict >= 1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module simplejson >= 3.14.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-frozendict >= 1.0
Requires:       python-simplejson >= 3.14.0
Requires:       python-six
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
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
%python_exec -m unittest discover
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*
%endif

%changelog
