#
# spec file for package python-openstack-doc-tools
#
# Copyright (c) 2020 SUSE LLC
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


%global module os_doc_tools
Name:           python-openstack-doc-tools
Version:        3.3.0
Release:        0
Summary:        OpenStack Docs Tools
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/openstack-doc-tools
Source0:        https://files.pythonhosted.org/packages/source/o/openstack-doc-tools/openstack-doc-tools-3.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-Sphinx
BuildRequires:  python3-demjson
BuildRequires:  python3-lxml >= 4.5.0
BuildRequires:  python3-mock
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-pbr >= 2.0.0
BuildArch:      noarch

%description
Tools used by the OpenStack Documentation Project.

%package -n python3-openstack-doc-tools
Summary:        OpenStack Docs Tools
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.13
Requires:       python3-Sphinx
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-lxml >= 4.5.0
Requires:       python3-openstackdocstheme
%if 0%{?suse_version}
Obsoletes:      python2-openstack-doc-tools < 1.8.0
%endif

%description -n python3-openstack-doc-tools
Tools used by the OpenStack Documentation Project.

This package contains the Python 3.x module.

%prep
%autosetup -n openstack-doc-tools-%{version}
%py_req_cleanup

%build
%py3_build

%install
%py3_install

%files -n python3-openstack-doc-tools
%license LICENSE
%doc README.rst
%{_bindir}/doc-tools-build-rst
%{_bindir}/doc-tools-check-languages
%{python3_sitelib}/%{module}
%{_datadir}/openstack-doc-tools
%{python3_sitelib}/*.egg-info

%changelog
