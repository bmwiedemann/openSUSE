#
# spec file for package python-pymod2pkg
#
# Copyright (c) 2020 SUSE LLC
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


%global sname pymod2pkg
Name:           python-pymod2pkg
Version:        0.25.0
Release:        0
Summary:        OpenStack Packaging - python module name to package name map
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://wiki.openstack.org/wiki/Rpm-packaging
Source0:        https://files.pythonhosted.org/packages/source/p/pymod2pkg/pymod2pkg-0.25.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-distro
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
pymod2pkg is a simple python module for translating python module names to
corresponding package names which is a common problem in the packaging world.

%package -n python3-pymod2pkg
Summary:        OpenStack Packaging - python module name to package name map
Group:          Development/Libraries/Python
Requires:       python3-distro
Requires:       python3-pbr >= 2.0.0
%if 0%{?suse_version}
Obsoletes:      python2-pymod2pkg < 0.23.0
%endif

%description -n python3-pymod2pkg
pymod2pkg is a simple python module for translating python module names to
corresponding package names which is a common problem in the packaging world.

This package contains the Python 3.x module.

%package -n python-pymod2pkg-doc
Summary:        Documentation for python module name to package name map library
Group:          Development/Libraries/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-pymod2pkg-doc
Documentation for python module name to package name map library.

%prep
%autosetup -p1 -n pymod2pkg-0.25.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
%sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-pymod2pkg
%license LICENSE
%doc README*
%{_bindir}/pymod2pkg
%{python3_sitelib}/*

%files -n python-pymod2pkg-doc
%doc doc/build/html
%license LICENSE

%changelog
