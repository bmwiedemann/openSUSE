#
# spec file for package python-bashate
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global skip_python2 1
Name:           python-bashate
Version:        2.0.0
Release:        0
Summary:        A PEP8 equivalent for bash scripts
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.org/project/bashate/
Source:         https://files.pythonhosted.org/packages/source/b/bashate/bashate-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 0.9.6}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-argparse
Requires:       python-Babel >= 0.9.6
Requires:       python-pbr
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-argparse
%endif
%python_subpackages

%description
A PEP8 equivalent for bash scripts

This program attempts to be an automated style checker for bash scripts
to fill the same part of code review that pep8 does in most OpenStack
projects. It started from humble beginnings in the DevStack project,
and will continue to evolve over time.

- Documentation: http://docs.openstack.org/developer/bashate
- Source: http://git.openstack.org/cgit/openstack-dev/bash8
- Bugs: http://bugs.launchpad.net/bash8

%prep
%setup -q -n bashate-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bashate
%{python_expand  #
rm -rf %{buildroot}%{$python_sitelib}/bashate/tests
sed -i -e '/^#!\//, 1d' %{buildroot}%{$python_sitelib}/bashate/bashate.py
}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m stestr.cli run

%post
%python_install_alternative bashate

%postun
%python_uninstall_alternative bashate

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst ChangeLog
%python_alternative %{_bindir}/bashate
%{python_sitelib}/*

%changelog
