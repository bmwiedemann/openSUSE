#
# spec file for package qt-fsarchiver
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
# or upstream https://sourceforge.net/p/qt-fsarchiver/tickets/


%define custom_version 0.8.5-12
Name:           qt-fsarchiver
Version:        0.8.5_12
Release:        0
Summary:        Qt GUI for fsarchiver
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            http://qt-fsarchiver.sourceforge.net/
Source0:        %{name}-%{custom_version}.tar.gz
Source1:        %{name}-terminal-%{custom_version}.tar.gz
BuildRequires:  e2fsprogs-devel
BuildRequires:  libattr-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(e2p)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(zlib)
Recommends:     btrfsprogs
Recommends:     gdisk
Recommends:     jfsutils
Recommends:     nfs-kernel-server
Recommends:     nmap
Recommends:     samba
Recommends:     sshfs
Recommends:     xfsprogs

%description
qt-fsarchiver is a GUI for the program fsarchiver to backup/save/restore partitions and folders.

%lang_package

%prep
%setup -q -n %{name}
%setup -T -D -a 1 -n %{name}
rm -f .qmake.stash
rm -f translations/*.qm
sed "s|target.path = /usr/sbin|target.path = %{_sbindir}|" -i %{name}.pro
sed "s|icon.path = /usr/share/app-install/icons|icon.path = %{_datadir}/icons/hicolor/48x48/apps|" -i %{name}.pro
sed "s|autostart.path = /usr/share/applications|autostart.path = %{_datadir}/applications|" -i %{name}.pro
sed "s|doc.path = /usr/share/doc/qt-fsarchiver/doc|doc.path = %{_docdir}/%{name}|" -i %{name}.pro
sed "s|Icon=/usr/share/app-install/icons/harddrive2.png|Icon=%{name}|" -i starter/%{name}.desktop
echo "GenericName=Qt GUI for fsarchiver" >> starter/%{name}.desktop
echo "GenericName[lt]=Qt fsarchiver" >> starter/%{name}.desktop

%build
pushd %{name}-terminal
%qmake5 %{name}-terminal.pro
%make_jobs
popd
%qmake5 %{name}.pro
%make_jobs

%install
pushd %{name}-terminal
%make_install INSTALL_ROOT=%{buildroot}
popd
%make_install INSTALL_ROOT=%{buildroot}

#clean doc directory from backup files
rm -rf %{buildroot}%{_datadir}/doc/%{name}/*~
rm -rf %{buildroot}%{_datadir}/doc/%{name}-terminal

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/applications
mv ~/rpmbuild/BUILD/qt-fsarchiver/src/sbin/findsmb-qt %{buildroot}/%{_sbindir}
mv ~/rpmbuild/BUILD/qt-fsarchiver/src/sbin/qt-fsarchiver.sh %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/harddrive2.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/qt5/translations/
install -m 0644 -p translations/*.qm %{buildroot}%{_datadir}/qt5/translations/

%suse_update_desktop_file -r %{name} System Filesystem

%files
%{_sbindir}/%{name}
%{_sbindir}/%{name}.sh
%{_sbindir}/%{name}-terminal
%{_sbindir}/findsmb-qt
%defattr(644,root,root,755)
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_docdir}/%{name}
%exclude %{_datadir}/qt5/translations/%{name}*.qm

%files lang
%dir %{_datadir}/qt5
%dir %{_datadir}/qt5/translations
%{_datadir}/qt5/translations/%{name}*.qm


%changelog
