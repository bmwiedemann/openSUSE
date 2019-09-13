#
# spec file for package gedit-latex
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gedit-latex
Version:        3.20.0
Release:        0
# Code itself is GPLv2+ as of 0.2, but upstream explicitly ships a GPLv3 COPYING file
Summary:        GEdit Plugin for Editing LaTeX Documents
License:        GPL-3.0+
Group:          Productivity/Text/Editors
Url:            https://live.gnome.org/Gedit/LaTeXPlugin
Source0:        http://download.gnome.org/sources/gedit-latex/3.20/%{name}-%{version}.tar.xz
# For directory ownership
BuildRequires:  fdupes
BuildRequires:  gedit
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin turns the gedit editor into a productive environment for
editing LaTeX documents and managing BibTeX bibliographies.

%package -n gedit-plugin-latex
Summary:        GEdit Plugin for Editing LaTeX Documents
Group:          Productivity/Text/Editors
Requires:       dbus-1-python
Requires:       gedit
# For gvfs-open
Requires:       gvfs
Requires:       rubber
Recommends:     %{name}-lang
# Nice, and needed to make lang package installable
Provides:       %{name} = %{version}
%glib2_gsettings_schema_requires

%description -n gedit-plugin-latex
This plugin turns the gedit editor into a productive environment for
editing LaTeX documents and managing BibTeX bibliographies.

%lang_package
%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1330
%post -n gedit-plugin-latex
%glib2_gsettings_schema_post

%postun -n gedit-plugin-latex
%glib2_gsettings_schema_postun
%endif

%files -n gedit-plugin-latex
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/gedit/plugins/latex/
%{_libdir}/gedit/plugins/latex.plugin
%{_datadir}/gedit/plugins/latex/
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml

%files lang -f %{name}.lang

%changelog
