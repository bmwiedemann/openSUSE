#
# spec file for package python-futurist
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


Name:           python-futurist
Version:        1.8.1
Release:        0
Summary:        Useful additions to futures, from the future.
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/futurist
Source0:        https://files.pythonhosted.org/packages/source/f/futurist/futurist-1.8.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PrettyTable >= 0.7.1
BuildRequires:  python2-Sphinx
BuildRequires:  python2-contextlib2 >= 0.4.0
BuildRequires:  python2-eventlet
BuildRequires:  python2-futures >= 3.0.0
BuildRequires:  python2-monotonic >= 0.6
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-setuptools
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python3-PrettyTable >= 0.7.1
BuildRequires:  python3-Sphinx
BuildRequires:  python3-eventlet
BuildRequires:  python3-monotonic >= 0.6
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-monotonic >= 0.6
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%ifpython2
Requires:       python-contextlib2 >= 0.4.0
Requires:       python-futures >= 3.0.0
%endif
%python_subpackages

%description
Useful additions to futures, from the future.

%prep
%autosetup -p1 -n futurist-1.8.1
%py_req_cleanup

%build
%{python_build}

# generate html docs
PBR_VERSION=1.8.1 sphinx-build -b html doc/source doc/build/html

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc doc/build/html README.rst
%license LICENSE
%{python_sitelib}/futurist
%{python_sitelib}/futurist-*-py?.?.egg-info

%changelog
