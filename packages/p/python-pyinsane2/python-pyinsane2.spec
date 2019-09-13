#
# spec file for package python-pyinsane2
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
Name:           python-pyinsane2
Version:        2.0.13
Release:        0
Summary:        Python library to access and use image scanners (Linux/Windows/etc)
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/openpaperwork/pyinsane
Source:         https://files.pythonhosted.org/packages/source/p/pyinsane2/pyinsane2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       sane-backends
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module nose >= 1.0}
BuildRequires:  sane-backends
# /SECTION
%python_subpackages

%description
Python library to access and use image scanners (Linux/Windows/etc)

%prep
%setup -q -n pyinsane2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%doc AUTHORS ChangeLog README.md
%license LICENSE
%{python_sitelib}/*

%changelog
