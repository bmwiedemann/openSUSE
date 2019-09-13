#
# spec file for package python-openstack-doc-tools
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


%global sname openstack-doc-tools
%global module os_doc_tools
Name:           python-openstack-doc-tools
Version:        1.8.0
Release:        0
Summary:        OpenStack Docs Tools
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-Babel
BuildRequires:  python-PyYAML >= 3.12
BuildRequires:  python-Sphinx
BuildRequires:  python-demjson >= 2.2.2
BuildRequires:  python-devel
BuildRequires:  python-lxml >= 3.4.1
BuildRequires:  python-mock
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-setuptools
BuildRequires:  python-testrepository
Requires:       python-PyYAML >= 3.12
Requires:       python-Sphinx
Requires:       python-iso8601 >= 0.1.11
Requires:       python-lxml >= 3.4.1
Requires:       python-openstackdocstheme
BuildArch:      noarch

%description
Tools used by the OpenStack Documentation Project.

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%py2_build

%install
%py2_install

%check
# We don't want to run the sitemap tests, it is not included in the package
rm -f test/test_sitemap_file.py test/test_pipelines.py
%{__python2} setup.py testr

%files
%license LICENSE
%doc README.rst
%{_bindir}/doc-tools-build-rst
%{_bindir}/doc-tools-check-languages
%{_bindir}/openstack-indexpage
%{_bindir}/openstack-jsoncheck
%{python2_sitelib}/%{module}
%{_datadir}/%{sname}
%{python2_sitelib}/*.egg-info

%changelog
