#
# spec file for package python-logilab-common
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-logilab-common
Version:        1.9.8
Release:        0
Summary:        Python lowlevel functionality shared by logilab projects
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://logilab-common.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/l/logilab-common/logilab-common-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The package logilab.common contains several modules providing low level
functionalities shared among some python projects developed by logilab.

The package is used by pylint, an advanced Python style and syntax
checker.

Please note that some of the modules have some extra dependencies. For
instance, logilab.common.db will require a db-api 2.0 compliant
database driver.

%prep
%setup -q -n logilab-common-%{version}

%build
%python_build

%install
%python_install
rm -f %{buildroot}%{_bindir}/logilab-pytest

%files %{python_files}
%license COPYING COPYING.LESSER
%doc ChangeLog README.rst
%{python_sitelib}/*

%changelog
