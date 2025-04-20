#
# spec file for package python-pmw
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


%{?sle15_python_module_pythons}
Name:           python-pmw
Version:        2.1.1
Release:        0
Summary:        High-level compound widgets in Python using the Tkinter module
License:        MIT
Group:          Development/Languages/Python
URL:            https://pmw.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/P/Pmw/Pmw-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tk
BuildArch:      noarch
%python_subpackages

%description
A toolkit for building high-level compound widgets in Python using the Tkinter
module. It contains a set of flexible and extensible megawidgets, including
notebooks, comboboxes, selection widgets, paned widgets, scrolled widgets and
dialog windows.

%prep
%autosetup -p1 -n Pmw-%{version}
sed -i '1d' Pmw/Pmw_1_3_3/{demos/All,bin/bundlepmw,tests/All,tests/ManualTests}.py # Fix non-executable scripts
sed -i '1d' Pmw/Pmw_2_1_1/{demos/All,bin/bundlepmw,tests/All,tests/ManualTests}.py # Fix non-executable scripts

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/[pP]mw
%{python_sitelib}/pmw-%{version}*-info

%changelog
