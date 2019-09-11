#
# spec file for package leafpad
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


Name:           leafpad
Version:        0.8.18.1
Release:        0
Summary:        Graphical text editor and Notepad clone
License:        GPL-2.0
Group:          Productivity/Editors/Other
Url:            http://tarot.freeshell.org/leafpad/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Leafpad is a GTK+ based text editor. The user interface is similar to
"notepad". It uses a Single Document Interface to set out windows to view at a
time, and purposely uses no toolbar. Character encoding is autodetected.

%prep
%setup -q

%build
%configure \
	--enable-print \
	--enable-chooser
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%suse_update_desktop_file -r leafpad Utility TextEditor
%find_lang "%{name}"

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files -f "%{name}.lang"
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/leafpad
%{_datadir}/applications/leafpad.desktop
%{_datadir}/pixmaps/leafpad.png
%{_datadir}/pixmaps/leafpad.xpm
%{_datadir}/icons/*/*/apps/leafpad.*

%changelog
