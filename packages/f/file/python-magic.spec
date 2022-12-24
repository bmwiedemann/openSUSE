#
# spec file for package python-magic
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


# PyPI package name is file-magic. Version is taken from setup.py
%define file_magic_version 0.3.0
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global         _miscdir    %{_datadir}/misc
Name:           python-magic
Version:        5.43
Release:        0
Summary:        Python module to use libmagic
License:        BSD-3-Clause AND BSD-4-Clause
Group:          Development/Languages/Python
URL:            https://www.darwinsys.com/file/
Source99:       file.spec
BuildRequires:  %{python_module setuptools}
BuildRequires:  findutils
BuildRequires:  libtool
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(zlib)
Requires:       libmagic1
Provides:       python-file-magic = %{file_magic_version}
%{expand:%(sed -n -e '/^Source0\?:/,/^BuildRoot:/p' <%{_sourcedir}/file.spec)}
%python_subpackages

%description
This package contains the Python binding that require the magic "file"
interface.

%prep
%{expand:%(sed -n -e '/^%%prep/,/^%%build/p' <%{_sourcedir}/file.spec | sed -e '1d' -e '$d')}
ln -sf README.md python/README

pushd python
%python_build
popd

%install
pushd python
%python_install
popd

%files %{python_files}
%doc python/README python/example.py
%{python_sitelib}/magic.py*
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/file_magic-*-py%{python_version}.egg-info

%changelog
