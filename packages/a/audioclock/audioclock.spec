#
# spec file for package audioclock
#
# Copyright (c) 2022 Bernhard M. Wiedemann / SUSE LLC
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


Name:           audioclock
Version:        1.3.2
Release:        0
Summary:        An audible clock
License:        GPL-2.0+
Url:            https://github.com/bmwiedemann/audioclock
Group:          Amusements/Toys/Clocks
BuildArch:      noarch
Source0:        %name-%version.tar.gz
Requires:       perl(Alien::SDL)
Requires:       perl(SDL::Mixer)

%description
This tool emulates the audio of a mechanical clock.
It shall help to notice the passing of time.

%prep
%setup

%build

%install
make install DESTDIR=%{buildroot}/usr

%files
%{_bindir}/audioclock
%{_datadir}/%name
%license COPYING README.md

%changelog
