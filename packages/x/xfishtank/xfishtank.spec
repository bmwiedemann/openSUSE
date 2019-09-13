#
# spec file for package xfishtank
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xfishtank
Version:        2.2
Release:        0
Summary:        An aquarium in the root window
License:        GPL-2.0+
Group:          Amusements/Toys/Background
Source:         %{name}-%{version}.tar.bz2
Source1:        README.KDE
Patch:          %{name}-%{version}-orig.patch
Patch1:         %{name}-%{version}-implicit_decl.patch
Patch2:         %{name}-%{version}-random_retval.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xproto)
Provides:       fishtank
Obsoletes:      fishtank

%description
A nice little aquarium with funny fish -- yet another background
screen.

%prep
%setup -q
%patch
%patch1
%patch2
install -m 0644 %{S:1} .

%build
xmkmf -a
make %{?_smp_mflags} CCOPTIONS="%optflags"

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%files
%defattr(-,root,root)
%doc README*
%_bindir/xfishtank

%changelog
