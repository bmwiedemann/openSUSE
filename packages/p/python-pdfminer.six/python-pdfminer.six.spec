#
# spec file for package python-pdfminer.six
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
%define skip_python2 1
Name:           python-pdfminer.six
Version:        20200726
Release:        0
Summary:        PDF parser and analyzer
License:        MIT
URL:            https://github.com/pdfminer/pdfminer.six
Source:         https://github.com/pdfminer/pdfminer.six/archive/%{version}.tar.gz#/pdfminer.six-%{version}.tar.gz
# https://github.com/pdfminer/pdfminer.six/pull/489
Patch0:         python-pdfminer.six-remove-nose.patch
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
Requires:       python-cryptography
Requires:       python-pycryptodome
Requires:       python-six
Requires:       python-sortedcontainers
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       python-pdfminer3k = %{version}
Obsoletes:      python-pdfminer3k < %{version}
BuildArch:      noarch
%python_subpackages

%description
Fork of PDFMiner using six for Python3 compatibility.

PDFMiner is a tool for extracting information from PDF documents.
Unlike other PDF-related tools, it focuses entirely on getting
and analyzing text data. PDFMiner allows to obtain the exact
location of texts in a page, as well as other information such
as fonts or lines. It includes a PDF converter that can transform
PDF files into other text formats (such as HTML). It has an
extensible PDF parser that can be used for other purposes instead
of text analysis.

%prep
%setup -q -n pdfminer.six-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' pdfminer/psparser.py
sed  -i '1i #!%{_bindir}/python3' tools/dumppdf.py tools/pdf2txt.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

mv %{buildroot}%{_bindir}/dumppdf.py %{buildroot}%{_bindir}/dumppdf
mv %{buildroot}%{_bindir}/pdf2txt.py %{buildroot}%{_bindir}/pdf2txt
%python_clone -a %{buildroot}%{_bindir}/pdf2txt
%python_clone -a %{buildroot}%{_bindir}/dumppdf

%check
%python_expand nosetests-%{$python_bin_suffix} -v

%post
%python_install_alternative pdf2txt
%python_install_alternative dumppdf

%postun
%python_uninstall_alternative pdf2txt
%python_uninstall_alternative dumppdf

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/dumppdf
%python_alternative %{_bindir}/pdf2txt
%{python_sitelib}/pdfminer*

%changelog
