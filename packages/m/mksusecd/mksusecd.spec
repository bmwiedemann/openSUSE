#
# spec file for package mksusecd
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Steffen Winterfeldt
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


Name:           mksusecd
Version:        1.77
Release:        0
Summary:        Tool to create SUSE Linux installation ISOs
License:        GPL-3.0+
Group:          Hardware/Other
Url:            https://github.com/wfeldt/mksusecd
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libuuid-devel
BuildRequires:  xz
Requires:       checkmedia
%if %suse_version >= 1500
Requires:       createrepo-implementation
Requires:       mkisofs
%else
Requires:       createrepo
Requires:       genisoimage
%endif
Requires:       dosfstools
Requires:       gpg2
Requires:       mtools
Requires:       squashfs
Requires:       xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a tool to create SUSE Linux installation ISOs.

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} LIBDIR=%{_libexecdir} BINDIR=%{_bindir} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libexecdir}/%{name}
%doc README* COPYING* *.md

%changelog
