#
# spec file for package python-weasyprint
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


%global brotli_min_version     1.0.1
%global cffi_min_version       0.6
%global cssselect2_min_version 0.1
%global fonttools_min_version  4.0.0
%global html5lib_min_version   1.1
%global Pillow_min_version     9.1.0
%global pypdf_min_version      0.10.0
%global Pyphen_min_version     0.9.1
%global tinycss2_min_version   1.3.0
%global zopfli_min_version     0.1.4

%{?sle15_python_module_pythons}
Name:           python-weasyprint
Version:        62.2
Release:        0
Summary:        Python module to convert web documents to PDF
License:        BSD-3-Clause
URL:            https://github.com/Kozea/WeasyPrint
Source:         https://files.pythonhosted.org/packages/source/w/weasyprint/weasyprint-%{version}.tar.gz
Source100:      python-weasyprint-rpmlintrc
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       libgobject-2_0-0
Requires:       pango
Requires:       python-Pillow >= %{Pillow_min_version}
Requires:       python-Pyphen >= %{Pyphen_min_version}
Requires:       python-base >= 3.7
Requires:       python-cffi >= %{cffi_min_version}
Requires:       python-cssselect2 >= %{cssselect2_min_version}
Requires:       python-html5lib >= %{html5lib_min_version}
Requires:       python-pydyf >= %{pypdf_min_version}
Requires:       python-tinycss2 >= %{tinycss2_min_version}
# SECTION fonttools[woff]
Requires:       python-FontTools >= %{fonttools_min_version}
Requires:       python-Brotli >= %{brotli_min_version}
Requires:       python-zopfli >= %{zopfli_min_version}
# /SECTION
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= %{fonttools_min_version}}
BuildRequires:  %{python_module Brotli >= %{brotli_min_version}}
BuildRequires:  %{python_module Pillow >= %{Pillow_min_version}}
BuildRequires:  %{python_module Pyphen >= %{Pyphen_min_version}}
BuildRequires:  %{python_module cffi   >= %{cffi_min_version}}
BuildRequires:  %{python_module cssselect2 >= %{cssselect2_min_version}}
BuildRequires:  %{python_module html5lib >= %{html5lib_min_version}}
BuildRequires:  %{python_module pydyf >= %{pypdf_min_version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tinycss2 >= %{tinycss2_min_version}}
BuildRequires:  %{python_module zopfli >= %{zopfli_min_version}}
BuildRequires:  dejavu-fonts
BuildRequires:  gs
BuildRequires:  libgobject-2_0-0
BuildRequires:  pango
BuildRequires:  xorg-x11-server
# /SECTION
Provides:       python-WeasyPrint = %{version}-%{release}
Obsoletes:      python-WeasyPrint < %{version}-%{release}
%python_subpackages

%description
WeasyPrint is a visual rendering engine for HTML and CSS that can
export to PDF. It aims to support web standards for printing.

It is based on various libraries but not on a full rendering engine
like WebKit or Gecko. The CSS layout engine is written in Python,
designed for pagination, and meant to be easy to hack on.

%prep
%autosetup -p1 -n weasyprint-%{version}
sed -i '/addopts/d' pyproject.toml

%build
export PYTHONPATH=$PWD
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/weasyprint

%check
%pytest -k 'not test_linear_gradients and (5 or 12)'  tests

%post
%python_install_alternative weasyprint

%postun
%python_uninstall_alternative weasyprint

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/weasyprint
%{python_sitelib}/weasyprint
%{python_sitelib}/weasyprint-%{version}.dist-info

%changelog
