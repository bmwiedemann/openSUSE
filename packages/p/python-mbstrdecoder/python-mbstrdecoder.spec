#
# spec file for package python-mbstrdecoder
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
%define skip_python2 1
Name:           python-mbstrdecoder
Version:        1.1.2
Release:        0
Summary:        Multi-byte character string decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/mbstrdecoder
Source:         https://files.pythonhosted.org/packages/source/m/mbstrdecoder/mbstrdecoder-%{version}.tar.gz
BuildRequires:  %{python_module Faker >= 1.0.2}
BuildRequires:  %{python_module chardet >= 3.0.4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Faker >= 1.0.2
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
