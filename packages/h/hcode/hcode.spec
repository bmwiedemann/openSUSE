#
# spec file for package hcode
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           hcode
License:        GPL-2.0+
Group:          System/I18n/Korean
AutoReqProv:    on
Summary:        Hangul Code Conversion Utilities (hcode, hdcode)
Version:        2.1
Release:        655
Source0:        hcode2.1-mailpatch3.tar.gz
Source1:        hdcode.c
Patch1:         hcode2.1-mailpatch3-ksc5601.patch
Patch2:         fix-implicit-declarations.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Hangul code conversion utilities (hcode, hdcode).



Authors:
--------
    Jungshik Shin &lt;jshin@pantheon.yale.edu&gt;
    Sang-yong Suh &lt;sysuh@kigam.re.kr&gt;

%prep
%setup -q -n hcode2.1-mailpatch3
cp -f %{SOURCE1} .
%patch1 -p1 -b .ksc5601
%patch2 -p1

%build
make CC="%__cc" CFLAGS="$RPM_OPT_FLAGS"
%__cc $RPM_OPT_FLAGS -D_MAIN -DCLEAN_QP -o hdcode  hdcode.c

%install
mkdir -p %{buildroot}%{_prefix}/bin
install -m 755 hcode  %{buildroot}%{_prefix}/bin/hcode
install -m 755 hdcode %{buildroot}%{_prefix}/bin/hdcode

%clean
rm -rf %{buildroot}

%files -n hcode
%defattr(-,root,root,-)
%doc CHANGES README README.elm README.mailpatch README.pine
%{_prefix}/bin/hcode
%{_prefix}/bin/hdcode

%changelog
