#
# spec file for package wxMaxima
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


%define tarname wxmaxima
Name:           wxMaxima
Version:        19.08.1
Release:        0
Summary:        Graphical User Interface for the maxima Computer Algebra System
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://wxmaxima-developers.github.io/wxmaxima/
Source0:        https://github.com/wxmaxima-developers/wxmaxima/archive/Version-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  maxima >= 5.30.0
BuildRequires:  rsvg-view
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel >= 3
# gnuplot is needed for plotting
Requires:       gnuplot
Requires:       maxima >= 5.30.0
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
ExcludeArch:    ppc64 ppc64le

%description
wxMaxima is a GUI for the computer algebra system maxima
based on wxWidgets.

%prep
%setup -q -n %{tarname}-Version-%{version}

%build
%cmake

make %{?_smp_mflags}

%install
%cmake_install
# INSTALL HI-RES ICONS GENERATED OUT OF UPSTREAM SVG ICON
for i in 24 32 48 64 128 256 512
do
  rsvg-convert -w ${i} data/io.github.wxmaxima_developers.wxMaxima.svg -o wxmaxima-${i}.png
  install -D -m 0644 wxmaxima-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.github.wxmaxima_developers.wxMaxima.png
done
install -D -m 0644 data/io.github.wxmaxima_developers.wxMaxima.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.github.wxmaxima_developers.wxMaxima.svg

# REMOVE UNNECESSARY ICONS OUT OF PIXMAPS
rm %{buildroot}%{_datadir}/pixmaps/*

# REMOVE README.md AND COPYING FILES INSTALLED BY mak install, WE INCLUDE THEM BY USING %%doc
rm %{buildroot}%{_datadir}/%{name}/README.md
rm %{buildroot}%{_datadir}/%{name}/COPYING

%suse_update_desktop_file io.github.wxmaxima_developers.wxMaxima

%fdupes %{buildroot}%{_prefix}

%find_lang %{name}

%post
%if 0%{?suse_version} < 1500
%desktop_database_post
%icon_theme_cache_post
%mime_database_post
%endif
%install_info --info-dir=%{_infodir} %{_infodir}/wxmaxima.info%{ext_info}

%postun
%if 0%{?suse_version} < 1500
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun
%endif
%install_info_delete --info-dir=%{_infodir} %{_infodir}/wxmaxima.info%{ext_info}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README.md ChangeLog
%{_datadir}/doc/%{tarname}/
%{_bindir}/*
%{_datadir}/wxMaxima/
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/*/apps/io.github.wxmaxima_developers.wxMaxima.*
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/wxmaxima
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/wxmaxima*%{ext_man}
%{_datadir}/mime/packages/*.xml

%changelog
