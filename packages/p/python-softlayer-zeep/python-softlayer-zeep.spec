#
# spec file for package python-softlayer-zeep
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
Name:           python-softlayer-zeep
Version:        5.0.0
Release:        0
Summary:        A modern/fast Python SOAP client based on lxml / requests
License:        MIT
#Git-Clone:     https://github.com/softlayer/softlayer-zeep
URL:            https://docs.python-zeep.org
Source:         https://files.pythonhosted.org/packages/source/s/softlayer-zeep/softlayer-zeep-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip-networked-test.patch gh#mvantellingen/python-zeep#1402 mcepl@suse.com
# skip tests requiring network connection
Patch0:         skip-networked-test.patch
# PATCH-FIX-UPSTREAM gh#mvantellingen/python-zeep#d1b0257 Fix regression in parsing xsd:Date with negative timezone
Patch1:         xsd-date.patch
BuildRequires:  %{python_module pip}
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
Conflicts:      python-zeep
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 17.2.0}
BuildRequires:  %{python_module freezegun >= 0.3.15}
BuildRequires:  %{python_module isodate >= 0.5.4}
BuildRequires:  %{python_module isort >= 5.3.2}
BuildRequires:  %{python_module legacy-cgi >= 2.6}
BuildRequires:  %{python_module lxml >= 4.6.0}
BuildRequires:  %{python_module platformdirs >= 1.4.0}
BuildRequires:  %{python_module pretend == 1.0.9}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-httpx}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module requests-file >= 1.5.1}
BuildRequires:  %{python_module requests-mock >= 0.7.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.7.1}
# /SECTION
%if 0%{?python_version_nodots} >= 313
Requires:       python-legacy-cgi >= 2.6
%endif
%python_subpackages

%description
A modern/fast Python SOAP client based on lxml / requests

%prep
%autosetup -p1 -n softlayer-zeep-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not network'

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/zeep
%{python_sitelib}/softlayer_zeep-%{version}.dist-info

%changelog
