#
# spec file for package python-weasyprint
#
# Copyright (c) 2021 SUSE LLC
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

Name:           python-weasyprint
Version:        53.4
Release:        0
Summary:        Python module to convert web documents to PDF
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Kozea/WeasyPrint
Source:         https://files.pythonhosted.org/packages/source/w/weasyprint/weasyprint-%{version}.tar.gz
Source100:      python-weasyprint-rpmlintrc
BuildRequires:  %{python_module setuptools >= 39.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       libgobject-2_0-0
Requires:       pango
Requires:       python-CairoSVG >= 2.4.0
Requires:       python-Pyphen >= 0.9.1
Requires:       python-cairocffi >= 0.9.0
Requires:       python-cairocffi-pixbuf
Requires:       python-cffi >= 0.6
Requires:       python-cssselect2 >= 0.1
Requires:       python-html5lib >= 0.999999999
Requires:       python-pdfrw >= 0.4
Requires:       python-setuptools >= 39.2.0
Requires:       python-tinycss2 >= 1.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools}
BuildRequires:  %{python_module CairoSVG >= 2.4.0}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Pyphen >= 0.9.1}
BuildRequires:  %{python_module cairocffi >= 0.9.0}
BuildRequires:  %{python_module cairocffi-pixbuf}
BuildRequires:  %{python_module cffi >= 0.6}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module cssselect2 >= 0.1}
BuildRequires:  %{python_module html5lib >= 0.999999999}
BuildRequires:  %{python_module pdfrw >= 0.4}
BuildRequires:  %{python_module pluggy >= 0.12}
BuildRequires:  %{python_module pydyf}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-flake8}
BuildRequires:  %{python_module pytest-isort}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tinycss2 >= 1.0.0}
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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#Kozea/WeasyPrint#1503
%pytest -k 'not (test_relative_links_missing_base_link or test_links)' tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
