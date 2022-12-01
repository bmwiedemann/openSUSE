#
# spec file for package python-renderspec
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


%global oldpython python
Name:           python-renderspec
Version:        2.2.0
Release:        0
Summary:        Generate spec files from Jinja2 templates
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/renderspec
Source0:        https://files.pythonhosted.org/packages/source/r/renderspec/renderspec-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Jinja2 >= 2.10
BuildRequires:  python3-ddt
BuildRequires:  python3-packaging >= 16.5
BuildRequires:  python3-pbr
BuildRequires:  python3-pymod2pkg >= 0.7.0
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
renderspec is a tool to convert a .spec.j2 Jinja2 template to
a rpm .spec file which is usable for different distributions
and follow their policies and processes.

%package -n python3-renderspec
Summary:        Generate spec files from Jinja2 templates
Requires:       python3-Jinja2 >= 2.10
Requires:       python3-PyYAML >= 3.10
Requires:       python3-packaging >= 16.5
Requires:       python3-pymod2pkg >= 0.7.0
Conflicts:      %{oldpython}-renderspec < %{version}

%description -n python3-renderspec
renderspec is a tool to convert a .spec.j2 Jinja2 template to
a rpm .spec file which is usable for different distributions
and follow their policies and processes.

%package -n python-renderspec-doc
Summary:        Documentation for the renderspec utility
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
Requires:       python3-renderspec = %{version}

%description -n python-renderspec-doc
Documentation for the renderspec tool which is a tool to convert
a spec.j2 Jinja2 template into a rpm .spec file.

%prep
%autosetup -p 1 -n renderspec-2.2.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=2.2.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-renderspec
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/renderspec
%{python3_sitelib}/renderspec
%{python3_sitelib}/*.egg-info

%files -n python-renderspec-doc
%doc doc/build/html
%license LICENSE

%changelog
