#
# spec file for package python-xvfbwrapper
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-xvfbwrapper
Version:        0.2.9
Release:        0
Summary:        Python wrapper for controlling X virtual framebuffer (Xvfb)
License:        MIT
URL:            https://github.com/cgoldberg/xvfbwrapper
Source:         https://files.pythonhosted.org/packages/source/x/xvfbwrapper/xvfbwrapper-%{version}.tar.gz
Patch0:         skip_failing_test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       xorg-x11-Xvfb
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  xorg-x11-Xvfb
%if %{with python2}
BuildRequires:  python-mock
%endif
# /SECTION
%python_subpackages

%description
Xvfb (X virtual framebuffer) is a display server implementing the X11
display server protocol. It runs in memory and does not require a
physical display.  Only a network layer is necessary.

Xvfb is useful for running acceptance tests on headless servers.

%prep
%setup -q -n xvfbwrapper-%{version}
%autopatch -p1
sed -i -e '/^#!\//, 1d' xvfbwrapper.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
