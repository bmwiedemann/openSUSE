#
# spec file for package python-linecache2
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-linecache2
Version:        1.0.0
Release:        0
Summary:        Backports of the linecache module
# This is a backport of code taken from the Python codebase,
# and such is under the same license as Python as a whole.
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/testing-cabal/linecache2
Source:         https://pypi.io/packages/source/l/linecache2/linecache2-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#!BuildIgnore:  python2-pyparsing
#!BuildIgnore:  python3-pyparsing
Requires:       python-pbr
BuildArch:      noarch
%python_subpackages

%description
A backport of linecache to older supported Pythons.

%prep
%setup -q -n linecache2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst AUTHORS ChangeLog
# Contains the license
%doc setup.cfg
%{python_sitelib}/linecache2
%{python_sitelib}/linecache2-%{version}-py*.egg-info

%changelog
