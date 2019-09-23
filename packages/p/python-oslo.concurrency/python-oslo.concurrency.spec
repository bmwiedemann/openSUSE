#
# spec file for package python-oslo.concurrency
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


Name:           python-oslo.concurrency
Version:        3.29.1
Release:        0
Summary:        OpenStack oslo.concurrency library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.concurrency
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.concurrency/oslo.concurrency-3.29.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-enum34 >= 1.0.4
BuildRequires:  python2-eventlet
BuildRequires:  python2-fasteners >= 0.7.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-futures
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-eventlet
BuildRequires:  python3-fasteners >= 0.7.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-fasteners >= 0.7.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%ifpython2
Requires:       python-enum34 >= 1.0.4
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
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package -n python-oslo.concurrency-doc
Summary:        Documentation for OpenStack concurrency library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.concurrency-doc
The oslo.concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.concurrency-3.29.1
%py_req_cleanup

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/lockutils-wrapper

%post
%python_install_alternative lockutils-wrapper

%postun
%python_uninstall_alternative lockutils-wrapper

%check
if [ "%_lib" = "lib64" ]; then
%python_exec -m stestr.cli run
fi

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%python_alternative %{_bindir}/lockutils-wrapper
%{python_sitelib}/oslo_concurrency
%{python_sitelib}/*.egg-info

%files -n python-oslo.concurrency-doc
%license LICENSE
%doc doc/build/html

%changelog
