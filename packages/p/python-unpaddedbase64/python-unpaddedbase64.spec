#
# spec file for package python-unpaddedbase64
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
%define         short_name unpaddedbase64
Name:           python-%{short_name}
Version:        1.1.0
Release:        0
Summary:        Unpadded Base64
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/python-unpaddedbase64
Source:         https://github.com/matrix-org/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Encode and decode Base64 without "=" padding.

RFC 4648 specifies that Base64 should be padded to a multiple of 4 bytes using
"=" characters. However this conveys no benefit so many protocols choose to use
Base64 without the "=" padding.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
