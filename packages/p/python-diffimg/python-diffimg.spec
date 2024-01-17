#
# spec file for package python-diffimg
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


%define modname diffimg
Name:           python-diffimg
Version:        0.3.0
Release:        0
Summary:        Library to compute the percent difference between images
License:        MIT
URL:            https://github.com/nicolashahn/python-image-diff
Source0:        https://files.pythonhosted.org/packages/source/d/diffimg/diffimg-%{version}.tar.gz
# License not bundled with tarball; download from github directly
Source1:        https://raw.githubusercontent.com/nicolashahn/diffimg/master/LICENSE.txt
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-Pillow >= 4.3
BuildArch:      noarch
%python_subpackages

%description
A library to get the percent difference in images and generate a diff image.

%prep
%setup -q -n diffimg-%{version}
cp %{S:1} ./
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" diffimg/__main__.py diffimg/test.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Missing benchmark images needed for tests
#%%check
#%%pyunittest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
