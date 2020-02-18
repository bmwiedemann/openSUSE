#
# spec file for package python-microversion_parse
#
# Copyright (c) 2019 SUSE LLC
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
URL:            https://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/m/microversion_parse/microversion_parse-0.2.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-WebOb >= 1.2.3
BuildRequires:  python2-gabbi
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testtools
BuildRequires:  python3-WebOb >= 1.2.3
BuildRequires:  python3-gabbi
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch
%python_subpackages

%description
A simple parser for OpenStack microversion headers.

%package -n python-microversion_parse-doc
Summary:        Documentation for OpenStack Microversion headers
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-oslosphinx

%description -n python-microversion_parse-doc
This package contains thedocumentation for OpenStack microversion
headers parsing library.

%prep
%autosetup -n microversion_parse-%{version}
%py_req_cleanup

%build
%python_build

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/microversion_parse
%{python_sitelib}/microversion_parse*egg-info

%files -n python-microversion_parse-doc
%license LICENSE
%doc doc/build/html

%changelog
