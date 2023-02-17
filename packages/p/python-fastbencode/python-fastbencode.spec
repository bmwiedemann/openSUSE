#
# spec file for package python-fastbencode
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


%{?!python_module:%define python_module() python3-%{**}}
Name:           python-fastbencode
Version:        0.2
Release:        0
Summary:        Implementation of the bencode serialization format
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/fastbencode
Source:         https://github.com/breezy-team/fastbencode/archive/refs/tags/v%{version}.tar.gz#/fastbencode-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  python-rpm-macros
%python_subpackages

%description
fastbencode is an implementation of the bencode serialization format
originally used by BitTorrent.

The package includes both a pure-Python version and an optional C extension
based on Cython. Both provide the same functionality, but the C extension
provides significantly better performance.

%prep
%autosetup -p1 -n fastbencode-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest_arch -v

%files %{python_files}
%doc README.md SECURITY.md
%license COPYING
%{python_sitearch}/fastbencode*

%changelog
