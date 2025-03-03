#
# spec file for package imgvtopgm
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           imgvtopgm
Version:        2.1
Release:        0
Summary:        Palm Pilot Image Viewer to PGM Converter
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Convertors
URL:            https://sf.net/projects/imgvtopgm/

#SVN-Clone:	svn://svn.code.sf.net/p/imgvtopgm/code/trunk
Source:         https://downloads.sf.net/%name/%name-%version.tar.gz
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
%setup -qn %name-%version

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS  CREDITS  INSTALL  NEWS Pilot16 ChangeLog  Pilot README
%doc samples/
%_bindir/*
%_mandir/man1/*.1*

%changelog
