#
# spec file for package python-biplist
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-biplist
Version:        1.0.3
Release:        0
Summary:        A library for reading/writing binary plists
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://bitbucket.org/wooster/biplist
Source:         https://files.pythonhosted.org/packages/source/b/biplist/biplist-%{version}.tar.gz
# Test on 32bit expects long==int which is true only on py3
Patch0:         skip-test.patch
# PATCH-FIX-UPSTREAM plistlib-Data.patch bt#wooster/biplist#12 mcepl@suse.com
# Add plistlib-Data.patch to avoid deprecated plistslib.Data
Patch1:         plistlib-Data.patch
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
biplist is a binary plist parser/generator for Python.

Binary Property List (plist) files provide a faster and smaller serialization
format for property lists on OS X. This is a library for generating binary
plists which can be read by OS X, iOS, or other clients.

%prep
%autosetup -p1 -n biplist-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -s tests -v

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%{python_sitelib}/*

%changelog
