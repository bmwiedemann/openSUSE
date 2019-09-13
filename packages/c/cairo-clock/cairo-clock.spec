#
# spec file for package cairo-clock (Version 0.3.4)
#
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           cairo-clock
Summary:        Cairo-rendered on-screen clock
Version:        0.3.4
Release:        1
URL:            http://macslow.thepimp.net/projects/cairo-clock
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM cairo-clock-fix-ldflags.patch deb#624922 vuntz@opensuse.org -- Taken from Debian, fix "unrecognized option '--export-dynamic'"
Patch0:         cairo-clock-fix-ldflags.patch
# Note: src/cairo-clock.c has a link to the GPL (unversioned) on gnu.org; when the file was created, that link was pointing to GPL-2.0, not GPL-3.0
License:        GPL-2.0
Group:          Amusements/Toys/Clocks
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libglade2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
It is an analog clock displaying the system-time. It leverages the
new visual features offered by a compositing manager to produce a
time display with pretty-pixels.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure
%__make %{?jobs:-j%jobs}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name} X-SuSE-DesktopUtility
%fdupes %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%doc %{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
