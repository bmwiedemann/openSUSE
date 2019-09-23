#
# spec file for package pinta
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pinta
Version:        1.6
Release:        0
Summary:        Drawing/editing application on C#
License:        MIT
Group:          Productivity/Graphics/Bitmap Editors
Url:            http://pinta-project.com/
Source:         https://github.com/PintaProject/Pinta/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  mono(Mono.Addins)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glib-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono) >= 2.8
BuildRequires:  pkgconfig(mono-cairo)
Recommends:     %{name}-lang = %{version}
BuildArch:      noarch

%description
Pinta is a free, open source drawing/editing application designed
after Paint.NET. Its goal is to provide users with a simple yet
powerful way to draw and manipulate images.


%lang_package

%prep
%setup -q
# update the project and solution files for mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . \( -name "*.csproj" -o -name "*.proj" \) -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g; s#Mono.Posix, Version.*"#Mono.Posix"#g' {} \;

%build
autoreconf -fi
%configure --libdir=%{_libexecdir}
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%check
make check

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc license-mit.txt readme.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man?/%{name}.?%{?ext_man}

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
