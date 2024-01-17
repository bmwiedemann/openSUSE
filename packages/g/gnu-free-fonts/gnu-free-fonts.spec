#
# spec file for package gnu-free-fonts
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


%define fontname freefont
%define fontversion 20120503
%define _ttfontsdir %{_datadir}/fonts/truetype
Name:           gnu-free-fonts
Version:        0.%{fontversion}
Release:        0
Summary:        Free UCS Outline Fonts
License:        SUSE-GPL-3.0+-with-font-exception
Group:          System/X11/Fonts
Url:            http://savannah.nongnu.org/projects/freefont/
Source0:        http://ftp.gnu.org/gnu/freefont/%{fontname}-src-%{fontversion}.tar.gz
Source10:       remove-kana-glyphs
Source11:       GenerateTrueType
# PATCH-FIX-UPSTREAM -- bmwiedemann fix build-compare https://savannah.gnu.org/bugs/index.php?47722
Patch0:         reproducible.patch
Patch1:         freefont-build-using-py3.patch
# PATCH-FIX-UPSTREAM -- https://savannah.gnu.org/bugs/index.php?47634
Patch2:         make_ff_version_check_forward_compatible.patch
BuildRequires:  fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires:  python3-base
# freefont was last used at openSUSE 12.1 (version 0.20110523)
Obsoletes:      %{fontname} < %{version}
Provides:       %{fontname} = %{version}
Provides:       scalable-font-bg
Provides:       scalable-font-el
Provides:       scalable-font-he
Provides:       scalable-font-ru
Provides:       locale(bg;el;he;ru;vi)
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A set of free outline (OpenType, for example) fonts covering the ISO
10646/Unicode UCS (Universal Character Set). The set consists of three
typefaces: one monospaced and two proportional (one with uniform and
one with modulated stroke).

%prep
%setup -q -n %{fontname}-%{fontversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
chmod 755 $RPM_SOURCE_DIR/remove-kana-glyphs
$RPM_SOURCE_DIR/remove-kana-glyphs ./sfd/*.sfd
make %{?_smp_mflags} ttf

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -pm 0644 sfd/*.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%license COPYING
%doc AUTHORS CREDITS ChangeLog README notes/troubleshooting.txt notes/usage.txt
%{_ttfontsdir}

%changelog
