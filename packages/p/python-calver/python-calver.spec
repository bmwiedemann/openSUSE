#
# spec file for package python-calver
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
%define skip_python2 1
%define ghtag 2022.06.26
Name:           python-calver
Version:        2022.6.26
Release:        0
Summary:        Setuptools extension for CalVer package versions
License:        Apache-2.0
URL:            https://github.com/di/calver
Source:         https://github.com/di/calver/archive/refs/tags/%{ghtag}.tar.gz#/calver-%{version}-gh.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirement
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pretend}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Setuptools extension for CalVer package versions

%prep
%setup -q -n calver-%{ghtag}
# We use the github archive because it has the tests. However, it will produce a dynamic calver version of today.
# We don't want that.
sed -i 's/calver_version(True)/"%{version}"/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/calver
%{python_sitelib}/calver-%{version}*-info

%changelog
