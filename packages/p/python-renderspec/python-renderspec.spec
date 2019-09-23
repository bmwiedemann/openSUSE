#
# spec file for package python-renderspec
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


%global oldpython python
Name:           python-renderspec
Version:        1.12.0
Release:        0
Summary:        Generate spec files from Jinja2 templates
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/renderspec
Source0:        https://files.pythonhosted.org/packages/source/r/renderspec/renderspec-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-Jinja2 >= 2.10
BuildRequires:  python2-ddt
BuildRequires:  python2-mock
BuildRequires:  python2-packaging >= 16.5
BuildRequires:  python2-pbr
BuildRequires:  python2-pymod2pkg >= 0.7.0
BuildRequires:  python2-stestr
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-ddt
BuildRequires:  python3-mock
BuildRequires:  python3-packaging >= 16.5
BuildRequires:  python3-pbr
BuildRequires:  python3-pymod2pkg >= 0.7.0
BuildRequires:  python3-stestr
Requires:       python-Jinja2 >= 2.10
Requires:       python-PyYAML >= 3.10
Requires:       python-packaging >= 16.5
Requires:       python-pymod2pkg >= 0.7.0
Requires:       python-six >= 1.10.0
Conflicts:      %{oldpython}-renderspec < %{version}
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
renderspec is a tool to convert a .spec.j2 Jinja2 template to
a rpm .spec file which is usable for different distributions
and follow their policies and processes.

%package -n python-renderspec-doc
Summary:        Documentation for the renderspec utility
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
Requires:       %{name} = %{version}

%description -n python-renderspec-doc
Documentation for the renderspec tool which is a tool to convert
a spec.j2 Jinja2 template into a rpm .spec file.

%prep
%autosetup -p 1 -n renderspec-1.12.0
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=1.12.0 sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%if 0%{?suse_version}
%python3_only %{_bindir}/renderspec
%else
%{_bindir}/renderspec
%endif
%{python_sitelib}/renderspec
%{python_sitelib}/*.egg-info

%files -n python-renderspec-doc
%doc doc/build/html
%license LICENSE

%changelog
