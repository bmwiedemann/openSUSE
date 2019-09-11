#
# spec file for package python-renderspec
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global sname renderspec
Name:           python-renderspec
Version:        1.9.1
Release:        0
Summary:        Generate spec files from Jinja2 templates
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://launchpad.net/%{sname}
Source0:        https://pypi.io/packages/source/r/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python-pbr >= 2.0.0
Requires:       python-Jinja2 >= 2.8
Requires:       python-PyYAML >= 3.10.0
Requires:       python-packaging >= 16.5
Requires:       python-pymod2pkg >= 0.7.0
Requires:       python-six >= 1.9.0
BuildArch:      noarch

%description
renderspec is a tool to convert a .spec.j2 Jinja2 template to
a rpm .spec file which is usable for different distributions
and follow their policies and processes.

%package doc
Summary:        Documentation for the renderspec utility
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-oslosphinx >= 4.7.0
Requires:       %{name} = %{version}

%description doc
Documentation for the renderspec tool which is a tool to convert
a spec.j2 Jinja2 template into a rpm .spec file.

%prep
%autosetup -p 1 -n %{sname}-%{version}
%py_req_cleanup

%build
%{py2_build}

%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py2_install}

%files
%license LICENSE
%doc README.rst ChangeLog
%{_bindir}/%{sname}
%{python2_sitelib}/%{sname}
%{python2_sitelib}/*.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
