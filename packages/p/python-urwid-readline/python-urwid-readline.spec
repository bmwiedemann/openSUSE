#
# spec file for package python-urwid-readline
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without python2
%{?sle15_python_module_pythons}
Name:           python-urwid-readline
Version:        0.13
Release:        0
Summary:        Text input widget for urwid that supports readline shortcuts
License:        MIT
URL:            https://pypi.org/project/urwid-readline/
Source:         https://files.pythonhosted.org/packages/source/u/urwid-readline/urwid_readline-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module urwid}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:  python-urwid

%python_subpackages

%description
Urwid-readline is a text input widget that supports readline shortcuts. Needed
by many apps like pudb.

%prep
%autosetup -p1 -n "urwid_readline-%{version}"

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.md
%{python_sitelib}/urwid_readline/
%{python_sitelib}/urwid_readline-%{version}-py%{python_version}.egg-info

%changelog
