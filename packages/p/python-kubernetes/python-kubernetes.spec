#
# spec file for package python-kubernetes
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        37.0.1
Release:        0
Summary:        Kubernetes python client
License:        Apache-2.0
URL:            https://github.com/kubernetes-client/python
# Source tar - https://pypi.org/project/kubernetes/#files
Source:         https://files.pythonhosted.org/packages/source/k/kubernetes/kubernetes-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 6.0.3}
BuildRequires:  %{python_module certifi >= 2026.7.22}
BuildRequires:  %{python_module durationpy >= 0.11}
BuildRequires:  %{python_module google-auth >= 1.0.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 2.13.5}
BuildRequires:  %{python_module python-dateutil >= 2.8.2}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 84.0.0}
BuildRequires:  %{python_module typing-extensions >= 4.16.0}
BuildRequires:  %{python_module urllib3 >= 2.8.0}
BuildRequires:  %{python_module websocket-client >= 0.32.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildConflicts: %{python_module websocket-client = 0.40.0}
BuildConflicts: %{python_module websocket-client = 0.41.0}
BuildConflicts: %{python_module websocket-client = 0.41.1}
Requires:       python-PyYAML >= 6.0.3
Requires:       python-certifi >= 2026.7.22
Requires:       python-durationpy >= 0.11
Requires:       python-google-auth >= 1.0.1
Requires:       python-oauthlib
Requires:       python-pydantic >= 2.13.5
Requires:       python-python-dateutil >= 2.8.2
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-typing-extensions >= 4.16.0
Requires:       python-urllib3 >= 2.8.0
Requires:       python-websocket-client >= 0.32.0
Conflicts:      python-websocket-client = 0.40.0
Conflicts:      python-websocket-client = 0.41.0
Conflicts:      python-websocket-client = 0.41.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python client for kubernetes http://kubernetes.io/

%prep
%setup -q -n kubernetes-%{version}

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
# kubernetes.aio is not shipped by setup.py (absent from packages=),
# so its tests, which need the aiohttp stack, are not run either
rm -rf kubernetes/aio
cat kubernetes/config/exec_provider_test.py
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/kubernetes
%{python_sitelib}/kubernetes-%{version}*-info

%changelog
