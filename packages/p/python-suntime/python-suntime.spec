#
# spec file for package python-suntime
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
Name:           python-suntime
Version:        1.2.5
Release:        0
Summary:        Python sunset and sunrise time calculation
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/SatAgro/suntime
Source:         https://files.pythonhosted.org/packages/source/s/suntime/suntime-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/SatAgro/suntime/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
Python sunset and sunrise time calculation library.

%prep
%setup -q -n suntime-%{version}
cp %{SOURCE1} .

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check no tests https://github.com/SatAgro/suntime/issues/9

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
