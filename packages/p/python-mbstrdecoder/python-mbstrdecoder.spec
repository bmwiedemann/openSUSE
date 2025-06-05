#
# spec file for package python-mbstrdecoder
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-mbstrdecoder
Version:        1.1.4
Release:        0
Summary:        Multi-byte character string decoder
License:        MIT
URL:            https://github.com/thombashi/mbstrdecoder
Source:         https://files.pythonhosted.org/packages/source/m/mbstrdecoder/mbstrdecoder-%{version}.tar.gz
BuildRequires:  %{python_module Faker >= 1.0.2}
BuildRequires:  %{python_module chardet >= 3.0.4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet >= 3.0.4
BuildArch:      noarch
%python_subpackages

%description
Python library for multi-byte character string decoding.

%prep
%setup -q -n mbstrdecoder-%{version}
# Remove build alias
sed -i '/build =/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/mbstrdecoder
%{python_sitelib}/mbstrdecoder-%{version}.dist-info

%changelog
