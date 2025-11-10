#
# spec file for package python-keystoneauth1
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


Name:           python-keystoneauth1
Version:        5.12.0
Release:        0
Summary:        OpenStack authenticating tools
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/keystoneauth
Source0:        https://files.pythonhosted.org/packages/source/k/keystoneauth1/keystoneauth1-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module betamax}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module iso8601 >= 2.0.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module oauthlib}
BuildRequires:  %{python_module os-service-types >= 1.8.0}
BuildRequires:  %{python_module oslo.config}
BuildRequires:  %{python_module oslo.utils}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-kerberos}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module urllib3 < 2}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML
Requires:       python-iso8601 >= 2.0.0
Requires:       python-lxml
Requires:       python-oauthlib
Requires:       python-os-service-types >= 1.8.0
Requires:       python-requests >= 2.14.2
Requires:       python-requests-kerberos
Requires:       python-stevedore >= 1.20.0
Requires:       python-typing-extensions >= 4.12
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-keystoneauth1 < %{version}
%endif
BuildArch:      noarch
%python_subpackages

%description
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

%package -n python-keystoneauth1-doc
Summary:        Documentation for OpenStack authenticating tools
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-keystoneauth1-doc
Documentation for OpenStack authenticating tools.

%prep
%autosetup -p1 -n keystoneauth1-%{version}
%py_req_cleanup

# cleanup intersphinx (we have no network during build)
echo "intersphinx_mapping = {}" >> doc/source/conf.py

%build
%{pyproject_wheel}

%install
%{pyproject_install}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
rm -v keystoneauth1/tests/unit/test_hacking_checks.py
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/keystoneauth1
%{python_sitelib}/keystoneauth1-%{version}.dist-info

%files -n python-keystoneauth1-doc
%doc doc/build/html
%license LICENSE

%changelog
