#
# spec file for package dbview
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


Name:           dbview
Version:        1.0.4
Release:        0
Summary:        Viewer for dBase III and dBase IV Files
License:        GPL-2.0+
Group:          Productivity/Databases/Tools
Url:            http://www.infodrom.org/projects/dbview/
Source0:        http://www.infodrom.org/projects/dbview/download/%{name}-%{version}.tar.gz
Source1:        http://www.infodrom.org/projects/dbview/download/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Patch1:         %{name}-%{version}-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
dbview is a little tool that displays dBase III and IV files. You can
also use it to convert your old .dbf files for further use with Unix.

%prep
%setup -q
%patch1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-, root, root)
%doc README dBASE CHANGES
%{_mandir}/man1/*
%{_bindir}/dbview

%changelog
