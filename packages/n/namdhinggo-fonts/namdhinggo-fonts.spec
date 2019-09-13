#
# spec file for package namdhinggo-fonts
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

%define fontname NamdhinggoSIL

Name:           namdhinggo-fonts
Version:        1.004
Release:        0
Summary:        SIL Limbu Font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=NamdhinggoSIL
Source0:        %{fontname}%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Limbu, or Kirat Sirijonga, script is used by around 400,000 people 
in Nepal and India. This Unicode-encoded font has been designed to 
support literacy and materials development in the Limbu language.

%prep
%setup -q -n %{fontname}

%build
dos2unix *.txt

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc OFL*.txt README.txt FONTLOG.txt
%{_ttfontsdir}

%changelog
