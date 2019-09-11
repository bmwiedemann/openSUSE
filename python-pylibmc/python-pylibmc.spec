#
# spec file for package python-pylibmc
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
Name:           python-pylibmc
Version:        1.6.0
Release:        0
Summary:        memcached client for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/lericson/pylibmc
Source:         https://files.pythonhosted.org/packages/source/p/pylibmc/pylibmc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
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
%{_sbindir}/memcached &
pid=$!
export NOSE_IGNORE_CONFIG_FILES=1
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
nosetests-%{$python_bin_suffix} tests
}
kill $pid

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
