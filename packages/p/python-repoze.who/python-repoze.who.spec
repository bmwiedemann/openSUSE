#
# spec file for package python-repoze.who
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global modname repoze.who
Name:           python-repoze.who
Version:        2.4.1
Release:        0
Summary:        Identification and authentication framework for WSGI
License:        SUSE-Repoze
URL:            http://www.repoze.org
Source:         https://files.pythonhosted.org/packages/source/r/repoze.who/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebOb
Requires:       python-zope.interface
BuildArch:      noarch
%python_subpackages

%description
repoze.who is an identification and authentication framework
for arbitrary WSGI applications.  repoze.who can be configured
either as WSGI middleware or as an API for use by an application.

repoze.who is inspired by Zope 2's Pluggable Authentication
Service (PAS) (but repoze.who is not dependent on Zope in any
way; it is useful for any WSGI application).  It provides no facility
for authorization (ensuring whether a user can or cannot perform the
operation implied by the request).  This is considered to be the
domain of the WSGI application.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc *.txt
%{python_sitelib}/*

%changelog
