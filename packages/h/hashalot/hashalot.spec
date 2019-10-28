#
# spec file for package hashalot
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


Name:           hashalot
Version:        0.3
Release:        0
Summary:        Read a passphrase and print a hash
License:        GPL-2.0+
Group:          System/Base
Url:            http://www.paranoiacs.org/~sluskyb/hacks/hashalot/
Source:         http://www.paranoiacs.org/~sluskyb/hacks/hashalot/hashalot-%{version}.tar.gz
Patch10:        hashalot-fixes.diff
Patch11:        hashalot-libgcrypt.diff
Patch12:        hashalot-ctrl-d.diff
Patch13:        hashalot-timeout.diff
Patch14:        hashalot-manpage.diff
Patch15:        bug-476290_hashalot-hashlen.diff
Patch16:        hashalot-glibc210.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgcrypt-devel
Provides:       cryptsetup:/sbin/hashalot
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
hashalot  is  a small tool that reads a passphrase from standard
input, hashes it using the given hash type, and prints the result
to standard output. Used by legacy encrypted volumes.

Supported hashes:
* rmd160
* sha256
* sha384
* sha512

%prep
%setup -q
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# remove unwanted symlinks
rm -f %{buildroot}%{_sbindir}/{rmd160,sha256,sha384,sha512}

%files
%defattr(-,root,root)
%{_sbindir}/hashalot
%{_mandir}/man1/hashalot.1*

%changelog
