#
# spec file for package python-pdfminer.six
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
Patch1:         import-from-non-pythonpath-files.patch
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sortedcontainers}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
Requires:       python-cryptography
Requires:       python-sortedcontainers
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       python-pdfminer3k = %{version}
Obsoletes:      python-pdfminer3k < %{version}
BuildArch:      noarch
%python_subpackages

%description
Pdfminer.six is a community maintained fork of the original PDFMiner. It
is a tool for extracting information from PDF documents. It focuses on
getting and analyzing text data. Pdfminer.six extracts the text from a
page directly from the sourcecode of the PDF. It can also be used to get
the exact location, font or color of the text.

%prep
%setup -q -n pdfminer.six-%{version}
%autopatch -p1
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
%pytest

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
