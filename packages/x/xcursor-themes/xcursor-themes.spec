#
# spec file for package xcursor-themes
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


Name:           xcursor-themes
Version:        1.0.7
Release:        0
Summary:        Default set of cursor themes for X
License:        X11
Group:          System/X11/Icons
URL:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/data/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  xcursorgen
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a default set of cursor themes for use with libXcursor,
originally created for the XFree86 Project, and now shipped as part
of the X.Org software distribution.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README.md
%{_datadir}/icons/handhelds/
%{_datadir}/icons/redglass/
%{_datadir}/icons/whiteglass/

%changelog
