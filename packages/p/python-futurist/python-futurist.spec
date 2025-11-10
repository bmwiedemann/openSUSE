#
# spec file for package python-futurist
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


Name:           python-futurist
Version:        3.2.1
Release:        0
Summary:        Useful additions to futures, from the future.
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/futurist
Source0:        https://files.pythonhosted.org/packages/source/f/futurist/futurist-%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable}
BuildRequires:  %{python_module debtcollector >= 3.0.0}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
Requires:       python-debtcollector >= 3.0.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-futurist < %{version}
%endif
%python_subpackages

%description
Useful additions to futures, from the future.

%package -n python3-futurist
Summary:        Useful additions to futures, from the future.

%description -n python3-futurist
Useful additions to futures, from the future.

This package contains the Python 3.x module.

%prep
%autosetup -p1 -n futurist-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%doc doc/build/html README.rst
%license LICENSE
%{python_sitelib}/futurist
%{python_sitelib}/futurist-%{version}.dist-info

%changelog
