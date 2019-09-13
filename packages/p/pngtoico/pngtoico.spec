#
# spec file for package pngtoico
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           pngtoico
Version:        1.0.1
Release:        0
Summary:        Utility to convert PNG images to Microsoft ICO format
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Url:            http://www.kernel.org/pub/software/graphics/pngtoico/
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE pngtoico-makefile.patch -- adjusts path and linkage
Patch0:         %{name}-makefile.patch
# PATCH-FIX-UPSTREAM pngtoico-libpng15.patch -- pgajdos@suse.com; build with libpng15; sent today to hpa@zytor.com
# build against libpng14 should not be affected, otherwise please let me know
Patch1:         %{name}-libpng15.patch
BuildRequires:  libpng-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pngtoico is a small utility to convert a set of PNG images to Microsoft
ICO format. Supports transparency.

%prep
%setup -q
%patch0
%patch1 -p1

%build
make CFLAGS="%{optflags}"

%install
make "INSTALLROOT=%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_mandir}/man1/pngtoico.1.gz
%{_bindir}/pngtoico

%changelog
