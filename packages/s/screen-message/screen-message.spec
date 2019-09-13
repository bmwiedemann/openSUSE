#
# spec file for package screen-message
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


Name:           screen-message
Version:        0.23
Release:        0
Summary:        Displays a short text fullscreen
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://darcs.nomeata.de/screen-message.debian
Source:         %{name}-%{version}.tar.gz
Patch0:         inst-dir.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
BuildRequires:  pango-devel
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Screen Message is a small program to display a text as large as possible on your screen. You can edit the text while Screen Message is running. To blank the text, press Esc. To quit Screen Message, press Ctrl-Q or press Esc twice.

%prep
%setup -q
%patch0 -p1

%build
autoreconf --install
%configure --bindir=%{_bindir}
mv README.Win32 README
mv debian/changelog ChangeLog
make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot} %{?_smp_mflags}
%suse_update_desktop_file -r -N '%{name}' -G 'Screen-Message' sm Utility GTK Accessibility Presentation

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_bindir}/sm
%{_datadir}/applications/sm.desktop
%{_datadir}/icons/hicolor/48x48/apps/sm.png
%{_mandir}/man6/sm.6%{ext_man}

%changelog
