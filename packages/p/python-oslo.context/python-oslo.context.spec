#
# spec file for package python-oslo.context
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


%bcond_without test
Name:           python-oslo.context
Version:        3.1.1
Release:        0
Summary:        OpenStack Oslo context library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.context
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.context/oslo.context-3.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-pbr >= 2.0.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-oslotest
BuildRequires:  python3-stestr
%endif

%description
The Oslo context library has helpers to maintain useful information
about a request context.
The request context is usually populated in the WSGI pipeline and
used by various modules such as logging.

%package -n python3-oslo.context
Summary:        OpenStack Oslo context library
Group:          Development/Languages/Python
Requires:       python3-debtcollector >= 1.2.0

%description -n python3-oslo.context
The Oslo context library has helpers to maintain useful information
about a request context.
The request context is usually populated in the WSGI pipeline and
used by various modules such as logging.

This package contains the Python 3.x module.

%package -n python-oslo.context-doc
Summary:        Documentation for OpenStack common context library
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.context-doc
Documentation for the oslo-context library.

%prep
%autosetup -p1 -n oslo.context-3.1.1
%py_req_cleanup

%build
%{py3_build}
# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%if %{with test}
%check
python3 -m stestr.cli run
%endif

%files -n python3-oslo.context
%license LICENSE
%doc README.rst
%{python3_sitelib}/oslo_context
%{python3_sitelib}/*.egg-info

%files -n python-oslo.context-doc
%license LICENSE
%doc doc/build/html

%changelog
