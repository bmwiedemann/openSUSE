#
# spec file for package clack
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           clack
Version:        0.1.4
Release:        0
Summary:        Simple text viewer
License:        GPL-3.0+
Group:          Productivity/Text/Editors
URL:            http://cassidyjames.com
Source:         https://github.com/cassidyjames/clack/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  elementary-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)

%description
Basic utility that just displays plain text files.

%prep
%setup -q

sed -i 's/\bmetainfo\b/appdata/' $(grep -rwl 'metainfo')

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file -r com.github.cassidyjames.clack GTK Utility TextEditor

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%doc AUTHORS LICENSE README.md
%{_bindir}/com.github.cassidyjames.clack
%dir %{_datadir}/appdata
%{_datadir}/appdata/com.github.cassidyjames.clack.appdata.xml
%{_datadir}/applications/com.github.cassidyjames.clack.desktop

%changelog
