#
# spec file for package q5go
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


Name:           q5go
Version:        2.0
Release:        0
Summary:        A Go board including an editor and analysis frontend
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://github.com/bernds/q5go
Source0:        https://github.com/bernds/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
# Required for https://doc.qt.io/qt-5/qmetaobject.html#invokeMethod-4
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)

%description
q5Go is a tool for Go players which performs the following functions:

 * SGF editor
 * Analysis frontend for Leela Zero (or compatible engines)
 * GTP interface
 * IGS client
 * Export to a variety of formats

%prep
%autosetup -p1 -n q5Go-q5go-%{version}

%build
pushd src
%qmake5 q5go.pro

%make_jobs
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/q5go/translations

pushd src
install -m 0755 q5go %{buildroot}%{_bindir}/

# install translations
install -m 0644 translations/*.qm %{buildroot}%{_datadir}/q5go/translations/

# q5go doesn't have a highres icon
install -m 0644 images/clientwindow/Bowl.png %{buildroot}%{_datadir}/pixmaps/q5go.png

%suse_update_desktop_file -c q5Go q5Go "Go client" q5go q5go "Qt;Game;BoardGame;"
popd

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/q5go
%{_datadir}/applications/q5Go.desktop
%{_datadir}/pixmaps/q5go.png
%{_datadir}/q5go

%changelog
