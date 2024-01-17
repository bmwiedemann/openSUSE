#
# spec file for package mscgen
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mscgen
Version:        0.20
Release:        0
Summary:        Message Sequence Chart Renderer
License:        GPL-2.0
Group:          Productivity/Graphics/Visualization/Graph
Url:            http://www.mcternan.me.uk/mscgen/
Source:         http://www.mcternan.me.uk/mscgen/software/mscgen-src-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gd-devel
BuildRequires:  libX11-devel
BuildRequires:  libXpm-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mscgen is a small program that parses Message Sequence Chart descriptions and
produces PNG, EPS, SVG or server side image maps (ismaps) as the
output. Message Sequence Charts (MSCs) are a way of representing entities and
interactions over some time period and are often used in combination with SDL.
MSCs are popular in Telecoms to specify how protocols operate although MSCs
need not be complicated to create or use. Mscgen aims to provide a simple text
language that is clear to create, edit and understand, which can also be
transformed into images.

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	--with-freetype
make %{?_smp_mflags}

%install
%make_install

%check
make %{?_smp_mflags} test

%files
%defattr(-,root,root)
%doc COPYING README ChangeLog
%{_docdir}/%{name}
%{_bindir}/mscgen
%{_mandir}/man1/mscgen.1%{ext_man}

%changelog
