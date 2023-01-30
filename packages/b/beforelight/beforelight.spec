#
# spec file for package beforelight
#
# Copyright (c) 2023 SUSE LLC
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


Name:           beforelight
Version:        1.0.6
Release:        0
Summary:        Sample implementation of a screen saver for X servers
License:        MIT
Group:          System/X11/Utilities
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The beforelight program is a sample implementation of a screen saver
for X servers supporting the MIT-SCREEN-SAVER extension. It is only
recommended for use as a code sample, as it does not include features
such as screen locking or configurability, and relies on the legacy Xaw
toolkit.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog README.md
%license COPYING
%{_bindir}/beforelight
%dir %{_datadir}/X11/app-defaults
%{_datadir}/X11/app-defaults/Beforelight
%{_mandir}/man1/beforelight.1%{?ext_man}

%changelog
