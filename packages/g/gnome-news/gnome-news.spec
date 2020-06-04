#
# spec file for package gnome-news
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gnome-news
Version:        0.0.1+20200418
Release:        0
Summary:        GNOME News Reader
License:        GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://git.gnome.org//browse/gnome-news
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-shell-no-jhbuild.patch boo#1109687 dimstar@opensuse.org -- Drop special code for jhbuild, make the package noarch
Patch0:         gnome-shell-no-jhbuild.patch
BuildRequires:  appstream-glib-devel >= 0.7.3
BuildRequires:  autoconf-archive
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  python3-gobject
BuildArch:      noarch

%description
A GNOME 3 Feed Reader.

%lang_package

%prep
%autosetup -p1
#Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -type f -exec perl -pi -e 'BEGIN{undef $/};s[^#\!%{_bindir}/env python3][#\!%{_bindir}/python3]' {} \;

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.News.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.News.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.News*
# Own dir for openSUSE Leap
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.News.appdata.xml
%{python3_sitelib}/gnomenews/

%files lang -f %{name}.lang

%changelog
