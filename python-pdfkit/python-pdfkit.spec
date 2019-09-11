#
# spec file for package python-pdfkit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pdfkit
Version:        0.6.1
Release:        0
Summary:        Python wrapper for wkhtmltopdf, a HTML-to-PDF converter that uses Qt/WebKit
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/JazzCore/python-pdfkit
Source:         https://files.pythonhosted.org/packages/source/p/pdfkit/pdfkit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       wkhtmltopdf
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  wkhtmltopdf
# /SECTION
%python_subpackages

%description
Python wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

%prep
%setup -q -n pdfkit-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
