#
# spec file for package python-pylibmc
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


Name:           python-pylibmc
Version:        1.6.3
Release:        0
Summary:        memcached client for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lericson/pylibmc
Source:         https://files.pythonhosted.org/packages/source/p/pylibmc/pylibmc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  libmemcached-devel
BuildRequires:  memcached
BuildRequires:  python-rpm-macros
BuildRequires:  zlib-devel
%python_subpackages

%description
pylibmc is a Python client for (lib)memcached written in C.
The Python interface is similar to python-memcached.

pylibmc leverages configurable behaviors, data pickling, data
compression, tested GIL retention, consistent distribution, and the
binary memcached protocol.

%prep
%setup -q -n pylibmc-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
if [ -f %{_sbindir}/memcached ]; then
  %{_sbindir}/memcached &
elif [ -f %{_bindir}/memcached ]; then
  %{_bindir}/memcached &
else
  echo "Failed to start memcached - tests can't pass"
  exit 1
fi
pid=$!
%pytest_arch
kill $pid

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/pylibmc
%{python_sitearch}/_pylibmc*.so
%{python_sitearch}/pylibmc-%{version}*-info

%changelog
