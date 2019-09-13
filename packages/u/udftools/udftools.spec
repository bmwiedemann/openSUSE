#
# spec file for package udftools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           udftools
Version:        2.1
Release:        0
Summary:        UDF filesystem tools
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            https://github.com/pali/udftools
Source:         https://github.com/pali/udftools/releases/download/%{version}/udftools-%{version}.tar.gz
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake
BuildRequires:  glibc
BuildRequires:  libtool
BuildRequires:  udev
Provides:       udf = %{version}
Obsoletes:      udf < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
These are tools for UDF file systems as used, e.g., on DVD-ROMs.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure

make %{?_smp_mflags}

%install
%make_install  %{?_smp_mflags}

mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/udftools %{buildroot}%{_docdir}/udftools
rm -r %{buildroot}%{_datadir}/doc

%files
%defattr(-,root,root)
%{_bindir}/cdrwtool
%{_bindir}/udfinfo
%{_bindir}/wrudf
%{_sbindir}/mkfs.udf
%{_sbindir}/mkudffs
%{_sbindir}/pktsetup
%{_sbindir}/udflabel
%{_mandir}/man1/cdrwtool.1%{ext_man}
%{_mandir}/man1/udfinfo.1%{ext_man}
%{_mandir}/man1/wrudf.1%{ext_man}
%{_mandir}/man8/mkfs.udf.8%{ext_man}
%{_mandir}/man8/mkudffs.8%{ext_man}
%{_mandir}/man8/pktsetup.8%{ext_man}
%{_mandir}/man8/udflabel.8%{ext_man}
%{_udevrulesdir}/80-pktsetup.rules

%changelog
