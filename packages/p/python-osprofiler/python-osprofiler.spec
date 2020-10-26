#
# spec file for package python-osprofiler
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


Name:           python-osprofiler
Version:        3.4.0
Release:        0
Summary:        OpenStack Profiler Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/osprofiler
Source0:        https://files.pythonhosted.org/packages/source/o/osprofiler/osprofiler-3.4.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-ddt
BuildRequires:  python3-docutils
BuildRequires:  python3-elasticsearch
BuildRequires:  python3-importlib-metadata
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
BuildArch:      noarch

%description
OSProfiler provides a tiny but powerful library that is used by
most (soon to be all) OpenStack projects and their python clients. It
provides functionality to be able to generate 1 trace per request, that goes
through all involved services. This trace can then be extracted and used
to build a tree of calls which can be quite handy for a variety of
reasons (for example in isolating cross-project performance issues).

%package -n python3-osprofiler
Summary:        OpenStack Profiler Library
Group:          Development/Languages/Python
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-WebOb >= 1.7.1
Requires:       python3-importlib-metadata
Requires:       python3-oslo.concurrency >= 3.26.0
Requires:       python3-oslo.config
Requires:       python3-oslo.log
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-six >= 1.10.0
%if 0%{?suse_version}
Obsoletes:      python2-osprofiler < 3.0.0
%endif

%description -n python3-osprofiler
OSProfiler provides a tiny but powerful library that is used by
most (soon to be all) OpenStack projects and their python clients. It
provides functionality to be able to generate 1 trace per request, that goes
through all involved services. This trace can then be extracted and used
to build a tree of calls which can be quite handy for a variety of
reasons (for example in isolating cross-project performance issues).

This package contains the Python 3.x module

%package -n python-osprofiler-doc
Summary:        Documentation for OSProfiler
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-osprofiler-doc
Documentation for OSProfiler.

%prep
%autosetup -p1 -n osprofiler-3.4.0
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
python3 -m stestr.cli run --black-regex '(^osprofiler.tests.unit.drivers.test_jaeger.JaegerTestCase.*$)'

%files -n python3-osprofiler
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/osprofiler
%{python3_sitelib}/*.egg-info
%{_bindir}/osprofiler

%files -n python-osprofiler-doc
%license LICENSE
%doc doc/build/html

%changelog
