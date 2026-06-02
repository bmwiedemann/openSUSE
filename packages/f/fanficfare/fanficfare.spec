#
# spec file for package fanficfare
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define modname FanFicFare
%define modnamedown fanficfare
Name:           fanficfare
Version:        4.58.0
Release:        0
Summary:        Tool for making eBooks from stories on fanfiction and other web sites
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/JimmXinu/FanFicFare
Source:         https://github.com/JimmXinu/FanFicFare/archive/v%{version}/FanFicFare-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-chardet
BuildRequires:  python3-cloudscraper
BuildRequires:  python3-html2text
BuildRequires:  python3-html5lib
BuildRequires:  python3-pip
BuildRequires:  python3-requests-file
BuildRequires:  python3-setuptools >= 17.1
BuildRequires:  python3-wheel
Requires:       python3-Brotli
Requires:       python3-beautifulsoup4
Requires:       python3-chardet
Requires:       python3-cloudscraper
Requires:       python3-html2text
Requires:       python3-html5lib
Requires:       python3-requests
Requires:       python3-requests-file
Requires:       python3-urllib3
BuildArch:      noarch
# Renaming a package
Provides:       python3-fanficfare = %{version}
Provides:       python311-fanficfare = %{version}
Provides:       python313-fanficfare = %{version}
Provides:       python314-fanficfare = %{version}
Obsoletes:      python3-fanficfare < %{version}
Obsoletes:      python311-fanficfare < %{version}
Obsoletes:      python313-fanficfare < %{version}
Obsoletes:      python314-fanficfare < %{version}

%description
FanFicFare is a tool for downloading fanfiction and original stories from various sites into ebook form.

FanFicFare is the rename and move of the FanFictionDownLoader (AKA FFDL, AKA fanficdownloader) project.

Main Features of FanFicFare:
    - Download fanfiction stories from various sites into ebooks.
    - Create various ebook formats (currently epub, mobi, HTML, txt)
    - Also available as a Calibre plugin (not in this package)
    - Ability to update already downloaded book

%prep
%autosetup -p1 -n %{modname}-%{version}

rm -rf included_dependencies/

find . -name \*.py -exec sed -i -e '/^#!\/usr\/bin\/python/d' '{}' \;
dos2unix DESCRIPTION.rst README.md

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%check
# no upstream tests

%files
%license LICENSE
%doc DESCRIPTION.rst README.md
%{_bindir}/fanficfare
%{python3_sitelib}/[fF]anficfare-%{version}*-info
%{python3_sitelib}/[fF]anficfare

%changelog
