#
# spec file for package python-os-win
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


Name:           python-os-win
Version:        4.2.0
Release:        0
Summary:        Hyper-V library for OpenStack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/os-win
Source0:        https://files.pythonhosted.org/packages/source/o/os-win/os-win-4.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-Sphinx
BuildRequires:  python2-ddt
BuildRequires:  python2-eventlet >= 0.18.2
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.concurrency >= 3.26.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-Sphinx
BuildRequires:  python3-ddt
BuildRequires:  python3-devel
BuildRequires:  python3-eventlet >= 0.18.2
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.concurrency >= 3.26.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-eventlet >= 0.18.2
Requires:       python-oslo.concurrency >= 3.26.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.service
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
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
Library contains Windows / Hyper-V code commonly used in the OpenStack projects:
nova, cinder, networking-hyperv.

%package -n python-os-win-doc
Summary:        Documentation for OpenStack Windows/Hyper-V Library
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-os-win-doc
Documentation for the Hyper-V library.

%prep
%autosetup -n os-win-4.2.0
%py_req_cleanup
# we dont want to run the hacking tests again (and dont want the needed deps)
rm -f os_win/tests/unit/test_hacking.py

%build
%{python_build}
%{__python2} setup.py build_sphinx --builder=html,man
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
install -p -D -m 644 doc/build/man/os-win.1 %{buildroot}/%{_mandir}/man1/os-win.1
%python_clone -a %{buildroot}%{_mandir}/man1/os-win.1

%post
%python_install_alternative os-win.1

%check
%{python_expand rm -rf .testrepository
PYTHON=$python $python setup.py test
}

%files %{python_files}
%doc README.rst ChangeLog
%license LICENSE
%{python_sitelib}/os_win*
%{python_sitelib}/*.egg-info
%python_alternative %{_mandir}/man1/os-win.1

%files -n python-os-win-doc
%doc doc/build/html
%license LICENSE

%changelog
