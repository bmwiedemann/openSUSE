#
# spec file for package vnote
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


Name:           vnote
Version:        3.10.1
Release:        0
Summary:        A Vim-inspired note-taking application, especially for Markdown
License:        LGPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://github.com/tamlok/vnote
Source0:        https://github.com/tamlok/vnote/archive/v%{version}.tar.gz#/vnote-%{version}.tar.gz
Source1:        vtextedit-08b440d.zip
Source2:        hunspell-efb0389.zip
Source3:        sonnet-403863f.zip
Source4:        syntax-highlighting-807895f.zip
BuildRequires:  libqt5-qtbase-devel >= 5.12
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libqt5-qtwebengine-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
Recommends:     libssl44
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
VNote is a note-taking application, designed especially for Markdown.
VNote provides both note management and Markdown edit experience.

%package -n libVSyntaxHighlighting1
Summary:        Library files for vnote
Group:          System/Libraries

%description -n libVSyntaxHighlighting1
This package provides library files for vnote.

%package -n libVTextEdit1
Summary:        Library files for vnote
Group:          System/Libraries

%description -n libVTextEdit1
This package provides library files for vnote.

%prep
%setup -q

cd libs
rm -r vtextedit
unzip %{_sourcedir}/vtextedit-08b440d.zip
mv vtextedit-* vtextedit

cd vtextedit/src/libs
rm -r hunspell sonnet syntax-highlighting
unzip %{_sourcedir}/hunspell-efb0389.zip
mv hunspell-* hunspell
unzip %{_sourcedir}/sonnet-403863f.zip
mv sonnet-* sonnet
unzip %{_sourcedir}/syntax-highlighting-807895f.zip
mv syntax-highlighting-* syntax-highlighting

%build
mkdir build && cd build
qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true" ../vnote.pro
make %{?_smp_mflags}

%install
cd build
make install INSTALL_ROOT="%{buildroot}"
rm %{buildroot}%{_prefix}/lib/libVSyntaxHighlighting.so
rm %{buildroot}%{_prefix}/lib/libVTextEdit.so
%suse_update_desktop_file -r vnote Utility TextEditor

%post -n libVSyntaxHighlighting1 -p /sbin/ldconfig
%postun -n libVSyntaxHighlighting1 -p /sbin/ldconfig

%post -n libVTextEdit1 -p /sbin/ldconfig
%postun -n libVTextEdit1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/vnote
%{_bindir}/vnote_extra.rcc
%{_datadir}/applications/vnote.desktop
%{_datadir}/icons/hicolor
%doc README.md changes.md
%license COPYING.LESSER

%files -n libVSyntaxHighlighting1
%{_prefix}/lib/libVSyntaxHighlighting.so*

%files -n libVTextEdit1
%{_prefix}/lib/libVTextEdit.so*

%changelog
