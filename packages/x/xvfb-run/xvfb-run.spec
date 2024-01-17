#
# spec file for package xvfb-run
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xvfb-run
Version:        1.5.2
Release:        0
Summary:        Script to run a virtualized X-Server
License:        GPL-2.0-only
Group:          System/X11/Utilities
URL:            https://packages.debian.org/de/sid/xvfb
Source0:        http://svn.exactcode.de/t2/trunk/package/xorg/xorg-server/xvfb-run.sh
Source1:        https://manpages.debian.org/testing/xvfb/xvfb-run.1.en.gz#/xvfb-run.1.gz
# PATCH-FIX-OPENSUSE https://bugzilla.redhat.com/show_bug.cgi?id=508739#c6
Patch0:         xvfb-run-mktemp.patch
Requires:       coreutils
Requires:       util-linux
Requires:       which
Requires:       xauth
Requires:       xorg-x11-server
Requires:       xorg-x11-xauth
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This script starts an instance of Xvfb, the "fake" X server, runs a command
with that server available, and kills the X server when done. The return
value of the command becomes the return value of this script.

%prep
cp %{SOURCE0} .
%patch0 -p0

%build

%install
install -p -D %{_builddir}/xvfb-run.sh %{buildroot}%{_bindir}/xvfb-run
chmod 755 %{buildroot}%{_bindir}/xvfb-run

mkdir -p %{buildroot}%{_mandir}/man1/
cp %{SOURCE1} %{buildroot}%{_mandir}/man1/xvfb-run.1.gz

%files
%defattr(-,root,root,-)
%{_bindir}/xvfb-run
%{_mandir}/*/xvfb-run.1.gz

%changelog
