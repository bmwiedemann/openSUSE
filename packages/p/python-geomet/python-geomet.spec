#
# spec file for package python-geomet
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


Name:           python-geomet
Version:        1.0.0
Release:        0
Summary:        GeoJSON <-> WKT/WKB conversion utilities
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/geomet/geomet
Source:         https://github.com/geomet/geomet/archive/%{version}.tar.gz
# https://github.com/geomet/geomet/issues/90
Patch0:         python-geomet-no-six.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
GeoJSON <-> WKT/WKB conversion utilities

%prep
%autosetup -p1 -n geomet-%{version}

%build
sed -i '1{/^#!/ d}' geomet/*.py
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/geomet
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative geomet

%postun
%python_uninstall_alternative geomet

%files %{python_files}
%doc AUTHORS.txt README.md
%license LICENSE
%python_alternative %{_bindir}/geomet
%{python_sitelib}/geomet
%{python_sitelib}/geomet-%{version}-py*.egg-info

%changelog
