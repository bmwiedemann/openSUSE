#
# spec file for package python-mistralclient
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


%global oldpython python
Name:           python-mistralclient
Version:        4.1.1
Release:        0
Summary:        Python API and CLI for OpenStack Mistral
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-mistralclient/python-mistralclient-4.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).

%package -n python3-mistralclient
Summary:        Python API and CLI for OpenStack Mistral
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.13
Requires:       python3-cliff >= 2.8.0
Requires:       python3-keystoneclient
Requires:       python3-os-client-config
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-osprofiler
Requires:       python3-requests >= 2.14.2
Requires:       python3-six
Requires:       python3-stevedore >= 1.20.0
Conflicts:      %{oldpython}-mistralclient < %version

%description -n python3-mistralclient
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).

This package contains the Python 3.x module.

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
%autosetup -p1 -n python-mistralclient-4.1.1
%py_req_cleanup

%build
%{py3_build}

# Build HTML docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-mistralclient
%license LICENSE
%{python3_sitelib}/mistralclient
%{python3_sitelib}/*.egg-info
%{_bindir}/mistral

%files -n python-mistralclient-doc
%license LICENSE
%doc README.rst doc/build/html

%changelog
