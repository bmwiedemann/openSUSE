#
# spec file for package pcmanfm
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.3.2+git20241103.1312f60
Release:        0
Summary:        The LXDE file manager
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://www.lxde.org/
Source0:        %{name}-%{version}.tar.zst
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libfm)
BuildRequires:  pkgconfig(libfm-gtk)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(x11)
# needed for trash
Requires:       gvfs
Requires:       gvfs-backends
# needed to mount devices
Requires:       menu-cache
Requires:       polkit-gnome
# needed to switch to root
Requires:       xdg-utils
Recommends:     %{name}-lang
%lang_package

%description
A file manager with tabbed browsing. It's also the
LXDE default file manager.

%package devel
Summary:        Development files for PCManFM
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtk3-devel
Requires:       libfm-gtk4
Requires:       libfm4
Requires:       pkgconfig
BuildArch:      noarch

%description devel
Development files for PCManFM.

%prep
%setup -q
find . -name COPYING -exec chmod -c 644 {} \;

%build
./autogen.sh
%configure
%make_build

%install
%make_install
# no user-desktop in hicolor icon theme
sed -i "3d" %{buildroot}%{_datadir}/applications/pcmanfm-desktop-pref.desktop
%fdupes %{buildroot}
%find_lang %{name}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/*.ui
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/pcmanfm-desktop-pref.desktop
%{_mandir}/man1/pcmanfm.1%{?ext_man}
%dir %{_sysconfdir}/xdg/pcmanfm
%dir %{_sysconfdir}/xdg/pcmanfm/default
%config %{_sysconfdir}/xdg/pcmanfm/default/pcmanfm.conf

%files lang -f %{name}.lang
%license COPYING

%files devel
%license COPYING
%{_includedir}/%{name}-modules.h

%changelog
