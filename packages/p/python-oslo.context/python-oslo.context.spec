#
# spec file for package python-oslo.context
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        6.1.0
Release:        0
Summary:        OpenStack Oslo context library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.context
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_context/oslo_context-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.context < %{version}
%endif
%if %{with test}
BuildRequires:  %{python_module debtcollector}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module stestr}
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
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.context-doc
Documentation for the oslo-context library.

%prep
%autosetup -p1 -n oslo_context-%{version}
%py_req_cleanup

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%if %{with test}
%check
%{openstack_stestr_run}
%endif

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/oslo_context
%{python_sitelib}/oslo_context-%{version}.dist-info

%files -n python-oslo.context-doc
%license LICENSE
%doc doc/build/html

%changelog
