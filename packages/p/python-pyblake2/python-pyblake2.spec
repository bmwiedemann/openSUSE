#
# spec file for package python-pyblake2
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
Name:           python-pyblake2
Version:        1.1.2
Release:        0
Summary:        BLAKE2 hash function extension module
License:        CC0-1.0
Group:          Development/Languages/Python
URL:            https://github.com/dchest/pyblake2
Source:         https://files.pythonhosted.org/packages/source/p/pyblake2/pyblake2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
pyblake2 is an extension module for Python implementing BLAKE2 hash function.

BLAKE2 is a cryptographic hash function, which offers highest security while
being as fast as MD5 or SHA-1, and comes in two flavors:

* BLAKE2b, optimized for 64-bit platforms and produces digests of any size
  between 1 and 64 bytes,

* BLAKE2s, optimized for 8- to 32-bit platforms and produces digests of any
  size between 1 and 32 bytes.

BLAKE2 supports keyed mode (a faster and simpler replacement for HMAC),
salted hashing, personalization, and tree hashing.

Hash objects from this module follow the API of standard library's
`hashlib` objects.

%prep
%setup -q -n pyblake2-%{version}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test/test.py

%files %{python_files}
%doc README.rst
%%license COPYING
%{python_sitearch}/*

%changelog
