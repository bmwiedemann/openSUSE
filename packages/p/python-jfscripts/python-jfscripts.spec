#
# spec file for package python-jfscripts
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-jfscripts
Version:        0.5.0
Release:        0
Summary:        A collection of various tools written by Josef Friedrich
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Josef-Friedrich/python-scripts
Source:         https://files.pythonhosted.org/packages/source/j/jfscripts/jfscripts-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyPDF2
Requires:       python-sphinx-argparse
Requires:       python-termcolor
BuildArch:      noarch
%python_subpackages

%description
A collection of various tools written by Josef Friedrich
  * dns-ipv6-prefix.py
  * extract-pdftext.py
  * find-dupes-by-size.py
  * list-files.py
  * mac-to-eui64.py
  * pdf-compress.py
  * image-into-pdf.py

%prep
%setup -q -n jfscripts-%{version}
find jfscripts/ -name "*.py" -exec sed -i 's|#! %{_bindir}/env python3|#!%{_bindir}/python3|g' {} \;

%build
%python_build

%install
%python_install
%python_expand find %{buildroot}/%{$python_sitelib}/jfscripts/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
%python_expand cd %{buildroot}%{_bindir} && find . -name "*.py" -exec sh -c 'mv $0 `basename "$0" .py`' '{}' \;
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -f %{buildroot}%{_bindir}/_current_flavor

#%%check
# Upstream does not provide any tests

%files %{python_files}
%license LICENSE
%doc README.rst
%python3_only %{_bindir}/dns-ipv6-prefix
%python3_only %{_bindir}/extract-pdftext
%python3_only %{_bindir}/find-dupes-by-size
%python3_only %{_bindir}/list-files
%python3_only %{_bindir}/mac-to-eui64
%python3_only %{_bindir}/pdf-compress
%python3_only %{_bindir}/image-into-pdf
%{python_sitelib}/jfscripts*

%changelog
