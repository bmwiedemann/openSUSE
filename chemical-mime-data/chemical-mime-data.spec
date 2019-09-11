#
# spec file for package chemical-mime-data
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


Name:           chemical-mime-data
Version:        0.1.94
Release:        0
Summary:        A collection of data files for various chemical MIME types
License:        LGPL-2.0+
Group:          System/Base
Url:            http://chemical-mime.sourceforge.net/
Source0:        http://downloads.sourceforge.net/chemical-mime/%{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM -- ToDo
Patch0:         reproducible.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  intltool
BuildRequires:  libxslt-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  rsvg-view
BuildRequires:  shared-mime-info
Requires:       ImageMagick
Requires:       hicolor-icon-theme
Requires:       pkgconfig
Requires:       rsvg-view
Requires:       shared-mime-info
Recommends:     gnome-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops, such as KDE and GNOME.

Chemical MIMEs have been proposed in 1995, though it seems they have never
been registered with IANA. However, they are widely used and the project's aim is,
to support these important, but unofficial MIME types.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static \
           --disable-update-database \
           --without-gnome-mime \
           --without-kde-mime \
           --docdir=%{_defaultdocdir}/%{name}

make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}
%fdupes %{buildroot}/%{_prefix}

%post
%mime_database_post

%postun
%mime_database_postun

%files -f %{name}.lang
%defattr (-, root, root)
%doc %{_defaultdocdir}/%{name}
%doc AUTHORS ChangeLog COPYING HACKING NEWS README THANKS TODO
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-chemical.png
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-chemical.svgz
%{_datadir}/pixmaps/chemistry.png
%{_datadir}/pixmaps/gnome-mime-chemical.png
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/pkgconfig/chemical-mime-data.pc

%changelog
