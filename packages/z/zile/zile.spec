#
# spec file for package zile
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           zile
Version:        2.6.2
Release:        0
Summary:        Lightweight Emacs Clone
License:        GPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://www.gnu.org/software/zile/
Source0:        https://ftp.gnu.org/gnu/zile/zile-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/zile/zile-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=20805#/%{name}.keyring
Source3:        zile.desktop
Source4:        zile.png
BuildRequires:  help2man >= 1.29
BuildRequires:  perl >= 5.5
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(ncurses)
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
Provides:       %{name}-base = %{version}
Provides:       %{name}-desktop = %{version}
Obsoletes:      %{name}-base < %{version}
Obsoletes:      %{name}-desktop < %{version}

%description
Zile is another Emacs-clone.  Zile is a customizable, self-documenting
real-time, open-source display editor.  Zile was written to be as similar
as possible to Emacs; every Emacs user should feel at home with Zile.

%prep
%autosetup

%build
export CFLAGS="%{optflags} -Wno-incompatible-pointer-types"
%configure \
  --disable-debug \
  --disable-silent-rules \
  --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

install -Dpm 0644 %{SOURCE3} \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 %{SOURCE4} \
  %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc ChangeLog README THANKS AUTHORS FAQ NEWS dotzile.sample
%license COPYING
%{_bindir}/zile
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man?/zile.?%{?ext_man}

%changelog
