#
# spec file for package python-pyface
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

# Tests have a dependency loop with traitsui
%bcond_with     test

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
%define         X_display         ":98"
Name:           python-pyface
Version:        6.1.2
Release:        0
Summary:        Traits-capable windowing framework
License:        BSD-3-Clause and EPL-1.0 and LGPL-2.1 and LGPL-3.0 and SUSE-Public-Domain
Group:          Development/Libraries/Python
# Source code is under BSD but images are under different licenses
# and details are inside image_LICENSE.txt
Url:            https://github.com/enthought/pyface
Source:         https://files.pythonhosted.org/packages/source/p/pyface/pyface-%{version}.tar.gz
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module traits}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module qt5}
BuildRequires:  xorg-x11-server
%endif
Requires:       python-traits
Recommends:     python-Pygments
Recommends:     python-qt5
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
%setup -q -n pyface-%{version}

%build
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyface/sizers
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/pyface/sizers
%fdupes %{buildroot}%{$python_sitelib}/pyface/sizers
}

%if %{with test}
%check
export ETS_TOOLKIT=qt4
export DISPLAY=%{X_display}
Xvfb %{X_display} >& Xvfb.log &
trap "kill $! || true" EXIT
sleep 10

%{python_expand mkdir tester_%{$python_bin_suffix}
pushd tester_%{$python_bin_suffix}
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -m nose.core -v pyface --exclude=wx
popd
}
%endif

%files %{python_files}
%doc CHANGES.txt README.rst TODO.txt
%license LICENSE.txt image_LICENSE*.txt
%{python_sitelib}/pyface/
%{python_sitelib}/pyface-%{version}-py*.egg-info

%changelog
