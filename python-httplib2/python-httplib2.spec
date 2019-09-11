#
# spec file for package python-httplib2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# Tests require network connection
%bcond_with tests

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-httplib2
Version:        0.10.3
Release:        0
Url:            https://github.com/httplib2/httplib2
Summary:        A Python HTTP client library
License:        MIT AND Apache-2.0 AND (MPL-1.1 OR GPL-2.0+ OR LGPL-2.1+)
Group:          Development/Libraries/Python
Source:         https://files.pythonhosted.org/packages/source/h/httplib2/httplib2-%{version}.tar.gz
# PATCH-FIX-OPENSUSE: Don't ship private copy of Mozilla NSS certs, use system certs instead (bnc#761162)
Patch0:         httplib2-use-system-certs.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with tests}
# Test requirements (for ssl module):
BuildRequires:  python
BuildRequires:  python3
%endif
Requires:       ca-certificates
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
A comprehensive HTTP client library that supports many features
left out of other HTTP libraries.


%prep
%setup -q -n httplib2-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install

%if %{with tests}
%check
%if %have_python2
python2 python2/httplib2test.py
%endif
%if %have_python2
python3 python3/httplib2test.py
%endif
%endif

%files %{python_files}
%defattr(-,root,root)
%{python_sitelib}/httplib2-%{version}-py*.egg-info
%{python_sitelib}/httplib2

%changelog
