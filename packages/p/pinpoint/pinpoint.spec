#
# spec file for package pinpoint
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pinpoint
Version:        0.1.8
Release:        0
Summary:        Simple Presentation Tool for Excellent Presentations
License:        LGPL-2.1+
Group:          Productivity/Publishing/Presentation
Url:            http://live.gnome.org/Pinpoint
Source:         http://download.gnome.org/sources/pinpoint/0.1/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(clutter-1.0) >= 1.23.7
BuildRequires:  pkgconfig(clutter-gst-3.0) >= 3.0.0
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.6
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pinpoint a simple presentation tool that hopes to avoid audience death
by bullet point and instead encourage presentations containing beautiful
images and small amounts of concise text in slides.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/pinpoint
%{_datadir}/pinpoint/

%changelog
