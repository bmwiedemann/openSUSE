#
# spec file for package lector
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define display_name Lector
Name:           lector
Version:        0.5.1
Release:        0
Summary:        Qt based ebook reader
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/BasioMeusPuga/%{display_name}
Source:         https://github.com/BasioMeusPuga/%{display_name}/archive/%{version}.tar.gz#/%{display_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-devel
BuildRequires:  python3-qt5
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       python3 >= 3.6
Requires:       python3-beautifulsoup4
Requires:       python3-lxml
Requires:       python3-qt5
Requires:       python3-xmltodict
Recommends:     python3-poppler-qt5
Recommends:     python3-PyMuPDF
BuildArch:      noarch

%description

Currently supports:

* pdf
* epub
* mobi
* azw / azw3 / azw4
* cbr / cbz

%prep
%setup -q -n %{display_name}-%{version}

%build
%python3_build

%install
%python3_install

%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes -s %{buildroot}/%{_prefix}

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md AUTHORS TODO
%{python3_sitelib}/*
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{display_name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
