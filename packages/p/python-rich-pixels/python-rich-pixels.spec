#
# spec file for package python-rich-pixels
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024, Martin Hauke <mardnh@gmx.de>
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
Name:           python-rich-pixels
Version:        3.0.1
Release:        0
Summary:        A python library for writing pixel images and ASCII art to the terminal
License:        MIT
URL:            https://github.com/darrenburns/rich-pixels
Source:         https://files.pythonhosted.org/packages/source/r/rich_pixels/rich_pixels-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 10.0.0
Requires:       python-rich >= 12.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 10.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 12.0.0}
BuildRequires:  %{python_module syrupy}
# /SECTION
%python_subpackages

%description
A Rich-compatible library for writing pixel images and other colourful
grids to the terminal.

%prep
%autosetup -p1 -n rich_pixels-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/rich_pixels
%{python_sitelib}/rich_pixels-%{version}.dist-info

%changelog
