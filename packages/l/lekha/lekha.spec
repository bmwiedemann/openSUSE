#
# spec file for package lekha
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


Name:           lekha
Version:        0.2.1
Release:        0
Summary:        PDF Reader
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/PDF
URL:            https://github.com/kaihu/lekha
Source0:        %{URL}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Lekha doesn't ship a icon so ship a generic one for it for now
Source1:        graphics-viewer-document.png
# .desktop files contained actions with no action defined
#  I couldn't work out what the actions should do so they are removed
Patch0:         fix-invalid-actions-in-desktop-file.patch
BuildRequires:  efl-devel
BuildRequires:  python3-PyPDF2
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-efl
BuildRequires:  python3-xdg
Requires:       python3-PyPDF2
Requires:       python3-efl
Requires:       python3-xdg

%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
ExcludeArch:    %ix86

%description
EFL and python based pdf reader.

%prep
%setup -q
%patch0

%build
python3 setup.py build

%install
python3 setup.py install --root "%{buildroot}"

# install icon
mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/accessories-document-viewer.png

%if 0%{?suse_version}
%suse_update_desktop_file lekha "Office;Viewer;"
%endif
rm -rf "%{buildroot}/%{_datadir}/doc"

%files
%defattr(-,root,root,-)
%doc README.md COPYING
%{_bindir}/lekha
%{python3_sitelib}/*
%{_datadir}/pixmaps/accessories-document-viewer.png
%{_datadir}/applications/lekha.desktop

%changelog
