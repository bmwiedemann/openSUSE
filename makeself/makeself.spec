#
# spec file for package makeself
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011-2017 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           makeself
Version:        2.3.1
Release:        0
Summary:        Make self-extractable archives on Unix
License:        GPL-2.0+
Group:          Productivity/Archiving/Compression
Url:            http://www.megastep.org/makeself/
Source0:        https://github.com/megastep/%{name}/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Small shell script that generates a self-extractable tar.gz archive from a
directory. The resulting file appears as a shell script (many of those
have a .run suffix), and can be launched as is. The archive will then
uncompress itself to a temporary directory and an optional arbitrary
command will be executed (for example an installation script).

This is pretty similar to archives generated with WinZip Self-Extractor in
the Windows world. Makeself archives also include checksums for integrity
self-validation (CRC and/or MD5 checksums).

%prep
%setup -q -n %{name}-release-%{version}

%build

%install
install -Dm0755 makeself.sh  %{buildroot}%{_bindir}/makeself
ln -s /usr/bin/makeself %{buildroot}%{_bindir}/makeself.sh
install -Dm0755 makeself-header.sh  %{buildroot}%{_bindir}/makeself-header.sh
install -Dm0644 makeself.1 %{buildroot}%{_mandir}/man1/makeself.1

%files
%defattr(-,root,root,-)
%doc README.md COPYING
%{_bindir}/makeself-header.sh
%{_bindir}/makeself.sh
%{_bindir}/makeself
%{_mandir}/man1/makeself.1%{?ext_man}

%changelog
