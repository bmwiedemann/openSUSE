#
# spec file for package kopano-webapp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Kopano B.V.
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


%define langdir %{_datadir}/%{name}/server/language
%define plugindir %{_datadir}/%{name}/plugins
Name:           kopano-webapp
Version:        3.5.4
Release:        0
Summary:        Improved WebApp for Kopano
License:        AGPL-3.0-only
Group:          Productivity/Networking/Email/Clients
Url:            https://kopano.io
Source:         kopano-webapp-%{version}.tar.xz
BuildRequires:  ant
BuildRequires:  xz
Requires:       %{name}-lang = %{version}
Requires:       mod_php_any
Requires:       php >= 5.3
Requires:       php-gettext
Requires:       php-mapi
Requires:       php-openssl
Requires:       php-zlib
Suggests:       php-opcache
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
%if 0%{?suse_version} >= 1220
BuildRequires:  libxml2-tools
%else
BuildRequires:  libxml2
%endif

%description
Provides a web-client written in PHP that makes use of Jason and ExtJS
to allow users to make full use of the Kopano platform
through a modern web browser.

%package lang
# FIXME: consider using %%lang_package macro
Summary:        Languages for package %{name}
Group:          System/Localization

%description lang
Provides translations to the package %{name}.

%package contactfax
Version:        3.5.4
Release:        0
Summary:        Contact fax plugin for kopano-webapp
Group:          Productivity/Networking/Email/Clients

%description contactfax
Opens a new "create mail" dialog with contact's fax number in the To:
field of the email.

%package folderwidgets
Version:        3.5.4
Release:        0
Summary:        Folder widgets plugin for kopano-webapp
Group:          Productivity/Networking/Email/Clients

%description folderwidgets
A collection of widgets which can show the contents of some of the
default folders for a user.

%package gmaps
Version:        3.5.4
Release:        0
Summary:        Google Maps plugin for kopano-webapp
Group:          Productivity/Networking/Email/Clients

%description gmaps
Shows contact address on Google Maps.

%package pimfolder
Version:        3.5.4
Release:        0
Summary:        Plugin for kopano-webapp to quickly move mail into another folder
Group:          Productivity/Networking/Email/Clients

%description pimfolder
Kopano PIM plugin, allows you to set-up a folder quickly moving your mail to another folder; like "Archive" in GTD

%package quickitems
Version:        3.5.4
Release:        0
Summary:        Quick Items plugin for kopano-webapp
Group:          Productivity/Networking/Email/Clients

%description quickitems
Special widgets for easily creating new Mails, Appointments, Contacts,
Tasks and Notes.

%package titlecounter
Version:        3.5.4
Release:        0
Summary:        Title counter plugin for kopano-webapp
Group:          Productivity/Networking/Email/Clients

%description titlecounter
Plugin to show number of unread messages in the window title.

%package webappmanual
Version:        3.5.4
Release:        0
Summary:        Manual plugin for kopano-webapp
Group:          Productivity/Networking/Email/Clients

%description webappmanual
Plugin with manual for Kopano WebApp

%package zdeveloper
Version:        3.5.4
Release:        0
Summary:        Developer plugin for kopano-webapp
Group:          Development/Tools/Debuggers

%description zdeveloper
Shows all available insertion points on the screen.

%prep
%setup -q
find . -type f "(" -name "*.js" -o -name "*.php" ")" \
	-exec chmod a-x "{}" "+";
echo "%{version}" > version

%build
ant deploy deploy-plugins;

%install
b="%{buildroot}";
d="$b/%{_datadir}";
mkdir -p "$d";
cp -a deploy "$d/%{name}";
mkdir -p "$b/%{_sysconfdir}/apache2/conf.d"
mv "$d/%{name}/kopano-webapp.conf" "$b/%{_sysconfdir}/apache2/conf.d"
mkdir -p "$b/%{_sysconfdir}/kopano/webapp"
mv "$d/%{name}/config.php.dist" "$b/%{_sysconfdir}/kopano/webapp/config.php"
ln -s "%{_sysconfdir}/kopano/webapp/config.php" \
	"$d/%{name}/config.php"
rm "$d/%{name}/debug.php.dist"
mkdir -p "$b%{_localstatedir}/lib/%{name}/tmp"
%if 0%{?fdupes:1}
%fdupes %{buildroot}/%{_prefix}
%endif

%files
%defattr(-,root,root)
%{_datadir}/%{name}
%exclude %{plugindir}/*
%exclude %{langdir}
%dir %{_sysconfdir}/kopano
%dir %{_sysconfdir}/kopano/webapp
%config(noreplace) %{_sysconfdir}/kopano/webapp/config.php
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d
%config(noreplace) %{_sysconfdir}/apache2/conf.d/kopano-webapp.conf
%dir %{_localstatedir}/lib/kopano-webapp
%dir %attr(0775, wwwrun, www) %{_localstatedir}/lib/kopano-webapp/tmp

%files lang
%defattr(-,root,root)
%dir %{langdir}
#lang(bg_BG) %langdir/bg_BG.UTF-8
%lang(ca_ES) %{langdir}/ca_ES.UTF-8
%lang(cs_CZ) %{langdir}/cs_CZ.UTF-8
%lang(da_DK) %{langdir}/da_DK.UTF-8
%lang(de_DE) %{langdir}/de_DE.UTF-8
%lang(el_GR) %{langdir}/el_GR.UTF-8
%lang(en_US) %{langdir}/en_US.UTF-8
%lang(es_CA) %{langdir}/es_CA.UTF-8
%lang(es_ES) %{langdir}/es_ES.UTF-8
%lang(et_EE) %{langdir}/et_EE.UTF-8
%lang(fa_IR) %{langdir}/fa_IR.UTF-8
%lang(fi_FI) %{langdir}/fi_FI.UTF-8
%lang(fr_FR) %{langdir}/fr_FR.UTF-8
%lang(gl_ES) %{langdir}/gl_ES.UTF-8
%lang(he_IL) %{langdir}/he_IL.UTF-8
%lang(hr_HR) %{langdir}/hr_HR.UTF-8
%lang(hu_HU) %{langdir}/hu_HU.UTF-8
%lang(it_IT) %{langdir}/it_IT.UTF-8
%lang(ja_JP) %{langdir}/ja_JP.UTF-8
%lang(ko_KR) %{langdir}/ko_KR.UTF-8
%lang(lt_LT) %{langdir}/lt_LT.UTF-8
%lang(nb_NO) %{langdir}/nb_NO.UTF-8
%lang(nl_NL) %{langdir}/nl_NL.UTF-8
%lang(pl_PL) %{langdir}/pl_PL.UTF-8
%lang(pt_BR) %{langdir}/pt_BR.UTF-8
%lang(pt_PT) %{langdir}/pt_PT.UTF-8
%lang(ru_RU) %{langdir}/ru_RU.UTF-8
%lang(sl_SI) %{langdir}/sl_SI.UTF-8
%lang(sv_SE) %{langdir}/sv_SE.UTF-8
%lang(tr_TR) %{langdir}/tr_TR.UTF-8
%lang(uk_UA) %{langdir}/uk_UA.UTF-8
%lang(zh_CN) %{langdir}/zh_CN.UTF-8
%lang(zh_TW) %{langdir}/zh_TW.UTF-8

%files contactfax
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/contactfax

%files folderwidgets
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/folderwidgets

%files gmaps
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/gmaps

%files pimfolder
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/pimfolder

%files quickitems
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/quickitems

%files titlecounter
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/titlecounter

%files webappmanual
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/webappmanual

%files zdeveloper
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{plugindir}
%{plugindir}/zdeveloper

%changelog
