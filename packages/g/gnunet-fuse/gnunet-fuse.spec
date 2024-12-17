#
# spec file for package gnunet-fuse
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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
#


Name:           gnunet-fuse
Version:        0.23.0
Release:        0
Summary:        GNUnet FUSE interface
License:        GPL-3.0-only
Group:          Productivity/Networking/File-Sharing
URL:            https://www.gnunet.org/
Source:         http://ftpmirror.gnu.org/gnunet/%{name}-%{version}.tar.gz
Source2:        http://ftpmirror.gnu.org/gnunet/%{name}-%{version}.tar.gz.sig
# https://gnunet.org/~schanzen/3D11063C10F98D14BD24D1470B0998EF86F59B6A
Source3:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(gnunetcore) >= 0.21
BuildRequires:  pkgconfig(gnunetutil) >= 0.9.0
Requires:       gnunet

%description
GNUnet-fuse allows you to mount directories published on GNUnet.

GNUnet is peer-to-peer framework focusing on security. The first and
primary application for GNUnet is anonymous file-sharing.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{ext_info}

%changelog
