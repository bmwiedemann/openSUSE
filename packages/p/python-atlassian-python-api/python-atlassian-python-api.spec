#
# spec file for package python-atlassian-python-api
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


Name:           python-atlassian-python-api
Version:        3.41.4
Release:        0
Summary:        Python Atlassian REST API Wrapper
License:        Apache-2.0
URL:            https://github.com/atlassian-api/atlassian-python-api
Source:         https://files.pythonhosted.org/packages/source/a/atlassian-python-api/atlassian-python-api-%{version}.tar.gz
Source1:        python-atlassian-python-api.rpmlintrc
BuildRequires:  %{python_module deprecated}
BuildRequires:  %{python_module kerberos}
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-deprecated
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
%autosetup -p1 -n atlassian-python-api-%{version}

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
%{python_sitelib}/atlassian
%{python_sitelib}/atlassian_python_api*-info

%changelog
