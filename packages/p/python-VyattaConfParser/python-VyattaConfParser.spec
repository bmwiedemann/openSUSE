#
# spec file for package python-VyattaConfParser
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017-2019, Martin Hauke <mardnh@gmx.de>
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


Name:           python-VyattaConfParser
Version:        0.5.5
Release:        0
Summary:        A python config parser for Vyatta/VyOS
License:        MIT
URL:            https://github.com/hedin/vyatta-conf-parser
#Source:         https://files.pythonhosted.org/packages/source/V/VyattaConfParser/VyattaConfParser-%%{version}.tar.gz
Source:         VyattaConfParser-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module datadiff}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Vyatta/VyOS config parser with unicode support and without dependencies.

%prep
%setup -q -n VyattaConfParser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/[Vv]yatta[Cc]onf[Pp]arser
%{python_sitelib}/[Vv]yatta[Cc]onf[Pp]arser-%{version}*-info

%changelog
