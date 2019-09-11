#
# spec file for package 4pane
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Packman Team <packman@links2linux.de>
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

Name:           4pane
Version:        5.0
Release:        0
Summary:        A multi-pane detailed-list file manager
License:        GPL-3.0
Group:          Productivity/File utilities
Url:            http://www.4pane.co.uk/
Source0:        https://sourceforge.net/projects/fourpane/files/%{version}/%{name}-%{version}.tar.gz
%if 0%{?is_opensuse}
BuildRequires:  wxWidgets-devel >= 3
%else
# SLE_12 lacks wxWidgets_3.0-devel
BuildRequires:  wxWidgets-devel < 3
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%endif
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  xz-devel
Recommends:     %{name}-lang

%description
4Pane is a multi-pane detailed-list file manager.
It favors speed over visual effects.
In addition to standard file manager features, it offers multiple undo and redo
of most operations (including deletions), archive management including "virtual
browsing" inside archives, multiple renaming/duplication of files, a terminal
emulator and user-defined tools.

%lang_package

%prep
%setup -q
sed -i -e "s|\$(datadir)/doc|%{_docdir}|g" Makefile.in
sed -i -e "s|/usr/doc/4Pane/|%{_docdir}/4Pane/|g" Configure.cpp

%build
%configure
make %{?_smp_mflags}


%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%find_lang 4Pane
mkdir -vp %{buildroot}/%{_datadir}/applications
mkdir -vp %{buildroot}/%{_datadir}/appdata
cd %{buildroot}/%{_datadir}/applications
ln -s ../4Pane/rc/4Pane.desktop 4Pane.desktop
pushd %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
convert -strip -resize 48x48! 4Pane.png 4Pane.png
popd
%fdupes -s %{buildroot}/%{_datadir}

%files
%defattr(-,root,root,-)
%doc LICENCE
%{_bindir}/%{name}
%{_bindir}/4Pane
%dir %{_datadir}/4Pane
%dir %{_datadir}/4Pane/bitmaps
%{_datadir}/4Pane/bitmaps/*
%{_datadir}/appdata
%{_datadir}/icons/hicolor/*
%{_datadir}/4Pane/rc
%{_datadir}/applications/4Pane.desktop
%dir %{_docdir}/4Pane
%{_docdir}/4Pane/*

%files lang -f 4Pane.lang
%defattr(-,root,root,-)

%changelog
