#
# spec file for package mfsm
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mfsm
BuildRequires:  imake
BuildRequires:  openmotif
BuildRequires:  openmotif-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
Url:            http://members.tripod.com/SDHEngSoft/mfsm.html
Version:        1.4
Release:        0
Summary:        X Window System Based du
License:        ISC
Group:          System/Monitoring
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch:          %{name}-%{version}.patch
Patch1:         %{name}-%{version}-file-close.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
X Window Motif utility that monitors free space and user quotas of file
systems.

%prep
%setup -q
%patch
%patch1

%build
xmkmf -a
test -x /usr/sbin/switch_motif_linking && \
  /usr/sbin/switch_motif_linking dynamic
make CCOPTIONS="$RPM_OPT_FLAGS" LDFLAGS="-L%_libdir" %{?_smp_mflags}

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot/%_mandir/man1
install -m 0755 mfsm %buildroot/%_bindir
install -m 0644 mfsm._man %buildroot/%_mandir/man1/mfsm.1x
%suse_update_desktop_file -i %name System Filesystem

%files
%defattr(-,root,root)
%_datadir/applications/%name.desktop
%_bindir/mfsm
%doc %_mandir/man1/mfsm.1x.gz
%doc README THANKS TODO FIXES

%changelog
