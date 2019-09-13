#
# spec file for package python-oslosphinx
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


Name:           python-oslosphinx
Version:        4.18.0
Release:        0
Summary:        OpenStack Sphinx
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslosphinx
Source0:        https://files.pythonhosted.org/packages/source/o/oslosphinx/oslosphinx-4.18.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-setuptools
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
The Oslo Sphinx library provides an OpenStack common
layer of Sphinx plugins.

%prep
%autosetup -p1 -n oslosphinx-4.18.0
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/oslosphinx
%{python_sitelib}/*.egg-info

%changelog
