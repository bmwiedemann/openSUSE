#
# spec file for package python-xhtml2pdf
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


Name:           python-xhtml2pdf
Version:        0.2.16
Release:        0
Summary:        PDF Generator Using HTML and CSS
License:        Apache-2.0
URL:            https://github.com/xhtml2pdf/xhtml2pdf
Source:         https://github.com/xhtml2pdf/xhtml2pdf/archive/refs/tags/v%{version}.tar.gz#/xhtml2pdf-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/xhtml2pdf/xhtml2pdf/pull/784 fix reDOS CVE in getColor function
Patch0:         CVE-2024-25885.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 8.1.1
Requires:       python-arabic-reshaper >= 3.0.0
Requires:       python-html5lib >= 1.1
Requires:       python-pyHanko >= 0.12.1
Requires:       python-pyhanko-certvalidator >= 0.19.5
Requires:       python-pypdf >= 3.1.0
Requires:       python-python-bidi >= 0.4.2
Requires:       python-reportlab >= 4.0.4
Requires:       python-svglib >= 1.2.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      python-pisa
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 8.1.1}
BuildRequires:  %{python_module arabic-reshaper >= 3.0.0}
BuildRequires:  %{python_module html5lib >= 1.1}
BuildRequires:  %{python_module pyHanko >= 0.12.1}
BuildRequires:  %{python_module pyhanko-certvalidator >= 0.19.5}
BuildRequires:  %{python_module pypdf >= 3.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-bidi >= 0.4.2}
BuildRequires:  %{python_module reportlab >= 4.0.4}
BuildRequires:  %{python_module svglib >= 1.2.1}
# /SECTION
%python_subpackages

%description
xhtml2pdf is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and
pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3). It is completely
written in pure Python so it is platform independent.

The main benefit of this tool that a user with Web skills like HTML and CSS is
able to generate PDF templates very quickly without learning new technologies.

%prep
%autosetup -p1 -n xhtml2pdf-%{version}

sed -i '1{/^#!/d}' xhtml2pdf/paragraph.py xhtml2pdf/w3c/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/xhtml2pdf
%python_clone -a %{buildroot}%{_bindir}/pisa
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_document_with_broken_image or test_document_cannot_identify_image)'

%post
%python_install_alternative xhtml2pdf
%python_install_alternative pisa

%postun
%python_uninstall_alternative xhtml2pdf
%python_uninstall_alternative pisa

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/xhtml2pdf
%{python_sitelib}/xhtml2pdf-%{version}.dist-info
%python_alternative %{_bindir}/pisa
%python_alternative %{_bindir}/xhtml2pdf

%changelog
