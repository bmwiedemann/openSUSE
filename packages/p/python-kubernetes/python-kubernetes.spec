#
# spec file for package python-kubernetes
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-kubernetes
Version:        30.1.0
Release:        0
Summary:        Kubernetes python client
License:        Apache-2.0
URL:            https://github.com/kubernetes-client/python
# Source tar - https://pypi.org/project/kubernetes/#files
Source:         https://files.pythonhosted.org/packages/source/k/kubernetes/kubernetes-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.4.1}
BuildRequires:  %{python_module certifi >= 14.05.14}
BuildRequires:  %{python_module google-auth >= 1.0.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 21.0.0}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module urllib3 >= 1.24.2}
BuildRequires:  %{python_module websocket-client >= 0.32.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 1.4}
BuildRequires:  %{python_module pluggy >= 0.3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module recommonmark}
%if 0%{?sle_version} && 0%{?sle_version} > 150400
# Build python-kubernetes with oauthlib >=3.2.2, for sle_version > SLE-15-SP4
BuildRequires:  %{python_module oauthlib >= 3.2.2}
# /SECTION
Requires:       python-oauthlib >= 3.2.2
%endif
Requires:       python-PyYAML >= 5.4.1
Requires:       python-certifi >= 14.05.14
Requires:       python-google-auth >= 1.0.1
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-six >= 1.9.0
Requires:       python-urllib3 >= 1.24.2
Requires:       python-websocket-client >= 0.32.0
BuildArch:      noarch
%python_subpackages

%description
Python client for kubernetes http://kubernetes.io/

%prep
%autosetup -p1 -n kubernetes-%{version}

%build
%if 0%{?sle_version} && 0%{?sle_version} >= 150500
%bcond_without pyproject
%else
%bcond_with pyproject
%endif

%if %{with pyproject}
%pyproject_wheel
%else
%python_build
%endif

%install
%if %{with pyproject}
%pyproject_install
%else
%python_install
%endif
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# quote CONTRIBUTING.md:
# 2. [End to end tests](kubernetes/e2e_test): these are tests that can only be verified with a live kubernetes server.
rm kubernetes/dynamic/test_client.py
rm kubernetes/dynamic/test_discovery.py
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/kubernetes
%{python_sitelib}/kubernetes-%{version}*-info

%changelog
