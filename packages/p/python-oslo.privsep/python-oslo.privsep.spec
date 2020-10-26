#
# spec file for package python-oslo.privsep
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


Name:           python-oslo.privsep
Version:        2.4.0
Release:        0
Summary:        OpenStack library for privilege separation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.privsep
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.privsep/oslo.privsep-2.4.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-cffi >= 1.14.0
BuildRequires:  python3-eventlet >= 0.21.0
BuildRequires:  python3-greenlet >= 0.4.14
BuildRequires:  python3-mock
BuildRequires:  python3-msgpack >= 0.6.0
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
OpenStack library for privilege separation

%package -n python3-oslo.privsep
Summary:        OpenStack library for privilege separation
Group:          Development/Languages/Python
Requires:       python3-cffi >= 1.14.0
Requires:       python3-eventlet >= 0.21.0
Requires:       python3-greenlet >= 0.4.14
Requires:       python3-msgpack >= 0.6.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.utils >= 3.33.0
%if 0%{?suse_version}
Obsoletes:      python2-oslo.privsep < 2.0.0
%endif

%description -n python3-oslo.privsep
OpenStack library for privilege separation

%package -n python-oslo.privsep-doc
Summary:        oslo.privsep documentation
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.privsep-doc
Documentation for oslo.privsep

%prep
%autosetup -p1 -n oslo.privsep-2.4.0
%py_req_cleanup

%build
%py3_build
# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
export PYTHONPATH=.
python3  -m stestr.cli run

%files -n python3-oslo.privsep
%doc README.rst
%license LICENSE
%{_bindir}/privsep-helper
%{python3_sitelib}/oslo_privsep
%{python3_sitelib}/oslo.privsep-*-py?.?.egg-info

%files -n python-oslo.privsep-doc
%doc doc/build/html

%changelog
