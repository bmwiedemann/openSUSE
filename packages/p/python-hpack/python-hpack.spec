#
# spec file for package python-hpack
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-hpack
Version:        3.0.0
Release:        0
Summary:        Pure-Python HPACK header compression
License:        MIT
URL:            https://github.com/python-hyper/hpack
Source:         https://files.pythonhosted.org/packages/source/h/hpack/hpack-%{version}.tar.gz
Patch0:         healthcheck.patch
Patch1:         pytest5.patch
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic for use in
Python programs that implement HTTP/2. It also contains a compatibility layer that
automatically enables the use of nghttp2 if it’s available.

%prep
%setup -q -n hpack-%{version}
%autopatch -p1

%build
export LC_ALL="en_US.UTF-8"
%python_build

%install
export LC_ALL="en_US.UTF-8"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k "not (test_can_decode_a_story or test_can_decode_a_story_no_huffman or test_can_encode_a_story_with_huffman or test_can_encode_a_story_no_huffman or test_decode_either_succeeds_or_raises_error)"

%files %{python_files}
%license LICENSE
%doc HISTORY.rst CONTRIBUTORS.rst README.rst
%{python_sitelib}/hpack
%{python_sitelib}/hpack-%{version}-py%{python_version}.egg-info

%changelog
