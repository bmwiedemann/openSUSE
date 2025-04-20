#
# spec file for package flamp
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           flamp
Version:        2.2.13
Release:        0
Summary:        Amateur Multicast Protocol - file transfer program
License:        GPL-2.0
Group:          Productivity/Hamradio/Other
URL:            https://www.w1hkj.org/
#Git-Clone:     https://git.code.sf.net/p/fldigi/flamp
Source:         http://sourceforge.net/projects/fldigi/files/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  fltk-devel
BuildRequires:  flxmlrpc-devel
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
FLAMP is a program for AMP or Amateur Multicast Protocol. An FLAMP session will
transmit one or more files with one or more iterations of the transmission. Each
file is broken into blocks, each of which has a check sum. The receiving station
saves the blocks that pass check sum. Successive transmissions will fill in the
missing blocks provided that the new blocks pass the check sum. After the
transmission sequence, the entire file is assembled and may be saved. “Fills”
may be provided by retransmitting the entire file or by the sending station
only sending the missing blocks.

%prep
%autosetup -p1

%build
export BUILD_DATE=`date -d@0`
export BUILD_USER=openSUSE
export BUILD_HOST=openSUSE
%configure
%make_build

%install
%make_install

%suse_update_desktop_file -i flamp

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/flamp
%{_datadir}/applications/flamp.desktop
%{_datadir}/pixmaps/flamp.xpm

%changelog
