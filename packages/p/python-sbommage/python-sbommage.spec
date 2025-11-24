#
# spec file for package python-sbommage
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} >= 1699
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif

Name:           python-sbommage
Version:        1.0.2
Release:        0
Summary:        Interactive terminal frontend for viewing SBOM files
License:        MIT
URL:            https://github.com/popey/sbommage
Source:         sbommage-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module textual >= 5.3.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-textual >= 5.3.0
Recommends:     syft
BuildArch:      noarch
%python_subpackages

%description
Interactive terminal frontend for viewing Software Bill of Materials (SBOM)
files in various formats.

%prep
%autosetup -p1 -n sbommage-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

sed -i '1s/env python/python3/' %{buildroot}%{python_sitelib}/sbommage.py

rm -vf %{buildroot}%{python_sitelib}/Dockerfile
rm -vf %{buildroot}%{python_sitelib}/LICENSE
rm -vf %{buildroot}%{python_sitelib}/MANIFEST.in
rm -vf %{buildroot}%{python_sitelib}/README.md
rm -vf %{buildroot}%{python_sitelib}/_current_flavor
rm -vf %{buildroot}%{python_sitelib}/pyproject.toml
rm -vf %{buildroot}%{python_sitelib}/release.py
rm -vf %{buildroot}%{python_sitelib}/__pycache__/release*
rm -vf %{buildroot}%{python_sitelib}/snap/snapcraft.yaml

%fdupes %{buildroot}%{python_sitelib}/__pycache__/

%files %{python_files}
%{_bindir}/sbommage
%doc example_sboms
%doc README.md
%license LICENSE
%{python_sitelib}/sbommage.py
%{python_sitelib}/sbommage-%{version}.dist-info
%pycache_only %{python_sitelib}/__pycache__/

%changelog
