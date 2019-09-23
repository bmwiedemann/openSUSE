#
# spec file for package xprintidle
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xprintidle
Version:        0.2
Release:        0
Summary:        Utility to print user's idle time in X
License:        GPL-2.0
Group:          System/X11/Utilities
Url:            http://freecode.com/projects/xprintidle
Source:         http://httpredir.debian.org/debian/pool/main/x/%{name}/%{name}_%{version}.orig.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
An utility that queries the X server for the user's idle time and
prints it to stdout (in milliseconds).

%prep
%setup -q
sed -i 's/dist-lzma //' configure.ac

%build
export LIBS="-lXext"
autoreconf -fi
%configure \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir}
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/%{name}

%changelog
