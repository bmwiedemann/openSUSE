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


# LIFECYCLE values: beta pre maintained unmaintained
%define LIFECYCLE maintained
%define SUSE_PROD openSUSE
%define RELEASENOTES_DIR %{buildroot}%{_datadir}/doc/release-notes/%{SUSE_PROD}
%define INSTALL %{__install} -m 0644 -D

Name:           release-notes-openSUSE
Version:        84.87.20180228.827b030
Release:        0
Summary:        Release Notes for openSUSE
License:        GFDL-1.3
Group:          Documentation/SUSE
Url:            https://github.com/openSUSE/release-notes-openSUSE
Source:         %{name}-%{version}.tar.xz
BuildRequires:  daps
BuildRequires:  gettext-tools
BuildRequires:  itstool
BuildRequires:  suse-xsl-stylesheets
BuildRequires:  w3m
BuildRequires:  xmlcharent
BuildRequires:  xmlformat
BuildRequires:  xsltproc
BuildArch:      noarch
Provides:       release-notes = %{version}

%description
This package contains the release notes with the most important changes
for openSUSE Tumbleweed.

%prep
%autosetup

%build
make linguas
make all LIFECYCLE=%{LIFECYCLE} VERSION='%{version}'

%install
%{INSTALL} LICENSE %{RELEASENOTES_DIR}/LICENSE
for dir in build/release-notes.*; do
	lang=$(echo "$dir" | cut -d '.' -f 2)
	%{INSTALL} "${dir}/single-html/release-notes.${lang}/release-notes.${lang}.html" "%{RELEASENOTES_DIR}/RELEASE-NOTES.${lang}.html"
	%{__cp} -R "${dir}/single-html/release-notes.${lang}/static/"                    "%{RELEASENOTES_DIR}"
	%{INSTALL} "${dir}/yast-html/release-notes.${lang}.html"                         "%{RELEASENOTES_DIR}/RELEASE-NOTES.${lang}.rtf"
	%{INSTALL} "${dir}/release-notes.${lang}_${lang}.pdf"                            "%{RELEASENOTES_DIR}/RELEASE-NOTES.${lang}.pdf" ||
	%{INSTALL} "${dir}/release-notes.${lang}_color_${lang}.pdf"                      "%{RELEASENOTES_DIR}/RELEASE-NOTES.${lang}.pdf" # daps 4.x pdf output dropped the _color
	%{INSTALL} "${dir}/release-notes.${lang}.txt"                                    "%{RELEASENOTES_DIR}/RELEASE-NOTES.${lang}.txt"
done

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/release-notes/

%changelog
