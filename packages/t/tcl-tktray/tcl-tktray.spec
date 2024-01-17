#
# spec file for package tcl-tktray
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 open-slx GmbH <Sascha.Manns@open-slx.de>
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


Name:           tcl-tktray
Version:        1.3.9
Release:        0
Summary:        System Tray Icon Support for Tk on X11
License:        TCL
Group:          Development/Languages/Tcl
Url:            http://sw4me.com/wiki/Tktray
Source:         http://tktray.googlecode.com/files/tktray%{version}.tar.gz
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  xorg-x11-libXext-devel
Requires:       tcl
Requires:       tk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tktray is a Tk extension that is able to create system tray icons. It
follows http://www.freedesktop.org specifications when looking up the system
tray manager.  This protocol is supported by modern versions of KDE and
Gnome panels, and by some other panel-like application.

%prep
%setup -q -n tktray%{version}

%build
%configure \
    --with-tcl=%{_libdir} \
    --with-tk=%{_libdir} \
    --libdir=%{tcl_archdir}
make %{?_smp_mflags}

%install
%make_install

mkdir html
mv docs/*.html html

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{tcl_archdir}/tktray%{version}
%{tcl_archdir}/tktray%{version}/libtktray%{version}.so
%{tcl_archdir}/tktray%{version}/pkgIndex.tcl
%{_mandir}/mann/tktray.n.*
%doc ChangeLog license.terms README html/

%changelog
