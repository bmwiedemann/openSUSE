#
# spec file for package python-cliff
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


Name:           python-cliff
Version:        3.4.0
Release:        0
Summary:        Command Line Interface Formulation Framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-cliff
Source0:        https://files.pythonhosted.org/packages/source/c/cliff/cliff-3.4.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable
BuildRequires:  python3-PyYAML
BuildRequires:  python3-cmd2
BuildRequires:  python3-docutils
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-pbr
BuildRequires:  python3-pytest
BuildRequires:  python3-python-subunit
BuildRequires:  python3-stevedore
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python3-PrettyTable
Requires:       python3-PyYAML
Requires:       python3-cmd2
Requires:       python3-pyparsing
Requires:       python3-six
Requires:       python3-stevedore
BuildArch:      noarch

%description
cliff is a framework for building command line programs. It uses
setuptools entry points to provide subcommands, output formatters, and
other extensions.

%package -n python3-cliff
Summary:        Command Line Interface Formulation Framework
Group:          Development/Languages/Python
Requires:       python3-PrettyTable
Requires:       python3-PyYAML
Requires:       python3-cmd2
Requires:       python3-pyparsing
Requires:       python3-six
Requires:       python3-stevedore

%description -n python3-cliff
cliff is a framework for building command line programs. It uses
setuptools entry points to provide subcommands, output formatters, and
other extensions.

This package contains the Python 3.x module.

%package -n python-cliff-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
Provides:       %{python_module cliff-doc = %{version}}

%description -n python-cliff-doc
cliff is a framework for building command line programs. It uses
setuptools entry points to provide subcommands, output formatters, and
other extensions.

This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n cliff-3.4.0
%py_req_cleanup

%build
%py3_build
PBR_VERSION=3.4.0 PYTHONPATH=. %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
# doesn't work with pytest atm
rm -v cliff/tests/test_commandmanager.py
python3 -m pytest cliff/tests

%files -n python3-cliff
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/cliff
%{python3_sitelib}/*.egg-info

%files -n python-cliff-doc
%license LICENSE
%doc doc/build/html

%changelog
