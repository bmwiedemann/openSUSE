#
# spec file for package hcode
#
# Copyright (c) 2023 SUSE LLC
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


Name:           hcode
Version:        2.1
Release:        0
Summary:        Hangul Code Conversion Utilities (hcode, hdcode)
License:        GPL-2.0-or-later
Group:          System/I18n/Korean
Source0:        hcode2.1-mailpatch3.tar.gz
Source1:        hdcode.c
Patch1:         hcode2.1-mailpatch3-ksc5601.patch
Patch2:         fix-implicit-declarations.patch

%description
Hangul code conversion utilities (hcode, hdcode).

%prep
%setup -q -n hcode2.1-mailpatch3
cp -f %{SOURCE1} .
%patch1 -p1 -b .ksc5601
%patch2 -p1

%build
%make_build CFLAGS="%{optflags}"
gcc %{optflags} -D_MAIN -DCLEAN_QP -o hdcode hdcode.c

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 hcode  %{buildroot}%{_bindir}/hcode
install -m 755 hdcode %{buildroot}%{_bindir}/hdcode

%files -n hcode
%doc CHANGES README README.elm README.mailpatch README.pine
%{_bindir}/hcode
%{_bindir}/hdcode

%changelog
