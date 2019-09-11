#
# spec file for package hmconv
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           hmconv
Version:        1.0pl5
Release:        0
Summary:        HangulCode Conversion Program
License:        SUSE-Public-Domain
Group:          System/I18n/Korean
Url:            http://ftp.kaist.ac.kr/hangul/code/hmconv/
Source0:        hmconv1.0pl3.tar.gz
Source1:        hmconv.c
Patch0:         hmconv.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
HangulCode conversion program.



Authors:
--------
    Jungshik Shin &lt;jshin@pantheon.yale.edu&gt;

%prep
%setup -q -n hmconv

%build
cp %{SOURCE1} .
patch -p0 -i $RPM_SOURCE_DIR/hmconv.patch
%__cc $RPM_OPT_FLAGS -o hmconv hmconv.c

%install
mkdir -p %{buildroot}%{_prefix}/bin
install -m 755 hmconv %{buildroot}%{_prefix}/bin

%files -n hmconv
%defattr(-,root,root)
%doc CHANGES README README.elm README.pine hmailedit
%{_prefix}/bin/hmconv

%changelog
