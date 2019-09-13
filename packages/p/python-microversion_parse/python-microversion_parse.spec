#
# spec file for package python-microversion_parse
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


Name:           python-microversion_parse
Version:        0.2.1
Release:        0
Summary:        OpenStack microversion header parser
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/m/microversion_parse/microversion_parse-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-WebOb >= 1.2.3
BuildRequires:  python-gabbi
BuildRequires:  python-setuptools
BuildRequires:  python-stestr
BuildRequires:  python-testrepository
BuildRequires:  python-testtools
BuildArch:      noarch

%description
A simple parser for OpenStack microversion headers.

%package doc
Summary:        Documentation for OpenStack Microversion headers
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-oslosphinx

%description doc
This package contains thedocumentation for OpenStack microversion
headers parsing library.

%prep
%autosetup -n microversion_parse-%{version}
%py_req_cleanup

%build
%{py2_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py2_install}

%check
stestr run

%files
%license LICENSE
%doc ChangeLog README.rst
%{python2_sitelib}/microversion_parse
%{python2_sitelib}/microversion_parse*egg-info

%files doc
%license LICENSE
%doc doc/build/html

%changelog
