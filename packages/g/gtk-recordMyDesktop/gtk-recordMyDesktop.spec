#
# spec file for package gtk-recordMyDesktop (Version 0.3.8)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

%define _name gtk-recordmydesktop

Name:           gtk-recordMyDesktop
Summary:        Graphical Frontend for recordMyDesktop
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            http://recordmydesktop.sourceforge.net
License:        GPL-2.0+
Version:        0.3.8
Release:        1
Source:         %{_name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  python-devel
BuildRequires:  python-gtk-devel
BuildRequires:  update-desktop-files
Requires:       python-gtk
Requires:       recordmydesktop
Requires:       jack
Requires:       xwininfo
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%py_requires
%if 0%{?suse_version} < 1120
%define python_sitelib %{py_sitedir}
%endif

%description
Adds an easy to use graphical icon on the GNOME toolbar to make a
pleasure use and configure the audio and video capture and screencast
application recordMyDesktop.

%lang_package

%prep
%setup -q -n %{_name}-%{version}

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{_name}
%fdupes %{buildroot}/%{python_sitelib}

%clean
rm -rf %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/gtk-recordMyDesktop
%{_datadir}/applications/gtk-recordmydesktop.desktop
%{_datadir}/pixmaps/gtk-recordmydesktop.png
%{python_sitelib}/recordMyDesktop

%files lang -f %{name}.lang

%changelog
