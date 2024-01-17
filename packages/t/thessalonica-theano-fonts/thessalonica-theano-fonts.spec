#
# spec file for package thessalonica-theano-fonts
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


Name:           thessalonica-theano-fonts
Version:        2.0
Release:        0
Summary:        Theano Classical Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.thessalonica.org.ru/en/theano.html
Source0:        http://thessalonica.org.ru/downloads/theano-%{version}.otf.zip
Source1:        http://thessalonica.org.ru/downloads/theano-%{version}.ttf.zip
Source2:        http://www.thessalonica.org.ru/downloads/theano-specimen.pdf
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Theano Classical Fonts include three fonts listed below. Each font is
currently available just in one weight/shape (regular) and contains
Latin, Greek and Cyrillic letters.

Theano Didot.
A classicist face, with both its Roman and Greek parts implemented in
Didot style. Unlike Old Standard, this font is designed from French
sources.

Theano Modern.
A font with Greek letters designed in the Porsonic style. Unlike most
modern implementation, it is based on Figgins Pica No. 3 / Small Pica
No. 2 — probably the most successful and once the most popular Greek
face of a Porsonic origin — rather than on later Monotype's design.
The accompanying Latin font is implemented in the Modern style and
modelled after English Modern faces of later 19th century, often used
alonglide with Porsonic Greek types.

Theano Old Style.
A modernized "Old Style" Greek font with a large number of historic
ligatures and alternate forms, modelled after some early 19th century
types designed by Figgins' type foundry. It is accompanied by a Latin
face based on some "Old Style" Roman fonts of the late 19th and early
20th century.

%package -n thessalonica-theano-otf-fonts
Summary:        Theano Classical Fonts (OpenType Format)
Group:          System/X11/Fonts
Provides:       theano-fonts-otf = %{version}
Provides:       locale(el;ru)
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      theano-fonts-otf <= 2.0

%description -n thessalonica-theano-otf-fonts
Theano Classical Fonts include three fonts listed below. Each font is
currently available just in one weight/shape (regular) and contains
Latin, Greek and Cyrillic letters.

Theano Didot.
A classicist face, with both its Roman and Greek parts implemented in
Didot style. Unlike Old Standard, this font is designed from French
sources.

Theano Modern.
A font with Greek letters designed in the Porsonic style. Unlike most
modern implementation, it is based on Figgins Pica No. 3 / Small Pica
No. 2 — probably the most successful and once the most popular Greek
face of a Porsonic origin — rather than on later Monotype's design.
The accompanying Latin font is implemented in the Modern style and
modelled after English Modern faces of later 19th century, often used
alonglide with Porsonic Greek types.

Theano Old Style.
A modernized "Old Style" Greek font with a large number of historic
ligatures and alternate forms, modelled after some early 19th century
types designed by Figgins' type foundry. It is accompanied by a Latin
face based on some "Old Style" Roman fonts of the late 19th and early
20th century.

This package contains fonts in OpenType format.

%package -n thessalonica-theano-ttf-fonts
Summary:        Theano Classical Fonts (TrueType Format)
Group:          System/X11/Fonts
Provides:       theano-fonts-ttf = %{version}
# FIXME: This causes a rpmlint warning; change "<=" to "<" once there's
# a new upstream version.
Obsoletes:      theano-fonts-ttf <= 2.0

%description -n thessalonica-theano-ttf-fonts
Theano Classical Fonts include three fonts listed below. Each font is
currently available just in one weight/shape (regular) and contains
Latin, Greek and Cyrillic letters.

Theano Didot.
A classicist face, with both its Roman and Greek parts implemented in
Didot style. Unlike Old Standard, this font is designed from French
sources.

Theano Modern.
A font with Greek letters designed in the Porsonic style. Unlike most
modern implementation, it is based on Figgins Pica No. 3 / Small Pica
No. 2 — probably the most successful and once the most popular Greek
face of a Porsonic origin — rather than on later Monotype's design.
The accompanying Latin font is implemented in the Modern style and
modelled after English Modern faces of later 19th century, often used
alonglide with Porsonic Greek types.

Theano Old Style.
A modernized "Old Style" Greek font with a large number of historic
ligatures and alternate forms, modelled after some early 19th century
types designed by Figgins' type foundry. It is accompanied by a Latin
face based on some "Old Style" Roman fonts of the late 19th and early
20th century.

This package contains fonts in TrueType format.

%prep
%setup -cqn %{name}-%{version}
unzip -oq %{SOURCE1}
cp %{SOURCE2} .
sed -i 's/\r$//g' OFL-FAQ.txt

%build

%install
install -dm 0755 %{buildroot}%{_ttfontsdir}
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets -n thessalonica-theano-otf-fonts

%reconfigure_fonts_scriptlets -n thessalonica-theano-ttf-fonts

%files -n thessalonica-theano-otf-fonts
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt theano-specimen.pdf
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%files -n thessalonica-theano-ttf-fonts
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt OFL-FAQ.txt theano-specimen.pdf
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
