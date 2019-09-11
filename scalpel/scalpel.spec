#
# spec file for package scalpel
#
# Copyright (c) 2011 Sebastien Braun.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# norootforbuild

Name:           scalpel
Version:        2.0
Release:        0
Summary:        Fast, filesystem-independent file carver
Group:          System/Filesystems

License:        GPL-2.0+
URL:            http://www.digitalforensicssolutions.com/Scalpel/
Source0:        http://www.digitalforensicssolutions.com/Scalpel/scalpel-2.0.tar.gz

BuildRequires:  tre-devel

%description
Scalpel is a fast file carver that reads a database of header and footer
definitions and extracts matching files or data fragments from a set of 
image files or raw device files. Scalpel is filesystem-independent and will
carve files from FATx, NTFS, ext2/3, HFS+, or raw partitions. 
It is useful for both digital forensics investigation and file recovery.

%prep
%setup -q

%build
%configure
make

%install
%make_install
install -D -m 0644 %{name}.conf %{buildroot}%{_datadir}/%{name}/%{name}.conf.example

%files
%defattr(644,root,root,755)
%doc gpl.txt README
%attr(755,root,root) /usr/bin/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}

%changelog
