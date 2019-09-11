#
# spec file for package python-textfsm
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


%define oldpython python
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-textfsm
Version:        1.1.0
Release:        0
Summary:        Python module for parsing semi-structured text into python tables
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/google/textfsm
Source:         https://github.com/google/textfsm/archive/v%{version}.tar.gz
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Requires:       python-six
%ifpython2
Requires:       python-future
%endif
Conflicts:      python-texttable
BuildArch:      noarch
%ifpython2
Conflicts:      %{oldpython}-texttable
%endif
%python_subpackages

%description
Python module which implements a template based state machine for parsing
semi-formatted text. Originally developed to allow programmatic access to
information returned from the command line interface (CLI) of networking
devices.

%prep
%setup -q -n textfsm-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/*

%changelog
