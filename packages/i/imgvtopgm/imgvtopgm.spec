#
# spec file for package imgvtopgm
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


Name:           imgvtopgm
Version:        2.0
Release:        0
Summary:        Palm Pilot Image Viewer to PGM Converter
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Url:            http://sf.net/projects/imgvtopgm/

#SVN-Clone:	svn://svn.code.sf.net/p/imgvtopgm/code/trunk
Source:         http://downloads.sf.net/%name/%name-%version.tar.gz
Patch0:         %{name}-%{version}-warnings-fix.diff
Patch1:         imgvtopgm-lib-cleanup.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libnetpbm-devel
Requires:       netpbm

%description
Tools for converting Pilot Image Viewer pdb files to and from Portable
Graymaps and Portable Bitmaps. The tools support grayscale and
monochrome images with or without compression and with or without
notes.

If you are looking for a cool (and free) image viewer for your Pilot,
you should look at TinyViewer (http://www.righto.com/pilot/tv.html).

%prep
%setup -qn %name-%version.orig
%patch0
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS  CREDITS  INSTALL  NEWS Pilot16 COPYING  ChangeLog  Pilot README
%doc samples/
%_bindir/*
%_mandir/man1/*.1*

%changelog
