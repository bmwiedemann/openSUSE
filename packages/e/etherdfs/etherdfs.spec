#
# spec file for package etherdfs
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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

%define realversion 20180203
%define realname ethersrv-linux
Name:           etherdfs
Version:        0~%{realversion}
Release:        0
Summary:        Ethernet DOS File System server
License:        MIT
Group:          System/Filesystems
URL:            https://etherdfs.sourceforge.net/
Source:         https://sourceforge.net/projects/etherdfs/files/%{realname}/%{realname}-%{realversion}.tar.xz
Source1:        ethersrv-linux.8
Provides:       etherdfs-server
Provides:       ethersrv-linux

%description
EtherDFS is a DOS installable filesystem, mapping a DOS drive letter
to a remote share. This package contains the server side of EtherDFS,
a daemon exporting one or more directories for remote access by the
EtherDFS DOS TSR.

%prep
%setup -q -n ethersrv-linux-%{realversion}
sed -i 's/\r$//' ethersrv-linux.txt history.txt

%build
%make_build CFLAGS="%{optflags} -std=gnu89"

%install
install -Dpm 0755 %{realname} %{buildroot}/%{_sbindir}/ethersrv-linux
install -Dpm 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man8/ethersrv-linux.8

%files
%license ethersrv-linux.txt
%doc ethersrv-linux.txt history.txt
%{_sbindir}/ethersrv-linux
%{_mandir}/man8/ethersrv-linux.8%{?ext_man}

%changelog
