#
# spec file for package python-olefile
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


%{?sle15_python_module_pythons}
Name:           python-olefile
Version:        0.47
Release:        0
Summary:        Python package to read and write Microsoft OLE2 files
License:        BSD-2-Clause AND HPND
URL:            https://github.com/decalage2/olefile
Source:         https://files.pythonhosted.org/packages/source/o/olefile/olefile-%{version}.zip
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
Olefile is a Python package to parse, read and write Microsoft OLE2
files (also called Structured Storage, Compound File Binary Format or
Compound Document File Format), such as Microsoft Office 97-2003
documents, vbaProject.bin in MS Office 2007+ files, Image Composer and
FlashPix files, Outlook messages, StickyNotes, several Microscopy file
formats, McAfee antivirus quarantine files, etc.

%prep
%setup -q -n olefile-%{version}
# Fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc CONTRIBUTORS.txt README.md
%license LICENSE.txt
%{python_sitelib}/olefile
%{python_sitelib}/olefile-*.dist-info

%changelog
