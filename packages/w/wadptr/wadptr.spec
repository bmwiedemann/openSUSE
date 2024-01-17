#
# spec file for package wadptr
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

Name:           wadptr
Version:        2.4
Release:        0
Group:          Development/Tools/Building
Summary:        Redundancy compressor for Doom WAD files
License:        GPL-2.0+
Url:            http://soulsphere.org/projects/wadptr/

Source:         wadptr-%version.tar.xz
Patch1:         wadptr-automake.diff

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  xz

%description
WADptr is a utility for reducing the size of Doom WAD files. The
"compressed" WADs will still work the same as the originals. The
program works by exploiting the WAD file format to combine repeated /
redundant material.

%prep
%setup
%patch -P 1 -p1

%build
autoreconf -fi;
%configure --docdir=%_docdir/%name
make %{?_smp_mflags};
perl -i -pe 's/\x0d//gs' wadptr.txt;

%install
b="%buildroot";
make install DESTDIR="$b";

%files
%defattr(-,root,root)
%_bindir/*
%doc %_docdir/%name

%changelog
