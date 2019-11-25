#
# spec file for package rdesktop
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           rdesktop
Version:        1.9.0
Release:        0
Summary:        A Remote Desktop Protocol client
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.rdesktop.org/
Source:         https://github.com/rdesktop/rdesktop/releases/download/v%{version}/%{name}-%{version}.tar.gz
## FIX-openSUSE: remove "Don't depend on pkg-config"
Patch0:         rdesktop-fix_pkgconfig_check.patch
# PATCH-FIX-OPENSUSE rdesktop-Fix-keymap-script.patch
Patch3:         rdesktop-Fix-keymap-script.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  krb5-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libnettle-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libtool
BuildRequires:  pcsc-lite-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
rdesktop is a client for connecting to Windows Remote Desktop
Services, capable of natively speaking Remote Desktop Protocol (RDP)
in order to present the user's Windows desktop. rdesktop is known to
work with Windows server versions ranging from NT 4 terminal server
to Windows Server 2012 R2.

%prep
%setup -q
%patch0
%patch3 -p1

## rpmlint
# incorrect-fsf-address /usr/share/rdesktop/keymaps/convert-map
perl -p -i -e 's|^# Foundation.*|# Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110-1335, USA|' keymaps/convert-map

%build
autoreconf -fiv
CFLAGS="%{optflags} -fno-strict-aliasing" \
%configure \
  --enable-smartcard \
  --with-openssl=%{_prefix} \
  --with-ipv6
make %{?_smp_mflags}

%install
%make_install STRIP=true installman
mkdir -p %{buildroot}%{_datadir}/rdesktop
cp -r keymaps %{buildroot}%{_datadir}/rdesktop
chmod -R a+r %{buildroot}%{_datadir}/rdesktop/keymaps

%files
%defattr(-,root,root,755)
%doc doc README.md
%license COPYING
%{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/rdesktop.1.gz

%changelog
