#
# spec file for package otf2bdf
#
# Copyright (c) 2025 SUSE LLC
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


Name:           otf2bdf
Version:        3.1
Release:        0
Summary:        Conversion utility for OpenType outline fonts to BDF bitmap fonts
License:        MIT
Group:          System/X11/Utilities
URL:            https://github.com/jirutka/otf2bdf
Source0:        %{name}-%{version}.tar.gz
Patch0:         otf2bdf-configure-c99.patch
BuildRequires:  freetype2-devel
BuildRequires:  gcc
BuildRequires:  make

%description
otf2bdf is a command line utility that uses the FreeType 2 font
rendering library to generate BDF bitmap fonts from OpenType outline
fonts at different sizes and resolutions. This program is essentially
the same as the ttf2bdf program, except that it uses FreeType 2.x, not
FreeType 1.x, has some bug fixes, and includes a new command line
parameter to print out the available encoding tables in the font.

%prep
%autosetup -p1

%build
%configure
%make_build

%install

install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
