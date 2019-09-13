#
# spec file for package mirror
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mirror
Version:        2.9
Release:        0
Summary:        Perl Scripts for Mirroring FTP Servers
License:        SUSE-mirror
Group:          Productivity/Networking/Web/Utilities
URL:            ftp://ftp.sai.msu.su/pub/unix/FTP/mirror/
Source0:        ftp://ftp.sai.msu.su/pub/unix/FTP/mirror/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}.ftp-ls-timeout.patch
Patch2:         %{name}-%{version}.y2k-fix.patch
Patch3:         %{name}-%{version}.name_map-default.patch
Patch4:         %{name}-%{version}.gzip.patch
Patch5:         mirror-exec-path.dif
Patch6:         dont-build-as-root.diff
Patch7:         mirror-timelocal.patch
Patch8:         mirror-dump.patch
Requires:       perl = %{perl_version}
BuildArch:      noarch

%description
Mirror is a package written in Perl that uses the FTP protocol to duplicate
a directory hierarchy between the machine it is run on and a remote host. It
avoids copying files unnecessarily by comparing the file time-stamps and
file sizes before transferring. Amongst other things, it can optionally
rename, compress, gzip, and split files.

%prep
%setup -q -c
%patch0
%patch1 -p1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8 -p1

%build

%install
install -d -m 755 %{buildroot}%{perl_vendorlib}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
%make_install PLDIR=%{perl_vendorlib}
cd %{buildroot}%{_bindir}/
ln -sf mirror-master mm

%files
%license copyright.html
%doc *.txt *.html mirror-on-dusk.gif mirror.defaults
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*

%changelog
