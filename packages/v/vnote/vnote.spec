#
# spec file for package vnote
#
# Copyright (c) 2020 SUSE LLC
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


Name:           vnote
Version:        2.10
Release:        0
Summary:        A Vim-inspired note-taking application, especially for Markdown
License:        MIT
Group:          Productivity/Text/Editors
URL:            https://github.com/tamlok/vnote
Source0:        %{name}-%{version}.tar.gz
Source1:        hoedown-e63d216.zip
Source2:        marked-f1ddca7.zip
BuildRequires:  libqt5-qtbase-devel >= 5.9
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtwebengine-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Recommends:     libssl44
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
VNote is a note-taking application, designed especially for Markdown.
VNote provides both note management and Markdown edit experience.

%prep
%setup -q

cp %{_sourcedir}/hoedown-e63d216.zip .
unzip hoedown-e63d216.zip
rm hoedown-e63d216.zip

cp %{_sourcedir}/marked-f1ddca7.zip .
unzip marked-f1ddca7.zip
rm marked-f1ddca7.zip
mv marked src/utils

%build
mkdir build && cd build
qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true" ../VNote.pro
make %{?_smp_mflags}

%install
cd build
make install INSTALL_ROOT="%{buildroot}"
%suse_update_desktop_file -r vnote Utility TextEditor

%files
%defattr(-,root,root)
%{_bindir}/VNote
%{_bindir}/vnote
%{_datadir}/applications/vnote.desktop
%{_datadir}/icons/hicolor
%doc README.md changes.md
%license LICENSE

%changelog
