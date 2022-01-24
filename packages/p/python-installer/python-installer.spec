#
# spec file for package python-installer
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-installer
# DO NOT UPGRADE UNTIL PDM WORKS WITH MORE RECENT VERSIONS!!!
Version:        0.3.0
Release:        0
Summary:        A library for installing Python wheels
License:        MIT
URL:            https://github.com/pradyunsg/installer
Source:         https://files.pythonhosted.org/packages/source/i/installer/installer-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM remove-mock.patch mcepl@suse.com
# Make dependency on mock package optional
Patch0:         remove-mock.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A library for installing Python wheels.

%prep
%autosetup -p1 -n installer-%{version}

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
%{python_sitelib}/*

%changelog
