#
# spec file for package python-python-vlc
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


Name:           python-python-vlc
Version:        3.0.18121
Release:        0
Summary:        VLC bindings for python
License:        LGPL-2.0-or-later
Group:          Development/Languages/Python
URL:            http://wiki.videolan.org/PythonBinding
Source:         https://files.pythonhosted.org/packages/source/p/python-vlc/python-vlc-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-docs.patch -- Fix some example code in the docs
Patch0:         fix-docs.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  vlc-devel
Requires:       libvlc5 >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
VLC bindings for python.

This module provides ctypes-based bindings for the native libvlc API
(see http://wiki.videolan.org/LibVLC) of the VLC video player.

%prep
%autosetup -p1 -n python-vlc-%{version}
sed -i -e '1{\,^#! %{_bindir}/python,d}' vlc.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README.module
%{python_sitelib}/*

%changelog
