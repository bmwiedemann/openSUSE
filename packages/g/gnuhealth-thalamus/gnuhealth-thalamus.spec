#
# spec file for package gnuhealth-thalamus
#
# Copyright (c) 2019 SUSE LLC.
# Copyright (c) 2017-2019 Dr. Axel Braun
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


%bcond_without test

%define modname thalamus
Name:           gnuhealth-%{modname}
Version:        0.9.11
Release:        0
Summary:        The GNU Health Federation Message and Authentication Server
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://health.gnu.org
Source:         https://files.pythonhosted.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  postgresql-server
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with test}
BuildRequires:  python3-Flask
BuildRequires:  python3-Flask-HTTPAuth
BuildRequires:  python3-Flask-RESTful
BuildRequires:  python3-Flask-WTF
BuildRequires:  python3-bcrypt
BuildRequires:  python3-psycopg2
%endif
BuildRequires:  fdupes
Requires:       postgresql-server
Requires:       python3-Flask
Requires:       python3-Flask-HTTPAuth
Requires:       python3-Flask-RESTful
Requires:       python3-Flask-WTF
Requires:       python3-bcrypt
Requires:       python3-psycopg2
BuildArch:      noarch

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
%setup -q -n %{modname}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix="%{_prefix}" --root=%{buildroot}
%fdupes %{buildroot}%{$python_sitelib}

%files
%defattr(-,root,root)
%doc README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
