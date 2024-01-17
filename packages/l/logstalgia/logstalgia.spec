#
# spec file for package logstalgia
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


Name:           logstalgia
Version:        1.1.4
Release:        0
Summary:        A website access log visualization tool
License:        GPL-3.0-or-later
Group:          Amusements/Toys/Other
URL:            https://logstalgia.io/
Source:         https://github.com/acaudwell/Logstalgia/releases/download/logstalgia-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-libGLU-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  glm-devel >= 0.9.3
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(SDL2_image) >= 2.0
BuildRequires:  pkgconfig(freetype2) >= 9.0.3
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(sdl2) >= 2.0
Requires:       freefont
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel >= 1.46
BuildRequires:  libboost_headers-devel >= 1.46
BuildRequires:  libboost_system-devel >= 1.46
%else
BuildRequires:  boost-devel >= 1.46
%endif

%description
Logstalgia is a website traffic visualization that replays or streams
Apache web-server access logs as a pong-like battle between the web
server and an never ending torrent of requests. Requests appear as
colored balls (the same color as the host) which travel across the
screen to arrive at the requested location. Successful requests are
hit by the paddle while unsuccessful ones (eg 404 - File Not Found)
are missed and pass through.

%prep
%setup -q

%build
%configure \
  --enable-ttf-font-dir=%{_datadir}/fonts/truetype
%make_build

%install
%make_install

%files
%license COPYING
%doc README THANKS ChangeLog
%{_mandir}/man1/logstalgia*
%{_bindir}/logstalgia
%{_datadir}/logstalgia/

%changelog
