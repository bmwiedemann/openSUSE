#
# spec file for package gparted
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


Name:           gparted
Version:        1.6.0
Release:        0
Summary:        Gnome Partition Editor
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://gparted.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/gparted/gparted/gparted-%{version}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/project/gparted/gparted/gparted-%{version}/%{name}-%{version}.tar.gz.sig
Source98:       %{name}.policy
Source99:       %{name}.keyring
BuildRequires:  polkit-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  polkit
BuildRequires:  /usr/bin/pkexec
BuildRequires:  update-desktop-files
BuildRequires:  xfsprogs-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.32
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.4.0
BuildRequires:  pkgconfig(libparted) >= 2.2
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.5.1
Requires:       gpart
Requires:       hdparm
Requires:       mtools
Requires:       parted
Requires:       polkit
Requires:       util-linux
Recommends:     btrfsprogs >= 4.1
Recommends:     cryptsetup
Recommends:     e2fsprogs
Recommends:     exfatprogs
Recommends:     hfsutils
Recommends:     jfsutils
Recommends:     nilfs-utils
Recommends:     ntfsprogs
Recommends:     udftools
Recommends:     xfsprogs
Requires:     /usr/bin/pkexec
%if !0%{?is_opensuse}
BuildRequires:  translation-update-upstream
%endif

%description
GParted is a utility for creating, destroying, resizing, moving,
checking and copying partitions, and the filesystems on them. This is
useful for creating space for new operating systems, reorganizing
disk usage, copying data residing on hard disks and mirroring one
partition with another (disk imaging).

%lang_package

%prep
%autosetup -p1
%if !0%{?is_opensuse}
translation-update-upstream
%endif

%build
export GKSUPROG="pkexec"
%configure \
  --enable-libparted-dmraid \
  --enable-xhost-root
%make_build

%install
%make_install

install -Dm0644 %{SOURCE98} %{buildroot}%{_datadir}/polkit-1/actions/org.opensuse.policykit.%{name}.policy
# Here we remove upstream policy file since we have our own
rm %{buildroot}%{_datadir}/polkit-1/actions/org.gnome.%{name}.policy

%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%files
%doc README ChangeLog AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{_libexecdir}/%{name}bin
%{_mandir}/man8/%{name}.8%{?ext_man}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/polkit-1/actions/org.opensuse.policykit.%{name}.policy
%{_datadir}/help/C/%{name}/index.docbook
%{_datadir}/help/C/%{name}/figures/gparted_window.png
%dir %{_datadir}/help/C/%{name}
%dir %{_datadir}/help/C/%{name}/figures

%files lang -f %{name}.lang

%changelog
