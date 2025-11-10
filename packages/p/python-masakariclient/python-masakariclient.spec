#
# spec file for package python-masakariclient
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
Name:           python-masakariclient
Version:        8.7.0
Release:        0
Summary:        Python API and CLI for OpenStack Masakari
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-masakariclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-masakariclient/python_masakariclient-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module openstacksdk >= 0.13.0}
BuildRequires:  %{python_module osc-lib >= 1.8.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-openstacksdk >= 0.13.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
%python_subpackages

%description
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).

%package -n python3-masakariclient-doc
Summary:        Documentation for OpenStack Masakari API client libary
Group:          Documentation/HTML
%define oldpython python
Provides:       %{oldpython}-masakariclient-doc = %{version}
Obsoletes:      %{oldpython}-masakariclient-doc < %{version}
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-masakariclient-doc
Client library for Masakari built on the Masakari API. It provides a Python API
(the masakariclient module) and a command-line tool (masakari).
This package contains the documentation.

%prep
%autosetup -p1 -n python_masakariclient-%{version}

%build
%pyproject_wheel

# Build HTML docs and man page
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=%{version} %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
# man pages
install -p -D -m 644 doc/build/man/python-masakariclient.1 %{buildroot}%{_mandir}/man1/python-masakariclient.1

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{python_sitelib}/masakariclient
%{python_sitelib}/python_masakariclient-%{version}.dist-info

%files -n python3-masakariclient-doc
%license LICENSE
%doc doc/build/html
%{_mandir}/man1/python-masakariclient.1.*

%changelog
