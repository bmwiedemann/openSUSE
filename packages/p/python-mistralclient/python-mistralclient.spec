#
# spec file for package python-mistralclient
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


%global oldpython python
Name:           python-mistralclient
Version:        3.10.0
Release:        0
Summary:        Python API and CLI for OpenStack Mistral
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-mistralclient/python-mistralclient-3.10.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-nose
BuildRequires:  python2-openstackclient
BuildRequires:  python2-oslotest
BuildRequires:  python2-osprofiler
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-openstackclient
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
Requires:       python-PyYAML >= 3.12
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneclient
Requires:       python-os-client-config
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-osprofiler
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
Conflicts:      %{oldpython}-mistralclient < %version
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).

%package -n python-mistralclient-doc
Summary:        Documentation for OpenStack Mistral API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-mistralclient-doc
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).
This package contains the documentation.

%prep
%autosetup -p1 -n python-mistralclient-3.10.0
%py_req_cleanup

%build
%{python_build}

# Build HTML docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/mistral

%post
%python_install_alternative mistral

%postun
%python_uninstall_alternative mistral

%check
find . -type f -name *.pyc -delete
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} nosetests-%{$python_version} mistralclient/tests/unit

%files %{python_files}
%license LICENSE
%{python_sitelib}/mistralclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/mistral

%files -n python-mistralclient-doc
%license LICENSE
%doc README.rst doc/build/html

%changelog
