#
# spec file for package yast2-metapackage-handler
#
# Copyright (c) 2023 SUSE LLC
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


Name:           yast2-metapackage-handler
Version:        4.6.0
Release:        0
Summary:        YaST2 - Easy Installation of Add-on RPMs using Metapackages
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-metapackage-handler
Source0:        %{name}-%{version}.tar.bz2
# should be required by devtools
BuildRequires:  pkgconfig
# desktop files
BuildRequires:  update-desktop-files
BuildRequires:  yast2
# ycpc
BuildRequires:  yast2-core
BuildRequires:  yast2-country-data
# y2tool
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  yast2-packager
BuildRequires:  yast2-transfer
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# needed at runtime for invoking root mode
Requires:       %{_bindir}/xdg-su
Requires:       yast2
# Language
Requires:       yast2-country-data
Requires:       yast2-packager
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-transfer
BuildArch:      noarch

%description
With this technology users can install packages and add repositories
with a simple click on a link in a website.

%prep
%setup -q

%build

%install
%yast_install

%suse_update_desktop_file org.opensuse.yast.MetapackageHandler

%files
%license COPYING
%doc %{yast_docdir}
%{_bindir}/OneClickInstall*
%{yast_clientdir}
%{yast_moduledir}
%{_datadir}/icons/hicolor/*/apps/yast-oneclick*
%{_datadir}/applications/org.opensuse.yast.MetapackageHandler.desktop
%{_datadir}/mime/packages/yast2-metapackage-handler-mimetypes.xml

%changelog
