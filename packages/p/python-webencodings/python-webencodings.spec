#
# spec file for package python-webencodings
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-webencodings
Version:        0.5.1
Release:        0
Summary:        Character encoding aliases for legacy web content
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/SimonSapin/python-webencodings
Source:         https://files.pythonhosted.org/packages/source/w/webencodings/webencodings-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/gsnedders/python-webencodings/v%{version}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a Python implementation of the WHATWG Encoding standard.

In order to be compatible with legacy web content when interpreting
something like Content-Type: text/html; charset=latin1, tools need to
use a particular set of aliases for encoding labels as well as some
overriding rules. For example, US-ASCII and iso-8859-1 on the web are
actually aliases for windows-1252, and an UTF-8 or UTF-16 BOM takes
precedence over any other encoding declaration. The Encoding standard
defines all such details so that implementations do not have to
reverse-engineer each other.

This module has encoding labels and BOM detection, but the actual
implementation for encoders and decoders is Python’s.

%prep
%setup -q -n webencodings-%{version}
cp %{SOURCE1} ./

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/webencodings/
%{python_sitelib}/webencodings-%{version}-py%{py_ver}.egg-info

%changelog
