#
# spec file for package kasumi
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           kasumi
BuildRequires:  anthy-devel gcc-c++ gtk2-devel libtool update-desktop-files
License:        GPL-2.0+
Group:          System/I18n/Japanese
AutoReqProv:    on
Provides:       locale(anthy:ja)
Version:        2.5
Release:        1
Url:            http://kasumi.sourceforge.jp/
Source0:        kasumi-%{version}.tar.bz2
Patch:          desktop.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Dictionary Tool for Anthy

%description
A graphical tool to edit the personal dictionary for Anthy.



Authors:
--------
    Takashi Nakamoto <bluedwarf@openoffice.org>

%prep
%setup -q
%patch -p1

%build
libtoolize --force
autoreconf --force --install
%configure
make  %{?jobs:-j %jobs}

%install
%makeinstall
%suse_update_desktop_file -i %name System SystemSetup
%find_lang kasumi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kasumi.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_datadir}/pixmaps/kasumi.png
%{_datadir}/applications/kasumi.desktop
%{_mandir}/man1/*

%changelog
