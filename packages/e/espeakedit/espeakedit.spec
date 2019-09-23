#
# spec file for package espeakedit
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


%define _version %{version}-source
#Fix ability to use wxcontainer instead of stl variant for WxWidgets
Name:           espeakedit
Version:        1.48.03
Release:        0
Summary:        Software speech synthesizer (text-to-speech)
License:        GPL-3.0+
Group:          Productivity/Other
Url:            http://espeak.sourceforge.net
Source:         %{name}-%{version}.zip
Source1:        espeakedit.1
#PATCH-FIX-UPSTREAM marguerite@opensuse.org - lack of next line mark in Makefile
Patch1:         espeakedit-1.48.03-next-line.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org - fix narrowing conversion from int to char inside {} 
Patch2:         espeakedit-1.48.03-gcc6.patch
Patch3:         espeakedit-wx3.diff
#PATCH-FIX-UPSTREAM marguerite@opensuse.org - fix destbufferoverflow bsp check at dictionary.cpp
Patch4:         espeakedit-gcc7-destbufferoverflow.patch
BuildRequires:  gcc-c++
BuildRequires:  portaudio-devel
BuildRequires:  pulseaudio-devel
BuildRequires:  unzip
BuildRequires:  wxWidgets-devel >= 3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
eSpeak is a software speech synthesizer for English, and some other languages.
eSpeakEdit provides a User Interface to edit the eSpeak voices.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch -P 3 -p1
%patch4 -p1
# Build against portaudio v19 (see ReadMe)
cp -f src/portaudio19.h src/portaudio.h

%build
cd src
make %{?_smp_mflags} CFLAGS="%{optflags}"
cd ..

%install
cd src
mkdir -p %{buildroot}/%{_bindir}/
cp espeakedit %{buildroot}/%{_bindir}/
cd ..
# Install manpage
install -D -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/espeakedit.1

%files
%defattr (-,root,root,755)
%{_bindir}/espeakedit
%{_mandir}/man1/espeakedit.1%{ext_man}

%changelog
