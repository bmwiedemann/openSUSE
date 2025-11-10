#
# spec file for package python-glanceclient
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


%global pythons %{primary_python}
Name:           python-glanceclient
Version:        4.10.0
Release:        0
Summary:        Python API and CLI for OpenStack Glance
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-glanceclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_glanceclient/python_glanceclient-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.1}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneclient}
BuildRequires:  %{python_module os-client-config}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyOpenSSL >= 17.1.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module urllib3 < 2}
BuildRequires:  %{python_module warlock >= 1.2.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-keystoneauth1 >= 3.6.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-pyOpenSSL >= 17.1.0
Requires:       python-requests >= 2.14.2
Requires:       python-warlock >= 1.2.0
Requires:       python-wrapt >= 1.7.0
BuildArch:      noarch
%python_subpackages

%description
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%package -n python3-glanceclient
Summary:        Python API and CLI for OpenStack Glance

%description -n python3-glanceclient
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.

%package -n python3-glanceclient-doc
Summary:        Documentation for OpenStack Glance API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python3-glanceclient-doc
This is a client for the OpenStack Glance API. There's a Python API (the
glanceclient module), and a command-line script (glance). Each implements
100% of the OpenStack Glance API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_glanceclient-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=%{version} %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
rm -rf doc/build/man/.{doctrees,buildinfo}

%install
%pyproject_install
#man pages
install -p -D -m 644 doc/build/man/glance.1 %{buildroot}%{_mandir}/man1/glance.1

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/glance
%{_mandir}/man1/glance.1*
%{python_sitelib}/glanceclient
%{python_sitelib}/python_glanceclient-%{version}.dist-info

%files -n python3-glanceclient-doc
%license LICENSE
%doc doc/build/html

%changelog
