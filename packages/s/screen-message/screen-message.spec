#
# spec file for package screen-message
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


Name:           screen-message
Version:        0.25
Release:        0
Summary:        Program to display a short text fullscreen
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://www.joachim-breitner.de/en/projects#screen-message
Source:         https://www.joachim-breitner.de/archive/screen-message/%{name}-%{version}.tar.gz
Patch0:         inst-dir.patch
# PATCH-FIX-UPSTREAM my_gdk_rgba_parse_void.patch -- fix return value of function
Patch1:         my_gdk_rgba_parse_void.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
BuildRequires:  pango-devel
BuildRequires:  update-desktop-files

%description
Screen Message is a program to display a text as large as possible on
the screen. The text can be edited while Screen Message is running.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf --install
%configure --bindir=%{_bindir}
mv README.Win32 README
make %{?_smp_mflags}

%install
%make_install %{?_smp_mflags}
%suse_update_desktop_file -r -N '%{name}' -G 'Screen-Message' sm Utility GTK Accessibility Presentation

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%doc README
%{_bindir}/sm
%{_datadir}/applications/sm.desktop
%{_datadir}/icons/hicolor/48x48/apps/sm.png
%{_mandir}/man6/sm.6%{?ext_man}

%changelog
