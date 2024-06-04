#
# spec file for package epy
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


Name:           epy
Version:        2022.12.11+git.1686460830.6b0e9fe
Release:        0
Summary:        CLI ebook reader
License:        GPL-3.0-only
URL:            https://github.com/wustho/epy
# Source:         https://files.pythonhosted.org/packages/source/e/epy-reader/epy-reader-%%{version}.tar.gz#/epy-%%{version}.tar.gz
Source:         epy-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  python311-curses
BuildRequires:  python311-pip
BuildRequires:  python311-poetry-core
BuildRequires:  python311-pytest
BuildRequires:  python311-setuptools
BuildRequires:  python311-wheel
Requires:       python311-curses
Suggests:       dictd
Suggests:       mimic
Suggests:       sdcv
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
    Inline formats: bold and italic (depend on terminal and font
        capability. Italic only supported in python>=3.7)
    Text-to-Speech (with additional setup)
    Double Spread

%prep
%autosetup -p1 -n epy-%{version}

# All those shebangs are just harmful
find . -name \*.py -print0 | while IFS= read -r -d $'\0' script; do
    sed -i "1{/#!\s*\/usr\/bin\/\(env \)\?python/d}" "$script"
    chmod -x "$script"
done

%build
%python311_pyproject_wheel

%install
%python311_pyproject_install
%fdupes %{buildroot}/%{python311_sitelib}
%python311_fix_shebang

%check
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}/%{python311_sitelib}
pytest-3.11 -v tests

%files
%doc README.md
%license LICENSE
%{_bindir}/epy
%{python311_sitelib}/epy_reader-2023.6.11.dist-info
%{python311_sitelib}/epy_reader

%changelog
