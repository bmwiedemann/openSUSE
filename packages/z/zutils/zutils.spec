#
# spec file for package zutils
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


Name:           zutils
Version:        1.7
Release:        0
Summary:        Collection of utilities for dealing with compressed files
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://www.nongnu.org/zutils/zutils.html
Source0:        https://download.savannah.gnu.org/releases/zutils/zutils-%{version}.tar.lz
Source1:        https://download.savannah.gnu.org/releases/zutils/zutils-%{version}.tar.lz.sig
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM zutils-1.7-zcat-buffer-overrun.patch
Patch0:         zutils-1.7-zcat-buffer-overrun.patch
# PATCH-FIX-OPENSUSE zutils-1.7-noconflict.patch
Patch1:         zutils-1.7-noconflict.patch
BuildRequires:  gcc-c++
BuildRequires:  lzip
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
Zutils is a collection of utilities able to deal with any combination
of compressed and uncompressed files transparently. If any given file,
including standard input, is compressed, its decompressed content is
used. Compressed files are decompressed on the fly; no temporary files
are created.
These utilities are not wrapper scripts but safer and more efficient
C++ programs. In particular the "--recursive" option is very efficient
in those utilities supporting it.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make CXXFLAGS="%{optflags}" %{?_smp_mflags}

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%doc ChangeLog README
%license COPYING
%config %{_sysconfdir}/zutilsrc
%{_bindir}/zutils-zcat
%{_bindir}/zutils-zcmp
%{_bindir}/zutils-zdiff
%{_bindir}/zutils-zegrep
%{_bindir}/zutils-zfgrep
%{_bindir}/zutils-zgrep
%{_bindir}/ztest
%{_bindir}/zupdate
%{_infodir}/zutils.info%{?ext_info}
%{_mandir}/man1/zutils-zcat.1%{?ext_man}
%{_mandir}/man1/zutils-zcmp.1%{?ext_man}
%{_mandir}/man1/zutils-zdiff.1%{?ext_man}
%{_mandir}/man1/zutils-zgrep.1%{?ext_man}
%{_mandir}/man1/ztest.1%{?ext_man}
%{_mandir}/man1/zupdate.1%{?ext_man}

%changelog
