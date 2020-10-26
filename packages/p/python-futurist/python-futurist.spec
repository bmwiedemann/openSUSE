#
# spec file for package python-futurist
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


Name:           python-futurist
Version:        2.3.0
Release:        0
Summary:        Useful additions to futures, from the future.
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/futurist
Source0:        https://files.pythonhosted.org/packages/source/f/futurist/futurist-2.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable
BuildRequires:  python3-Sphinx
BuildRequires:  python3-eventlet
BuildRequires:  python3-monotonic
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildArch:      noarch

%description
Useful additions to futures, from the future.

%package -n python3-futurist
Summary:        Useful additions to futures, from the future.
Group:          Development/Languages/Python
Requires:       python3-PrettyTable
Requires:       python3-six >= 1.10.0

%description -n python3-futurist
Useful additions to futures, from the future.

This package contains the Python 3.x module.

%prep
%autosetup -p1 -n futurist-2.3.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=2.3.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-futurist
%doc doc/build/html README.rst
%license LICENSE
%{python3_sitelib}/futurist
%{python3_sitelib}/futurist-*-py?.?.egg-info

%changelog
