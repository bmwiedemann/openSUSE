#
# spec file for package paps
#
# Copyright (c) 2025 SUSE LLC
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


Name:           paps
Version:        0.8.0
Release:        0
Summary:        A text to postscript converter through pango
License:        LGPL-2.0-only
Group:          System/Base
URL:            https://github.com/dov/paps
Source:         https://github.com/dov/paps/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         paps-header_features.patch
Patch1:         71.patch
# PATCH-FIX-UPSTREAM no-python2.patch gh#dov/paps!75 mcepl@suse.com
# Remove dependency on python 2
Patch2:         no-python2.patch
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  rpm_macro(meson)
Requires:       glibc-locale

%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%description
paps is a command line program for converting Unicode text encoded in UTF-8 to postscript and pdf by using pango.

%prep
%setup -qT -b0 -n %{name}-%{version}
%autopatch -p1

%build
%add_optflags -D_XOPEN_SOURCE
%meson
%meson_build

%install
%meson_install
%python3_fix_shebang

%files
%defattr(-,root,root)
%license COPYING.LIB
%{_bindir}/*
%{_mandir}/*/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/pango_markup.outlang

%changelog
