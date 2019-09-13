#
# spec file for package python-osprofiler
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


Name:           python-osprofiler
Version:        2.6.0
Release:        0
Summary:        OpenStack Profiler Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/osprofiler
Source0:        https://files.pythonhosted.org/packages/source/o/osprofiler/osprofiler-2.6.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PrettyTable >= 0.7.2
BuildRequires:  python2-WebOb >= 1.7.1
BuildRequires:  python2-ddt
BuildRequires:  python2-docutils
BuildRequires:  python2-elasticsearch
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.concurrency >= 3.26.0
BuildRequires:  python2-oslo.config
BuildRequires:  python2-oslo.log
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-pymongo
BuildRequires:  python2-python-subunit
BuildRequires:  python2-redis
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testtools
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-ddt
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-elasticsearch
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.concurrency >= 3.26.0
BuildRequires:  python3-oslo.config
BuildRequires:  python3-oslo.log
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pymongo
BuildRequires:  python3-python-subunit
BuildRequires:  python3-redis
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-WebOb >= 1.7.1
Requires:       python-oslo.concurrency >= 3.26.0
Requires:       python-oslo.config
Requires:       python-oslo.log
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-six >= 1.10.0
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
OSProfiler provides a tiny but powerful library that is used by
most (soon to be all) OpenStack projects and their python clients. It
provides functionality to be able to generate 1 trace per request, that goes
through all involved services. This trace can then be extracted and used
to build a tree of calls which can be quite handy for a variety of
reasons (for example in isolating cross-project performance issues).

%package -n python-osprofiler-doc
Summary:        Documentation for OSProfiler
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-osprofiler-doc
Documentation for OSProfiler.

%prep
%autosetup -p1 -n osprofiler-2.6.0
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/osprofiler

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%post
%python_install_alternative osprofiler

%postun
%python_uninstall_alternative osprofiler

%check
%python_exec -m stestr.cli run --black-regex '(^osprofiler.tests.unit.drivers.test_jaeger.JaegerTestCase.*$)'

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/osprofiler
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/osprofiler

%files -n python-osprofiler-doc
%license LICENSE
%doc doc/build/html

%changelog
