#
# spec file for package python-ly
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


%{?sle15_python_module_pythons}
Name:           python-ly
Version:        0.9.9
Release:        0
Summary:        Tool and library for manipulating LilyPond files
License:        GPL-2.0-or-later
URL:            https://github.com/frescobaldi/python-ly
Source:         https://github.com/frescobaldi/python-ly/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
#BuildRequires:  %%{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Tool and library for manipulating LilyPond files

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ly
%python_clone -a %{buildroot}%{_bindir}/ly-server
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/frescobaldi/python-ly/issues/153
#%%pytest

%post
%python_install_alternative ly ly-server

%postun
%python_uninstall_alternative ly

%files %{python_files}
%doc CHANGELOG.md README.rst
%python_alternative %{_bindir}/ly
%python_alternative %{_bindir}/ly-server
%{python_sitelib}/ly
%{python_sitelib}/python_ly-%{version}.dist-info

%changelog
