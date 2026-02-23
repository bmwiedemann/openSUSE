#
# spec file for package python-oslo.reports
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        3.7.0
Release:        0
Summary:        OpenStack oslo.reports library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.reports
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_reports/oslo_reports-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module oslo.config >= 5.1.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil >= 3.2.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
Requires:       python-Jinja2 >= 2.10
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-psutil >= 3.2.2
BuildArch:      noarch
%python_subpackages

%description
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".

%package -n python-oslo.reports-doc
Summary:        Documentation for OpenStack reports library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.reports-doc
The project oslo.reports hosts a general purpose error report generation
framework, known as the "guru meditation report".
This package contains the documentation.

%prep
%autosetup -p1 -n oslo_reports-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/oslo_reports
%{python_sitelib}/oslo_reports-%{version}.dist-info

%files -n python-oslo.reports-doc
%license LICENSE
%doc doc/build/html

%changelog
