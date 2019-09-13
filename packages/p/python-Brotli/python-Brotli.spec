#
# spec file for package python-Brotli
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
Name:           python-Brotli
Version:        1.0.7
Release:        0
Summary:        Python bindings for the Brotli compression library
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/google/brotli
Source:         https://files.pythonhosted.org/packages/source/B/Brotli/Brotli-%{version}.zip
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip

%python_subpackages

%description
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

The specification of the Brotli Compressed Data Format is defined in RFC 7932.

%prep
%setup -q -n Brotli-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/*

%changelog
