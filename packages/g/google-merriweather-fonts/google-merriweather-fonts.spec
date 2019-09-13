#
# spec file for package google-merriweather-fonts
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


%define fontname merriweather

Name:           google-merriweather-fonts
Version:        2.001
Release:        0
Summary:        Readable Text Serif Font for Screen
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.google.com/webfonts/specimen/Merriweather
Source0:        %{fontname}-%{version}.tar.bz2
Source1:        OFL.txt
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Merriweather was designed to be a text face that is pleasant to read on screens.

Merriweather is an evolving and will be updated.
As of now there are 4 styles: Regular, Light, Bold, and Black. There will also
be Italic in each of these weights.
And fairly soon after that there will also be a sans serif version which mirrors
the weights and styles of the Serif design.

Designed by Eben Sorkin, Merriweather features a very large x height, slightly
condensed letterforms, a mild diagonal stress, sturdy serifs and open forms.

Because Merriweather is a work in progress and will be improved regularly.
This means you can request improvements
and even fund specific features if if they are outside of the current scope of work.
For more information and to stay updated see Eben Sorkin's blog and Flickr stream and
the Merriweather Twitter microblog.

Designer: Eben Sorkin

%prep
%setup -n %{fontname}-%{version}

%build
cp %{SOURCE1} .

%install
mkdir -p  %{buildroot}%{_ttfontsdir}
cp *.ttf  %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root, root)
%doc AUTHORS.txt FONTLOG.txt CONTRIBUTORS.txt README.md OFL.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
