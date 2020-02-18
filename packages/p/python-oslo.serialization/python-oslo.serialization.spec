#
# spec file for package python-oslo.serialization
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


Name:           python-oslo.serialization
Version:        2.29.2
Release:        0
Summary:        OpenStack serialization library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.serialization
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.serialization/oslo.serialization-2.29.2.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-ipaddress
BuildRequires:  python2-mock
BuildRequires:  python2-msgpack >= 0.5.2
BuildRequires:  python2-netaddr
BuildRequires:  python2-oslo.i18n
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-stestr
BuildRequires:  python3-mock
BuildRequires:  python3-msgpack >= 0.5.2
BuildRequires:  python3-netaddr
BuildRequires:  python3-oslo.i18n
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
Requires:       python-msgpack >= 0.5.2
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pytz >= 2013.6
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
The oslo.serialization library provides support for representing objects
in transmittable and storable formats, such as Base64, JSON and MessagePack.

%package -n python-oslo.serialization-doc
Summary:        Documentation for OpenStack serialization library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.serialization-doc
The oslo.serialization library provides support for representing objects
in transmittable and storable formats, such as Base64, JSON and MessagePack.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.serialization-2.29.2
sed -i -e "s,bandit.*,," test-requirements.txt
%py_req_cleanup

%build
%{python_build}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/oslo_serialization
%{python_sitelib}/*.egg-info

%files -n python-oslo.serialization-doc
%license LICENSE
%doc doc/build/html

%changelog
