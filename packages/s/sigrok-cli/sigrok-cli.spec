#
# spec file for package sigrok-cli
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


Summary:        Logic Analyzer Command Line Tool
License:        GPL-3.0+
Group:          Productivity/Scientific/Electronics

Name:           sigrok-cli
Version:        0.7.0
Release:        0
Url:            http://sigrok.org
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  libsigrok-devel >= 0.4.0
BuildRequires:  libsigrokdecode-devel >= 0.4.0
BuildRequires:  libtool
Source0:        http://sigrok.org/download/source/sigrok-cli/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The sigrok project aims at creating a portable, cross-platform,
Free/Libre/Open-Source logic analyzer software that supports various
logic analyzer hardware products.

sigrok-cli is a command-line tool written in C, which uses both
libsigrok and libsigrokdecode to provide the basic sigrok
functionality from the command-line. Among other things, it's useful
for scripting purposes.

%prep
%setup -q

%build
#./autogen.sh
autoreconf -fiv
%configure
make %{?smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc NEWS README COPYING
%doc %_mandir/*/*
%_bindir/*

%changelog
