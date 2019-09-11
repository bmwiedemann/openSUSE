#
# spec file for package python-reno
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


Name:           python-reno
Version:        2.11.3
Release:        0
Summary:        RElease NOtes manager
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/r/reno/reno-2.11.3.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PyYAML
BuildRequires:  python2-Sphinx
BuildRequires:  python2-docutils
BuildRequires:  python2-dulwich
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PyYAML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-docutils
BuildRequires:  python3-dulwich
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-PyYAML
Requires:       python-Sphinx
Requires:       python-docutils
Requires:       python-dulwich
Requires:       python-pbr
Requires:       python-six
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  git-core
BuildRequires:  gpg2
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
BuildRequires:  git
BuildRequires:  gnupg
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
Reno is a release notes manager for storing release notes in a git
repository and then building documentation from them.

%prep
%autosetup -p1 -n reno-2.11.3
# we dont need hacking
sed -i '/^hacking.*/d' test-requirements.txt
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/reno

%post
%python_install_alternative reno

%postun
%python_uninstall_alternative reno

%check
rm -rf .git
git init .
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/reno
%{python_sitelib}/reno
%{python_sitelib}/*.egg-info

%changelog
