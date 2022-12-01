#
# spec file for package python-swiftclient
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


Name:           python-swiftclient
Version:        4.1.0
Release:        0
Summary:        OpenStack Object Storage API Client Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-swiftclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-swiftclient/python-swiftclient-4.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-pbr
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildArch:      noarch

%description
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

%package -n python3-swiftclient
Summary:        OpenStack Object Storage API Client Library
Requires:       python3-requests >= 1.1.0
%if 0%{?suse_version}
Obsoletes:      python2-swiftclient < 3.9.0
%endif

%description -n python3-swiftclient
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

This package contains the Python 3.x module.

%package -n python-swiftclient-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-swiftclient-doc
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n python-swiftclient-4.1.0
%py_req_cleanup

%build
%{py3_build}
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-swiftclient
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/swiftclient
%{python3_sitelib}/*.egg-info
%{_bindir}/swift
%{_mandir}/man1/swift.1*

%files -n python-swiftclient-doc
%license LICENSE
%doc doc/build/html

%changelog
