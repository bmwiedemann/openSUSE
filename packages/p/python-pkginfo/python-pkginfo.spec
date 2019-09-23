#
# spec file for package python-pkginfo
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
Name:           python-pkginfo
Version:        1.5.0.1
Release:        0
Summary:        Python package for querying metadatdata from sdists/bdists/installed packages
License:        MIT
Group:          Development/Languages/Python
URL:            http://pypi.python.org/pypi/pkginfo/
Source:         https://files.pythonhosted.org/packages/source/p/pkginfo/pkginfo-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(preun): update-alternatives
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This package provides an API for querying the distutils metadata written in
the PKG-INFO file inside a source distriubtion (an sdist) or a
binary distribution (e.g., created by running bdist_egg).  It can
also query the EGG-INFO directory of an installed distribution, and
the *.egg-info stored in a "development checkout"
(e.g, created by running setup.py develop).

%prep
%setup -q -n pkginfo-%{version}
# fix tests until fixed upstream
sed -i "s|'2\.1'|None|" pkginfo/tests/test_installed.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pkginfo

%check
%pytest

%post
%python_install_alternative pkginfo

%preun
%python_uninstall_alternative pkginfo

%files %{python_files}
%license LICENSE.txt
%doc README.txt CHANGES.txt TODO.txt
%python_alternative %{_bindir}/pkginfo
%{python_sitelib}/pkginfo
%{python_sitelib}/pkginfo-%{version}-py*.egg-info

%changelog
