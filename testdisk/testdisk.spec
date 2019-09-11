#
# spec file for package testdisk
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           testdisk
Version:        7.1
Release:        0
Summary:        Tool to Recover and Fix Partitions
License:        GPL-2.0
Group:          System/Filesystems
Url:            https://www.cgsecurity.org/wiki/TestDisk
Source0:        https://www.cgsecurity.org/%{name}-%{version}.tar.bz2
BuildRequires:  hicolor-icon-theme
BuildRequires:  libewf-devel
BuildRequires:  libext2fs-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libreiserfs-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
%if 0%{?suse_version} >= 1210
BuildRequires:  libntfs-3g-devel
%else
BuildRequires:  ntfsprogs-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TestDisk is a data recovery software primarily designed to help recover lost
partitions and/or make non-booting disks bootable again.

%package -n photorec
Summary:        Tool to Undelete Files
Group:          System/Filesystems

%description -n photorec
PhotoRec is a file data recovery software designed to recover lost files
including video, documents and archives from hard disks and CD Rom and lost
pictures (Photo Recovery) from digital camera memory. PhotoRec ignores the
filesystem and goes after the underlying data, so it works even if your media's
filesystem is severely damaged or reformatted.

%package -n qphotorec
Summary:        Graphical tool to Undelete Files
Group:          System/Filesystems

%description -n qphotorec
QPhotoRec is a Graphical User Interface (Qt based GUI) version of PhotoRec.
More user friendly, it recognizes the same file formats.

%prep
%define TAR_TOP_FOLDER %{name}-%{version}
%setup -q -n %{TAR_TOP_FOLDER}
cp README.md README

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
# move back the documentation
mv %{buildroot}%{_datadir}/doc/%{name}/* .

%suse_update_desktop_file qphotorec

%files
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS documentation.html
%{_bindir}/testdisk
%{_mandir}/man8/testdisk.8%{ext_man}
%{_mandir}/zh_CN/man8/testdisk.8%{ext_man}

%files -n photorec
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS documentation.html
%{_bindir}/fidentify
%{_bindir}/photorec
%{_mandir}/man8/fidentify.8%{ext_man}
%{_mandir}/man8/photorec.8%{ext_man}
%{_mandir}/zh_CN/man8/fidentify.8%{ext_man}
%{_mandir}/zh_CN/man8/photorec.8%{ext_man}

%files -n qphotorec
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS documentation.html
%{_bindir}/qphotorec
%{_datadir}/applications/qphotorec.desktop
%{_datadir}/icons/hicolor/48x48/apps/qphotorec.png
%{_datadir}/icons/hicolor/scalable/apps/qphotorec.svg
%{_mandir}/man8/qphotorec.8%{ext_man}
%{_mandir}/zh_CN/man8/qphotorec.8%{ext_man}

%changelog
