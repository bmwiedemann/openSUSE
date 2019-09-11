#
# spec file for package oto
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           oto
Version:        0.4
Release:        0
Url:            http://sourceforge.net/projects/oto/
#Original source: http://prdownloads.sourceforge.net/oto/oto-0.4.tar.gz
Source0:        http://prdownloads.sourceforge.net/oto/oto-%{version}.tar.bz2
Patch0:         fix-implicit-declarations.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Open Type Organizer
License:        GPL-2.0+
Group:          System/I18n/Chinese

%description
The 'Open Type Organizer' project provides programs to list and modify
tables in OpenType font files, specifically, their 'name' and 'cmap'
tables.  It can be used to translate 'name' and 'cmap' of OpenType font
in locale encodings to Unicode encoding so the font file can be used in
an environment which does not understand locale encodings.  The
translated tables are added to the font while keeping the original
tables intact.

Do you have a True Type font which does not work with Xft (e.g. with
KDE and Antialiasing)? Chances are, the font doesn't have a Unicode
'cmap'!  Open Type Organizer (oTo) will help to solve the problem.  It
will add Unicode 'name' and Unicode 'cmap' tables by translating the
original ones.	Your favorite ttf font can really work for you now.



Authors:
--------
    Yao Zhang <yaoz@users.sourceforge.net>

%prep
%setup0
%patch0 -p1

%build
rm -f config.cache
export CFLAGS="$RPM_OPT_FLAGS" 
./configure --prefix=/usr \
            --mandir=%{_mandir} \
            --infodir=%{_infodir} \
            %{_target_cpu}-suse-linux
make 

%install
rm -rf $RPM_BUILD_ROOT;
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/*
/usr/share/*

%changelog
