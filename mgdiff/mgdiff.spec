#
# spec file for package mgdiff
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


Name:           mgdiff
BuildRequires:  imake
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXp-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  openmotif
BuildRequires:  openmotif-devel
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
Version:        1.0.1
Release:        0
Summary:        Compare Files Side by Side
License:        MIT
Group:          Productivity/Text/Utilities
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         mgdiff-1.0.tar.bz2
Source1:        mgdiff.desktop
Patch:          mgdiff-1.0.dif
Patch1:         mgdiff-1.0.1.diff
Patch2:         mgdiff-1.0-locale.diff
# PATCH-FIX-SUSE Avoid getline in local name space
Patch3:         mgdiff-1.0-getline.diff
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%global _mandir     %{_exec_prefix}/man
%define _x11data    %{_exec_prefix}/lib/X11
%define _appdefdir  %{_x11data}/app-defaults
%define _mgdifflnk  ../lib/X11/mgdiff
%else
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults
%define _mgdifflnk  ../share/X11/mgdiff
%endif

%description
Mgdiff is a graphical front-end to the Unix diff command based on X11
and the Motif widget set. It allows the user to select two files for
comparison, runs the diff command, parses the output and presents the
results graphically.



Authors:
--------
    Daniel Williams <dan@sass.com>

%prep
%setup -n mgdiff-1.0 -q
%patch1
%patch
%patch2 -p1
%patch3
xmkmf -a
%if 0%{?suse_version} >= 1320
sed -ri 's/-D_BSD_SOURCE[[:space:]]+-D_SVID_SOURCE/-D_DEFAULT_SOURCE/' Makefile
%endif

%build
make CCOPTIONS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install.man
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_x11data}/mgdiff
mkdir -p %{buildroot}%{_mandir}/man1
test -e debian/cvsmgdiff.1x || mv debian/cvsmgdiff.1 debian/cvsmgdiff.1x
install -m 0755 debian/cvsmgdiff 	%{buildroot}%{_bindir}/
install -m 0755 debian/rmgdiff		%{buildroot}%{_x11data}/mgdiff/
install -m 0644 debian/rmgdiff.awk	%{buildroot}%{_x11data}/mgdiff/
ln -sf   %{_mgdifflnk}/rmgdiff		%{buildroot}%{_bindir}/
install -m 0644 debian/cvsmgdiff.1x	%{buildroot}%{_mandir}/man1/
install -m 0644 debian/rmgdiff.1x	%{buildroot}%{_mandir}/man1/
%suse_update_desktop_file -i %name Development RevisionControl

%files
%defattr(-,root,root)
%doc README
/usr/share/applications/*.desktop
%{_bindir}/*diff
%dir %{_x11data}/mgdiff
%dir %{_x11data}/app-defaults
%{_x11data}/mgdiff/rmgdiff*
%{_appdefdir}/Mgdiff
%doc %{_mandir}/man1/*.1x.gz

%changelog
