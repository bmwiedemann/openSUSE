#
# spec file for package oneko
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


Name:           oneko
Version:        1.2.sakura.5
Release:        0
Summary:        A Cat Catches Your Mouse
License:        SUSE-Public-Domain
Group:          Amusements/Toys/Graphics
Url:            http://www.daidouji.com/oneko/
Source:         %{URL}/distfiles/oneko-%{version}.tar.gz
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
A nice program that changes your cursor into a cat playing with your
mouse cursor.  The manual page shows more possibilities to change your
cursor.

%prep
%setup -q -b0

%build
xmkmf -a
make all %{?_smp_mflags}

%install
%make_install install.man
mv README README.jp

%files
%doc README.jp README-NEW sample.resource
%{_bindir}/*
%{_mandir}/man1/oneko.1x%{?ext_man}

%changelog
