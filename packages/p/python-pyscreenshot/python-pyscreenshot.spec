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


%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pyscreenshot%{psuffix}
Version:        3.0
Release:        0
Summary:        Python screenshots
License:        BSD-3-Clause
URL:            https://github.com/ponty/pyscreenshot
Source:         https://files.pythonhosted.org/packages/source/p/pyscreenshot/pyscreenshot-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-EasyProcess
Requires:       python-entrypoint2
Requires:       python-jeepney
Requires:       python-mss
Requires:       xorg-x11-server-extra
Recommends:     ImageMagick
Recommends:     maim
Suggests:       gnome-screenshot
Suggests:       python-wxPython
Suggests:       scrot
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module EasyProcess}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyVirtualDisplay}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module entrypoint2}
BuildRequires:  %{python_module jeepney}
BuildRequires:  %{python_module mss}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module pyscreenshot >= %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-xlib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wxPython}
BuildRequires:  ImageMagick
BuildRequires:  gnome-screenshot
BuildRequires:  maim
BuildRequires:  pqiv-gdkpixbuf
BuildRequires:  xdpyinfo
BuildRequires:  xmessage
BuildRequires:  xorg-x11-server-extra
BuildRequires:  xvfb-run
%endif
%python_subpackages

%description
The pyscreenshot module can be used to copy the contents of the screen
to a Pillow image memory using various back-ends.
Replacement for the ImageGrab Module.

%prep
%autosetup -p1 -n pyscreenshot-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
cd tests/
# test_maim fails on Leap 15.x
%{python_expand # Necessary to run configure with all python flavors
export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run --server-args "-br -screen 0 900x800x24" -w 5 $python -m pytest -v -k 'not test_maim'
rm -rf /tmp/fillscreen*
}
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/pyscreenshot
%{python_sitelib}/pyscreenshot-%{version}*-info
%endif

%changelog
