#
# spec file for package python-bugzillatools
#
# Copyright (c) 2025 SUSE LLC
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


%define oldpython python
%bcond_without libalternatives
Name:           python-bugzillatools
Version:        0.5.5
Release:        0
Summary:        Bugzilla CLI client, XML-RPC binding and VCS plugins
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/frasertweedale/bugzillatools
Source:         https://files.pythonhosted.org/packages/source/b/bugzillatools/bugzillatools-%{version}.tar.gz
# Port to Python3 from yet unreleased commits in the upstream repo
Patch0:         0001-Working-on-both-2.7-and-3.4.patch
# Some more py3k fixes
# https://github.com/rawrgulmuffins/bugzillatools/pull/26
Patch1:         no-bzrlib-py3k.patch
# PATCH-FIX-OPENSUSE python312.patch
Patch2:         python312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
# We want to conflict even package literally called python-bugzilla
# without the python version number
Conflicts:      %{oldpython}-bugzilla
#Recommends:     bzr
# File conflict for /usr/bin/bugzilla with all lang flavours:
Conflicts:      %{python_module bugzilla}
BuildArch:      noarch
%python_subpackages

%description
Provides a CLI program and Python library for interacting with the
Bugzilla_ bug tracking system, and plugins for version control
systems that enable interaction with Bugzilla installations.

%prep
%autosetup -p1 -n bugzillatools-%{version}

sed -i "/.bugzillarc.sample/d" setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bugzilla
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%pre
%python_libalternatives_reset_alternative bugzilla

%files %{python_files}
%doc CHANGES README.rst gpl-3.0.txt
%python_alternative %{_bindir}/bugzilla
%{python_sitelib}/bzlib
%{python_sitelib}/bzrlib
%{python_sitelib}/bugzillatools-%{version}.dist-info

%changelog
