#
# spec file for package python-napalm-digineo-procurve
#
# Copyright (c) 2023 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define skip_python2 1
Name:           python-napalm-digineo-procurve
Version:        0.2.0
Release:        0
Summary:        NAPALM - HP ProCurve/Aruba network driver
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/digineo/napalm-digineo-procurve
Source:         https://files.pythonhosted.org/packages/source/n/napalm-digineo-procurve/napalm-digineo-procurve-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-napalm >= 2.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module napalm >= 2.4.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
# /SECTION
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
%{python_sitelib}/napalm_digineo_procurve
%{python_sitelib}/napalm_digineo_procurve-%{version}*-info

%changelog
