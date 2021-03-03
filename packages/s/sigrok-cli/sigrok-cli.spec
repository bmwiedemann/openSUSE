#
# spec file for package sigrok-cli
#
# Copyright (c) 2021 SUSE LLC
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


Summary:        Logic Analyzer Command Line Tool
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Electronics

Name:           sigrok-cli
Version:        0.7.2
Release:        0
URL:            https://sigrok.org
BuildRequires:  glib2-devel
BuildRequires:  libsigrok-devel >= 0.4.0
BuildRequires:  libsigrokdecode-devel >= 0.4.0
Source0:        https://sigrok.org/download/source/sigrok-cli/%{name}-%{version}.tar.gz

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
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README
%doc %_mandir/*/*
%_bindir/*
%dir %{_datadir}/applications/
%{_datadir}/applications/org.sigrok.sigrok-cli.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable/
%dir %{_datadir}/icons/hicolor/scalable/apps/
%{_datadir}/icons/hicolor/scalable/apps/sigrok-cli.svg

%changelog
