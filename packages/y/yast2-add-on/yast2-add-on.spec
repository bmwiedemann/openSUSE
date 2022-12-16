#
# spec file for package yast2-add-on
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast2-add-on
Version:        4.5.3
Release:        0
Summary:        YaST2 - Add-On media installation code
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-add-on

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# UIExtensionChecker
BuildRequires:  yast2 >= 4.4.19
BuildRequires:  yast2-devtools >= 3.1.10
# Y2packager::Resolvables
BuildRequires:  yast2-packager >= 4.2.11

Requires:       autoyast2-installation
# UIExtensionChecker
Requires:       yast2 >= 4.4.19
Requires:       yast2-country
Requires:       yast2-installation
# Packager ProductLicense#HandleLicenseDialogRet allowing "refuse" action
Requires:       yast2-packager >= 4.2.16
# "raw_name" in Pkg.SourceEditGet/Set()
Requires:       yast2-pkg-bindings >= 4.2.8
Requires:       yast2-ruby-bindings >= 1.0.0

Obsoletes:      yast2-add-on-devel-doc

Supplements:    autoyast(add-on)

BuildArch:      noarch

%description
This package contains YaST Add-On media installation code.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_libdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
