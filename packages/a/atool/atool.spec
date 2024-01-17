#
# spec file for package atool
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           atool
Version:        0.39.0
Release:        0
Summary:        Commandline Tool for Managing File Archives of various Types
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/atool/
Source0:        http://download-mirror.savannah.gnu.org/releases/atool/atool-%{version}.tar.gz
Source1:        http://download-mirror.savannah.gnu.org/releases/atool/atool-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=%{name}&download=1#/%{name}.keyring
Requires:       bzip2
Requires:       gzip
Requires:       tar
Suggests:       arc
Suggests:       arj
Suggests:       cpio
Suggests:       lha
Suggests:       lzma
Suggests:       lzop
Suggests:       nomarch
%if 0%{?suse_version} > 1500
Suggests:       p7zip-full
%else
Suggests:       p7zip
%endif
Suggests:       rar
Suggests:       unace
Suggests:       unalz
Suggests:       unarj
Suggests:       unrar
Suggests:       unzip
Suggests:       zip
BuildArch:      noarch

%description
atool is a script for managing file archives of various types (tar,
tar+gzip, zip, etc).

The main command is probably "aunpack" which extracts files from an
archive. It overcomes the dreaded "multiple files in archive root"
problem by first extracting to a unique subdirectory, and then moving
back the files if possible.

aunpack also prevents local files from being overwritten by
mistake. Other commands provided are apack (for creating archives),
als (for listing files in archives), and acat (for extracting files to
stdout).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/acat
%{_bindir}/adiff
%{_bindir}/als
%{_bindir}/apack
%{_bindir}/arepack
%{_bindir}/atool
%{_bindir}/aunpack
%{_mandir}/man1/acat.1%{?ext_man}
%{_mandir}/man1/adiff.1%{?ext_man}
%{_mandir}/man1/als.1%{?ext_man}
%{_mandir}/man1/apack.1%{?ext_man}
%{_mandir}/man1/arepack.1%{?ext_man}
%{_mandir}/man1/atool.1%{?ext_man}
%{_mandir}/man1/aunpack.1%{?ext_man}

%changelog
