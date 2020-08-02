#
# spec file for package python-napalm-digineo-procurve
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
%define skip_python2 1
Name:           python-napalm-digineo-procurve
Version:        0.2.0
Release:        0
License:        Apache-2.0
Summary:        NAPALM - HP ProCurve/Aruba network driver
Url:            https://github.com/digineo/napalm-digineo-procurve
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/n/napalm-digineo-procurve/napalm-digineo-procurve-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 2.4.0}
BuildRequires:  %{python_module pytest }
# /SECTION
BuildRequires:  fdupes
Requires:       python-napalm >= 2.4.0
BuildArch:      noarch
%python_subpackages

%description
Napalm driver for HP ProCurve/Aruba switches.

%prep
%setup -q -n napalm-digineo-procurve-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.md
%doc README.md
%{python_sitelib}/*

%changelog
