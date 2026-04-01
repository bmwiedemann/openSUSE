#
# spec file for package lxinput
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           lxinput
Version:        0.3.6
Release:        0
Summary:        Keyboard and mouse configuration tool
License:        GPL-2.0-only
Group:          System/GUI/LXDE
URL:            https://www.lxde.org/
Source0:        https://github.com/lxde/releases/raw/refs/heads/master/releases/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-runtime
BuildRequires:  gettext-tools
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
Recommends:     %{name}-lang
%lang_package

%description
LXinput is just the LXDE Keyboard and mouse config tool

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
%fdupes -s %{buildroot}

%check
%make_build check

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.ui
%{_datadir}/%{name}/input-keyboard.png
%{_datadir}/%{name}/input-mouse.png
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
