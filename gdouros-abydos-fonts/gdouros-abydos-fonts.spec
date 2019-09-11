#
# spec file for package gdouros-abydos-fonts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gdouros-abydos-fonts
Version:        1.96
Release:        0
Summary:        A data font of 7440 Egyptian hieroglyphs
License:        SUSE-Permissive
Group:          System/X11/Fonts
Url:            http://users.teilar.gr/~g1951d/
# Download URL
# http://users.teilar.gr/~g1951d/AbydosFont.zip
Source0:        AbydosFont-%{version}.zip
# Download URL
# http://users.teilar.gr/~g1951d/Abydos.pdf
Source1:        Abydos-20171217.pdf
# Download URL
# http://users.teilar.gr/~g1951d/AbydosGlyph.pdf
Source2:        AbydosGlyph-20171217.pdf
Source3:        README-SUSE
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Font containing 7440 Egyptian hieroglyphs.
Abydos is mainly based on Glyph for Windows version 2.0; it also covers
proposals for encoding Egyptian Hieroglyphs in The Unicode Standard:
  * Hans van den Berg, Eric Aubourg, “Hieroglyphic Text Processing:
    Glyph for Windows”, CCER, 2007
  * Michel Suignard, “Source analysis of an extended Egyptian
    Hieroglyphs repertoire”, L2/16-257,
  * “New draft for the encoding of an extended Egyptian Hieroglyphs
    repertoire”, L2/17-073

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description    doc
Contains pdf documentation for %{name}.

%prep
%setup -q -cT -a0

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/
# install docs
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} \
   -t .
for i in *-*.pdf; do
        IFS=-. read -r a b c <<< "$i"; mv "$i" "$a.$c"
done

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc README-SUSE
%{_ttfontsdir}

%files doc
%defattr(-,root,root)
%doc Abydos.pdf AbydosGlyph.pdf

%changelog
