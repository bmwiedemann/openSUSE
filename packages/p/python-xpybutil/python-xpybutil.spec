#
# spec file for package python-xpybutil
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


Name:           python-xpybutil
Version:        0.0.6
Release:        0
Summary:        Abstraction over xpyb
License:        WTFPL
Group:          Development/Languages/Python
URL:            https://github.com/BurntSushi/xpybutil
Source:         https://github.com/BurntSushi/xpybutil/archive/%{version}.tar.gz
Patch0:         python-xpybutil-0.0.5-remove-selftest.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xcffib}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xcffib
BuildArch:      noarch
%python_subpackages

%description
xpybutil is an abstraction over the X Python Binding (xpyb). It exists because xpyb is a very low level library that communicates with X.

%prep
%autosetup -p1 -n xpybutil-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/xpybutil
%{python_sitelib}/xpybutil-%{version}.dist-info

%changelog
