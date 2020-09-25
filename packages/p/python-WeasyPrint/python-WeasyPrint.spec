#
# spec file for package python-WeasyPrint
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-WeasyPrint
Version:        51
Release:        0
Summary:        Python module to convert web documents to PDF
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Kozea/WeasyPrint
Source:         https://files.pythonhosted.org/packages/source/W/WeasyPrint/WeasyPrint-%{version}.tar.gz
Source100:      python-WeasyPrint-rpmlintrc
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libgobject-2_0-0
Requires:       pango
Requires:       python-Pyphen >= 0.9.1
Requires:       python-cairocffi >= 0.9.0
Requires:       python-cairocffi-pixbuf
Requires:       python-cffi >= 0.6
Requires:       python-cssselect2 >= 0.1
Requires:       python-html5lib >= 0.999999999
Requires:       python-pdfrw >= 0.4
Requires:       python-setuptools >= 39.2.0
Requires:       python-tinycss2 >= 1.0.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-CairoSVG >= 2.4.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module CairoSVG >= 2.4.0}
BuildRequires:  %{python_module Pyphen >= 0.9.1}
BuildRequires:  %{python_module cairocffi >= 0.9.0}
BuildRequires:  %{python_module cairocffi-pixbuf}
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module cssselect2 >= 0.1}
BuildRequires:  %{python_module html5lib >= 0.999999999}
BuildRequires:  %{python_module pdfrw >= 0.4}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module tinycss2 >= 1.0.0}
BuildRequires:  dejavu-fonts
BuildRequires:  libgobject-2_0-0
BuildRequires:  pango
BuildRequires:  xorg-x11-server
# /SECTION
%python_subpackages

%description
WeasyPrint is a visual rendering engine for HTML and CSS that can
export to PDF. It aims to support web standards for printing.

It is based on various libraries but not on a full rendering engine
like WebKit or Gecko. The CSS layout engine is written in Python,
designed for pagination, and meant to be easy to hack on.

%prep
%setup -q -n WeasyPrint-%{version}
sed -i '/\(addopts\|pytest-\(cov\|flake8\|isort\)\)/d' setup.cfg

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/weasyprint
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/Kozea/WeasyPrint/issues/913
%pytest -k 'not test_linear_gradients_7'

%post
%python_install_alternative weasyprint

%postun
%python_uninstall_alternative weasyprint

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/weasyprint
%{python_sitelib}/*

%changelog
