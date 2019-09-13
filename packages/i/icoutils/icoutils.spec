#
# spec file for package icoutils
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


Name:           icoutils
Version:        0.31.3
Release:        0
Summary:        Extracting and Converting Microsoft Icon and Cursor Files
License:        GPL-3.0+
Group:          Productivity/Graphics/Convertors
Url:            http://www.nongnu.org/icoutils/
Source0:        http://savannah.nongnu.org/download/icoutils/%{name}-%{version}.tar.bz2
Source1:        http://savannah.nongnu.org/download/icoutils/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The icoutils are a set of programs for extracting and converting images
in Microsoft Windows icon and cursor files. These files usually have the
extension .ico or .cur, but they can also be embedded in executables or
libraries (.dll-files).

%prep
%setup -q

%build
# Don't compile strange locales en@boldquot and en@quot.
# Otherwise, remove '--disable-nls'.
%configure --disable-nls
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/*
%{_mandir}/man?/*

%changelog
