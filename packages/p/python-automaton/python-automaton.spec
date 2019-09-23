#
# spec file for package python-automaton
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


Name:           python-automaton
Version:        1.16.0
Release:        0
Summary:        Friendly state machines for python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/automaton
Source0:        https://files.pythonhosted.org/packages/source/a/automaton/automaton-1.16.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PrettyTable >= 0.7.2
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-devel
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-pbr >= 2.0.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
Friendly state machines for python.

%package -n python-automaton-doc
Summary:        Documentation for the Automaton Library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-automaton-doc
Documentation for the Automaton library.

%prep
%autosetup -p1 -n automaton-1.16.0
%py_req_cleanup

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the Sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/automaton
%{python_sitelib}/*.egg-info

%files -n python-automaton-doc
%license LICENSE
%doc doc/build/html

%changelog
