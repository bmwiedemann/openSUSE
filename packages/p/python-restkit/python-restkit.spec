#
# spec file for package python-restkit
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


Name:           python-restkit
Version:        4.2.2
Release:        0
Summary:        Python REST kit
License:        MIT
Group:          Development/Languages/Python
Url:            http://benoitc.github.com/restkit
Source:         http://pypi.python.org/packages/source/r/restkit/restkit-%{version}.tar.gz
# PATCH-FIX-UPSTREAM / orphaned https://github.com/benoitc/restkit/pull/145
Patch0:         reproducible.patch
BuildRequires:  python-Sphinx
BuildRequires:  python-WebOb
BuildRequires:  python-devel
BuildRequires:  python-http-parser
BuildRequires:  python-nose
BuildRequires:  python-setuptools
BuildRequires:  python-socketpool
Requires:       python-WebOb
Requires:       python-http-parser
Requires:       python-socketpool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
Restkit is an HTTP resource kit for Python. It allows you to easily access to
HTTP resource and build objects around it. It's the base of couchdbkit, a
Python CouchDB framework.

Restkit is a full HTTP client using pure socket calls and its own HTTP parser.
It's not based on httplib or urllib2.

%prep
%setup -q -n restkit-%{version}
%patch0 -p1

%build
python setup.py build
cd doc
export PYTHONPATH=../
make html && rm -r _build/html/.buildinfo

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -rf %{buildroot}%{_prefix}/restkit # Remove wrongly installed documentation
rm -rf %{buildroot}%{python_sitelib}/tests # Remove global "tests" module

# Fail for instance
#%check
#python setup.py test

%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE README.rst THANKS TODO.txt examples doc/_build/html
%{_bindir}/restcli
%{python_sitelib}/*

%changelog
