#
# spec file for package python-python-mpv
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


Name:           python-python-mpv
Version:        1.0.1
Release:        0
Summary:        Python interface to the mpv media player
License:        AGPL-3.0-or-later
URL:            https://github.com/jaseg/python-mpv
Source0:        https://files.pythonhosted.org/packages/source/p/python-mpv/python-mpv-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  %{python_module setuptools}
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
%setup -q -n python-mpv-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
