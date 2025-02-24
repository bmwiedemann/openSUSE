#
# spec file for package python-extract-msg
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-extract-msg
Version:        0.53.1
Release:        0
Summary:        Extracts emails and attachments saved in Microsoft Outlook's msg files
License:        GPL-3.0-only
URL:            https://github.com/TeamMsgExtractor/msg-extractor
Source:         %{url}/archive/v%{version}.tar.gz#/extract_msg-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4 >= 4.11.1}
BuildRequires:  %{python_module RTFDE >= 0.1.1}
BuildRequires:  %{python_module compressed_rtf >= 1.0.6}
BuildRequires:  %{python_module ebcdic >= 1.1.1}
BuildRequires:  %{python_module olefile >= 0.47}
BuildRequires:  %{python_module red-black-tree-mod >= 1.20}
BuildRequires:  %{python_module tzlocal >= 4.2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-RTFDE >= 0.1.1
Requires:       python-beautifulsoup4 >= 4.11.1
Requires:       python-compressed_rtf >= 1.0.6
Requires:       python-ebcdic >= 1.1.1
Requires:       python-olefile >= 0.47
Requires:       python-red-black-tree-mod >= 1.20
Requires:       python-tzlocal >= 4.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The python package extract-msg automates the extraction of key email
data (from, to, cc, date, subject, body) and the email’s attachments.

%prep
%autosetup -p1 -n msg-extractor-%{version}
sed -i '/\#\!\/usr\/bin\/env python3/d' extract_msg/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/extract_msg
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v tests.py

%post
%python_install_alternative extract_msg

%postun
%python_uninstall_alternative extract_msg

%files %{python_files}
%python_alternative %{_bindir}/extract_msg
%{python_sitelib}/extract_msg
%{python_sitelib}/extract_msg-%{version}.dist-info

%changelog
