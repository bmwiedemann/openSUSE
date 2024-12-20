#
# spec file for package python-zeep
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


Name:           python-zeep
Version:        4.3.1
Release:        0
Summary:        A Python SOAP client based on lxml/requests
License:        MIT
URL:            http://docs.python-zeep.org
Source:         https://files.pythonhosted.org/packages/source/z/zeep/zeep-%{version}.tar.gz
# PATCH-FIX-OPENSUSE xfail tests that require network access
Patch0:         xfail-network-tests.patch
# PATCH-FIX-UPSTREAM gh#mvantellingen/python-zeep#1447
Patch1:         support-new-httpx.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.2.0
Requires:       python-isodate >= 0.5.4
Requires:       python-lxml >= 4.6.0
Requires:       python-platformdirs >= 1.4.0
Requires:       python-pytz
Requires:       python-requests >= 2.7.0
Requires:       python-requests-file >= 1.5.1
Requires:       python-requests-toolbelt >= 0.7.1
Recommends:     python-httpx >= 0.15.0
Recommends:     python-packaging
Recommends:     python-xmlsec >= 0.6.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module platformdirs >= 1.4.0}
BuildRequires:  %{python_module aiohttp >= 1.0}
BuildRequires:  %{python_module aioresponses >= 0.4.1}
BuildRequires:  %{python_module attrs >= 17.2.0}
BuildRequires:  %{python_module freezegun >= 0.3.15}
BuildRequires:  %{python_module isodate >= 0.5.4}
BuildRequires:  %{python_module lxml >= 4.6.0}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pretend >= 1.0.9}
BuildRequires:  %{python_module pytest >= 6.0.1}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpx}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module requests-file >= 1.5.1}
BuildRequires:  %{python_module requests-mock >= 0.7.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.7.1}
BuildRequires:  %{python_module xmlsec >= 0.6.1}
BuildRequires:  libxmlsec1-openssl1
# /SECTION
%python_subpackages

%description
Python SOAP client based on python-lxml and python-requests

%prep
%autosetup -p1 -n zeep-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest tests

%files %{python_files}
%doc CHANGES README.md
%license LICENSE
%{python_sitelib}/zeep
%{python_sitelib}/zeep-%{version}.dist-info

%changelog
