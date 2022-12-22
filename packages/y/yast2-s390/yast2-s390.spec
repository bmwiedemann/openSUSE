#
# spec file for package yast2-s390
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


Name:           yast2-s390
Version:        4.5.2
Release:        0
Group:          System/YaST
License:        GPL-2.0-only
Summary:        YaST2 - S/390 Specific Features Configuration
URL:            https://github.com/yast/yast-s390/

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-ruby-bindings >= 3.1.7
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# Y2Storage::Inhibitors
BuildRequires:  yast2-storage-ng >= 4.0.175
Requires:       s390-tools
Requires:       yast2
Requires:       yast2-ruby-bindings >= 3.1.7
Requires:       yast2-storage-ng >= 4.0.175

Supplements:    yast2-storage-ng
Supplements:    autoyast(xpram:zfcp:dasd)

ExclusiveArch:  s390 s390x

%description
This package contains the YaST component for configuration of
S/390-specific features.

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
%{yast_clientdir}
%{yast_libdir}
%{yast_moduledir}
%{yast_scrconfdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%doc %{yast_docdir}
%license COPYING

%changelog
