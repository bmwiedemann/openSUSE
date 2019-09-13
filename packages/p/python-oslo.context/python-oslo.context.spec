#
# spec file for package python-oslo.context
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


%bcond_without test
Name:           python-oslo.context
Version:        2.22.1
Release:        0
Summary:        OpenStack Oslo context library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.context
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.context/oslo.context-2.22.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python3-pbr >= 2.0.0
Requires:       python-debtcollector >= 1.2.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-oslotest
BuildRequires:  python2-stestr
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslotest
BuildRequires:  python3-stestr
%endif
%python_subpackages

%description
The Oslo context library has helpers to maintain useful information
about a request context.
The request context is usually populated in the WSGI pipeline and
used by various modules such as logging.

%package -n python-oslo.context-doc
Summary:        Documentation for OpenStack common context library
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.context-doc
Documentation for the oslo-context library.

%prep
%autosetup -p1 -n oslo.context-2.22.1
%py_req_cleanup

%build
%{python_build}
# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%if %{with test}
%check
%python_exec -m stestr.cli run
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python2_sitelib}/oslo_context
%{python2_sitelib}/*.egg-info

%files -n python-oslo.context-doc
%license LICENSE
%doc doc/build/html

%changelog
