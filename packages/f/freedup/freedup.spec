#
# spec file for package freedup
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


%define mainversion 1.6
%define subversion 3
Name:           freedup
Version:        %{mainversion}~%{subversion}
Release:        0
Summary:        Links substantially identical, duplicate files to save file system space
License:        GPL-3.0+
Group:          Productivity/Archiving/Backup
Url:            http://freedup.org/
Source:         http://freedup.org/freedup-%{version}-src.tar.bz2
Patch:          nostrip.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Freedup eliminates duplicate files by linking them, and thus reduces the amount
of used disk space within one or more file systems. By default, hardlinks are
used on a single device, symbolic links when the devices differ. A set of
options allows you to modify the methods of file comparison, the hash functions,
the linking behavior, and the reporting style. You may use batch or interactive
mode. Freedup usually only considers identical files, but when comparing audio
or graphics files, you may elect to ignore the tags. Multimedia files often are
a good target for deduplication.

%prep
%setup -q -n %{name}-%{mainversion}-%{subversion}
%patch -p1

%build
make CFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -DFLAVOUR="\"d\"" -DHASHSUM=0 -std=gnu99' clean freedup symharden ChangeLog

%install
make \
  DESTDIR=%{buildroot} \
  PRE=%{buildroot} \
  install \
  %{?_smp_mflags}

chmod -x %{buildroot}/%{_mandir}/man1/*

%files
%defattr(-,root,root)
%doc COPYING COPYING.SHA ChangeLog
%{_bindir}/freedup
%{_bindir}/symharden
%{_mandir}/man1/*

%changelog
