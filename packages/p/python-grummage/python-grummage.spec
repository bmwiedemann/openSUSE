#
# spec file for package python-grummage
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


%if 0%{?suse_version} >= 1699
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif

Name:           python-grummage
Version:        0.1.0
Release:        0
Summary:        Interactive terminal frontend to Grype
License:        MIT
URL:            https://github.com/popey/grummage
Source:         https://github.com/popey/grummage/archive/v%{version}.tar.gz#/grummage-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module textual >= 0.85.2}
BuildRequires:  fdupes
Requires:       python-textual >= 0.85.2
Requires:       grype
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Grype + Rummage = Grummage.

Grummage is an interactive terminal frontend to Grype.

%prep
%autosetup -p1 -n grummage-%{version}

%build
sed -i 's/env python/python3/g' grummage

%install
install -D -m 0755 grummage %{buildroot}/%{_bindir}/grummage

%files %{python_files}
%{_bindir}/grummage
%doc example_sboms
%doc README.md
%license LICENSE

%changelog
