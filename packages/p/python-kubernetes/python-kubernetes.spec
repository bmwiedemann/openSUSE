#
# spec file for package python-kubernetes
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-kubernetes
Version:        24.2.0
Release:        0
Summary:        Kubernetes python client
License:        Apache-2.0
URL:            https://github.com/kubernetes-incubator/client-python
Source:         https://files.pythonhosted.org/packages/source/k/kubernetes/kubernetes-%{version}.tar.gz
# https://github.com/kubernetes-client/python/issues/1790
Patch0:         python-kubernetes-no-mock.patch
BuildRequires:  %{python_module PyYAML >= 5.4.1}
BuildRequires:  %{python_module certifi >= 14.05.14}
BuildRequires:  %{python_module google-auth >= 1.0.1}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.5.3}
BuildRequires:  %{python_module recommonmark}
BuildRequires:  %{python_module requests-oauthlib}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 21.0.0}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module urllib3 >= 1.23}
BuildRequires:  %{python_module websocket-client >= 0.32.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 5.4.1
Requires:       python-certifi >= 14.05.14
Requires:       python-google-auth >= 1.0.1
Requires:       python-python-dateutil >= 2.5.3
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-setuptools >= 21.0.0
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
%python_build

%install
%python_install
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
%{python_sitelib}/*

%changelog
