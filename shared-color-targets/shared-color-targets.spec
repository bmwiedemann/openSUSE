#
# spec file for package shared-color-targets
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Luis Medinas, Portugal
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


Name:           shared-color-targets
Version:        0.1.7
Release:        0
Summary:        Color targets for creating color profiles
License:        GPL-2.0-or-later AND SUSE-Public-Domain AND CC-BY-SA-3.0
Group:          System/GUI/Other
Url:            http://github.com/hughsie/shared-color-targets
Source:         http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The shared-color-targets package contains various targets which are
useful for programs that create ICC profiles.

%prep
%setup -q

%build
%configure

%install
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%dir %{_datadir}/color
%dir %{_datadir}/color/targets
%{_datadir}/color/targets/*.it8
%dir %{_datadir}/shared-color-targets

# Wolf Faust
%{_datadir}/shared-color-targets/wolf_faust/
%dir %{_datadir}/color/targets/wolf_faust
%dir %{_datadir}/color/targets/wolf_faust/reflective
%{_datadir}/color/targets/wolf_faust/reflective/*.it8
%dir %{_datadir}/color/targets/wolf_faust/transmissive
%{_datadir}/color/targets/wolf_faust/transmissive/*.it8

%changelog
