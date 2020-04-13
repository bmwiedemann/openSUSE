#
# spec file for package mp3gain
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012 Packman Team <packman@links2linux.de>
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


%define realversion 1_6_2
Name:           mp3gain
Version:        1.6.2
Release:        0
Summary:        MP3 Volume Normalizer based on Replay Gain
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://mp3gain.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/mp3gain/mp3gain/%{version}/mp3gain-%{realversion}-src.zip
Source1:        %{name}.1.gz
# PATCH-FIX-UPSTREAM 0001-fix-security-bugs.patch boo#1154971
Patch0:         0001-fix-security-bugs.patch
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(libmpg123)

%description
MP3Gain analyzes and adjusts mp3 files so that they have the same volume.
It does not just do peak normalization, as many normalizers do. Instead,
it does some statistical analysis to determine how loud the file actually
sounds to the human ear. Also, the changes MP3Gain makes are completely
lossless. There is no quality lost in the change because the program
adjusts the mp3 file directly, without decoding and re-encoding.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p2

%build
export CFLAGS="%{optflags}"
%make_build

%install
install -D -m 0755 mp3gain %{buildroot}%{_bindir}/mp3gain
install -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%license lgpl.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
