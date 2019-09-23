#
# spec file for package python-pmw
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define oldpython python
Name:           python-pmw
Version:        2.0.1
Release:        0
Summary:        High-level compound widgets in Python using the Tkinter module
License:        MIT
Group:          Development/Languages/Python
URL:            http://pmw.sourceforge.net/
Source:         https://files.pythonhosted.org/packages/source/P/Pmw/Pmw-%{version}.tar.gz
#PATCH-FIX-UPSTREAM py36.patch https://sourceforge.net/p/pmw/patches/7/
Patch0:         py36.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tk
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-pmw < %{version}
Provides:       %{oldpython}-pmw = %{version}
%endif
%python_subpackages

%description
A toolkit for building high-level compound widgets in Python using the Tkinter
module. It contains a set of flexible and extensible megawidgets, including
notebooks, comboboxes, selection widgets, paned widgets, scrolled widgets and
dialog windows.

%prep
%setup -q -n Pmw-%{version}
%patch0
sed -i '1d' Pmw/Pmw_1_3_3/{demos/All,bin/bundlepmw,tests/All,tests/ManualTests}.py # Fix non-executable scripts
sed -i '1d' Pmw/Pmw_2_0_1/{demos/All,bin/bundlepmw,tests/All,tests/ManualTests}.py # Fix non-executable scripts

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*

%changelog
