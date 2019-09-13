#
# spec file for package python-oslo.reports
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


Name:           python-oslo.reports
Version:        1.29.2
Release:        0
Summary:        OpenStack oslo.reports library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.reports
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.reports/oslo.reports-1.29.2.tar.gz
# https://review.openstack.org/588088
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-Jinja2 >= 2.10
BuildRequires:  python2-eventlet
BuildRequires:  python2-greenlet
BuildRequires:  python2-oslo.config
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-psutil >= 3.2.2
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-devel
BuildRequires:  python3-eventlet
BuildRequires:  python3-greenlet
BuildRequires:  python3-oslo.config
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-psutil >= 3.2.2
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
Requires:       python-Jinja2 >= 2.10
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-psutil >= 3.2.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%{python_subpackages}

%description
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".

%package -n python-oslo.reports-doc
Summary:        Documentation for OpenStack reports library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.reports-doc
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.reports-1.29.2
%py_req_cleanup

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python2_sitelib}/oslo_reports
%{python2_sitelib}/*.egg-info

%files -n python-oslo.reports-doc
%license LICENSE
%doc doc/build/html

%changelog
