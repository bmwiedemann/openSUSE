#
# spec file for package python-pyface
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


Name:           python-pyface
Version:        8.0.0
Release:        0
Summary:        Traits-capable windowing framework
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND SUSE-Public-Domain
URL:            https://github.com/enthought/pyface
Source:         https://files.pythonhosted.org/packages/source/p/pyface/pyface-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix-wx-tests.patch
Patch0:         fix-wx-tests.patch
# PATCH-FIX-UPSTREAM skip-qt4-tests.patch gh#enthought/pyface#1252 mcepl@suse.com
Patch1:         skip-qt4-tests.patch
# gh#enthought/pyface#1255, might be pulled in by wxPython
# BuildRequires:  %%{python_module Pillow}
#!BuildIgnore:  python39-Pillow
#!BuildIgnore:  python310-Pillow
#!BuildIgnore:  python311-Pillow
#!BuildIgnore:  python312-Pillow
#!BuildIgnore:  python313-Pillow
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.10}
BuildRequires:  %{python_module importlib-resources >= 1.1.0 if %python-base < 3.9}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module qtwebengine-qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traits >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wxWidgets}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
%if %{python_version_nodots} < 310
Requires:       python-importlib-metadata
%endif
%if %{python_version_nodots} < 39
Requires:       python-importlib-resources >= 1.1.0
%endif
Requires:       python-traits >= 6.2
Recommends:     python-Pygments
Recommends:     python-numpy
Recommends:     python-qt5
Recommends:     python-qtwebengine-qt5
Recommends:     python-traitsui
Recommends:     python-wxWidgets
BuildArch:      noarch

%python_subpackages

%description
The pyface project contains a toolkit-independent GUI abstraction layer,
which is used to support the "visualization" features of the Traits package.
Thus, you can write code in terms of the Traits API (views, items, editors,
etc.), and let pyface and your selected toolkit and back-end take care of
the details of displaying them.

Part of the Enthought Tool Suite (ETS).

%prep
%autosetup -p1 -n pyface-%{version}

# Fix executable bits
find . -name \*.py -exec chmod -x '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyface/sizers
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyface/sizers
%fdupes %{buildroot}%{$python_sitelib}/pyface/sizers
}

%check
export ETS_TOOLKIT=qt
%{python_expand mkdir tester_%{$python_bin_suffix}
pushd tester_%{$python_bin_suffix}
cp -a %{buildroot}%{$python_sitelib} python_sitelib # copy to avoid modification of original https://github.com/enthought/pyface/issues/1254
export PYTHONPATH=`pwd`/python_sitelib
xvfb-run --server-args "-screen 0 1920x1080x24" $python -m unittest discover -v pyface
rm -rf python_sitelib
popd
# wait 2 seconds before the next xvfb-run
sleep 2
}

%files %{python_files}
%doc README.rst
%license LICENSE.txt image_LICENSE*.txt
%{python_sitelib}/pyface
%{python_sitelib}/pyface-%{version}*-info

%changelog
