#
# spec file for package python-bencode
#
# Copyright (c) 2023 SUSE LLC
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
%define oldpython python
Name:           python-bencode
Version:        4.0.0
Release:        0
Summary:        The BitTorrent bencode module as light-weight, standalone package
License:        BitTorrent-1.1
URL:            https://github.com/fuzeman/bencode.py
Source0:        https://files.pythonhosted.org/packages/source/b/bencode.py/bencode.py-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This package simply re-packages the existing bencoding and bdecoding
implemention from the 'official' BitTorrent client as a separate,
leight-weight package for re-using them without having the entire
BitTorrent software as a dependency.

%prep
%setup -q -n bencode.py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
