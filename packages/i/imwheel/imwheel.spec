#
# spec file for package imwheel
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           imwheel
Version:        1.0.0pre12
Release:        0
Summary:        Mouse Event to Key Event Mapper Daemon
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://imwheel.sourceforge.net
Source:         http://prdownloads.sourceforge.net/imwheel/imwheel-%{version}.tar.gz
# PATCH-FIX-UPSTREAM to prevent compiler warnings
# "cast from pointer to integer of different size"
Patch1:         imwheel-intptr_t.patch
# PATCH-FIX-UPSTREAM to fix uninitialized variable hsi.
Patch2:         imwheel-fix_uninitialized_var.patch
# PATCH-FIX-OPENSUSE not to install to root only.
Patch3:         imwheel-fix_destdir.patch
# PATCH-FEATURE-OPENSUSE to put configs to /etc/ instead of /etc/X11.
Patch4:         imwheel-config_file_path.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A daemon for X11, which watches for mouse wheel actions and outputs them as
keypresses. It can be configured separately for different windows. It also
allows input from it's own (included) gpm, or from jamd, or from XFree86 ZAxis
mouse wheel conversion.

%prep
%setup -q
%patch1
%patch2
%patch3
%patch4

%build
autoreconf -fiv
%configure \
  --with-x 
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog COPYING EMACS FREEBSD
%doc M-BA47 NEWS README TODO
%config(noreplace) %{_sysconfdir}/imwheelrc
%{_bindir}/imwheel
%{_mandir}/man1/imwheel.1*

%changelog
