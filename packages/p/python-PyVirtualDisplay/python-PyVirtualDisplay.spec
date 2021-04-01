#
# spec file for package python-PyVirtualDisplay
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-PyVirtualDisplay
Version:        2.1
Release:        0
Summary:        Python wrapper for Xvfb, Xephyr and Xvnc
License:        BSD-2-Clause
URL:            https://github.com/ponty/PyVirtualDisplay
Source:         https://files.pythonhosted.org/packages/source/P/PyVirtualDisplay/PyVirtualDisplay-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-EasyProcess
Requires:       xorg-x11-Xvfb
Suggests:       xorg-x11-Xvnc
Suggests:       xorg-x11-server-extra
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module EasyProcess}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module entrypoint2}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vncdotool >= 0.13.0}
BuildRequires:  maim
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-extra
BuildRequires:  xvfb-run
# /SECTION
%python_subpackages

%description
PyVirtualDisplay is a python wrapper for Xvfb, Xephyr and Xvnc.

%prep
%setup -q -n PyVirtualDisplay-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# xvnc omitted due to "vncext: pseudocolour not supported"
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run --server-args "-screen 0 1920x1080x24" $python -m pytest tests -rs -k 'not (examples or smart or xvnc)'

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/pyvirtualdisplay
%{python_sitelib}/PyVirtualDisplay-%{version}-*info

%changelog
