#
# spec file for package python-swiftclient
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
Name:           python-swiftclient
Version:        4.8.0
Release:        0
Summary:        OpenStack Object Storage API Client Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-swiftclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_swiftclient/python_swiftclient-%{version}.tar.gz
BuildRequires:  %{python_module keystoneclient}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-requests >= 2.4.0
BuildArch:      noarch
%python_subpackages

%description
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

%package -n python-swiftclient-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-swiftclient-doc
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n python_swiftclient-%{version}

%build
%pyproject_wheel
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{_bindir}/swift
%{python_sitelib}/swiftclient
%{python_sitelib}/python_swiftclient-%{version}.dist-info
%{_mandir}/man1/swift.1%{?ext_man}

%files -n python-swiftclient-doc
%license LICENSE
%doc doc/build/html

%changelog
