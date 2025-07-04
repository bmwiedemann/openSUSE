#
# spec file for package python-PyVirtualDisplay
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-PyVirtualDisplay%{psuffix}
Version:        3.0
Release:        0
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc
License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source:         https://files.pythonhosted.org/packages/source/P/PyVirtualDisplay/PyVirtualDisplay-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-EasyProcess
Requires:       xorg-x11-Xvfb
Suggests:       xorg-x11-Xvnc
Suggests:       xorg-x11-server-extra
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module PyVirtualDisplay}
BuildRequires:  %{python_module EasyProcess}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module entrypoint2}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  /usr/bin/who
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-extra
BuildRequires:  xvfb-run
# /SECTION
%endif
%python_subpackages

%description
PyVirtualDisplay is a python wrapper for Xvfb, Xephyr and Xvnc.

%prep
%setup -q -n PyVirtualDisplay-%{version}
# Ignore test_xvnc.py to remove python-vncdotool build dependency
rm tests/test_xvnc.py

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
donttest="examples or smart"
# This test fails sometimes because a race condition with threads
donttest+=" or test_disp_var"
%{python_expand #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run --server-args "-screen 0 1920x1080x24" \
  $python -m pytest -v tests -rs -k "not ($donttest)" -n auto
}
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/pyvirtualdisplay
%{python_sitelib}/[Pp]y[Vv]irtual[Dd]isplay-%{version}.dist-info
%endif

%changelog
