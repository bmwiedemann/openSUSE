#
# spec file for package python-grype2html
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


%if 0%{?suse_version} >= 1699
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif

Name:           python-grype2html
Version:        0.0.1~1739230997.5f96631
Release:        0
Summary:        Convert Grype vulnerability scan results into interactive HTML reports
License:        MIT
URL:            https://github.com/popey/grype2html
Source:         grype2html-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       grype
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Convert Grype vulnerability scan results into interactive HTML reports.

%prep
%autosetup -p1 -n grype2html-%{version}

%build

%install
install -D -m 0755 grype2html.py %{buildroot}/%{_bindir}/grype2html
%python3_fix_shebang

%files %{python_files}
%{_bindir}/grype2html
%doc README.md
%license LICENSE

%changelog
