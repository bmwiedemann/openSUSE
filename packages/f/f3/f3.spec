#
# spec file for package f3
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


Name:           f3
Version:        7.2
Release:        0
Summary:        Fight Flash Fraud / Fight Fake Flash
License:        GPL-3.0-only
Group:          Hardware/Other
URL:            http://oss.digirati.com.br/f3/
Source:         https://github.com/AltraMayor/f3/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libparted)
BuildRequires:  pkgconfig(libudev)

%description
This package contains tools for identifying fake flash drives (primarily USB
sticks and memory cards).

A fake flash drive fraudulently inflates its apparent storage capacity (far)
beyond the physical capacity of its flash memory. Not surprisingly, using such
a flash drive will, sooner or later, result in data loss and/or corruption.

The main tools in this package are an open-source implementation of the H2testw
algorithm. Some extra tools are also provided, among them one for using
the actual storage capacity of fake drives as safely as possible.

%prep
%setup -q

%build
# workaround for libargp problem. see:
# https://github.com/AltraMayor/f3/issues/34#issuecomment-168775122
%if %{?suse_version} < 1500
export CFLAGS="%{optflags} -fgnu89-inline"
%else
export CFLAGS="%{optflags}"
%endif
%make_build all extra

mkdir examples
mv log-f3wr f3write.h2w examples
chmod a-x examples/*

%install
%make_install PREFIX=%{_prefix} install-extra

%files
%doc changelog README.rst examples
%license LICENSE
%{_bindir}/f3read
%{_bindir}/f3write
%{_bindir}/f3probe
%{_bindir}/f3brew
%{_bindir}/f3fix
%{_mandir}/man1/f3read.1%{?ext_man}
%{_mandir}/man1/f3write.1%{?ext_man}

%changelog
