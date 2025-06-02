#
# spec file for package python-rich
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-rich
Version:        14.0.0
Release:        0
Summary:        A Python library for rich text and beautiful formatting in the terminal
License:        MIT
URL:            https://github.com/Textualize/rich
Source:         https://github.com/Textualize/rich/archive/refs/tags/v%{version}.tar.gz#/rich-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/Textualize/rich/pull/3604 Fix test that changed with Pygments 2.19.
# and https://github.com/Textualize/rich/pull/3608 fix remaining tests with Pygments 2.19 #3604 did not fix
Patch:          pygments.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module markdown-it-py >= 2.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pygments >= 2.13.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-markdown-it-py >= 2.2.0
Requires:       python-pygments >= 2.13.0
Suggests:       python-ipywidgets >= 7.5.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module attrs}
# /SECTION
%python_subpackages

%description
Render rich text, tables, progress bars, syntax highlighting,
markdown and more to the terminal.

%prep
%autosetup -p1 -n rich-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/rich
%{python_sitelib}/rich-%{version}.dist-info

%changelog
