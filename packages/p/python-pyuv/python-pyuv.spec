#
# spec file for package python-pyuv
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
Name:           python-pyuv
Version:        1.4.0
Release:        0
Summary:        Python interface for libuv
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/saghul/pyuv
Source:         https://files.pythonhosted.org/packages/source/p/pyuv/pyuv-%{version}.tar.gz
# Both patches in https://github.com/saghul/pyuv/pull/262
Patch0:         tests_async_keyword.patch
Patch1:         tests_py3.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libuv)
%python_subpackages

%description
Python interface for libuv.

%prep
%setup -q -n pyuv-%{version}
%patch0 -p1
%patch1 -p1
# Force system libuv
rm -r deps/libuv
rmdir deps
sed -i 's/self.use_system_libuv = 0/self.use_system_libuv = 1/' setup_libuv.py

sed -i 's/"python"/sys.executable/' tests/test_process.py
# Allow tests to be invoked at parent directory, and proc_*.py found in subdirectory
sed -i 's:"proc_:"tests/proc_:' tests/test_process.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv pyuv .pyuv
%pytest_arch -k 'not (test_tty or test_getaddrinfo_service or test_getaddrinfo_service_bytes or UDPBroadcastTest or UDPTestMulticast)'
mv .pyuv pyuv

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
