#
# spec file for package google-inconsolata-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define  fontname   inconsolata

Name:           google-inconsolata-fonts
Version:        1.014
Release:        0
License:        OFL-1.1
Summary:        Monospace Font Designed for Printed Code Listings
Url:            http://code.google.com/webfonts/family?family=Inconsolata
Group:          System/X11/Fonts
Source0:        %{fontname}.tar.bz2
BuildRequires:	fontpackages-devel
BuildRequires:  bzip2
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Inconsolata Bold is a Unicode typeface family that supports
languages that use the Latin script and its variants, and
could be expanded to support other scripts.

Designer: Raph Levien

%prep
%setup -n %{fontname} 
# Remove DOS line endings:
sed -i 's/.$//' OFL.txt

%build
# -- Nothing to do --


%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc *.txt
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*

%changelog
