#
# spec file for package python-mujson
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
Name:           python-mujson
Version:        1.4
Release:        0
Summary:        Module that selects the fastest JSON functions available at import time
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/mattgiles/mujson
Source0:        https://files.pythonhosted.org/packages/source/m/mujson/mujson-%{version}.tar.gz
# https://github.com/mattgiles/mujson/issues/8
Source1:        https://raw.githubusercontent.com/mattgiles/mujson/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A Python module that selects the fastest JSON functions available at
import time.

%prep
%setup -q -n mujson-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no uptream tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
