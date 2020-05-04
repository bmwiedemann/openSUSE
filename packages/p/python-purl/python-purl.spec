#
# spec file for package python-purl
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-purl
Version:        1.5
Release:        0
Summary:        An immutable URL class for URL building and manipulation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/codeinthehole/purl
Source:         https://github.com/codeinthehole/purl/archive/%{version}.tar.gz
# https://github.com/codeinthehole/purl/pull/42
Patch0:         use_pytest.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
An immutable URL class for URL building and manipulation.

%prep
%setup -q -n purl-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/utils_tests.py tests/expansion_tests.py tests/template_tests.py  tests/url_tests.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
