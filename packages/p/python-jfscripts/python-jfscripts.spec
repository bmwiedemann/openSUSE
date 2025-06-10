#
# spec file for package python-jfscripts
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_without libalternatives
Name:           python-jfscripts
Version:        1.1.0
Release:        0
Summary:        A collection of various tools written by Josef Friedrich
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Josef-Friedrich/python-scripts
Source:         https://files.pythonhosted.org/packages/source/j/jfscripts/jfscripts-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-termcolor
Requires:       python-typing-extensions
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
%pyproject_wheel

%install
%pyproject_install
%python_expand find %{buildroot}/%{$python_sitelib}/jfscripts/ -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \;
%python_expand cd %{buildroot}%{_bindir} && find . -name "*.py" -exec sh -c 'mv $0 `basename "$0" .py`' '{}' \;
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -f %{buildroot}%{_bindir}/_current_flavor
# Prepare for alts usage
for p in dns-ipv6-prefix extract-pdftext find-dupes-by-size image-into-pdf \
    list-files mac-to-eui64 pdf-compress ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

#%%check
# Upstream does not provide any tests

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative dns-ipv6-prefix
%python_libalternatives_reset_alternative extract-pdftext
%python_libalternatives_reset_alternative find-dupes-by-size
%python_libalternatives_reset_alternative image-into-pdf
%python_libalternatives_reset_alternative list-files
%python_libalternatives_reset_alternative mac-to-eui64
%python_libalternatives_reset_alternative pdf-compress

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/dns-ipv6-prefix
%python_alternative %{_bindir}/extract-pdftext
%python_alternative %{_bindir}/find-dupes-by-size
%python_alternative %{_bindir}/list-files
%python_alternative %{_bindir}/mac-to-eui64
%python_alternative %{_bindir}/pdf-compress
%python_alternative %{_bindir}/image-into-pdf
%{python_sitelib}/jfscripts*

%changelog
