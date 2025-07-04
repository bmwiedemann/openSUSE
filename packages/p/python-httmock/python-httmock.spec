#
# spec file for package python-httmock
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


Name:           python-httmock
Version:        1.4.0
Release:        0
Summary:        A mocking library for requests
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/patrys/httmock
Source:         https://github.com/patrys/httmock/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 1.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module requests >= 1.0.0}
# /SECTION
%python_subpackages

%description
A mocking library for requests.

You can use it to mock third-party APIs and test libraries that use
`requests` internally, conditionally using mocked replies with the
`urlmatch` decorator.

%prep
%setup -q -n httmock-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/httmock.py
%{python_sitelib}/httmock-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/httmock*

%changelog
