#
# spec file for package python-logilab-common
#
# Copyright (c) 2025 SUSE LLC
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

%{?sle15_python_module_pythons}
Name:           python-logilab-common
Version:        2.1.0
Release:        0
Summary:        Python lowlevel functionality shared by logilab projects
License:        LGPL-2.1-or-later
URL:            https://logilab-common.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/l/logilab_common/logilab_common-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mypy_extensions
Requires:       python-setuptools
Requires:       python-typing_extensions
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
%setup -q -n logilab_common-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -f %{buildroot}%{_bindir}/logilab-pytest

%files %{python_files}
%license COPYING COPYING.LESSER
%doc ChangeLog README.rst
%dir %{python_sitelib}/logilab
%{python_sitelib}/logilab/common
%{python_sitelib}/logilab_common-%{version}-*-nspkg.pth
%{python_sitelib}/logilab_common-%{version}.dist-info

%changelog
