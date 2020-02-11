#
# spec file for package python-DataProperty
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-DataProperty
Version:        0.45.0
Release:        0
License:        MIT
Summary:        Python library for extract property from data
Url:            https://github.com/thombashi/DataProperty
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/D/DataProperty/DataProperty-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools >= 38.3.0}
# SECTION test requirements
BuildRequires:  %{python_module mbstrdecoder >= 0.8.3}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module typepy >= 0.6.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module termcolor}
BuildRequires:  %{python_module pytz >= 2018.9}
BuildRequires:  %{python_module python-dateutil >= 2.8.0}
BuildRequires:  python-futures
BuildRequires:  python-ipaddress
BuildRequires:  python-enum34
# /SECTION
BuildRequires:  fdupes
Requires:       python-mbstrdecoder >= 0.8.3
Requires:       python-setuptools >= 38.3.0
Requires:       python-six >= 1.10.0
Requires:       python-typepy >= 0.6.4
%ifpython2
Requires:       python-futures
Requires:       python-ipaddress
Requires:       python-enum34
%endif
BuildArch:      noarch
%python_subpackages

%description
Python library for extract property from data.

%prep
%setup -q -n DataProperty-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/dataproperty*
%{python_sitelib}/DataProperty*

%changelog
