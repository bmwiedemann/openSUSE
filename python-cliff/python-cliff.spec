#
# spec file for package python-cliff
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


Name:           python-cliff
Version:        2.14.1
Release:        0
Summary:        Command Line Interface Formulation Framework
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-cliff
Source0:        https://files.pythonhosted.org/packages/source/c/cliff/cliff-2.14.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PrettyTable
BuildRequires:  python2-PyYAML
BuildRequires:  python2-cmd2
BuildRequires:  python2-mock
BuildRequires:  python2-pbr
BuildRequires:  python2-python-subunit
BuildRequires:  python2-setuptools
BuildRequires:  python2-stevedore
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-unicodecsv
BuildRequires:  python3-PrettyTable
BuildRequires:  python3-PyYAML
BuildRequires:  python3-mock
BuildRequires:  python3-pbr
BuildRequires:  python3-python-subunit
BuildRequires:  python3-setuptools
BuildRequires:  python3-stevedore
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-PrettyTable
Requires:       python-PyYAML
Requires:       python-cmd2
Requires:       python-pyparsing
Requires:       python-six
Requires:       python-stevedore
BuildArch:      noarch
%ifpython2
Requires:       python-unicodecsv
%endif
%python_subpackages

%description
cliff is a framework for building command line programs. It uses
setuptools entry points to provide subcommands, output formatters, and
other extensions.

%package -n python-cliff-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python2-Sphinx
Provides:       %{python_module cliff-doc = %{version}}

%description -n python-cliff-doc
cliff is a framework for building command line programs. It uses
setuptools entry points to provide subcommands, output formatters, and
other extensions.

This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n cliff-2.14.1

%py_req_cleanup

%build
%python_build
%{__python2} setup.py build_sphinx
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install

%check
%{python_expand rm -rf .testrepository
$python setup.py test
}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/cliff
%{python_sitelib}/*.egg-info

%files -n python-cliff-doc
%license LICENSE
%doc doc/build/html

%changelog
