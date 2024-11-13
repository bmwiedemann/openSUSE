#
# spec file for package python-spake2
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-spake2
Version:        0.9
Release:        0
Summary:        Pure-Python SPAKE2
License:        MIT
URL:            http://github.com/warner/python-spake2
Source:         https://files.pythonhosted.org/packages/source/s/spake2/spake2-%{version}.tar.gz
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module hkdf}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
Requires:       python-hkdf
BuildArch:      noarch
%python_subpackages

%description
SPAKE2 password-authenticated key exchange.

%prep
%autosetup -p1 -n spake2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/spake2
%{python_sitelib}/spake2-%{version}.dist-info

%changelog
