#
# spec file for package pcmanfm
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


Name:           pcmanfm
Version:        1.3.1
Release:        0
Summary:        The LXDE file manager
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
Url:            http://www.lxde.org/
Source0:        http://downloads.sourceforge.net/pcmanfm/pcmanfm-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libfm) >= 1.0
BuildRequires:  pkgconfig(libfm-gtk) >= 1.0.1
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(x11)
# needed for trash
Requires:       gvfs
Requires:       gvfs-backends
Requires:       libfm
# needed to mount devices
Requires:       menu-cache
Requires:       polkit-gnome
# needed to switch to root
Requires:       xdg-utils
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%lang_package

%description
A file manager with tabbed browsing. It's also the
LXDE default file manager.

%package devel
Summary:        Development files for PCManFM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtk2-devel
Requires:       libfm-gtk4 >= %{version}
Requires:       libfm4 >= %{version}
Requires:       pkg-config

%description devel
Development files for PCManFM.


%prep
%setup   -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# no user-desktop in hicolor icon theme
sed -i "3d" %{buildroot}%{_datadir}/applications/pcmanfm-desktop-pref.desktop
%suse_update_desktop_file %{name} Application System Utility GTK FileManager
%suse_update_desktop_file pcmanfm-desktop-pref
%fdupes %{buildroot}
%find_lang %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/pcmanfm-desktop-pref.desktop
%{_mandir}/man1/pcmanfm.1.gz
%dir %{_sysconfdir}/xdg/pcmanfm
%dir %{_sysconfdir}/xdg/pcmanfm/default
%config %{_sysconfdir}/xdg/pcmanfm/default/pcmanfm.conf

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}-modules.h

%changelog
