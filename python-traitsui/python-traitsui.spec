#
# spec file for package python-traitsui
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
%define         X_display         ":98"
Name:           python-traitsui
Version:        6.1.2
Release:        0
Summary:        Traits-capable windowing framework
License:        BSD-3-Clause and EPL-1.0 and LGPL-2.1 and LGPL-3.0
Group:          Development/Libraries/Python
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
Url:            https://github.com/enthought/traitsui
Source:         https://files.pythonhosted.org/packages/source/t/traitsui/traitsui-%{version}.tar.gz
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pyface}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module traits}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  Mesa-dri
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module wxPython}
BuildRequires:  python-mock
BuildRequires:  xorg-x11-server
# /SECTION
Requires:       python-configobj
Requires:       python-pyface
Requires:       python-six
Requires:       python-traits
Recommends:     python-qt5
Recommends:     python-wxWidgets
%ifpython2
Provides:       %{oldpython}-TraitsGUI = %{version}
Obsoletes:      %{oldpython}-TraitsGUI < %{version}
Provides:       %{oldpython}-TraitsBackendQt = %{version}
Obsoletes:      %{oldpython}-TraitsBackendQt < %{version}
Provides:       %{oldpython}-TraitsBackendWx = %{version}
Obsoletes:      %{oldpython}-TraitsBackendWx < %{version}
%endif
BuildArch:      noarch

%python_subpackages

%description
The TraitsGUI project contains a toolkit-independent GUI abstraction layer
(known as Pyface), which is used to support the "visualization" features of
the Traits package. Thus, you can write code in terms of the Traits API
(views, items, editors, etc.), and let TraitsGUI and your selected toolkit
and back-end take care of the details of displaying them.

Part of the Enthought Tool Suite (ETS).

%prep
%setup -q -n traitsui-%{version}

%build
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/traitsui/wx/extra/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/traitsui/wx/extra/
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/traitsui/wx/extra/windows/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/traitsui/wx/extra/windows/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
export LANG=en_US.UTF-8
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%{python_expand mkdir tester_%{$python_bin_suffix}
pushd tester_%{$python_bin_suffix}
export PYTHONPATH=%{buildroot}%{$python_sitelib}
nosetests-%{$python_bin_suffix} -v traitsui.tests --exclude=wx --exclude=test_splitter_prefs_are_restored
popd
}

%files %{python_files}
%doc CHANGES.txt README.rst TODO.txt
%doc docs/README.rst docs/traits*.*
%doc examples/
%license LICENSE.txt image_LICENSE*.txt
%{python_sitelib}/traitsui/
%{python_sitelib}/traitsui-%{version}-py*.egg-info

%changelog
