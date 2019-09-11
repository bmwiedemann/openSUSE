#
# spec file for package python-metamagic.json
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-metamagic.json
Version:        0.9.6
Release:        0
License:        BSD-2-Clause
Summary:        Fast JSON encoder
Url:            http://github.com/sprymix/metamagic.json
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/m/metamagic.json/metamagic.json-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes

%python_subpackages

%description
A fast Python 3 implementation of a JSON encoder for Python objects
designed to be compatible with native JSON decoders in various web browsers.

%prep
%setup -q -n metamagic.json-%{version}
touch metamagic/__init__.py

sed -i 's/from metamagic.utils.debug import assert_raises/from pytest import raises as assert_raises/' metamagic/json/tests/test_encoder.py

# Broken imports
rm metamagic/json/tests/benchmark_encoder.py

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%{python_expand rm -r \
  %{buildroot}%{$python_sitearch}/metamagic/json/tests \
  %{buildroot}%{$python_sitearch}/metamagic/json/_encoder/*.[ch]

%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pytest_arch

%files %{python_files}
%doc NEWS README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
