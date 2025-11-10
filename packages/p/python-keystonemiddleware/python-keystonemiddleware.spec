#
# spec file for package python-keystonemiddleware
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


Name:           python-keystonemiddleware
Version:        10.12.0
Release:        0
Summary:        Middleware for OpenStack Identity
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/keystonemiddleware
Source0:        https://files.pythonhosted.org/packages/source/k/keystonemiddleware/keystonemiddleware-%{version}.tar.gz
BuildRequires:  %{python_module WebOb >= 1.7.1}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneauth1 >= 3.12.0}
BuildRequires:  %{python_module keystoneclient >= 3.20.0}
BuildRequires:  %{python_module oslo.cache >= 1.26.0}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.context >= 2.19.2}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.messaging}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycadf >= 1.1.0}
BuildRequires:  %{python_module python-memcached}
BuildRequires:  %{python_module requests >= 2.14.2}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-WebOb >= 1.7.1
Requires:       python-keystoneauth1 >= 3.12.0
Requires:       python-keystoneclient >= 3.20.0
Requires:       python-oslo.cache >= 1.26.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.messaging
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pycadf >= 1.1.0
Requires:       python-python-memcached
Requires:       python-requests >= 2.14.2
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-keystonemiddleware < %{version}
%else
Conflicts:      python3-keystonemiddleware < %{version}
%endif
%python_subpackages

%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than Keystone
The most prominent module is keystonemiddleware.auth_token. This package
does not expose any CLI or Python API features.

%package -n python-keystonemiddleware-doc
Summary:        Documentation for Middleware for OpenStack Identity
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-keystonemiddleware-doc
Documentation for Middleware for OpenStack Identity.

%prep
%autosetup -p1 -n keystonemiddleware-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# generate html docs
export PYTHONPATH=.
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
rm -v keystonemiddleware/tests/unit/audit/test_logging_notifier.py
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/keystonemiddleware
%{python_sitelib}/keystonemiddleware-%{version}.dist-info

%files -n python-keystonemiddleware-doc
%doc doc/build/html
%license LICENSE

%changelog
