#
# spec file for package python-fanficfare
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fanficfare
Version:        4.2.0
Release:        0
Summary:        Tool for making eBooks from stories on fanfiction and other web sites
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/JimmXinu/FanFicFare
Source:         https://github.com/JimmXinu/%{modname}/archive/v%{version}/%{modname}-%{version}.tar.gz
# Source:         %%{modname}-%%{version}.tar.gz
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module cloudscraper}
BuildRequires:  %{python_module html2text}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module setuptools >= 17.1}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-chardet
Requires:       python-cloudscraper
Requires:       python-html2text
Requires:       python-html5lib
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

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

sed -i -e '/^#!\/usr\/bin\/python/d' fanficfare/mobi{,html}.py
dos2unix DESCRIPTION.rst README.md

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/%{modnamedown}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative fanficfare

%postun
%python_uninstall_alternative fanficfare

%check
# no upstream tests

%files %{python_files}
%license LICENSE
%doc DESCRIPTION.rst README.md
%python_alternative %{_bindir}/%{modnamedown}
%{python_sitelib}/*

%changelog
