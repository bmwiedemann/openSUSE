#
# spec file for package python-python-mpv
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-python-mpv
Version:        1.0.7
Release:        0
Summary:        Python interface to the mpv media player
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://github.com/jaseg/python-mpv
Source0:        https://files.pythonhosted.org/packages/source/p/python-mpv/python_mpv-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Needed to be able to set the proper dependency to the library
BuildRequires:  mpv-devel
# workaround via define needed as python_ubpackages wants to interpret Requires: lines
%define libmpv  %(rpm -qf $(readlink -f %{_libdir}/libmpv.so) --qf "%%{name}")
Requires:       %libmpv
BuildArch:      noarch
%python_subpackages

%description
A ctypes-based python interface to the mpv media player.
It gives more or less full control of all features of the player,
just like the lua interface does.

%prep
%setup -q -n python_mpv-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.GPL LICENSE.LGPL
%doc README.rst
%{python_sitelib}/mpv.py
%{python_sitelib}/__pycache__/mpv.cpython*
%{python_sitelib}/python_mpv-%{version}.dist-info

%changelog
