#
# spec file for package yast2-installation-control
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


Name:           yast2-installation-control
Version:        4.6.0
Release:        0
Summary:        YaST2 - RNG schema for installation control files
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-installation-control
Source0:        %{name}-%{version}.tar.bz2
# smoke test during build
BuildRequires:  libxml2-tools
BuildRequires:  yast2-devtools >= 4.4.0
BuildArch:      noarch

%description
This package contains RNG schema for validating the installation control files.

%prep
%setup -q

%build
%yast_build

%install
%yast_install

%files
%license COPYING
%dir %{yast_controldir}
%{yast_controldir}/*.rng
%{yast_controldir}/*.rnc
%{_rpmmacrodir}/macros.skelcd

%changelog
