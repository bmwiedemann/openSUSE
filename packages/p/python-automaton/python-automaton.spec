#
# spec file for package python-automaton
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


Name:           python-automaton
Version:        3.1.0
Release:        0
Summary:        Friendly state machines for python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/automaton
Source0:        https://files.pythonhosted.org/packages/source/a/automaton/automaton-3.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-devel
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Friendly state machines for python.

%package -n python3-automaton
Summary:        Friendly state machines for python
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-pbr >= 2.0.0
Requires:       python3-six

%description -n python3-automaton
Friendly state machines for python.

This package contains the Python 3.x module.

%package -n python-automaton-doc
Summary:        Documentation for the Automaton Library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-automaton-doc
Documentation for the Automaton library.

%prep
%autosetup -p1 -n automaton-3.1.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
%{openstack_stestr_run}

%files -n python3-automaton
%doc README.rst
%license LICENSE
%{python3_sitelib}/automaton
%{python3_sitelib}/*.egg-info

%files -n python-automaton-doc
%license LICENSE
%doc doc/build/html

%changelog
