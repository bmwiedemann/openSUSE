#
# spec file for package kew
#
# Copyright (c) 2024 SUSE LLC
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


Name:           kew
Version:        2.5.1
Release:        0
Summary:        A command-line music player
License:        GPL-2.0-only
URL:            https://github.com/ravachol/kew
Source:         %{url}/archive/v%{version}/kew-%{version}.tar.gz
BuildRequires:  freeimage-devel
BuildRequires:  gcc >= 13
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(vorbisfile)

%description
Listen to music in the terminal.

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README*
%{_bindir}/kew
%{_mandir}/man1/kew.1%{?ext_man}

%changelog
