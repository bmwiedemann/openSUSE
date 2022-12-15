#
# spec file for package python-anyascii
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-anyascii
Version:        0.3.1
Release:        0
Summary:        Unicode to ASCII transliteration
License:        ISC
URL:            https://github.com/anyascii/anyascii
Source:         https://files.pythonhosted.org/packages/source/a/anyascii/anyascii-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Converts Unicode characters to their best ASCII representation.

%prep
%setup -qn anyascii-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/anyascii
%{python_sitelib}/anyascii-%{version}.dist-info

%changelog
