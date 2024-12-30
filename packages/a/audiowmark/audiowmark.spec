#
# spec file for package audiowmark
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           audiowmark
Version:        0.6.3
Release:        0
Summary:        Audio watermarking
License:        GPL-3.0-or-later
URL:            https://uplex.de/audiowmark/
Source:         https://uplex.de/audiowmark/releases/%{name}-%{version}.tar.zst
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
BuildRequires:  zita-resampler-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(libgcrypt) >= 1.2.0
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(sndfile) >= 1.1.0

%description
audiowmark is an open source solution for watermarking audio files. It is is
designed to be robust, fast, secure, and to produce a a watermark is not audible
for most users.

%prep
%autosetup -p1

%build
%configure \
	--with-ffmpeg \
	%{nil}
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS README.adoc
%{_bindir}/audiowmark
%{_bindir}/videowmark

%changelog
