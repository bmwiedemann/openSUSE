#
# spec file for package mtools
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           mtools
Version:        4.0.44
Release:        0
Summary:        Tools to access MS-DOS filesystems without kernel drivers
License:        GPL-3.0-or-later
Group:          System/Filesystems
URL:            https://www.gnu.org/software/mtools/
Source0:        https://ftp.gnu.org/gnu/mtools/%{name}-%{version}.tar.bz2
Source1:        https://ftp.gnu.org/gnu/mtools/%{name}-%{version}.tar.bz2.sig
# https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=mtools
Source2:        %{name}.keyring
Patch0:         %{name}-conf.diff
BuildRequires:  makeinfo
BuildRequires:  texinfo
Requires:       glibc-gconv-modules-extra
Requires:       glibc-locale-base

%description
Mtools allows access to an MS-DOS file system on disk without
mounting it. It includes commands for working with MS-DOS files:
mdir, mcd, mcopy, and mformat.

XDF support for OS/2 is also provided.

%package doc
Summary:        Documentation for mtools, a toolset for MS-DOS filesystem access
License:        GFDL-1.3-only AND GPL-3.0-or-later
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
Mtools allows access to an MS-DOS file system on disk without
mounting it. This subpackage contains the documentation for it.

%prep
%autosetup -p0

%build
%configure \
	--includedir=%{_prefix}/src/linux/include \
	--disable-floppyd

%make_build -j1 all info pdf

%install
install -d -m 755 %{buildroot}%{_sysconfdir}
make DESTDIR=%{buildroot} install --jobs 1
cp -p mtools.conf %{buildroot}%{_sysconfdir}

%files
%config %{_sysconfdir}/mtools.conf
%doc Release.notes NEWS README*
%license COPYING
%{_mandir}/man?*/*
%exclude %{_mandir}/man?*/f*
%{_infodir}/mtools.info%{?ext_info}
%{_bindir}/*
%exclude %{_bindir}/f*

%files doc
%license COPYING
%doc *.pdf

%changelog
