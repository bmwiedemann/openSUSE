#
# spec file for package python-os-testr
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


Name:           python-os-testr
Version:        1.0.0
Release:        0
Summary:        A testr wrapper to provide functionality for OpenStack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/os-testr
Source0:        https://files.pythonhosted.org/packages/source/o/os-testr/os-testr-1.0.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-ddt
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-six
BuildRequires:  python2-stestr >= 1.0.0
BuildRequires:  python2-testscenarios
BuildRequires:  python3-ddt
BuildRequires:  python3-devel
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-six
BuildRequires:  python3-stestr >= 1.0.0
BuildRequires:  python3-testscenarios
Requires:       python-pbr >= 2.0.0
Requires:       python-python-subunit >= 1.0.0
Requires:       python-stestr >= 1.0.0
Requires:       python-testtools >= 2.2.0
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
A testr wrapper to provide functionality for OpenStack projects
* Documentation: https://docs.openstack.org/developer/os-testr
* Source: http://git.openstack.org/cgit/openstack/os-testr
* Bugs: https://bugs.launchpad.net/os-testr

%package -n python-os-testr-doc
Summary:        Documentation for the testr
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-os-testr-doc
Documentation for the testr wrapper.

%prep
%autosetup -p1 -n os-testr-1.0.0
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/generate-subunit
%python_clone -a %{buildroot}%{_bindir}/ostestr
%python_clone -a %{buildroot}%{_bindir}/subunit-trace
%python_clone -a %{buildroot}%{_bindir}/subunit2html

%post
%python_install_alternative generate-subunit
%python_install_alternative ostestr
%python_install_alternative subunit-trace
%python_install_alternative subunit2html

%postun
%python_uninstall_alternative generate-subunit
%python_uninstall_alternative ostestr
%python_uninstall_alternative subunit-trace
%python_uninstall_alternative subunit2html

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%python_alternative %{_bindir}/generate-subunit
%python_alternative %{_bindir}/ostestr
%python_alternative %{_bindir}/subunit-trace
%python_alternative %{_bindir}/subunit2html
%{python_sitelib}/os_testr
%{python_sitelib}/os_testr*egg-info

%files -n python-os-testr-doc
%license LICENSE
%doc doc/build/html README.rst ChangeLog

%changelog
