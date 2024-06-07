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
Version:        2.18
Release:        0
Summary:        Tool to create SUSE Linux installation ISOs
License:        GPL-3.0+
Group:          Hardware/Other
URL:            https://github.com/wfeldt/mksusecd
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libuuid-devel
BuildRequires:  xz
%if 0%?suse_version >= 1500 || 0%?sle_version >= 120400
BuildRequires:  rubygem(asciidoctor)
%else
BuildRequires:  asciidoc
%if 0%?suse_version >= 1310 || 0%?sle_version >= 120000
BuildRequires:  libxslt-tools
%endif
%endif
Requires:       checkmedia >= 6.0
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
install -D -m 644 mksusecd.1 %{buildroot}%{_mandir}/man1/mksusecd.1

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libexecdir}/%{name}
%doc README* *.md
%doc %{_mandir}/man1/mksusecd.*
%if %suse_version >= 1500
%license COPYING*
%else
%doc COPYING*
%endif

%changelog
