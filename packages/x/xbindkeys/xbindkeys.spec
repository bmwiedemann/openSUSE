#
# spec file for package xbindkeys
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


# Guile support is disabled by default, has no real
# advantages except being able to write xbindkeys
# configuration in a lisp-alike syntax but it pulls
# in guile, which is rarely used by most end-users.
#
# To enable guile support, build the spec file and
# pass --with guile to rpmbuild.
%bcond_with guile
Name:           xbindkeys
Version:        1.8.6
Release:        0
Summary:        Events Grabbing Program for X-Window
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            http://www.nongnu.org/xbindkeys/
Source:         http://www.nongnu.org/%{name}/%{name}-%{version}.tar.gz
Requires:       tk
%if %{with guile}
BuildRequires:  guile-devel
%endif
%if 0%{?suse_version} > 1110
BuildRequires:  pkgconfig(x11)
%else
BuildRequires:  xorg-x11-devel
%endif

%description
xbindkeys is a program that associates keys or mouse buttons to shell commands
under X. After a little configuration, it can start many commands with the
keyboard (e.g. control+alt+x starts an xterm) or with the mouse buttons.

%if !%{with guile}
guile support is disabled in this package.
To enable guile support, rebuild the src.rpm and pass --with guile
to rpmbuild.
%endif

%prep
%setup -q

%build
%configure \
%if %{with guile}
    --enable-guile
%else
    --disable-guile
%endif

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING ChangeLog README TODO xbindkeysrc
%if %{with guile}
%doc xbindkeysrc-combo.scm xbindkeysrc.scm
%endif
%{_bindir}/%{name}
%{_bindir}/%{name}_show
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/%{name}_show.1%{ext_man}

%changelog
