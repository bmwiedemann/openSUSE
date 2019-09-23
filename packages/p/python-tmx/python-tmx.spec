#
# spec file for package python-tmx
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
Name:           python-tmx
Version:        1.10
Release:        0
Summary:        Python library for reading/writing TMX tile files
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://python-tmx.nongnu.org
Source:         http://download.savannah.gnu.org/releases/python-tmx/%{version}/tmx-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.4.0
BuildArch:      noarch
%python_subpackages

%description
This library reads and writes the Tiled TMX format.
This is useful for map editors or generic level editors like
Tiled to edit a game's levels.

%prep
%setup -q -n tmx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no testsuite found

%files %{python_files}
%doc README
%license tmx/COPYING
%{python_sitelib}/*

%changelog
