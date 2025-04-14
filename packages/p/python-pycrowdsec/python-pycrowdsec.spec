#
# spec file for package python-pycrowdsec
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


%define         _modname pycrowdsec
Name:           python-pycrowdsec
Version:        0.0.5
Release:        0
Summary:        Python bouncer and clients for crowdsec
License:        MIT
URL:            https://github.com/crowdsecurity/pycrowdsec
Source:         https://files.pythonhosted.org/packages/source/p/pycrowdsec/pycrowdsec-%{version}.tar.gz
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-dotenv}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-requests
Suggests:       python-geoip2
BuildArch:      noarch
%python_subpackages

%description
Python bouncer and clients for crowdsec

%prep
%autosetup -p1 -n %{_modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# python-redislite is abandoned
# mtls tests needs docker
%pytest tests --ignore "tests/test_redis_integration.py" --ignore "tests/test_mtls.py"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{_modname}
%{python_sitelib}/%{_modname}-%{version}.dist-info
%pycache_only %{python_sitelib}/%{_modname}/__pycache__

%changelog
