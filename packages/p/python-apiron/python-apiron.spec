#
# spec file for package python-apiron
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2022 Dr. Axel Braun <DocB@opensuse.org>
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


%{?sle15_python_module_pythons}
Name:           python-apiron
Version:        8.0.0.post1
Release:        0
Summary:        Apiron helps you cook a tasty client for RESTful APIs
License:        MIT
URL:            https://github.com/ithaka/apiron
Source:         https://files.pythonhosted.org/packages/source/a/apiron/apiron-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.11.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.11.1
BuildArch:      noarch
%python_subpackages

%description
Gathering data from multiple services has become a ubiquitous task for web application developers. The complexity can grow quickly: calling an API endpoint with multiple parameter sets, calling multiple API endpoints, calling multiple endpoints in multiple APIs. While the business logic can get hairy, the code to interact with those APIs doesn't have to.

apiron provides declarative, structured configuration of services and endpoints with a unified interface for interacting with them.

%prep
%setup -q -n apiron-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# TestEndpoint.test_call - online test
%pytest -k 'not test_call'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/apiron
%{python_sitelib}/apiron-%{version}.dist-info

%changelog
