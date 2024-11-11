#
# spec file for package MozillaFirefox-branding-openSUSE
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2008-2024 Wolfgang Rosenauer
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define pkgname @BUILD_FLAVOR@

%if "%{pkgname}" == "MozillaFirefox-branding-openSUSE"
%define targetpkg MozillaFirefox
%define progdir %{_libdir}/firefox
%define appname Firefox
%else
%if "%{pkgname}" == "firefox-esr-branding-openSUSE"
%define targetpkg firefox-esr
%define progdir %{_libdir}/firefox-esr
%define appname Firefox ESR
%else
%define pkgname MozillaFirefox-branding-openSUSE
ExclusiveArch:  do-not-build
%endif
%endif

Name:           %{pkgname}
BuildRequires:  bc
BuildRequires:  unzip
BuildRequires:  zip
Version:        68
Release:        0
Summary:        openSUSE branding of MozillaFirefox
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            http://www.opensuse.org
Source:         susefox-20120626.tar.bz2
Source1:        opensuse-software.xml.in
Source2:        all-openSUSE.js
Source3:        firefox-suse-default-prefs.js
Source4:        firefox.schemas
Source5:        distribution.ini.in
Source6:        MozillaFirefox-branding-openSUSE-COPYING
Supplements:    packageand(%{targetpkg}:branding-openSUSE)
Provides:       %{targetpkg}-branding = %{version}
Conflicts:      otherproviders(%{targetpkg}-branding)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%global libgssapi  libgssapi_krb5.so.2

%global suseversion undefined
%if %suse_version == 1315
  # Leap 42
  %if %sle_version == 120100
    %global suseversion 42.1
  %else
    %if %sle_version == 120200
      %global suseversion 42.2
    %else
      %if %sle_version == 120300
        %global suseversion 42.3
      %endif
    %endif
  %endif
%endif
%if %suse_version == 1500
  # Leap 15
  %if %sle_version == 150000
    %global suseversion 15.0
  %else
    %if %sle_version == 150100
      %global suseversion 15.1
    %else
      %if %sle_version == 150200
        %global suseversion 15.2
      %else
        %if %sle_version == 150300
          %global suseversion 15.3
        %else
          %if %sle_version == 150400
            %global suseversion 15.4
          %else
            %if %sle_version == 150500
              %global suseversion 15.5
            %endif
          %endif
        %endif
      %endif
    %endif
  %endif
%endif

%if %suse_version >= 1550
  # Tumbleweed
  %global suseversion Tumbleweed
%endif

# Leap or not
%if 0%{?sle_version}
  %global prjname Leap:%{suseversion}
  %global distname openSUSE Leap
%else
  %global prjname %{suseversion}
  %global distname openSUSE
%endif

%global homepage      https://search.opensuse.org/
%global susefox       0
%global susefox_guid  {ec8030f7-c20a-464f-9b0e-13a3a9e97384}

%description
This package provides openSUSE look and feel for Firefox.

%prep
cp -a %{SOURCE6} COPYING
%if %susefox
%setup -n susefox -q
mv COPYING COPYING.susefox
%endif

%build
%if %susefox
./build.sh
%endif

%install
# apply SUSE defaults
sed -e 's,GSSAPI,%{libgssapi},g' \
    %{SOURCE3} > firefox-openSUSE.js

install -d %{buildroot}%{progdir}/browser/defaults/preferences/
install -m 0644 firefox-openSUSE.js %{buildroot}%{progdir}/browser/defaults/preferences/

install -d %{buildroot}%{progdir}/defaults/pref/
install -m 0644 %{SOURCE2} %{buildroot}%{progdir}/defaults/pref/

# distribution.ini -- openSUSE bookmarks, homepage and Mozilla partner info
sed -e 's,%%VERSION%%,%{suseversion},g
s,%%HOMEPAGE%%,%{homepage},g
s,%%FLAVOR%%,%{appname},g
s,%%DIST%%,%{distname},g' \
    %{SOURCE5} > distribution.ini

install -d %{buildroot}%{progdir}/distribution/
install -m 0644 distribution.ini %{buildroot}%{progdir}/distribution/

# openSUSE software search plugin
sed -e 's,%%PRJNAME%%,%{prjname},g' \
    %{SOURCE1} > opensuse-software.xml

install -d %{buildroot}%{progdir}/distribution/searchplugins/common/
install -m 0644 opensuse-software.xml %{buildroot}%{progdir}/distribution/searchplugins/common/

%if %susefox
# install the system extension
unzip -u susefox\@opensuse.org ../susefox.xpi
mkdir -p %{buildroot}%{_datadir}/mozilla/extensions/%{susefox_guid}/
cp -r susefox\@opensuse.org \
    %{buildroot}%{_datadir}/mozilla/extensions/%{susefox_guid}/
%endif

%files
%defattr(-,root,root)
%if %susefox
%license COPYING.susefox
%license ../COPYING
%{_datadir}/mozilla
%endif
%{progdir}

%changelog
