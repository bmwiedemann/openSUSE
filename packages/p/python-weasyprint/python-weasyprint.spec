#
# spec file for package python-weasyprint
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-weasyprint
Version:        59.0
Release:        0
Summary:        Python module to convert web documents to PDF
License:        BSD-3-Clause
URL:            https://github.com/Kozea/WeasyPrint
Source:         https://files.pythonhosted.org/packages/source/w/weasyprint/weasyprint-%{version}.tar.gz
Source100:      python-weasyprint-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       libgobject-2_0-0
Requires:       pango
Requires:       python-Pillow >= 9.1.0
Requires:       python-Pyphen >= 0.9.1
Requires:       python-base >= 3.7
Requires:       python-cffi >= 0.6
Requires:       python-cssselect2 >= 0.1
Requires:       python-html5lib >= 1.1
Requires:       python-pydyf >= 0.6.0
Requires:       python-tinycss2 >= 1.1.0
# SECTION fonttools[woff]
Requires:       python-FontTools
Requires:       python-Brotli >= 1.0.1
Requires:       python-zopfli >= 0.1.4
# /SECTION
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools}
BuildRequires:  %{python_module Brotli >= 1.0.1}
BuildRequires:  %{python_module Pillow >= 9.1.0}
BuildRequires:  %{python_module Pyphen >= 0.9.1}
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module cssselect2 >= 0.1}
BuildRequires:  %{python_module html5lib >= 1.1}
BuildRequires:  %{python_module pydyf >= 0.6.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tinycss2 >= 1.1.0}
BuildRequires:  %{python_module zopfli >= 0.1.4}
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
%setup -q -n weasyprint-%{version}
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
%{python_sitelib}/weasyprint-%{version}*-info

%changelog
