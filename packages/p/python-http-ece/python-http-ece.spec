#
# spec file for package python-http-ece
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
Name:           python-http-ece
Version:        1.1.0
Release:        0
Summary:        Encrypted Content Encoding for HTTP
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/martinthomson/encrypted-content-encoding
Source:         https://files.pythonhosted.org/packages/source/h/http_ece/http_ece-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/web-push-libs/encrypted-content-encoding/v%{version}/python/http_ece/tests/test_ece.py
Source2:        https://raw.githubusercontent.com/web-push-libs/encrypted-content-encoding/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography >= 2.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cryptography >= 2.5}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Encrypted Content Encoding for HTTP.

%prep
%setup -q -n http_ece-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
