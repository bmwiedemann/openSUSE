#
# spec file for package python-modern-colorthief
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

%{?sle15_python_module_pythons}
Name:           python-modern-colorthief
Version:        0.1.2
Release:        0
Summary:        Colorthief reimagined
License:        MIT
URL:            https://github.com/baseplate-admin/modern_colorthief
Source:         https://files.pythonhosted.org/packages/source/m/modern-colorthief/modern_colorthief-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module Pillow}
BuildRequires:  fdupes
Requires:       python3-Pillow
BuildArch:      noarch
%python_subpackages

%description
%{summary}.

%prep
%autosetup -p1 -n modern_colorthief-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_expand rm %{buildroot}%{$python_sitelib}/LICENSE.colorthief

%check
# the singular test is relying on the old abandoned python-colorthief.

%files %{python_files}
%{python_sitelib}/modern_colorthief
%{python_sitelib}/modern_colorthief-%{version}.dist-info
%license LICENSE LICENSE.colorthief

%changelog
