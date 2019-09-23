#
# spec file for package python-oslo.privsep
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


Name:           python-oslo.privsep
Version:        1.32.1
Release:        0
Summary:        OpenStack library for privilege separation
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.privsep
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.privsep/oslo.privsep-1.32.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-Sphinx
BuildRequires:  python2-cffi >= 1.7.0
BuildRequires:  python2-eventlet >= 0.18.2
BuildRequires:  python2-greenlet >= 0.4.10
BuildRequires:  python2-mock
BuildRequires:  python2-msgpack >= 0.5.0
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python3-Sphinx
BuildRequires:  python3-cffi >= 1.7.0
BuildRequires:  python3-eventlet >= 0.18.2
BuildRequires:  python3-greenlet >= 0.4.10
BuildRequires:  python3-mock
BuildRequires:  python3-msgpack >= 0.5.0
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
Requires:       python-cffi >= 1.7.0
Requires:       python-eventlet >= 0.18.2
Requires:       python-greenlet >= 0.4.10
Requires:       python-msgpack >= 0.5.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.utils >= 3.33.0
BuildArch:      noarch
%ifpython2
BuildRequires:  python-enum34 >= 1.0.4
BuildRequires:  python-futures >= 3.1.1
Requires:       python-enum34 >= 1.0.4
Requires:       python-futures >= 3.1.1
%endif
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
OpenStack library for privilege separation

%package -n python-oslo.privsep-doc
Summary:        oslo.privsep documentation
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python-oslo.privsep-doc
Documentation for oslo.privsep

%prep
%autosetup -p1 -n oslo.privsep-1.32.1
%py_req_cleanup

%build
%python_build
# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/privsep-helper

%post
%python_install_alternative privsep-helper

%postun
%python_uninstall_alternative privsep-helper

%check
%{python_expand export PYTHONPATH=.
$python  -m stestr.cli run
}

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/privsep-helper
%{python_sitelib}/oslo_privsep
%{python_sitelib}/oslo.privsep-*-py?.?.egg-info

%files -n python-oslo.privsep-doc
%doc doc/build/html

%changelog
