#
# spec file for package xdg-user-dirs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xdg-user-dirs
Version:        0.17
Release:        0
Summary:        Utilities to handle user data directories
License:        GPL-2.0-only
Group:          System/GUI/Other
Url:            http://freedesktop.org/wiki/Software/xdg-user-dirs
Source0:        http://user-dirs.freedesktop.org/releases/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang

%description
xdg-user-dirs is a tool to help manage "well known" user directories
like the desktop folder and the music folder. It also
handles localization (i.e. translation) of the filenames.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# Change sr@Latn to sr@latin
mv %{buildroot}%{_datadir}/locale/sr@Latn %{buildroot}%{_datadir}/locale/sr@latin
%find_lang %{name} %{?no_lang_C}
# Create xinit script
mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d
echo "#!/bin/sh" >> %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
echo "%{_bindir}/xdg-user-dirs-update" >> %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
chmod a+x %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
%suse_update_desktop_file %{name}

%files
%doc AUTHORS COPYING README ChangeLog
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinitrc.d
%{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
%{_bindir}/xdg-user-dir
%{_bindir}/xdg-user-dirs-update
%{_sysconfdir}/xdg/autostart/xdg-user-dirs.desktop

%files lang -f %{name}.lang

%changelog
