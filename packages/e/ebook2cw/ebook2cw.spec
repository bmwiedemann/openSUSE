#
# spec file for package ebook2cw
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%bcond_without mp3
%bcond_without ogg
Name:           ebook2cw
Version:        0.8.5
Release:        0
Summary:        Convert ebooks to Morse MP3s/OGGs
License:        GPL-2.0-or-later
URL:            https://fkurz.net/ham/ebook2cw.html
Source:         https://fkurz.net/ham/ebook2cw/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
%if %{with mp3}
BuildRequires:  pkgconfig(lame)
%endif
%if %{with ogg}
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
%endif

%description
ebook2cw is a command line program (optional graphical user interface
available) which converts a plain text (ASCII, ISO 8859-1 or UTF-8) file (e. g.
an ebook) to Morse code MP3 or OGG audio files.

%prep
%autosetup -p1
dos2unix ebook2cw.conf

%build
%make_build \
%if !%{with mp3}
	USE_LAME=NO \
%endif
%if !%{with ogg}
	USE_OGG=NO \
%endif
	%{nil}

%install
%make_install \
	DESTDIR=%{buildroot}%{_prefix} \
	%{nil}
mkdir -p %{buildroot}%{_docdir}
mv -v %{buildroot}%{_datadir}/doc/%{name} %{buildroot}%{_docdir}/%{name}
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/ebook2cw.1%{?ext_man}
%{_docdir}/ebook2cw

%changelog
