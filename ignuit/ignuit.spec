#
# spec file for package ignuit
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


Name:           ignuit
Version:        2.24.3
Release:        0
Summary:        Flashcard learning system
License:        GPL-3.0+ and GPL-2.0
Group:          Amusements/Teaching/Other
Url:            http://savannah.gnu.org/projects/ignuit/
Source:         http://ftp.gnu.org/gnu/ignuit/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} < 1500
BuildRequires:  update-desktop-files
%endif
BuildRequires:  intltool >= 0.50.0
BuildRequires:  pkgconfig(gconf-2.0)  >= 3.2.6
BuildRequires:  pkgconfig(gnome-doc-utils) >= 0.3.2
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.8.2
BuildRequires:  pkgconfig(libglade-2.0) >= 2.6.4
BuildRequires:  pkgconfig(libgnomeui-2.0) >= 2.24.5
BuildRequires:  pkgconfig(libxslt) >= 1.1.28
PreReq:         %install_info_prereq

%description
Ignuit is a memorization aid based on the Leitner flashcard system.
It has a GNOME look and feel, a good selection of quiz options,
and supports UTF-8. It can be used for both long-term learning
and cramming. Ignuit can import and export several file formats,
including CSV.


%lang_package
%prep
%setup -q

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}

%install
%make_install

%find_gconf_schemas
%find_lang %{name}
cat %{name}.lang %{name}.schemas_list >%{name}.lst

%pre -f %{name}.schemas_pre

%posttrans -f %{name}.schemas_posttrans

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%if 0%{?suse_version} < 1500
%desktop_database_post
%icon_theme_cache_post
%endif

%preun -f %{name}.schemas_preun

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz
%if 0%{?suse_version} < 1500
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files -f %{name}.lst
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING COPYING.extras NEWS README TODO examples
%{_bindir}/*
%{_datadir}/applications/*
%dir %{_datadir}/gnome/help/%{name}
%dir %{_datadir}/gnome/help/%{name}/C
%dir %{_datadir}/gnome/help/%{name}/C/figures
%dir %{_datadir}/omf
%dir %{_datadir}/omf/%{name}
%doc %{_datadir}/gnome/help/%{name}/C/*.xml
%doc %{_datadir}/gnome/help/%{name}/C/figures/*.png
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/omf/%{name}/*.omf
%{_infodir}/%{name}.*
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
