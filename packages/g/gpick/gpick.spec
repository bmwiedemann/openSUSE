#
# spec file for package gpick
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gpick
Version:        0.2.5
Release:        0
Summary:        Advanced color picker writen in GTK+
License:        BSD-3-Clause
Group:          Productivity/Graphics/Visualization/Other
Url:            http://www.gpick.org/
Source0:        http://gpick.googlecode.com/files/%{name}_%{version}.tar.gz
Source1:        copyright
# PATCH-FIX-UPSTREAM reproducible.patch gh#thezbyg/gpick#138 bwiedemann@suse.com -- Fix reproducible builds
Patch0:         reproducible.patch
# PATCH-FIX-UPSTREAM 0001-build-support-scons-python3.patch dimstar@opensuse.org -- Support scons running with python3 as interpreter
Patch1:         0001-build-support-scons-python3.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  expat
BuildRequires:  flex
BuildRequires:  gcc-c++
# hicolor-icon-theme BuildRequires for directory ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  libexpat-devel
BuildRequires:  pkgconfig
BuildRequires:  scons
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lua) >= 5.2
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Gpick is a featured color picker with palette creation and modification
tools. It is written in C++ and uses GTK+ toolkit for user interface.

%lang_package
%prep
%setup -q -n %{name}_%{version}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
scons %{?_smp_mflags}

%install
export CFLAGS="%optflags"
export CXXFLAGS="%optflags"
scons install DESTDIR=%{buildroot}%{_prefix} LOCALEDIR=%{_datadir}/locale
%if 0%{?suse_version}
%suse_update_desktop_file %{name} Viewer
%endif
# Install copyright file. This file was given to me by the author/upstream.
cp %{SOURCE1} COPYRIGHT
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%if 0%{?fedora_version}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%endif

%files
%defattr(-,root,root)
%doc COPYRIGHT
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/doc/%{name}/
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_mandir}/man1/%{name}.*

%files lang -f %{name}.lang

%changelog
