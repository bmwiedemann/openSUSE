#
# spec file for package release-notes-openSUSE
#
# Copyright (c) 2014-2018, SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           release-notes-openSUSE
Version:        84.87.20180228.827b030
Release:        0
Summary:        Release Notes for openSUSE
License:        GFDL-1.3
Group:          Documentation/SUSE
Url:            https://github.com/openSUSE/release-notes-openSUSE
BuildRequires:  daps
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  xmlformat
BuildRequires:  w3m
BuildRequires:  gettext-tools
BuildRequires:  itstool
BuildRequires:  xmlcharent
BuildRequires:  xsltproc
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       release-notes = %{version}
Source:         %{name}-%{version}.tar.xz

%description
This package contains the release notes with the most important changes
for openSUSE Tumbleweed.

%prep
%setup -q

%build
%define SUSE_PROD openSUSE
make linguas
# values for LIFECYCLE: beta pre maintained unmaintained
make all LIFECYCLE=maintained VERSION='%{version}'

%install
rnpath=%{buildroot}%{_datadir}/doc/release-notes/%{SUSE_PROD}
%{__install} -m 0644 -D LICENSE ${rnpath}/LICENSE
for file in build/release-notes.*; do
	lang=$(echo "$file" | awk -F '.' '{print $2}')
	%{__install} -m 0644 -D "${file}/single-html/release-notes.${lang}/release-notes.${lang}.html" "${rnpath}/RELEASE-NOTES.${lang}.html"
	%{__cp} -R "${file}/single-html/release-notes.${lang}/static/" "${rnpath}"
	%{__install} -m 0644 -D "${file}/yast-html/release-notes.${lang}.html" "${rnpath}/RELEASE-NOTES.${lang}.rtf"
	%{__install} -m 0644 -D "${file}/release-notes.${lang}_color_$lang.pdf" "${rnpath}/RELEASE-NOTES.${lang}.pdf"
	%{__install} -m 0644 -D "${file}/release-notes.${lang}.txt" "${rnpath}/RELEASE-NOTES.${lang}.txt"
done

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/release-notes/

%changelog
