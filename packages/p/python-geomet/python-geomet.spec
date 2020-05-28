#
# spec file for package python-geomet
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-geomet
Version:        0.2.1
Release:        0
Summary:        GeoJSON <-> WKT/WKB conversion utilities
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/geomet/geomet
Source:         https://github.com/geomet/geomet/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
GeoJSON <-> WKT/WKB conversion utilities

%prep
%setup -q -n geomet-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/geomet
rm %{buildroot}%{_prefix}/LICENSE
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONDONTWRITEBYTECODE=1
%{python_expand \
sed -i 's:geomet:geomet-%{$python_version}:' geomet/tests/test_cli.py
export PYTHONPATH=:%{buildroot}%{$python_sitelib}
$python -m pytest
}

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
