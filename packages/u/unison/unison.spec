#
# spec file for package unison
#
# Copyright (c) 2025 SUSE LLC
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

%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "doc"
%define nsuffix -doc
%else
%define nsuffix %nil
%endif

%define     pkg unison
Name:           %pkg%nsuffix
Version:        2.53.7
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        File synchronization tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://github.com/bcpierce00/unison
Source0:        %pkg-%version.tar.xz
Source1:        %pkg.desktop
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-rpm-macros >= 20231101
%if "%build_flavor" == "doc"
BuildRequires:  hevea
BuildRequires:  lynx
BuildRequires:  texlive-collection-latex
BuildRequires:  texlive-metafont
%else
BuildRequires:  ocamlfind(lablgtk3)
BuildRequires:  pkgconfig(ncursesw)
%if 0%{?suse_version} > 0
BuildRequires:  update-desktop-files
%endif
%endif

%description
Graphical userinterface for Unison.

Unison is a file synchronization tool for Unix and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified
separately, then brought up to date by propagating the changes in each
replica to the other.

%package text
Summary:        File synchronization tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other

%description text
Text based userinterface for Unison.

Unison is a file synchronization tool for Unix and Windows. It allows
two replicas of a collection of files and directories to be stored on
different hosts (or different disks on the same host), modified
separately, then brought up to date by propagating the changes in each
replica to the other.

%prep
%autosetup -p1 -n %pkg-%version

%build
%if "%build_flavor" == "doc"
%make_build docs
%else
%make_build PREFIX=%_prefix
%endif

%install
%if "%build_flavor" == "doc"
echo '%%dir %_defaultdocdir/%pkg' > files
for ext in html pdf
do
  test -f doc/unison-manual.$ext || continue
  mkdir -vp %buildroot%_defaultdocdir/%pkg
  cp doc/unison-manual.$ext %buildroot%_defaultdocdir/%pkg
  echo "%%doc %_defaultdocdir/%pkg/unison-manual.$ext" >> files
done
%else
# The presence of _defaultlicensedir is no inidicator for a usable %%license macro
# If it is defined, but rpm is still too old, it will default to the last License: line.
if bash -x -c 'read a b c < <(rpm --version)
set -- ${c//./ }
test $1 -lt 4 && exit 1
if test $1 -eq 4 && test $2 -lt 14
then
	exit 1
fi
exit 0'
then
	echo '%%license src/COPYING' > files
else
	echo '%%doc src/COPYING' > files
fi
%make_install PREFIX=%_prefix

mv %buildroot%_bindir/%name %buildroot%_bindir/%name-text
mv %buildroot%_bindir/%name-gui %buildroot%_bindir/%name
install -m 644 -D icons/U.svg %buildroot%_datadir/pixmaps/%name.svg
%if %{defined suse_update_desktop_file}
%suse_update_desktop_file -i %name Utility SyncUtility
%else
install -m 644 -D %{SOURCE1} %buildroot/%_datadir/applications/%name.desktop
%endif
%endif

%files -f files
%defattr(-,root,root,-)
%if "%build_flavor" == ""
%_datadir/applications/*
%_datadir/pixmaps/*
%_bindir/%name
%_bindir/%name-fsmonitor
%_mandir/man1/*

%files text
%defattr(-,root,root,-)
%_bindir/%name-text
%endif

%changelog
