#
# spec file for package python-httmock
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
Name:           python-httmock
Version:        1.3.0
Release:        0
Summary:        A mocking library for requests
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/patrys/httmock
Source:         https://github.com/patrys/httmock/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module requests >= 1.0.0}
# /SECTION
Requires:       python-requests >= 1.0.0
BuildArch:      noarch

%python_subpackages

%description
A mocking library for requests.

You can use it to mock third-party APIs and test libraries that use
`requests` internally, conditionally using mocked replies with the
`urlmatch` decorator.

%prep
%setup -q -n httmock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
