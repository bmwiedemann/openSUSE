#
# spec file for package yast2-online-update-configuration
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-online-update-configuration
Version:        4.3.0
Release:        0
Summary:        Configuration of Online Update
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-online-update-configuration

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 2.17.0
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-packager
BuildRequires:  yast2-pkg-bindings >= 2.17.20
BuildRequires:  yast2-testsuite

PreReq:         %fillup_prereq
# Wizard::SetDesktopTitleAndIcon
Requires:       yast2 >= 2.21.0
Requires:       yast2-packager >= 2.17.0
Requires:       yast2-pkg-bindings >= 2.17.20
Requires:       yast2-ruby-bindings >= 1.0.0

Conflicts:      yast2-registration <= 2.19.1

Provides:       yast2-registration:/usr/share/YaST2/clients/online_update_configuration.ycp

BuildArch:      noarch

%description
Allows to configure automatic online update.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%post
%{fillup_only -ns automatic_online_update yast2-online-update-configuration}

%files
%license COPYING
%doc %{yast_docdir}
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%{yast_ybindir}
# agent
%{yast_scrconfdir}
# fillup
%{_fillupdir}/sysconfig.automatic_online_update-yast2-online-update-configuration

%changelog
