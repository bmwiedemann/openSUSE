#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-PyVirtualDisplay%{psuffix}
Version:        3.0
Release:        0
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc
License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source:         https://files.pythonhosted.org/packages/source/P/PyVirtualDisplay/PyVirtualDisplay-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
BuildRequires:  %{python_module vncdotool >= 0.13.0}
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

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
donttest="examples or smart"
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
%{python_sitelib}/PyVirtualDisplay-%{version}-*info
%endif

%changelog
