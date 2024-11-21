#
# spec file for package python-term-background
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define tarname term-background
%define modname %( echo %{tarname} | tr '-' '_' )
Name:           python-term-background
Version:        1.0.2
Release:        0
Summary:        Determine if shell has a light or dark background
License:        GPL-2.0-or-later
URL:            http://github.com/rocky/shell-term-background
Source0:        https://github.com/rocky/shell-term-background/releases/download/%{version}/%{tarname}-%{version}.tar.gz
# Missed in source tarball
Source1:        https://raw.githubusercontent.com/rocky/shell-term-background/%{version}/__pkginfo__.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION For tests
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A python module to determine if a shell has a light or dark background.

%prep
%setup -q -n %{tarname}-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}.dist-info

%changelog
