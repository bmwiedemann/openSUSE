#
# spec file for package xcape
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xcape
Version:        1.2
Release:        0
Summary:        Use a modifier key as another key
License:        GPL-3.0
Group:          System/X11/Utilities
Url:            https://github.com/alols/xcape
Source0:        https://github.com/alols/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)

%description
xcape allows you to use a modifier key as another key when pressed and released
on its own. The default behaviour is to generate the Escape key when Left Control 
is pressed and released on its own.

%prep
%setup -q

%build
make %{?_smp_mflags} \
     CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot} MANDIR="/share/man/man1"

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
