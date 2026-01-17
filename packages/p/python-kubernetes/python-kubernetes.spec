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
Version:        35.0.0
Release:        0
Summary:        Kubernetes python client
License:        Apache-2.0
URL:            https://github.com/kubernetes-client/python
# Source tar - https://pypi.org/project/kubernetes/#files
Source:         https://files.pythonhosted.org/packages/source/k/kubernetes/kubernetes-%{version}.tar.gz
# Patch file to fix failing kubernetes.config.exec_provider_test.ExecProviderTest
# in SLE-15 SP4 (Python 3.6.15, pytest-5.4.3, py-1.10.0, pluggy-0.13.1)
Patch1:         fix-exec-provider-test-sle-15-sp4.patch
BuildRequires:  %{python_module PyYAML >= 5.4.1}
BuildRequires:  %{python_module certifi >= 14.05.14}
BuildRequires:  %{python_module durationpy >= 0.7}
BuildRequires:  %{python_module google-auth >= 1.0.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 21.0.0}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module urllib3 >= 1.24.2}
BuildConflicts: %{python_module urllib3 = 2.6.0}
BuildRequires:  %{python_module websocket-client >= 0.32.0}
BuildConflicts: %{python_module websocket-client = 0.40.0}
BuildConflicts: %{python_module websocket-client = 0.41.0}
BuildConflicts: %{python_module websocket-client = 0.41.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx >= 1.4}
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module pluggy >= 0.3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module recommonmark}
# /SECTION
Requires:       python-oauthlib
Requires:       python-PyYAML >= 5.4.1
Requires:       python-certifi >= 14.05.14
Requires:       python-durationpy >= 0.7
Requires:       python-google-auth >= 1.0.1
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-six >= 1.9.0
Requires:       python-urllib3 >= 1.24.2
Conflicts:      python-urllib3 = 2.6.0
Requires:       python-websocket-client >= 0.32.0
Conflicts:      python-websocket-client = 0.40.0
Conflicts:      python-websocket-client = 0.41.0
Conflicts:      python-websocket-client = 0.41.1
BuildArch:      noarch
%python_subpackages

%description
Python client for kubernetes http://kubernetes.io/

%prep
%setup -q -n kubernetes-%{version}
%if 0%{?sle_version} && 0%{?sle_version} == 150400
%patch -P 1 -p1
%endif

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
cat kubernetes/config/exec_provider_test.py
%pytest

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/kubernetes
%{python_sitelib}/kubernetes-%{version}*-info

%changelog
