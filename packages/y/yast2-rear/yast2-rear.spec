#
# spec file for package yast2-rear
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


Name:           yast2-rear
Version:        4.6.0
Release:        0
Summary:        YaST2 - Rear - Relax and Recover
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-rear
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  perl-XML-Writer
BuildRequires:  sgml-skel
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.4.0
BuildRequires:  yast2-storage-ng
BuildRequires:  yast2-testsuite
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
Requires:       rear >= 1.10.0
Requires:       yast2
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-storage-ng

# Build the package only for architectures supported by rear (bsc#1189646)
# See https://github.com/rear/rear/blob/f06e0d22eeb3bd45ad8ce0b8fce0b538e4534f93/packaging/rpm/rear.spec#L27-L33
ExclusiveArch:  %ix86 x86_64 ppc ppc64 ppc64le ia64

%description
The YaST2 component for configuring Rear - Relax and Recover Backup

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%license COPYING
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_icondir}

%changelog
