#
# spec file for package yast2-metapackage-handler
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-metapackage-handler
Version:        4.1.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

# should be required by devtools
BuildRequires:  perl-XML-Writer
BuildRequires:  pkgconfig
# y2tool
BuildRequires:  yast2-devtools >= 3.1.10
# ycpc
BuildRequires:  yast2-core
# we have a Perl part
BuildRequires:  perl-XML-XPath
BuildRequires:  yast2
BuildRequires:  yast2-country-data
BuildRequires:  yast2-packager
BuildRequires:  yast2-perl-bindings
BuildRequires:  yast2-transfer
# desktop files
BuildRequires:  update-desktop-files

Patch0:         SLE.diff
Patch1:         103.diff

Requires:       perl-XML-XPath
Requires:       yast2
Requires:       yast2-packager
Requires:       yast2-perl-bindings
Requires:       yast2-transfer
# Language
Requires:       yast2-country-data
# needed at runtime for invoking root mode
Requires:       /usr/bin/xdg-su

BuildArch:      noarch

Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        YaST2 - Easy Installation of Add-on RPMs using Metapackages
License:        GPL-2.0-or-later
Group:          System/YaST

%description
With this technology users can install packages and add repositories
with a simple click on a link in a website.

%prep
%setup -n %{name}-%{version}

%if %suse_version <= 1020
%patch0
%endif

%if %suse_version <= 1030
%patch1
%endif

%build
%yast_build

%install
%yast_install

%if %suse_version <= 1020
mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/applnk/.hidden/
mkdir -p $RPM_BUILD_ROOT/opt/kde3/share/mimelnk/text/
chmod -R 0755 $RPM_BUILD_ROOT/opt/kde3
install -m 0644 src/kdeymp.desktop \
	$RPM_BUILD_ROOT/opt/kde3/share/applnk/.hidden/
install -m 0644 src/x-suse-ymp.desktop \
	$RPM_BUILD_ROOT/opt/kde3/share/mimelnk/text/
%endif
%suse_update_desktop_file yast2-metapackage-handler 
%suse_update_desktop_file yast2-metapackage-handler-ymu

%post
# #330352, SuSEconfig.desktop-file-utils only calls
# update-desktop-database
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%postun
if test -x usr/bin/update-mime-database ; then
  usr/bin/update-mime-database usr/share/mime >/dev/null
fi

%files
%defattr(-,root,root)
%doc %{yast_docdir}
/sbin/OneClickInstallUI
/sbin/OneClickInstallUrlHandler
/sbin/OneClickInstallCLI
/sbin/OCICLI
%{_sbindir}/OneClickInstallUI
%{_sbindir}/OneClickInstallUrlHandler
%{_sbindir}/OneClickInstallCLI
%{_sbindir}/OCICLI

%dir %{yast_clientdir}
%{yast_clientdir}/*.rb
%dir %{yast_moduledir}
%{yast_moduledir}/*.rb
%{yast_moduledir}/*.pm
%license COPYING
%if %suse_version <= 1020
/opt/kde3
%endif
%{_datadir}/mime/packages/*.xml
%{_datadir}/applications/yast2-metapackage-handler*.desktop

%changelog
