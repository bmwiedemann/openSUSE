#
# spec file for package stix-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define fontconf 61-stix

Name:           stix-fonts
Version:        1.1.0
Release:        0
%define archivename STIXv%{version}
Summary:        STIX scientific and engineering fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.stixfonts.org/
Source0:        %{archivename}.tar.bz2
Source1:        %{name}-License.txt
Source2:        %{fontconf}.conf
Source3:        %{fontconf}-pua.conf
Source4:        %{fontconf}-integrals.conf
Source5:        %{fontconf}-sizes.conf
Source6:        %{fontconf}-variants.conf
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
Requires:       fontconfig
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The mission of the Scientific and Technical Information Exchange (STIX) font
creation project is the preparation of a comprehensive set of fonts that serve
the scientific and engineering community in the process from manuscript
creation through final publication, both in electronic and print formats.

This package includes base Unicode fonts containing most glyphs for standard
use.

%package -n stix-pua-fonts
Summary:        STIX scientific and engineering fonts, PUA glyphs
Group:          System/X11/Fonts
Requires:       %{name} = %{version}
%reconfigure_fonts_prereq

%description -n stix-pua-fonts
This package includes fonts containing glyphs called out from the Unicode
Private Use Area (PUA) range. Glyphs in this range do not have an official
Unicode codepoint. They're generally accessible only through specialised
software. Text using them will break if they're ever accepted by the Unicode
Consortium and moved to an official codepoint.

%package -n stix-integrals-fonts
Summary:        STIX scientific and engineering fonts, additional integral glyphs
Group:          System/X11/Fonts
Requires:       %{name} = %{version}
%reconfigure_fonts_prereq

%description -n stix-integrals-fonts
This package includes fonts containing additional integrals of various size
and slant.

%package -n stix-sizes-fonts
Summary:        STIX scientific and engineering fonts, additional glyph sizes
Group:          System/X11/Fonts
Requires:       %{name} = %{version}
%reconfigure_fonts_prereq

%description -n stix-sizes-fonts
This package includes fonts containing glyphs in additional sizes (Mostly
"fence" and "piece" glyphs).

%package -n stix-variants-fonts
Summary:        STIX scientific and engineering fonts, additional glyph variants
Group:          System/X11/Fonts
Requires:       %{name} = %{version}
%reconfigure_fonts_prereq

%description -n stix-variants-fonts
This package includes fonts containing alternative variants of some glyphs.

%prep
%setup -q -n %{archivename}
install -m 0644 -p %{SOURCE1} License.txt
for txt in *.txt ; do
   fold -s $txt > $txt.new
   sed -i 's/\r//' $txt.new
   touch -r $txt $txt.new
   mv $txt.new $txt
done

%build

%install
install -m 0755 -d %{buildroot}%{_ttfontsdir}
install -m 0644 -p Fonts/STIX-General/*.otf %{buildroot}%{_ttfontsdir}
install -m 0755 -d %{buildroot}%{_docdir}/%{name}/
install -m 0644 License.txt %{buildroot}%{_docdir}/%{name}
#
%install_fontsconf %{SOURCE2}
%install_fontsconf %{SOURCE3}
%install_fontsconf %{SOURCE4}
%install_fontsconf %{SOURCE5}
%install_fontsconf %{SOURCE6}

%reconfigure_fonts_scriptlets

%reconfigure_fonts_scriptlets -n stix-pua-fonts

%reconfigure_fonts_scriptlets -n stix-integrals-fonts

%reconfigure_fonts_scriptlets -n stix-sizes-fonts

%reconfigure_fonts_scriptlets -n stix-variants-fonts

%files
%defattr(-, root, root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/STIXGeneral*.otf
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/License.txt
%files_fontsconf_availdir
%files_fontsconf_file -l %{fontconf}.conf

%files -n stix-pua-fonts
%defattr(-, root, root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/STIXNonUni*.otf
%files_fontsconf_file -l %{fontconf}-pua.conf

%files -n stix-integrals-fonts
%defattr(-, root, root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/STIXInt*.otf
%files_fontsconf_file -l %{fontconf}-integrals.conf

%files -n stix-sizes-fonts
%defattr(-, root, root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/STIXSiz*.otf
%files_fontsconf_file -l %{fontconf}-sizes.conf

%files -n stix-variants-fonts
%defattr(-, root, root)
%dir %{_ttfontsdir}
%{_ttfontsdir}/STIXVar*.otf
%files_fontsconf_file -l %{fontconf}-variants.conf

%changelog
