#
# spec file for package exfatprogs
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


Name:           exfatprogs
Version:        1.2.4
Release:        0
Summary:        Utilities for exFAT file system maintenance
License:        GPL-2.0-or-later
URL:            https://github.com/exfatprogs/exfatprogs
Source0:        https://github.com/exfatprogs/exfatprogs/archive/refs/tags/%{version}.tar.gz
Source1000:     exfatprogs.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
Conflicts:      exfat-utils
Obsoletes:      libexfat0 < %{version}

%description
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

%package -n libexfat0
Summary:        Utilities for exFAT file system maintenance

%description -n libexfat0
A set of utilities for creating, checking, dumping and labelling exFAT file
system.

This package contains the shared library.

%prep
%setup -q
chmod -x COPYING

%build
autoreconf -fi
%configure

%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_mandir}/man8/dump.exfat.8%{?ext_man}
%{_mandir}/man8/exfatlabel.8%{?ext_man}
%{_mandir}/man8/fsck.exfat.8%{?ext_man}
%{_mandir}/man8/mkfs.exfat.8%{?ext_man}
%{_mandir}/man8/tune.exfat.8%{?ext_man}
%{_mandir}/man8/exfat2img.8%{?ext_man}
%{_sbindir}/dump.exfat
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_sbindir}/exfat2img

%changelog
