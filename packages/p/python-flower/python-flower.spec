#
# spec file for package python-flower
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


Name:           python-flower
Version:        2.0.1
Release:        0
Summary:        A web frontend for monitoring and administrating Celery clusters
License:        BSD-3-Clause
URL:            https://github.com/mher/flower
Source:         https://files.pythonhosted.org/packages/source/f/flower/flower-%{version}.tar.gz
BuildRequires:  %{python_module celery >= 5.0.0}
BuildRequires:  %{python_module humanize}
BuildRequires:  %{python_module kombu}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module prometheus_client >= 0.8.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tornado >= 5.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-celery >= 5.0.0
Requires:       python-humanize
Requires:       python-prometheus_client >= 0.8.0
Requires:       python-pytz
Requires:       python-tornado >= 5.0.0
BuildArch:      noarch
%python_subpackages

%description
Flower is a web based tool for monitoring and administrating Celery clusters.

%prep
%autosetup -p1 -n flower-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/flower
%{python_sitelib}/flower-%{version}.dist-info

%changelog
