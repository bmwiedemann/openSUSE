#
# spec file for package epy
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


Name:           epy
Version:        2022.12.11+git.1675870044.c7a87f3
Release:        0
Summary:        CLI ebook reader
License:        GPL-3.0-only
URL:            https://github.com/wustho/epy
# Source:         https://files.pythonhosted.org/packages/source/e/epy-reader/epy-reader-%%{version}.tar.gz#/epy-%%{version}.tar.gz
Source:         epy-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  python3-curses
BuildRequires:  python3-mobi
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-curses
Requires:       python3-mobi
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
python3 -mpip wheel --no-deps --disable-pip-version-check --use-pep517 \
    --no-build-isolation --progress-bar off --verbose . -w build/

%install
python3 -mpip install --root %{buildroot} --no-warn-script-location \
    --disable-pip-version-check --no-compile --no-deps --progress-bar off \
    build/epy_reader-*-py3-none-any.whl

%check
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
pytest -v tests

%files
%doc README.md
%license LICENSE
%{_bindir}/epy
%{python3_sitelib}/*

%changelog
