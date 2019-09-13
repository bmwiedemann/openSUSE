#
# spec file for package gnome-epub-thumbnailer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Dominique Leuenberger, Amsterdam, The Netherlands
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


Name:           gnome-epub-thumbnailer
Version:        1.5
Release:        0
Summary:        Thumbnailer for EPub books
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://git.gnome.org/browse/gnome-epub-thumbnailer
Source0:        https://download.gnome.org/sources/gnome-epub-thumbnailer/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libxml-2.0)

%description
Thumbnailer for EPub books.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/gnome-epub-thumbnailer
%{_bindir}/gnome-mobi-thumbnailer
%dir %{_datadir}/thumbnailers/
%{_datadir}/thumbnailers/gnome-epub-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gnome-mobi-thumbnailer.thumbnailer

%changelog
