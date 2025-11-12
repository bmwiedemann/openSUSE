#
# spec file for package python-Brotli
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-Brotli
Version:        1.2.0
Release:        0
Summary:        Python bindings for the Brotli compression library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://pypi.org/project/Brotli/
Source:         https://files.pythonhosted.org/packages/source/b/brotli/brotli-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in RFC 7932.

%prep
%setup -q -n brotli-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch python/tests/*_test.py -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/brotli.py
%{python_sitearch}/_brotli*
%pycache_only %{python_sitearch}/__pycache__/brotli*
%{python_sitearch}/[Bb]rotli-%{version}*info

%changelog
