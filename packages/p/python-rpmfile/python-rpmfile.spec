#
# spec file for package specRPM_CREATION_NAME
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-rpmfile 
Version:        1.0.0+git20190702.208ac80
Release:        0
Summary:        Python module to read rpm files
License:        MIT
Group:          Development/Libraries/Python
Url:            https://github.com/srossross/rpmfile 
Source:         %{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Tools for inspecting RPM files in python. This module is modeled after the tarfile module.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE 
%doc README.md
%{python_sitelib}/rpmfile*

%changelog

