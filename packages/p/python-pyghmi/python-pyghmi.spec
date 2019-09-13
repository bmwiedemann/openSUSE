#
# spec file for package python-pyghmi
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


Name:           python-pyghmi
Version:        1.2.16
Release:        0
Summary:        General Hardware Management Initiative (IPMI and others)
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/pyghmi
Source0:        https://files.pythonhosted.org/packages/source/p/pyghmi/pyghmi-1.2.16.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-cryptography >= 2.1
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-oslotest
BuildRequires:  python2-stestr
BuildRequires:  python3-cryptography >= 2.1
BuildRequires:  python3-devel
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslotest
BuildRequires:  python3-stestr
Requires:       python-cryptography >= 2.1
BuildArch:      noarch
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
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

%package -n python-pyghmi-doc
Summary:        General Hardware Management Initiative (IPMI and others) -- Documentation
Group:          Documentation/HTML
BuildRequires:  python-Sphinx

%description -n python-pyghmi-doc
This is a pure python implementation of IPMI protocol.

pyghmicons and pyghmiutil are example scripts to show how one may incorporate
this library into python code

%prep
%autosetup -p1 -n pyghmi-%{version}
%py_req_cleanup

%build
%{python_build}

%{__python2} setup.py build_sphinx --builder=html
rm -rf html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/pyghmicons
%python_clone -a %{buildroot}%{_bindir}/pyghmiutil
%python_clone -a %{buildroot}%{_bindir}/virshbmc
%python_clone -a %{buildroot}%{_bindir}/fakebmc

%post
%python_install_alternative pyghmicons
%python_install_alternative pyghmiutil
%python_install_alternative virshbmc
%python_install_alternative fakebmc

%postun
%python_uninstall_alternative pyghmicons
%python_uninstall_alternative pyghmiutil
%python_uninstall_alternative virshbmc
%python_uninstall_alternative fakebmc

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.md ChangeLog
%license LICENSE
%python_alternative %{_bindir}/pyghmicons
%python_alternative %{_bindir}/pyghmiutil
%python_alternative %{_bindir}/virshbmc
%python_alternative %{_bindir}/fakebmc
%{python_sitelib}/pyghmi*
%{python_sitelib}/*.egg-info

%files -n python-pyghmi-doc
%doc doc/build/html
%license LICENSE

%changelog
