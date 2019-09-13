#
# spec file for package google-roboto-fonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define slab    robotoslab-fonts-20130925
%define docs    roboto-doc-20160623
%define font_version  2.135

Name:           google-roboto-fonts
Version:        20161103.%{font_version}
Release:        0
Summary:        Mechanical yet friendly fonts
License:        Apache-2.0
Group:          System/X11/Fonts
Url:            https://material.google.com/style/typography.html
Source0:        https://github.com/google/roboto/releases/download/v%{font_version}/roboto-unhinted.zip
Source1:        %{slab}.tar.bz2
# Docs manually assembled from Github and https://material.google.com/resources/roboto-noto-fonts.html
Source2:        %{docs}.tar.bz2
Source3:        google-roboto-slab.metainfo.xml
Source4:        google-roboto.metainfo.xml
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Material Design language relies on traditional typographic tools
such as scale, space, rhythm, and alignment with an underlying grid.
Successful deployment of these tools is essential to help users quickly
understand a screen of information.

To support such use of typography, Android 4.0 (Ice Cream Sandwich)
introduced a new type family named Roboto, created specifically for
the requirements of UI and high-resolution screens.

This package contains the original Roboto sans-serif font, a condensed
version of the sans-serif version, and a newer slab-serif version.

Designer: Christian Robertson


%prep
unzip -j -o %{S:0}
tar -xjvf %{S:1} --strip=1 %{slab}
tar -xjvf %{S:2} --strip=1 %{docs}

%build
# --- Nothing to do ---

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{S:3} %{S:4} %{buildroot}%{_datadir}/appdata

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.md *.pdf *.txt
%{_datadir}/appdata
%{_ttfontsdir}

%changelog
