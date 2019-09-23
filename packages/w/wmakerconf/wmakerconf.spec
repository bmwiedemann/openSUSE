#
# spec file for package wmakerconf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wmakerconf
Summary:        Configuration tool for Window Maker
License:        GPL-2.0+
Group:          System/GUI/Other
Version:        2.12
Release:        0
Url:            http://wmakerconf.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-2.9.dif
Patch1:         %{name}-fix-bad-po.patch
Patch3:         %{name}-2.9-destdir.patch
Patch4:         %{name}-2.9-config.patch
Patch5:         %{name}-no-imlib.patch
Patch7:         %{name}-2.9-varargs.diff
Patch9:         %{name}-datarootdir.patch
Patch10:        %{name}-2.12-wmaker-0.95_support.patch
# PATCH - Fix SUSE: implicit-pointer-decl
Patch11:        %{name}-implicit-pointer-decl.patch
# PATCH-FIX-UPSTREAM wmakerconf-link-x11.patch dimstar@opesuse.org -- Link mkpreview with libX11 for XOpenDisplay
Patch12:        %{name}-link-x11.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  WindowMaker-devel
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  perl-libwww-perl
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(x11)
Provides:       wmaconf = %{version}
Obsoletes:      wmaconf < %{version}
Requires:       WindowMaker
Requires:       perl-libwww-perl

%description
Wmakerconf is a GTK+ based configuration tool for Window Maker.

%prep
%setup -q
%patch0
%patch1
%patch3
%patch4
%patch5
%patch7
%patch9
%patch10
%patch11
%patch12 -p1
# ---------------------------------------------------------------------------

%build
gettextize -f
mv ChangeLog~ ChangeLog # drop changelog entries from gettextize to fix build-compare
autoreconf --install --force
test -f po/Makevars || mv po/Makevars.template po/Makevars
%ifarch x86_64
export LDFLAGS="$LDFLAGS -L%{_libdir} -L/usr/X11/lib64 -L/usr/X11R6/lib64"
%endif
%configure \
	--with-nlsdir=%{_datadir}/locale \
	--with-pixmapdir=%{_datadir}/WindowMaker/Pixmaps
make %{?_smp_mflags}
# ---------------------------------------------------------------------------

%install
%make_install
# Change no to nb
mv %{buildroot}%{_datadir}/locale/no %{buildroot}%{_datadir}/locale/nb
%find_lang %{name}
%find_lang wmakerconf-data %{name}.lang
%suse_update_desktop_file wmakerconf

# remove doc files from datadir
for i in ABOUT-NLS AUTHORS COPYING ChangeLog MANUAL NEWS NLS-TEAM1 README ; do
  rm -f %{buildroot}%{_datadir}/%{name}/$i
done
%fdupes -s %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog MANUAL NEWS NLS-TEAM1 README TODO
%{_bindir}/mkpreview
%{_bindir}/wmakerconf
%doc %{_mandir}/man?/mkpreview.*
%doc %{_mandir}/man?/wmakerconf.*
%{_datadir}/applications/wmakerconf.desktop
%{_datadir}/wmakerconf/

%changelog
