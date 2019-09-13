#
# spec file for package blueprint-cursor-theme
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           blueprint-cursor-theme
Summary:        X Window System Cursors for the Blue Print Theme
Version:        0.0.2
Release:        0
License:        GPL-2.0+
Group:          System/X11/Icons
Source:         %{name}-%{version}.tar.bz2
Patch:          links.diff
Patch1:         install-path.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildArch:      noarch

%description
A nice mouse cursor theme for the X Window System.

%prep
%setup -q
%patch
%patch1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm    $RPM_BUILD_ROOT/usr/share/icons/default/index.theme.blueprint
rmdir $RPM_BUILD_ROOT/usr/share/icons/default

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
/usr/share/icons/*

%changelog
