#
# spec file for package python-softlayer-zeep
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


%{?!python_module:%define python_module() python3-%{**}}
%global skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-softlayer-zeep
Version:        5.0.0
Release:        0
Summary:        A modern/fast Python SOAP client based on lxml / requests
License:        MIT
URL:            https://docs.python-zeep.org
Source:         https://files.pythonhosted.org/packages/source/s/softlayer-zeep/softlayer-zeep-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module attrs >= 17.2.0}
BuildRequires:  %{python_module freezegun >= 0.3.15}
BuildRequires:  %{python_module isodate >= 0.5.4}
BuildRequires:  %{python_module isort >= 5.3.2}
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
BuildRequires:  fdupes
Requires:       python-attrs >= 17.2.0
Requires:       python-isodate >= 0.5.4
Requires:       python-lxml >= 4.6.0
Requires:       python-platformdirs >= 1.4.0
Requires:       python-pytz
Requires:       python-requests >= 2.7.0
Requires:       python-requests-file >= 1.5.1
Requires:       python-requests-toolbelt >= 0.7.1
Provides:       python-zeep = %version
Obsoletes:      python-zeep < %version
BuildArch:      noarch
%python_subpackages

%description
A modern/fast Python SOAP client based on lxml / requests

%prep
%setup -q -n softlayer-zeep-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
