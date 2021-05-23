#
# spec file for package qt-fsarchiver
#
# Copyright (c) 2021 SUSE LLC
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


%define hyphen_version 0.8.5-22
%define terminal_version 0.8.5-22
Name:           qt-fsarchiver
Version:        0.8.5_22
Release:        0
Summary:        Qt GUI for fsarchiver
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://sourceforge.net/projects/qt-fsarchiver
Source0:        %{URL}/files/source/%{name}/%{name}-%{hyphen_version}.tar.gz
Source1:        %{URL}/files/source/%{name}-terminal/%{name}-terminal-%{terminal_version}.tar.gz
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
Requires:       ccrypt
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

rm -vf .qmake.stash
rm -vf translations/*.qm
# Fix file permissions
find doc -type f -exec chmod -x \{\} +

%build
export CFLAGS="%{optflags} -fcommon"
pushd %{name}-terminal
%qmake5 "DOC_DIR=%{_docdir}/%{name}-terminal" %{name}-terminal.pro
%make_build
popd
%qmake5 "DOC_DIR=%{_docdir}/%{name}" %{name}.pro
%make_build

%install
pushd %{name}-terminal
%make_install INSTALL_ROOT=%{buildroot}
popd
%make_install INSTALL_ROOT=%{buildroot}
# Install translations
mkdir -p %{buildroot}%{_datadir}/qt5/translations/
install -m 0644 translations/*.qm %{buildroot}%{_datadir}/qt5/translations/
# -terminal package contains the same documentation
rm -rf %{buildroot}%{_docdir}/%{name}-terminal

%files
%{_sbindir}/%{name}
%{_sbindir}/%{name}.sh
%{_sbindir}/%{name}-terminal
%doc %{_docdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%exclude %{_datadir}/qt5/translations/%{name}*.qm

%files lang
%dir %{_datadir}/qt5
%dir %{_datadir}/qt5/translations
%{_datadir}/qt5/translations/%{name}*.qm

%changelog
