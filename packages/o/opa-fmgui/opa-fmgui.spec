#
# spec file for package opa-fmgui
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
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
Url:            http://www.intel.com/
Source0:        %{name}-%{version}%{git_ver}.tar.gz
Source1:        antlr-2.7.7.jar
Source2:        dom4j-1.6.1.jar
# Source3:        gritty.jar
Source4:        hibernate-commons-annotations-4.0.4.Final.jar
Source5:        hibernate-core-4.3.5.Final.jar
Source6:        hibernate-entitymanager-4.3.5.Final.jar
Source7:        hibernate-jpa-2.1-api-1.0.0.Final.jar
Source8:        hsqldb-2.3.2.jar
Source9:        jandex-1.1.0.Final.jar
Source10:       javahelp-2.0.05.jar
Source11:       javassist-3.18.1-GA.jar
Source12:       javax.mail-1.5.2.jar
Source13:       jboss-logging-3.1.3.GA.jar
Source14:       jboss-logging-annotations-1.2.0.Beta1.jar
Source15:       jboss-transaction-api_1.2_spec-1.0.0.Final.jar
Source16:       jcommon-1.0.21.jar
Source17:       jfreechart-1.0.17.jar
Source18:       jgraphx-3.6.0.0.jar
Source19:       jsch-0.1.53.jar
Source20:       log4j-1.2.14.jar
Source21:       log4j-over-slf4j-1.7.7.jar
Source22:       logback-classic-1.1.2.jar
Source23:       logback-core-1.1.2.jar
Source24:       mbassador-1.2.4.2.jar
Source25:       slf4j-api-1.7.7.jar
Source26:       swingx-all-1.6.5.jar
Source27:       swingx-action-1.6.5.jar
Source28:       swingx-autocomplete-1.6.5.jar
Source29:       swingx-beaninfo-1.6.5.jar
Source30:       swingx-common-1.6.5.jar
Source31:       swingx-core-1.6.5.jar
Source32:       swingx-graphics-1.6.5.jar
Source33:       swingx-mavensupport-1.6.5.jar
Source34:       swingx-painters-1.6.5.jar
Source35:       swingx-plaf-1.6.5.jar
Source36:       swingx-testsupport-1.6.5.jar
Source37:       gradle-%{gradle_version}-bin.zip

Patch1:         gradle-use_local_repo.patch
Patch3:         opa-fmgui-intel-manifest-license.patch
# Patch auto extracted by service
Patch5:         stl-14927-jgraphx-update.patch
Patch6:         manifest-version.patch
Patch7:         opa-fmgui-fix-build-for-JDK9-Gradle-3.2.patch
Patch8:         opa-fmgui-force-loading-java.xml.bind-for-JDK9.patch

BuildRequires:  ant
BuildRequires:  jre >= 1.7
Requires:       jre >= 1.7
Requires:       mlocate
BuildRequires:  hicolor-icon-theme
BuildRequires:  openssl
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wget
# BuildRequires:  gradle
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
FMGUI is the Fabric Manager Graphical User Interface.  It can be run by invoking the Bash
script fmgui.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch1 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7
%patch8

%build
(cd %{_tmppath}; rm -Rf gradle-%{gradle_version}; unzip %{_sourcedir}/gradle-%{gradle_version}-bin.zip)
GRADLE_LIB_DIR=%{_sourcedir}
export GRADLE_LIB_DIR
%{_tmppath}/gradle-%{gradle_version}/bin/gradle copyDeps buildOPA --info

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
%defattr(-,root,root,-)
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
