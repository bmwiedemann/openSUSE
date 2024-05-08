#
# spec file for package python-seedir
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


Name:           python-seedir
Version:        0.4.2
Release:        0
Summary:        Package for creating, editing, and reading folder tree diagrams
License:        MIT
URL:            https://github.com/earnestt1234/seedir
Source:         https://github.com/earnestt1234/seedir/archive/refs/tags/v%{version}.tar.gz#/seedir-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module natsort}
# /SECTION
BuildRequires:  fdupes
Requires:       python-natsort
Suggests:       python-emoji
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Package for creating, editing, and reading folder tree diagrams.

%prep
%autosetup -p1 -n seedir-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/seedir
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m tests.tests

%post
%python_install_alternative seedir

%postun
%python_uninstall_alternative seedir

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%python_alternative %{_bindir}/seedir
%{python_sitelib}/seedir
%{python_sitelib}/seedir-%{version}.dist-info

%changelog
