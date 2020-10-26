#
# spec file for package python-oslo.reports
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


Name:           python-oslo.reports
Version:        2.2.0
Release:        0
Summary:        OpenStack oslo.reports library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.reports
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.reports/oslo.reports-2.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Jinja2 >= 2.10
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
BuildArch:      noarch

%description
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".

%package -n python3-oslo.reports
Summary:        OpenStack oslo.reports library
Group:          Development/Languages/Python
Requires:       python3-Jinja2 >= 2.10
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-psutil >= 3.2.2
Requires:       python3-six >= 1.10.0

%description -n python3-oslo.reports
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".

%package -n python-oslo.reports-doc
Summary:        Documentation for OpenStack reports library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.reports-doc
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.reports-2.2.0
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-oslo.reports
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/oslo_reports
%{python3_sitelib}/*.egg-info

%files -n python-oslo.reports-doc
%license LICENSE
%doc doc/build/html

%changelog
