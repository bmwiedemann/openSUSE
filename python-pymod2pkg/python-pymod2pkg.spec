#
# spec file for package python-pymod2pkg
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


%global sname pymod2pkg
Name:           python-pymod2pkg
Version:        0.21.0
Release:        0
Summary:        OpenStack Packaging - python module name to package name map
License:        Apache-2.0
Group:          Development/Libraries/Python
URL:            https://wiki.openstack.org/wiki/Rpm-packaging
Source0:        https://files.pythonhosted.org/packages/source/p/pymod2pkg/pymod2pkg-0.21.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testresources
BuildRequires:  python2-testtools
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
pymod2pkg is a simple python module for translating python module names to
corresponding package names which is a common problem in the packaging world.

%package -n python-pymod2pkg-doc
Summary:        Documentation for python module name to package name map library
Group:          Development/Libraries/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-pymod2pkg-doc
Documentation for python module name to package name map library.

%prep
%autosetup -p1 -n pymod2pkg-0.21.0
%py_req_cleanup

%build
%{python_build}

# generate html docs
%sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/pymod2pkg

%check
%python_exec -m stestr.cli run

%post
%python_install_alternative pymod2pkg

%postun
%python_uninstall_alternative pymod2pkg

%files %{python_files}
%license LICENSE
%doc README*
%python_alternative %{_bindir}/pymod2pkg
%{python_sitelib}/*

%files -n python-pymod2pkg-doc
%doc doc/build/html
%license LICENSE

%changelog
