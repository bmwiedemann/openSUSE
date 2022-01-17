#
# spec file for package python-traitsui
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-traitsui
Version:        7.2.1
Release:        0
Summary:        Traits-capable windowing framework
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
Group:          Development/Libraries/Python
URL:            https://github.com/enthought/traitsui
Source:         https://files.pythonhosted.org/packages/source/t/traitsui/traitsui-%{version}.tar.gz
# PATCH-FIX-UPSTREAM traitsui-pr1689-deprecations.patch -- gh#enthought/traitsui#1689 + gh#enthought/traitsui#1681
Patch0:         traitsui-pr1689-deprecations.patch
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module pyface >= 7.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traits >= 6.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyface >= 7.3
Requires:       python-traits >= 6.2
Recommends:     python-configobj
Recommends:     python-qt5
Recommends:     python-wxWidgets
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module wxPython >= 4}
BuildRequires:  Mesa-dri
# /SECTION
%python_subpackages

%description
The TraitsGUI project contains a toolkit-independent GUI abstraction layer
(known as Pyface), which is used to support the "visualization" features of
the Traits package. Thus, you can write code in terms of the Traits API
(views, items, editors, etc.), and let TraitsGUI and your selected toolkit
and back-end take care of the details of displaying them.

Part of the Enthought Tool Suite (ETS).

%prep
%autosetup -p1 -n traitsui-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
ln -sf examples/tutorials/doc_exmaples/default.css examples/tutorials/traitsui_4.0/default.css

%check
export LANG=en_US.UTF-8
# different splitters?
donttest="test_splitter_prefs_are_restored"
%pytest traitsui/tests -k "not ($donttest)"

%files %{python_files}
%doc README.rst
%doc docs/traits*.*
%doc examples/
%license LICENSE.txt image_LICENSE*.txt
%{python_sitelib}/traitsui/
%{python_sitelib}/traitsui-%{version}*-info

%changelog
