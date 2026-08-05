#
# spec file for package python-pillow-jxl-plugin
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         modname pillow_jxl_plugin
Name:           python-pillow-jxl-plugin
Version:        1.3.8
Release:        0
Summary:        Pillow plugin for JPEG-XL, using Rust for bindings
License:        GPL-3.0-or-later
URL:            https://github.com/Isotr0py/pillow-jpegxl-plugin
Source0:        https://files.pythonhosted.org/packages/source/p/pillow-jxl-plugin/%{modname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  %{python_module Brotli}
BuildRequires:  %{python_module OpenEXR}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module maturin >= 1.2}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyexiv2}
BuildRequires:  c++_compiler
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust+cargo
Requires:       python-Pillow
Requires:       python-packaging
Suggests:       python-cmake
Suggests:       python-numpy
Suggests:       python-OpenEXR
Suggests:       python-pyexiv2
%python_subpackages

%description
%{summary}.

%prep
%autosetup -a1 -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitearch}/pillow_jxl
%{python_sitearch}/%{modname}-%{version}.dist-info

%changelog
