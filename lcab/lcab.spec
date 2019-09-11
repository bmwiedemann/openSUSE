#
# spec file for package lcab
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lcab
Version:        1.0b12
Release:        0
Summary:        Create cabinet (.cab) files
License:        GPL-2.0+
Group:          Productivity/Archiving/Compression
URL:            http://freecode.com/projects/lcab
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake

%description
LCAB is a small program for linux that creates an uncompressed MS Cabinet
File from a set of input files.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
install -Dpm 0644 lcab.1 \
  %{buildroot}%{_mandir}/man1/lcab.1

%files
%doc COPYING README
%{_bindir}/lcab
%{_mandir}/man1/lcab.1%{ext_man}

%changelog
