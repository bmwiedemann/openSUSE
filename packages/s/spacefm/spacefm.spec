#
# spec file for package spacefm
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


Name:           spacefm
Version:        1.0.6
Release:        0
Summary:        Multi-panel tabbed file and desktop manager
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/File utilities
URL:            http://ignorantguru.github.io/spacefm
Source:         https://github.com/IgnorantGuru/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE spacefm-fix-implicit-decl.patch -- Fix implicit declaration of "major" and "minor" macros.
Patch0:         spacefm-fix-implicit-decl.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Fix-build-with-GCC10.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
# Not available in SLE
%if 0%{?is_opensuse}
BuildRequires:  pkgconfig(libffmpegthumbnailer)
%endif
BuildRequires:  pkgconfig(libudev) >= 143
Recommends:     %{name}-lang
# Mount without root requirement.
Recommends:     udisks2
# Plugin download.
Recommends:     wget
# Execution of SpaceFM and applications from root.
Recommends:     xdg-utils

%description
SpaceFM is a multi-panel tabbed file and desktop manager for GNU/Linux
with built-in VFS, udev-based device manager, customisable menu system
and bash integration. SpaceFM is popular among novice and power users
alike for its stability, speed, convenience and flexibility.

%lang_package

%prep
%autosetup -p1

echo 'tmp_dir=%{_tmppath}' > %{name}.conf

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --with-preferable-sudo=%{_bindir}/xdg-su \
%if 0%{?is_opensuse} < 1
  --disable-video-thumbnails               \
%endif
  --htmldir=%{_docdir}/%{name}

make %{?_smp_mflags} V=1

%install
%make_install

%suse_update_desktop_file -G 'Search for Files' %{name}-find GTK System Utility FileManager
%fdupes %{buildroot}%{_datadir}/
%find_lang %{name}

%files
%license COPYING COPYING-LGPL
%doc AUTHORS ChangeLog README
%{_docdir}/%{name}/
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%dir %{_datadir}/icons/Faenza/
%dir %{_datadir}/icons/Faenza/apps/
%dir %{_datadir}/icons/Faenza/apps/*/
%{_datadir}/icons/Faenza/apps/*/%{name}*.png
%{_datadir}/mime/packages/%{name}-mime.xml

%files lang -f %{name}.lang

%changelog
