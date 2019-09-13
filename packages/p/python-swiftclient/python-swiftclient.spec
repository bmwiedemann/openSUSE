#
# spec file for package python-swiftclient
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


Name:           python-swiftclient
Version:        3.7.0
Release:        0
Summary:        OpenStack Object Storage API Client Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-swiftclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-swiftclient/python-swiftclient-3.7.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-mock
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mock
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
Requires:       python-requests >= 1.1.0
Requires:       python-six >= 1.9.0
BuildArch:      noarch
%ifpython2
Requires:       python-futures >= 3.0.0
%endif
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

%package -n python-swiftclient-doc
Summary:        %{summary} - Documentation
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-futures >= 3.0.0
BuildRequires:  python-openstackdocstheme
Requires:       %{name} = %{version}

%description -n python-swiftclient-doc
This is a python client for the Swift API. There's a Python API (the
swiftclient module), and a command-line script (swift).

This package contains documentation files for %{name}.

%prep
%autosetup -p1 -n python-swiftclient-3.7.0
%py_req_cleanup

%build
%{python_build}
%{__python2} setup.py build_sphinx
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/swift
%python_clone -a %{buildroot}%{_mandir}/man1/swift.1

%post
%{python_install_alternative swift swift.1}

%postun
%python_uninstall_alternative swift

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/swiftclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/swift
%python_alternative %{_mandir}/man1/swift.1

%files -n python-swiftclient-doc
%license LICENSE
%doc doc/build/html

%changelog
