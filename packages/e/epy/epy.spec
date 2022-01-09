#
# spec file for package epy
#
# Copyright (c) 2022 SUSE LLC
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


Name:           epy
Version:        2022.1.8+git.1641653565.c1f9b4e
Release:        0
Summary:        CLI ebook reader
License:        GPL-3.0-only
URL:            https://github.com/wustho/epy
# Source:         https://files.pythonhosted.org/packages/source/e/epy-reader/epy-reader-%%{version}.tar.gz#/epy-%%{version}.tar.gz
Source:         epy-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-mobi
BuildRequires:  python3-setuptools
Requires:       python3-mobi
Suggests:       sdcv
Suggests:       dictd
Suggests:       mimic
BuildArch:      noarch

%description
CLI Ebook reader. Fork of epr with these extra features:

    Supported formats:
        Epub (.epub, .epub3)
        FictionBook (.fb2)
        Mobi (.mobi)
        AZW3 (.azw3), some but not all

    Reading progress percentage
    Bookmarks
    External dictionary integration (sdcv or dict)
    Inline formats: bold and italic (depend on terminal and font capability. Italic only supported in python>=3.7)
    Text-to-Speech (with additional setup)
    Double Spread

%prep
%autosetup -p1 -n epy-%{version}

# All those shebangs are just harmful
find . -name \*.py -exec sed -i "1{/#!\/usr\/bin\/env python/d}" '{}' \;

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/epy
%{python3_sitelib}/*

%changelog
