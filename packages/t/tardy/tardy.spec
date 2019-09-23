#
# spec file for package tardy
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


Name:           tardy
Version:        1.28
Release:        0
Summary:        Tar Archive Post-Processor
License:        GPL-3.0-only AND LGPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            http://tardy.sourceforge.net/
Source0:        http://sourceforge.net/projects/tardy/files/%{version}/%{name}-%{version}.D001.tar.gz
BuildRequires:  bison
BuildRequires:  cpio
BuildRequires:  gcc-c++
BuildRequires:  groff-full
BuildRequires:  libboost_headers-devel
BuildRequires:  libbz2-devel
BuildRequires:  libexplain-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
The tardy program is a tar(1) post-processor. It may be used to manipulate
the file headers in tar(5) archive files in various ways.

%prep
%autosetup

%build
%configure
# parallel builds fail
make --jobs 1

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/tardy

%files
%license LICENSE
%doc AUTHORS README ./etc/README.pdf ./etc/reference.pdf
%{_bindir}/tardy
%{_mandir}/man1/tardy.1%{?ext_man}
%{_mandir}/man1/tardy_license.1%{?ext_man}

%changelog
