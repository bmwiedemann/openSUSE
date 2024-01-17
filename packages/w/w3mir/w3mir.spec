#
# spec file for package w3mir
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



Name:           w3mir
Version:        1.0.10
Release:        667
License:        Artistic-1.0
Summary:        HTTP Copying and Mirroring Tool
Url:            http://langfeldt.net/w3mir/
Group:          Productivity/Networking/Web/Utilities
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-path.patch
BuildRequires:  perl-libwww-perl
BuildArch:      noarch
Requires:       perl = %{perl_version}
Requires:       perl-HTML-Parser
Requires:       perl-URI
Requires:       perl-libwww-perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
w3mir's main focus is to create and maintain a browsable copy of one or
several remote World Wide Web sites.

Used to its full potential, w3mir can retrieve the contents of several
related sites and leave the mirror browseable via a local web server or
from a file system, such as directly from a CD-ROM.

w3mir's goal is to be able to make useful mirrors of any reasonable
World Wide Web site. It specifically preserves link integrity within
the mirrored documents as well as the integrity of links outside the
mirror, if you want it to. w3mir has a powerful "multi scope" mechanism
enabling the user to make mirrors of several related sites and have
links between them refer to the mirrored documents rather than the
original site. w3mir has several features directed at getting mirrors
for CD-ROM burning and the handling of some rare problems when
mirroring.

%prep
%setup -q
%patch0

%build
perl Makefile.PL
make

%install
install -d %{buildroot}/%perl_archlib
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%defattr(-,root,root)
%doc Artistic Changes INSTALL MANIFEST example.cfg multiscope.cfg README w3mir-HOWTO.html
%doc %{_mandir}/man1/*
%{_bindir}/*
%{perl_vendorlib}/*.pm

%clean
rm -r %{buildroot}

%changelog
