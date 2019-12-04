#
# spec file for package python-yaql
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


%global oldpython python
Name:           python-yaql
Version:        1.1.3
Release:        0
Summary:        YAQL - Yet Another Query Language
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/yaql
Source0:        https://files.pythonhosted.org/packages/source/y/yaql/yaql-1.1.3.tar.gz
BuildRequires:  openstack-macros
# for testing
BuildRequires:  python2-Sphinx
BuildRequires:  python2-fixtures
BuildRequires:  python2-oslosphinx
BuildRequires:  python2-pbr
BuildRequires:  python2-ply
BuildRequires:  python2-python-dateutil
BuildRequires:  python2-python-subunit
BuildRequires:  python2-six
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-Sphinx
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslosphinx
BuildRequires:  python3-pbr
BuildRequires:  python3-ply
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-python-subunit
BuildRequires:  python3-six
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel
Requires:       python-ply
Requires:       python-python-dateutil
Requires:       python-six
Conflicts:      %{oldpython}-yaql < %version-%release
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query
language, that allows performing complex queries against arbitrary objects. It
has a vast and comprehensive standard library of frequently used querying
functions and can be extend even further with user-specified functions. YAQL is
written in python and is distributed via PyPI.

%prep
%autosetup -p1 -n yaql-1.1.3
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/yaql

%post
%{python_install_alternative yaql}

%postun
%python_uninstall_alternative yaql

%check
%{python_expand rm -rf .testrepository
$python setup.py testr
}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python_alternative %{_bindir}/yaql
%{python_sitelib}/yaql
%{python_sitelib}/yaql*.egg-info

%changelog
