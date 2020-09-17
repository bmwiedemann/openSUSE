#
# spec file for package tnef
#
# Copyright (c) 2020 SUSE LLC
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


Name:           tnef
Version:        1.4.18
Release:        0
Summary:        Uncompress MS-TNEF Archives
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://github.com/verdammelt/tnef/
Source:         https://github.com/verdammelt/tnef/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libtool

%description
This tool uncompresses MS-TNEF archives as used by some mailers.

%prep
%setup -q

%build
if [ ! -x configure ]; then
	autoreconf -fi
fi
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS BUGS COPYING ChangeLog NEWS README.md THANKS doc/FAQ contrib/
%{_bindir}/tnef
%{_mandir}/man1/tnef.1%{ext_man}

%changelog
