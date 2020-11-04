#
# spec file for package unison
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           unison
Version:        2.51.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        File synchronization tool
License:        GPL-3.0+
Group:          Productivity/Networking/Other
Url:            https://github.com/bcpierce00/unison
Source0:        %{name}-%{version}.tar.xz
#https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html
Source1:        unison-2.48.4-manual.html
Source2:        %{name}.desktop
Source3:        %{name}.png
Patch0:         Compatibility-with-OCaml-4.08.patch
Patch1:         Fix-for-lablgtk-2.18.6.patch
Patch2:         Fix-warnings-raised-by-OCaml-4.08.1.patch
Patch3:         Compile-without-unsafe-string.patch
BuildRequires:  gtk2-devel
BuildRequires:  ncurses-devel
BuildRequires:  ocaml(ocaml_base_version) >= 4.07
BuildRequires:  ocaml-lablgtk2-devel > 2.18.5
BuildRequires:  ocaml-rpm-macros >= 20200220
BuildRequires:  update-desktop-files

%description
Unison is a file synchronization tool for Unix and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified
separately, then brought up to date by propagating the changes in each
replica to the other.

%prep
%autosetup -p1

%build
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
%if 0%{?ocaml_native_compiler}
NATIVE=true
%else
NATIVE=false
%endif
make UISTYLE=gtk2 NATIVE=$NATIVE THREADS=true

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}
install -m 755 %{name}-fsmonitor %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}/%{_prefix}/share/pixmaps
install -m 644 %{SOURCE3} %{buildroot}/%{_prefix}/share/pixmaps
install -m 644 %{SOURCE1} unison-manual.html
%suse_update_desktop_file -i %name Utility SyncUtility

%files
%doc BUGS.txt CONTRIB COPYING NEWS README ROADMAP.txt unison-manual.html
%{_datadir}/applications/*
%{_datadir}/pixmaps/unison.png
%{_bindir}/%{name}
%{_bindir}/%{name}-fsmonitor

%changelog
