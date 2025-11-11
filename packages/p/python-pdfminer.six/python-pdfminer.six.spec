#
# spec file for package python-pdfminer.six
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pdfminer.six
Version:        20251107
Release:        0
Summary:        PDF parser and analyzer
License:        MIT
URL:            https://github.com/pdfminer/pdfminer.six
Source:         https://github.com/pdfminer/pdfminer.six/archive/%{version}.tar.gz#/pdfminer.six-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module charset-normalizer >= 2.0.0}
BuildRequires:  %{python_module cryptography >= 36.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 77.0.3}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-charset-normalizer >= 2.0.0
Requires:       python-cryptography >= 36.0.0
Provides:       python-pdfminer3k = %{version}
Obsoletes:      python-pdfminer3k < %{version}
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
Pdfminer.six is a community maintained fork of the original PDFMiner. It
is a tool for extracting information from PDF documents. It focuses on
getting and analyzing text data. Pdfminer.six extracts the text from a
page directly from the sourcecode of the PDF. It can also be used to get
the exact location, font or color of the text.

%prep
%autosetup -p1 -n pdfminer.six-%{version}
sed -i -e '/^#!\//, 1d' pdfminer/psparser.py
sed -i '1i #!/usr/bin/python3' tools/dumppdf.py tools/pdf2txt.py
sed -i "s/__VERSION__/%{version}/g" pdfminer/__init__.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
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

%pre
%python_libalternatives_reset_alternative pdf2txt
%python_libalternatives_reset_alternative dumppdf

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/dumppdf
%python_alternative %{_bindir}/pdf2txt
%{python_sitelib}/pdfminer
%{python_sitelib}/pdfminer[_.]six-%{version}.dist-info

%changelog
