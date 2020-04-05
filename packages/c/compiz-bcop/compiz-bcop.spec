#
# spec file for package compiz-bcop
#
# Copyright (c) 2020 SUSE LLC
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


%define _rev    5b37c3edbf45fcac9412c34e00383715
%define _name   bcop
Name:           compiz-bcop
Version:        0.8.18
Release:        0
Summary:        Compiz option code generator
License:        GPL-2.0-or-later
URL:            https://gitlab.com/compiz/compiz-bcop
Source:         https://gitlab.com/compiz/compiz-bcop/uploads/%{_rev}/%{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxslt)
Requires:       xsltproc
Recommends:     compiz >= %{version}
Provides:       %{name}-devel = %{version}
BuildArch:      noarch

%description
Compiz option code generator needed to build some plugins.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{_name}
%{_datadir}/%{_name}/
%{_datadir}/pkgconfig/%{_name}.pc

%changelog
