#
# spec file for package chrpath
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


Name:           chrpath
Version:        0.16
Release:        0
Summary:        Modifies the dynamic library load path of compiled programs and libraries
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            https://alioth.debian.org/projects/chrpath/
Source:         https://alioth.debian.org/frs/download.php/file/3979/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Chrpath allows you to modify the dynamic library load path (rpath and
runpath) of compiled programs. Currently, only removing and modifying the
rpath is supported. It cannot extend or add an rpath.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CC="gcc %{optflags}"

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot} doc_DATA=""

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/chrpath
%{_mandir}/man1/chrpath.1%{ext_man}

%changelog
