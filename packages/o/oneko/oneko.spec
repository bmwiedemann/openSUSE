#
# spec file for package oneko
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


Name:           oneko
Version:        1.2.sakura.5
Release:        0
Summary:        A Cat Catches Your Mouse
License:        SUSE-Public-Domain
Group:          Amusements/Toys/Graphics
URL:            https://www.daidouji.com/oneko/
Source0:        %{URL}/distfiles/oneko-%{version}.tar.gz
Patch0:         oneko-gcc14.patch
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)

%description
A nice program that changes your cursor into a cat playing with your
mouse cursor.  The manual page shows more possibilities to change your
cursor.

%prep
%setup -q -b0
%patch -P0 -b .p0

%build
%global optflags %{optflags} -fpermissive
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
