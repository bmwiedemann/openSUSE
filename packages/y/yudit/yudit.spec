#
# spec file for package yudit
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


%define	fontdir     %{_datadir}/fonts/truetype
Name:           yudit
Version:        3.0.7
Release:        0
Summary:        Unicode text editor
License:        LGPL-2.1-or-later
Group:          Productivity/Text/Editors
URL:            https://www.yudit.org/
Source0:        http://yudit.org/download/yudit-%{version}.tar.bz2
Source1:        fonts.scale.yudit
Source2:        yudit.gif
Patch1:         yudit-properties.patch
Patch2:         yudit-setlocale.patch
Patch3:         print-preview.patch
Patch7:         yudit-strip.patch
Patch9:         uniprint-catch-bad_alloc-exceptions.patch
BuildRequires:  autoconf
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
%reconfigure_fonts_prereq
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif

%description
yudit is a unicode package to edit and convert text of different
languages.

%prep
%setup -q
%patch1 -p1 -b .properties
%patch2 -p1 -b .setlocale
%patch3 -p1 -b .print-preview
%patch7
%patch9 -p1 -b .catch-bad_alloc-exceptions
for i in doc/HOWTO-baybayin.txt COPYING.TXT README.TXT doc/HOWTO-devanagari.txt doc/bidi/yudit.css doc/HOWTO-syntax.txt doc/notinstalled/cl.help
do
    dos2unix $i
done

%build
rm -f config.cache
autoconf
export CC="g++"
export CFLAGS="%{optflags} -fPIE"
export CXXFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 gnome-yudit.png %{buildroot}%{_datadir}/pixmaps/yudit.png
mkdir -p %{buildroot}%{fontdir}
mv %{buildroot}/%{_datadir}/%{name}/fonts/yudit.ttf \
   %{buildroot}%{fontdir}
install -m 644 $RPM_SOURCE_DIR/fonts.scale.yudit \
   %{buildroot}%{fontdir}
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
cp -a C* FAQ* READM* TOD*  *BUG* %{buildroot}/%{_defaultdocdir}/%{name}
cp -a doc %{buildroot}/%{_defaultdocdir}/%{name}
%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_datadir}
%endif

%reconfigure_fonts_scriptlets

%files
%doc %{_defaultdocdir}/%{name}
%config %{_datadir}/pixmaps/yudit.png
%{_bindir}/*
%dir %{fontdir}/
%{fontdir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/config
%config %{_datadir}/%{name}/config/*
%{_datadir}/%{name}/data/
%{_datadir}/%{name}/fonts/
%{_datadir}/%{name}/src/
%{_datadir}/%{name}/doc/
%{_datadir}/%{name}/locale/
%{_datadir}/%{name}/syntax/

%changelog
