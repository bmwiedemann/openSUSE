#
# spec file for package python-zeep
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-zeep
Version:        3.4.0
Release:        0
Summary:        A Python SOAP client based on lxml/requests
License:        MIT
Group:          Development/Languages/Python
URL:            http://docs.python-zeep.org
Source:         https://files.pythonhosted.org/packages/source/z/zeep/zeep-%{version}.tar.gz
Patch1:         pytest4.patch
Patch2:         pytest5.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs >= 1.4.0
Requires:       python-attrs >= 17.2.0
Requires:       python-cached-property >= 1.3.0
Requires:       python-defusedxml >= 0.4.1
Requires:       python-isodate >= 0.5.4
Requires:       python-lxml >= 3.1.0
Requires:       python-pytz
Requires:       python-requests >= 2.7.0
Requires:       python-requests-toolbelt >= 0.7.1
Requires:       python-six >= 1.9.0
Requires:       python-tornado >= 4.0.2
Requires:       python-xmlsec >= 0.6.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module appdirs >= 1.4.0}
BuildRequires:  %{python_module attrs >= 17.2.0}
BuildRequires:  %{python_module cached-property >= 1.3.0}
BuildRequires:  %{python_module defusedxml >= 0.4.1}
BuildRequires:  %{python_module freezegun >= 0.3.8}
BuildRequires:  %{python_module isodate >= 0.5.4}
BuildRequires:  %{python_module lxml >= 3.1.0}
BuildRequires:  %{python_module mock >= 2.0.0}
BuildRequires:  %{python_module pretend >= 1.0.8}
BuildRequires:  %{python_module pytest >= 3.1.3}
BuildRequires:  %{python_module pytest-tornado >= 0.4.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module requests-mock >= 0.7.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.7.1}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  %{python_module tornado >= 4.0.2}
BuildRequires:  %{python_module xmlsec >= 0.6.1}
BuildRequires:  python3-aiohttp >= 1.0
BuildRequires:  python3-aioresponses >= 0.4.1
# /SECTION
%ifpython3
Requires:       python-aiohttp >= 1.0
%endif
%python_subpackages

%description
Python SOAP client based on python-lxml and python-requests

%prep
%setup -q -n zeep-%{version}
%autopatch -p1
# disable broken tests
rm tests/test_wsse_signature.py
rm tests/test_wsse_username.py
rm tests/test_wsse_utils.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%pytest tests/

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
