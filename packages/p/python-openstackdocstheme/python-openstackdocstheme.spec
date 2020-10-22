#
# spec file for package python-openstackdocstheme
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


Name:           python-openstackdocstheme
Version:        2.2.5
Release:        0
Summary:        OpenStack Docs Theme
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/openstackdocstheme/openstackdocstheme-2.2.5.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Sphinx
BuildRequires:  python3-dulwich >= 0.15.0
BuildRequires:  python3-pbr >= 2.0.0
BuildArch:      noarch

%description
Theme and extension support for Sphinx documentation that is published
to docs.openstack.org. Intended for use by OpenStack projects.

%package -n python3-openstackdocstheme
Summary:        OpenStack Docs Theme
Group:          Development/Languages/Python
Requires:       python3-Sphinx
Requires:       python3-dulwich >= 0.15.0

%description -n python3-openstackdocstheme
Theme and extension support for Sphinx documentation that is published
to docs.openstack.org. Intended for use by OpenStack projects.

%prep
%autosetup -p1 -n openstackdocstheme-2.2.5

# we dont need hacking
sed -i '/^hacking.*/d' test-requirements.txt
%py_req_cleanup

%build
%py3_build

%install
%py3_install

%check
python3 setup.py test

%files -n python3-openstackdocstheme
%license LICENSE
%doc README.rst
%{_bindir}/docstheme-build-pdf
%{_bindir}/docstheme-build-translated.sh
%{_bindir}/docstheme-lang-display-name.py
%exclude %{_sysconfdir}/alternatives/*.pyc
%exclude %{_sysconfdir}/alternatives/*.pyo
%{python3_sitelib}/openstackdocstheme
%{python3_sitelib}/openstackdocstheme-*-py?.?.egg-info

%changelog
