#
# spec file for package exmh
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


Name:           exmh
BuildRequires:  tcl
Summary:        Front-End for nmh Written in tcl/tk
License:        MIT
Group:          Productivity/Networking/Email/Clients
Version:        2.8.0
Release:        0
BuildArch:      noarch
Requires:       expect
Requires:       metamail
Requires:       nmh
Source0:        ftp://ftp.tcl.tk/pub/tcl/exmh/exmh-%{version}.tar.gz
Url:            http://beedub.com/exmh/
Patch0:         %{name}-conf.patch
Patch1:         %name-expectk.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Exmh is an X user interface for NMH mail. NMH provides a set of UNIX
commands that manage folders and mail messages. NMH has many features
as a result of several years of availability. Exmh provides a graphical
interface to many of these features, but not everything.

%prep
%setup -q
for i in *.MASTER; do
	cp $i ${i%%.MASTER}
done
%patch0
%patch1

%build
echo 'auto_mkindex ./lib *.tcl' | tclsh

%install
mkdir -p %buildroot{%_bindir,%_mandir/man1}
mkdir -p %buildroot%tclscriptdir/exmh-%{version}
install -m755 -d %buildroot%_bindir
install -m755 exmh exmh-bg exmh-async ftp.expect %buildroot%_bindir
install -m755 -d %buildroot%_mandir/man1
for i in *.l; do
	install -m644 $i %buildroot%_mandir/man1/${i%%.l}.1
done
install -m755 -d %buildroot%tclscriptdir/exmh-%version
cp -ar lib/* %buildroot/%tclscriptdir/exmh-%version
rm -r misc/RPM
chmod a-x misc/mafe/help/mafe.html
mv misc examples

%files
%defattr(-,root,root)
%doc COPYRIGHT exmh.BUGS exmh.TODO exmh.README examples
%tclscriptdir
%_bindir/*
%_mandir/*/*

%changelog
