#
# spec file for package python-atlassian-python-api
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
Name:           python-atlassian-python-api
Version:        1.17.3
Release:        0
Summary:        Python Atlassian REST API Wrapper
License:        Apache-2.0
URL:            https://github.com/atlassian-api/atlassian-python-api
Source:         https://files.pythonhosted.org/packages/source/a/atlassian-python-api/atlassian-python-api-%{version}.tar.gz
BuildRequires:  %{python_module kerberos}
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-kerberos
Requires:       python-oauthlib
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-six
Suggests:       python-kerberos
BuildArch:      noarch
%python_subpackages

%description
Python Atlassian REST API Wrapper

%prep
%setup -q -n atlassian-python-api-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
