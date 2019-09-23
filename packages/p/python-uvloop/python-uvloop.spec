#
# spec file for package python-uvloop
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define skip_python2 1
Name:           python-uvloop
Version:        0.13.0
Release:        0
Summary:        An asyncio event loop on top of libuv
License:        MIT AND Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/MagicStack/uvloop
Source:         https://files.pythonhosted.org/packages/source/u/uvloop/uvloop-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.28}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libuv)
%python_subpackages

%description
uvloop is a drop-in replacement of the built-in asyncio
event loop.  uvloop is implemented in Cython and uses libuv
under the hood.

%prep
%setup -q -n uvloop-%{version}
# always use cython to generate code
sed -i -e "/self.cython_always/s/False/True/" setup.py
# use system libuv
sed -i -e "/self.use_system_libuv/s/False/True/" setup.py
# To be sure, no 3rd-party stuff
rm -vrf vendor/

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# https://github.com/MagicStack/uvloop/issues/70
%python_expand rm -vf %{buildroot}%{$python_sitearch}/%{modname}/_testbase.py
%python_expand rm -vf %{buildroot}%{$python_sitearch}/%{modname}/__pycache__/_testbase.*

%check
# Actually the tests are VERY flaky, thus continue even if they fail :(
#%%python_exec setup.py test || :

%files %{python_files}
%license LICENSE-APACHE LICENSE-MIT
%doc README.rst
%{python_sitearch}/*

%changelog
