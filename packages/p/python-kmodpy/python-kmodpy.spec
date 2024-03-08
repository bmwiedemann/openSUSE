#
# spec file for package python-kmodpy
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


Name:           python-kmodpy
Version:        0.1.13
Release:        0
Summary:        Python binding for kmod
License:        GPL-3.0-or-later
URL:            https://github.com/cnanakos/kmodpy
Source:         https://files.pythonhosted.org/packages/source/k/kmodpy/kmodpy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libkmod2
BuildArch:      noarch
%python_subpackages

%description
Python binding for kmod

%prep
%autosetup -p1 -n kmodpy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No tests upstream

%files %{python_files}
%doc AUTHORS README
%license COPYING
%{python_sitelib}/kmodpy
%{python_sitelib}/kmodpy-%{version}.dist-info

%changelog
