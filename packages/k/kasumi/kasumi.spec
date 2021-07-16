#
# spec file for package kasumi
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


Name:           kasumi
Version:        2.5
Release:        0
Summary:        Dictionary Tool for Anthy
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
URL:            http://kasumi.sourceforge.jp/
Source0:        kasumi-%{version}.tar.bz2
Patch1:         desktop.patch
Patch2:         kasumi-2.5-gtk3.patch
Patch3:         kasumi-2.5-configure-gtk3.patch
Patch4:         kasumi-2.5-c++14.patch
BuildRequires:  anthy-devel
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libtool
BuildRequires:  update-desktop-files
Provides:       locale(anthy:ja)

%description
A graphical tool to edit the personal dictionary for Anthy.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
libtoolize --force
autoreconf --force --install
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -i %{name} System SystemSetup
%find_lang kasumi

%files -f kasumi.lang
%license COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_datadir}/pixmaps/kasumi.png
%{_datadir}/applications/kasumi.desktop
%{_mandir}/man1/*

%changelog
