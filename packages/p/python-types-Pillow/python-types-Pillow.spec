#
# spec file for package python-types-Pillow
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


Name:           python-types-Pillow
Version:        10.2.0.20240822
Release:        0
Summary:        Typing stubs for Pillow
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source:         https://files.pythonhosted.org/packages/source/t/types-Pillow/types-Pillow-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Typing stubs for Pillow

%prep
%autosetup -p1 -n types-Pillow-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.md
%{python_sitelib}/PIL-stubs
%{python_sitelib}/types_Pillow-%{version}.dist-info

%changelog
