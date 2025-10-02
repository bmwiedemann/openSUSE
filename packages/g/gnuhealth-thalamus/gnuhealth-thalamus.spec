#
# spec file for package gnuhealth-thalamus
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2017-2025 Dr. Axel Braun
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


%bcond_without test 1

%define pythons python3
%define mypython python3
%define mysitelib %python_sitelib

%{?sle15_python_module_pythons}

%define modname thalamus
Name:           gnuhealth-%{modname}
Version:        0.9.16
Release:        0
Summary:        The GNU Health Federation Message and Authentication Server
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://health.gnu.org
Source:         https://files.pythonhosted.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  postgresql-server
BuildRequires:  python-rpm-macros

%if %{with test}
BuildRequires:  %{python_module Flask-Cors}
BuildRequires:  %{python_module Flask-HTTPAuth}
BuildRequires:  %{python_module Flask-RESTful}
BuildRequires:  %{python_module Flask-WTF}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module psycopg2}
%endif

Requires:       %{python_module Flask-HTTPAuth}
Requires:       %{python_module Flask-RESTful}
Requires:       %{python_module Flask-WTF}
Requires:       %{python_module Flask}
Requires:       %{python_module bcrypt}
Requires:       %{python_module psycopg2}
# postgres may run on own cluster
Suggests:       postgresql-server
BuildArch:      noarch

%python_subpackages

%description
Thalamus: The GNU Health Federation Message and Authentication Server
=====================================================================

The Thalamus project provides a RESTful API hub to all the GNU Health
Federation nodes. The main functions are:

#. **Message server**: A concentrator and message relay from and to
   the participating nodes in the GNU Health Federation and the GNU Health
   Information System (MongoDB). Some of the participating nodes include
   the GNU Health HMIS, MyGNUHealth mobile PHR application,
   laboratories, research institutions and civil offices.

#. **Authentication Server**: Thalamus also serves as an authentication and
   authorization server to interact with the GNUHealth Information System


Thalamus is part of the GNU Health project, but it is a self contained,
independent server that can be used in different health related scenarios.

%prep
%autosetup -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{mysitelib}

%files
%defattr(-,root,root)
%doc README.rst
%license LICENSE
%{mysitelib}/thalamus*

%changelog
