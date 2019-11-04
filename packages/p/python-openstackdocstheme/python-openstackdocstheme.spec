#
# spec file for package python-openstackdocstheme
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


Name:           python-openstackdocstheme
Version:        1.31.1
Release:        0
Summary:        OpenStack Docs Theme
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/o/openstackdocstheme/openstackdocstheme-1.31.1.tar.gz
# https://review.opendev.org/677868
Patch0:         0001-Catch-any-exception-when-trying-to-call-git.patch
BuildRequires:  openstack-macros
BuildRequires:  python2-Sphinx
BuildRequires:  python2-dulwich >= 0.15.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-setuptools
BuildRequires:  python3-Sphinx
BuildRequires:  python3-dulwich >= 0.15.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-setuptools
Requires:       python-Sphinx
Requires:       python-dulwich >= 0.15.0
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
Theme and extension support for Sphinx documentation that is published
to docs.openstack.org. Intended for use by OpenStack projects.

%prep
%autosetup -p1 -n openstackdocstheme-1.31.1

# we dont need hacking
sed -i '/^hacking.*/d' test-requirements.txt
%py_req_cleanup

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/docstheme-build-pdf
%python_clone -a %{buildroot}%{_bindir}/docstheme-build-translated.sh
%python_clone -a %{buildroot}%{_bindir}/docstheme-lang-display-name.py

%post
%{python_install_alternative docstheme-build-pdf docstheme-build-translated.sh docstheme-lang-display-name.py}

%postun
%python_uninstall_alternative docstheme-build-pdf

%check
%{python_expand rm -rf .testrepository
$python setup.py test
}

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/docstheme-build-pdf
%python_alternative %{_bindir}/docstheme-build-translated.sh
%python_alternative %{_bindir}/docstheme-lang-display-name.py
%exclude %{_sysconfdir}/alternatives/*.pyc
%exclude %{_sysconfdir}/alternatives/*.pyo
%{python_sitelib}/openstackdocstheme
%{python_sitelib}/openstackdocstheme-*-py?.?.egg-info

%changelog
