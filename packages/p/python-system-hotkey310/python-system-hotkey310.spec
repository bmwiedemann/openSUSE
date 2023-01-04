#
# spec file for package python-system-hotkey310
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-system-hotkey310
Version:        1.0.5
Release:        0
Summary:        System wide hotkeys
License:        BSD-3-Clause
URL:            https://github.com/hhannine/system_hotkey310
Source0:        https://files.pythonhosted.org/packages/source/s/system_hotkey310/system_hotkey310-%{version}.tar.gz
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xcffib}
BuildRequires:  %{python_module xpybutil}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(xcb)
Requires:       python-xcffib
Requires:       python-xpybutil
Conflicts:      python-system_hotkey
BuildArch:      noarch
%python_subpackages

%description
System wide hotkeys for python 3.

%prep
%setup -q -n system_hotkey310-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests in pypi package
# %%pytest

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/system_hotkey
%{python_sitelib}/*egg-info

%changelog
