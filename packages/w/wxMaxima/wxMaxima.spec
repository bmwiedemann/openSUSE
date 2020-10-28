#
# spec file for package wxMaxima
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


%define __builder ninja
%define tarname wxmaxima
Name:           wxMaxima
Version:        20.09.0
Release:        0
Summary:        Graphical User Interface for the maxima Computer Algebra System
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://wxmaxima-developers.github.io/wxmaxima/
Source0:        https://github.com/wxmaxima-developers/wxmaxima/archive/Version-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  hicolor-icon-theme
BuildRequires:  maxima >= 5.30.0
BuildRequires:  maxima-exec-sbcl
BuildRequires:  ninja
BuildRequires:  pandoc
BuildRequires:  po4a
%if 0%{suse_version} >= 1550 || 0%{?sle_version} >= 150200
BuildRequires:  rsvg-convert
%else
BuildRequires:  rsvg-view
%endif
BuildRequires:  update-desktop-files
%if 0%{?suse_version} >= 1550
BuildRequires:  wxGTK3-devel >= 3.1
%else
BuildRequires:  wxWidgets-devel >= 3
%endif
# gnuplot is needed for plotting
Requires:       gnuplot
Requires:       maxima >= 5.30.0
Recommends:     %{name}-lang
ExcludeArch:    ppc64 ppc64le

%lang_package

%description
wxMaxima is a GUI for the computer algebra system maxima
based on wxWidgets.

%prep
%setup -q -n %{tarname}-Version-%{version}

%build
%cmake

%cmake_build

%install
%cmake_install
# INSTALL HI-RES ICONS GENERATED OUT OF UPSTREAM SVG ICON
for i in 24 32 48 64 128 256 512
do
  rsvg-convert -w ${i} data/io.github.wxmaxima_developers.wxMaxima.svg -o wxmaxima-${i}.png
  install -D -m 0644 wxmaxima-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/io.github.wxmaxima_developers.wxMaxima.png
  rsvg-convert -w ${i} data/text-x-wxmathml.svg -o text-x-wxmathml-${i}.png
  install -D -m 0644 text-x-wxmathml-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/text-x-wxmathml.png
  rsvg-convert -w ${i} data/text-x-wxmaxima-batch.svg -o text-x-wxmaxima-batch-${i}.png
  install -D -m 0644 text-x-wxmaxima-batch-${i}.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/mimetypes/text-x-wxmaxima-batch.png
done
install -D -m 0644 data/io.github.wxmaxima_developers.wxMaxima.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/io.github.wxmaxima_developers.wxMaxima.svg
install -D -m 0644 data/text-x-wxmathml.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-wxmathml.svg
install -D -m 0644 data/text-x-wxmaxima-batch.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-wxmaxima-batch.svg

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/mimetypes

# REMOVE UNNECESSARY ICONS OUT OF PIXMAPS
rm %{buildroot}%{_datadir}/pixmaps/*

# REMOVE README.md AND COPYING FILES INSTALLED BY mak install, WE INCLUDE THEM BY USING %%doc
rm -fr %{buildroot}%{_datadir}/doc/%{tarname}/README*
rm -fr %{buildroot}%{_datadir}/doc/%{tarname}/COPYING

%suse_update_desktop_file io.github.wxmaxima_developers.wxMaxima

%fdupes %{buildroot}%{_prefix}

%find_lang %{name} %{?no_lang_C}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/wxmaxima.info%{ext_info}

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/wxmaxima.info%{ext_info}

%files
%license COPYING GPL.txt
%doc AUTHORS README.md ChangeLog
%{_datadir}/doc/%{tarname}/
%{_bindir}/*
%{_datadir}/wxMaxima/
%{_datadir}/icons/hicolor/*/apps/io.github.wxmaxima_developers.wxMaxima.*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/wxmaxima
%{_datadir}/metainfo/*.appdata.xml
%{_mandir}/man1/wxmaxima*%{ext_man}
%{_mandir}/*/man1/wxmaxima*%{ext_man}
%{_datadir}/mime/packages/*.xml

%files lang -f %{name}.lang

%changelog
