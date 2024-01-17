#
# spec file for package toilet
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


Name:           toilet
Version:        0.3
Release:        0
Summary:        Powerful figlet replacement
License:        WTFPL
URL:            http://caca.zoy.org/wiki/toilet
Source:         http://caca.zoy.org/raw-attachment/wiki/toilet/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libcaca-devel
BuildRequires:  zlib-devel

%description
TOIlet is in its very early development phase. It uses the powerful libcucul
library to achieve various text-based effects. TOIlet implements or plans to
implement the following features:
 * The ability to load FIGlet fonts
 * Support for Unicode input and output
 * Support for colour output
 * Support for various output formats: HTML, IRC, ANSI...

TOIlet also aims for full FIGlet compatibility. It is currently able to load
FIGlet fonts and perform horizontal smushing.

%prep
%setup -q
sed -i 's|11 10|16 15 14 13 12 11 10|' bootstrap

%build
./bootstrap
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/figlet
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
