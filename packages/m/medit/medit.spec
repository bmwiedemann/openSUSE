#
# spec file for package medit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2014 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           medit
# To keep in sync with po/maintain
%define		moo_package_name %{name}-1
Version:        1.2.0
Release:        0
Summary:        A programming and around-programming text editor
License:        LGPL-2.1-only
Group:          Productivity/Text/Editors
Url:            http://mooedit.sourceforge.net/
Source:         http://download.sourceforge.net/mooedit/medit/1.2.0/medit-1.2.0.tar.bz2
# PATCH-FIX-OPENSUSE medit-fix-configure-errors.patch malcolmlewis@opensuse.org -- Fix docdir location and add linker flag for gmodule-no-export-2.0.
Patch0:         medit-fix-configure-errors.patch
# PATCH-FIX-OPENSUSE medit-fix-incorrect-fsf-address.patch malcolmlewis@opensuse.org -- Fix FSF address warnings.
Patch1:         medit-fix-incorrect-fsf-address.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  perl-XML-Parser
BuildRequires:  python-gtk-devel
BuildRequires:  python-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
Requires:       python-gobject2
Requires:       python-gtk
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Started originally as a simple built-in editor component in GGAP,
it grew up to a real text editor.

Features
 * Configurable syntax highlighting.
 * Configurable keyboard accelerators.
 * Multiplatform - works on unix and windows.
 * Plugins: can be written in C, Python, or Lua.
 * Configurable tools available from the main and context menus.
   They can be written in Python or Lua, or it can be a shell script.
 * Regular expression search/replace, grep frontend, builtin file
   selector, etc.

%lang_package
%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --enable-shared \
           --disable-static
make %{?_smp_mflags} V=1

%install
%makeinstall
%suse_update_desktop_file -i %{name}
%fdupes %{buildroot}
%find_lang %{moo_package_name}-gsv
mv %{moo_package_name}-gsv.lang %{name}.lang
%find_lang %{moo_package_name}
cat %{moo_package_name}.lang >> %{name}.lang
chmod 0755 %{buildroot}%{_datadir}/%{moo_package_name}/language-specs/check.sh
chmod 0755 %{buildroot}%{_datadir}/%{moo_package_name}/python/pyconsole.py
# don't ship the terminal plugin: it requires python-vte, which is no longer maintained
rm %{buildroot}%{_datadir}/%{moo_package_name}/plugins/terminal.py
rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%icon_theme_cache_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS
%{_docdir}/%{moo_package_name}/
%{_bindir}/medit
%{_datadir}/applications/medit.desktop
%{_datadir}/icons/hicolor/48x48/apps/medit.png
%{_datadir}/%{moo_package_name}/
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
