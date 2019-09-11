#
# spec file for package mmv
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


Name:           mmv
Version:        1.01b
Release:        0
Summary:        Move/Copy/Append/Link Multiple Files by Wildcard Patterns
License:        GPL-1.0+
Group:          Productivity/File utilities
Url:            http://packages.qa.debian.org/m/mmv.html
Source0:        http://ftp.debian.org/debian/pool/main/m/mmv/%{name}_%{version}.orig.tar.gz
Source1:        http://packages.debian.org/changelogs/pool/main/m/mmv/current/copyright
# PATCH-FIX-OPENSUSE mmv-1.01b.dif -- Compilation and Makefile fixes
Patch0:         mmv-1.01b.dif
# PATCH-FIX-OPENSUSE allow-non-ascii.patch bnc#34232 jacke@exsuse.de -- Allow non-ASCII for the target file names
Patch1:         allow-non-ascii.patch
# PATCH-FIX-OPENSUSE mmv-1.01b-options.patch bnc#35289 tcrhak@suse.cz -- Honor '--' in option list
Patch2:         mmv-1.01b-options.patch
# PATCH-FIX-OPENSUSE mmv-1.01b-include.dif -- Fix include files
Patch3:         mmv-1.01b-include.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mmv moves (or copies, appends, or links, as specified) each source file matching
a from pattern to the target name specified by the to pattern.  This multiple
action is performed safely, i.e. without any unexpected deletion of files due to
collisions of target names with existing filenames or with other target names.
Furthermore, before doing anything, mmv attempts to detect any errors that would
result from the entire set of actions specified and gives the user the choice of
either proceeding by avoiding the offending parts or aborting.

%prep
%setup -q -n %{name}-%{version}.orig
%patch0
%patch1 -p 1 -b .allow-non-ascii
%patch2
%patch3
cp -a %{SOURCE1} .

%build
# Add LARGEFILE to CFLAGS bnc#137906
make \
  %{?_smp_mflags} \
  CC="gcc" \
  CFLAGS="%{optflags} -Wall -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
make "DESTDIR=%{buildroot}" install IMAN=%{buildroot}%{_mandir}
cd %{buildroot}%{_bindir}
ln -s mmv mad
ln -s mmv mcp
ln -s mmv mln
cd %{buildroot}%{_mandir}/man1/
ln -s mmv.1.gz mad.1.gz
ln -s mmv.1.gz mcp.1.gz
ln -s mmv.1.gz mln.1.gz

%files
%defattr(-,root,root,-)
%doc ANNOUNCE ARTICLE copyright
%{_bindir}/*
%{_mandir}/man1/*

%changelog
