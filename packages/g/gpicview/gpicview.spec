#
# spec file for package gpicview
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gpicview
Version:        0.2.5
Release:        0
Summary:        LXDE Photo Viewer
License:        GPL-2.0-only
Group:          Productivity/Graphics/Viewers
Url:            http://www.lxde.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-0.2.4_fix_boo_904558.patch
Patch1:         gpicview-0.2.5-addreturnvalue.patch
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-runtime
BuildRequires:  gettext-tools
BuildRequires:  gtk2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  perl
BuildRequires:  perl-XML-Parser
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%lang_package

%description
An extremely fast, lightweight, yet feature-rich photo viewer.
This software is part of the LXDE Desktop Environment.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%suse_update_desktop_file -r gpicview GTK Graphics Viewer
%find_lang %{name}
%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/gpicview.desktop
%dir %{_datadir}/gpicview
%dir %{_datadir}/gpicview/pixmaps
%dir %{_datadir}/gpicview/ui
%{_datadir}/gpicview/pixmaps/*.png
%{_datadir}/gpicview/ui/pref-dlg.ui
%{_datadir}/icons/hicolor/48x48/apps/gpicview.png

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog
