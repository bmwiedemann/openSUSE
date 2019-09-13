#
# spec file for package python-backports.html
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


%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-backports.html
Version:        1.1.0
Release:        0
Summary:        Backport of Python 34+'s html module
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/frostming/backports.html
Source:         https://github.com/frostming/backports.html/archive/v%{version}.tar.gz#/backports.html-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module backports}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-backports
BuildArch:      noarch
%python_subpackages

%description
Backport of Python 3.4+'s html module.

%prep
%setup -q -n backports.html-%{version}

%build
%python_build

%install
%python_install
%{python_expand rm %{buildroot}%{$python_sitelib}/backports/__init__.py*
rm -rf %{buildroot}%{$python_sitelib}/backports/__pycache__/
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
