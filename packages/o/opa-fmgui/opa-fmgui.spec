#
# spec file for package opa-fmgui
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 Intel Corporation
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


%define git_ver %{nil}
%define name opa-fmgui
%define appdir .
%define appfolder opa-fmgui
%define appjar opa-fmgui.jar
%define _binary_payload w9.gzdio
%define gradle_version	4.10.2
Name:           opa-fmgui
Version:        10.1.0.0.115
Release:        0
Summary:        Fabric Manager Graphical User Interface
License:        BSD-3-Clause AND LGPL-2.0-or-later
Group:          Productivity/Clustering/Computing
URL:            https://www.intel.com/
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        antlr-2.7.7.jar
Source2:        dom4j-1.6.1.jar
Source3:        hibernate-commons-annotations-4.0.4.Final.jar
Source4:        hibernate-core-4.3.5.Final.jar
Source5:        hibernate-entitymanager-4.3.5.Final.jar
Source6:        hibernate-jpa-2.1-api-1.0.0.Final.jar
Source7:        hsqldb-2.3.2.jar
Source8:        jandex-1.1.0.Final.jar
Source9:        javahelp-2.0.05.jar
Source10:       javassist-3.18.1-GA.jar
Source11:       javax.activation-api-1.2.0.jar
Source12:       javax.mail-1.5.2.jar
Source13:       jaxb-api-2.3.1.jar
Source14:       jboss-logging-3.1.3.GA.jar
Source15:       jboss-logging-annotations-1.2.0.Beta1.jar
Source16:       jboss-transaction-api_1.2_spec-1.0.0.Final.jar
Source17:       jcommon-1.0.21.jar
Source18:       jfreechart-1.0.17.jar
Source19:       jgraphx-3.6.0.0.jar
Source20:       jsch-0.1.53.jar
Source21:       log4j-over-slf4j-1.7.7.jar
Source22:       logback-classic-1.1.2.jar
Source23:       logback-core-1.1.2.jar
Source24:       mbassador-1.2.4.2.jar
Source25:       reload4j-1.2.20.jar
Source26:       slf4j-api-1.7.7.jar
Source27:       swingx-all-1.6.5.jar
Source28:       swingx-action-1.6.5.jar
Source29:       swingx-autocomplete-1.6.5.jar
Source30:       swingx-beaninfo-1.6.5.jar
Source31:       swingx-common-1.6.5.jar
Source32:       swingx-core-1.6.5.jar
Source33:       swingx-graphics-1.6.5.jar
Source34:       swingx-mavensupport-1.6.5.jar
Source35:       swingx-painters-1.6.5.jar
Source36:       swingx-plaf-1.6.5.jar
Patch0:         opa-fmgui-intel-manifest-license.patch
# Patch auto extracted by service
Patch1:         stl-14927-jgraphx-update.patch
Patch2:         manifest-version.patch
Patch3:         opa-fmgui-fix-build-for-JDK9-Gradle-3.2.patch
BuildRequires:  ant
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-devel >= 1.8
BuildRequires:  openssl
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wget
Requires:       jre >= 1.8
Requires:       mlocate
# BuildRequires:  gradle
BuildArch:      noarch

%description
FMGUI is the Fabric Manager Graphical User Interface.  It can be run by invoking the Bash
script fmgui.

%prep
%setup -q -n %{name}-%{version}%{git_ver}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3

%build
mkdir -p lib
cp %{_sourcedir}/*.jar lib/

pushd gritty
mkdir -p classes
javac -d classes -source 8 -target 8 -cp %{SOURCE20}:%{SOURCE25} $(find . -name \*.java | xargs)
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
  --create --file=../lib/gritty.jar -C classes .
popd

%{ant}

%install
mkdir -p %{buildroot}%{_javadir}/%{appfolder}
mkdir -p %{buildroot}%{_javadir}/%{appfolder}/lib
mkdir -p %{buildroot}%{_javadir}/%{appfolder}/help
mkdir -p %{buildroot}%{_javadir}/%{appfolder}/util
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/applications-merged
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}/%{_datadir}/doc/%{name}/
# mkdir -p %%{buildroot}/%%{_datadir}/doc/%%{name}/licenses
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor
mkdir -p  %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/desktop-directories

install -m 755 %{appdir}/%{appjar} %{buildroot}%{_javadir}/%{appfolder}

# cp %%{appdir}/LICENSE %%{buildroot}/%%{_datadir}/doc/%%{name}/
# cp  %%{appdir}/THIRD-PARTY-README %%{buildroot}/%%{_datadir}/doc/%%{name}/
# cp  %%{appdir}/Third_Party_Copyright_Notices_and_Licenses %%{buildroot}/%%{_datadir}/doc/%%{name}/
# cp  -r %%{appdir}/licenses %%{buildroot}/%%{_datadir}/doc/%%{name}/

install -m 644 -pDt %{buildroot}/%{_javadir}/%{appfolder}/lib %{appdir}/lib/*
cp -a %{appdir}/target/help/* %{buildroot}%{_javadir}/%{appfolder}/help
cp %{appdir}/help/*.html %{buildroot}%{_javadir}/%{appfolder}/help
#cp %%{appdir}/help/LICENSE %%{buildroot}%%{_javadir}/%%{appfolder}/help
install -m 755  %{appdir}/util/fmguiclear.sh %{buildroot}%{_javadir}/%{appfolder}/util
install -m 755  %{appdir}/util/postsetup.sh %{buildroot}%{_javadir}/%{appfolder}/util
cp -a %{appdir}/util/ClearFMGUICache.desktop %{buildroot}%{_javadir}/%{appfolder}/util

install -m 755 %{appdir}/install/opa-fmgui.sh %{buildroot}%{_bindir}/opa-fmgui

#for fmgui.desktop
cp -a  %{appdir}/install/fmguivars.sh %{buildroot}/%{_sysconfdir}/profile.d
cp -a %{appdir}/install/fmgui.desktop %{buildroot}
cp -a %{appdir}/install/Fabric.directory %{buildroot}%{_datadir}/desktop-directories
cp -a %{appdir}/install/images/* %{buildroot}/%{_datadir}/icons/hicolor
cp -a %{appdir}/install/Fabric.menu %{buildroot}/%{_sysconfdir}/xdg/menus/applications-merged

%suse_update_desktop_file -i fmgui Utility Filesystem

rm %{buildroot}/fmgui.desktop

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%doc README THIRD-PARTY-README Third_Party_Copyright_Notices_and_Licenses
%license LICENSE gritty/gritty_license.txt
%dir %{_sysconfdir}/xdg/menus
%dir %{_datadir}/desktop-directories
%dir %{_datadir}/doc/opa-fmgui
%dir %{_sysconfdir}/xdg/menus/applications-merged

%{_javadir}/%{appfolder}
%{_bindir}/opa-fmgui
%{_datadir}/applications/*.desktop
# %%{_datadir}/doc/%%{name}/*
%{_datadir}/desktop-directories/Fabric.directory
%{_datadir}/icons/hicolor

# %%license %%{_datadir}/doc/opa-fmgui/LICENSE
# %%license %%{_datadir}/doc/opa-fmgui/licenses/*

%config %{_sysconfdir}/xdg/menus/applications-merged/Fabric.menu
%config %{_sysconfdir}/profile.d/fmguivars.sh

%changelog
