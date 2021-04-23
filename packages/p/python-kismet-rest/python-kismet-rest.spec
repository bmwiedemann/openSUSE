#
# spec file for package python-kismet-rest
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
Name:           python-kismet-rest
Version:        2019.05.02
Release:        0
License:        GPL-2.0
Summary:        Python wrapper for the Kismet REST interface
Url:            https://www.kismetwireless.net
Group:          Development/Languages/Python
Source:         https://github.com/kismetwireless/python-kismet-rest/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
#BuildRequires:  %%{python_module requests}
#BuildRequires:  %%{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Simplified Python API for the Kismet REST interface.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are disabled for now since those need a docker environment for testing
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.rst
%{python_sitelib}/*

%changelog
