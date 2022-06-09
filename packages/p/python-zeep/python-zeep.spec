#
# spec file for package python-zeep
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


%define skip_python2 1
Name:           python-zeep
Version:        4.1.0
Release:        0
Summary:        A Python SOAP client based on lxml/requests
License:        MIT
Group:          Development/Languages/Python
URL:            http://docs.python-zeep.org
Source:         https://files.pythonhosted.org/packages/source/z/zeep/zeep-%{version}.tar.gz
Patch1:         httpx-test.patch
# https://github.com/mvantellingen/python-zeep/commit/1ddd118956870f9c68a24c9494207dc17441b416
Patch2:         python-zeep-no-mock.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 17.2.0
Requires:       python-cached-property >= 1.3.0
Requires:       python-isodate >= 0.5.4
Requires:       python-lxml >= 4.6.0
Requires:       python-platformdirs >= 1.4.0
Requires:       python-pytz
Requires:       python-requests >= 2.7.0
Requires:       python-requests-file >= 1.5.1
Requires:       python-requests-toolbelt >= 0.7.1
Recommends:     python-xmlsec >= 0.6.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module platformdirs >= 1.4.0}
BuildRequires:  %{python_module aiohttp >= 1.0}
BuildRequires:  %{python_module aioresponses >= 0.4.1}
BuildRequires:  %{python_module attrs >= 17.2.0}
BuildRequires:  %{python_module cached-property >= 1.3.0}
BuildRequires:  %{python_module freezegun >= 0.3.15}
BuildRequires:  %{python_module isodate >= 0.5.4}
BuildRequires:  %{python_module lxml >= 4.6.0}
BuildRequires:  %{python_module pretend >= 1.0.9}
BuildRequires:  %{python_module pytest >= 6.0.1}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpx}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module requests-file >= 1.5.1}
BuildRequires:  %{python_module requests-mock >= 0.7.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.7.1}
# gh#mehcode/python-xmlsec#204
BuildRequires:  %{python_module xmlsec >= 0.6.1 if %python-base < 3.10}
# /SECTION
%python_subpackages

%description
Python SOAP client based on python-lxml and python-requests

%prep
%setup -q -n zeep-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# broken tests
ignorefiles="--ignore tests/test_wsse_signature.py \
             --ignore tests/test_wsse_username.py \
             --ignore tests/test_wsse_utils.py"
%pytest tests/ ${$python_ignore} $ignorefiles

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/zeep
%{python_sitelib}/zeep-%{version}*-info

%changelog
