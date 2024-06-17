#
# spec file for package gnunet-messenger-cli
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gnunet-messenger-cli
Version:        0.3.0
Release:        0
Summary:        Terminal application using the GNUnet Messenger service
License:        AGPL-3.0-or-later
URL:            https://www.gnunet.org/
Source:         http://ftpmirror.gnu.org/gnunet/messenger-cli-%{version}.tar.gz
Source2:        http://ftpmirror.gnu.org/gnunet/messenger-cli-%{version}.tar.gz.sig
# https://gnunet.org/~schanzen/3D11063C10F98D14BD24D1470B0998EF86F59B6A
Source3:        %{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnunetchat) >= 0.5.0
BuildRequires:  pkgconfig(gnunetutil)
BuildRequires:  pkgconfig(ncurses)

%description
A terminal application using the GNUnet Messenger service.

%prep
%autosetup -p1 -n messenger-cli-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/messenger-cli

%changelog
