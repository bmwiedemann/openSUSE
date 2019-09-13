#
# spec file for package artha
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           artha
Version:        1.0.3
Release:        0
Summary:        Offline English thesaurus based on WordNet
License:        GPL-2.0-only
Group:          Productivity/Office/Dictionary
Url:            http://artha.sourceforge.net
Source:         http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM artha-fix-gio-linking.patch badshah400@gmail.com -- Pass libgio-2.0 to the linker to prevent building errors
Patch0:         artha-fix-gio-linking.patch
# PATCH-FIX-UPSTREAM artha-only-use-AM_PROG_AR-if-defined.patch badshah400@gmail.com -- Use the configure.ac variable AM_PROG_AR only if defined; this fixes build failures in openSUSE <= 12.1 when autoreconf is used
Patch1:         artha-only-use-AM_PROG_AR-if-defined.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wordnet-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.22
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24
Requires:       enchant
Requires:       hunspell
Requires:       wordnet
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Artha is a free cross-platform English thesaurus that works
completely off-line and is based on WordNet.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod -x TODO

%build
autoreconf -f
%configure
make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot} INSTALL="install -p"
%if 0%{?suse_version}
%suse_update_desktop_file -r artha Office Dictionary
%endif

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING NEWS TODO AUTHORS
%dir %{_datadir}/artha
%{_bindir}/artha
%{_datadir}/applications/artha.desktop
%{_datadir}/artha/gui.glade
%{_datadir}/pixmaps/artha.png
%{_mandir}/man1/artha.1.gz

%changelog
