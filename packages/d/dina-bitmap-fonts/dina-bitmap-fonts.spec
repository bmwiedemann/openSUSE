#
# spec file for package dina-bitmap-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define _miscfontsdir %{_datadir}/fonts/misc
%define fontname Dina

Name:           dina-bitmap-fonts
Version:        2.92.0
Release:        0
Summary:        Dina Programming Font
License:        MIT
Group:          System/X11/Fonts
Url:            http://www.donationcoder.com/Software/Jibz/Dina
Source:         %{fontname}-%{version}.tar.xz
BuildRequires:  bdftopcf
BuildRequires:  fontpackages-devel
BuildRequires:  tar
BuildRequires:  xz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{reconfigure_fonts_prereq}

%description
Dina is a monospace bitmap font, primarily aimed at programmers.
It is relatively compact to allow a lot of code on screen,
while (hopefully) clear enough to remain readable even at high resolutions.

%prep
%setup -q -n %{fontname}-%{version}

%build
sed -i 's/microsoft-cp1252/ISO8859-1/' BDF/*.bdf
_ex_pt() {
    _pt=${1%.bdf}
    _pt=${_pt#*-}
    echo $_pt
}

for i in BDF/Dina_i400-*.bdf; do
    bdftopcf -t -o BDF/DinaItalic$(_ex_pt $i).pcf $i
done
for i in BDF/Dina_i700-*.bdf; do
    bdftopcf -t -o BDF/DinaBoldItalic$(_ex_pt $i).pcf $i
done
for i in BDF/Dina_r400-*.bdf; do
    bdftopcf -t -o BDF/DinaMedium$(_ex_pt $i).pcf $i
done
for i in BDF/Dina_r700-*.bdf; do
    bdftopcf -t -o BDF/DinaBold$(_ex_pt $i).pcf $i
done
gzip -n9 BDF/*.pcf

%install
%{__install} -m0755 -d %{buildroot}%{_miscfontsdir}
%{__install} -m0644 BDF/*.pcf.gz %{buildroot}%{_miscfontsdir}/
%{reconfigure_fonts_scriptlets}

%files
%defattr(-, root, root)
%doc LICENSE NEWS README.md
%dir %{_miscfontsdir}
%{_miscfontsdir}/%{fontname}*.pcf.gz

%changelog
