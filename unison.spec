#
# spec file for package unison
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


Name:           unison
Version:        2.51.4_rc2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        File synchronization tool
License:        GPL-3.0+
Group:          Productivity/Networking/Other
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://github.com/bcpierce00/unison
Source0:        %{name}-%{version}.tar.xz
#https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html
Source1:        unison-2.48.4-manual.html
Source2:        %{name}.desktop
Source3:        %{name}.png
BuildRequires:  ocaml-lablgtk2-devel > 2.18.5
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(ppx_bin_prot)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(ncursesw)
%if 0%{?suse_version} > 0
BuildRequires:  update-desktop-files
%endif

%description
Unison is a file synchronization tool for Unix and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified
separately, then brought up to date by propagating the changes in each
replica to the other.

%prep
%setup -q

%build
make UISTYLE=gtk2 NATIVE=true

%install
install -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -m 755 -D %{name}-fsmonitor %{buildroot}%{_bindir}/%{name}-fsmonitor
install -m 644 -D %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -m 644 %{SOURCE1} unison-manual.html
%if %{defined suse_update_desktop_file}
%suse_update_desktop_file -i %name Utility SyncUtility
%else
install -m 644 -D %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}.desktop
%endif

%files
%defattr(-,root,root,-)
%doc BUGS.txt CONTRIB COPYING NEWS README unison-manual.html
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_bindir}/%{name}
%{_bindir}/%{name}-fsmonitor

%changelog
