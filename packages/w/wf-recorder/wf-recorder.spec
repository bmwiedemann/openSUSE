#
# spec file for package wf-recorder
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2018 Michael Aquilina
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


Name:           wf-recorder
Version:        0.6.0+git4
Release:        0%{?dist}
Summary:        Utility program for screen recording of wlroots-based compositors
License:        MIT
URL:            https://github.com/ammen99/wf-recorder
Source0:        %{name}-%{version}.tar.zst
Patch0:         0001-Add-openSUSE-specific-defaults-to-help-output.patch
BuildRequires:  c++_compiler
BuildRequires:  fish
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 1.0.5
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildSystem:    meson
# Since the only good non-patented video codec is AV1 and there are
# no fast software encoders for it, let’s just pick a fast lossless codec
# with support for GBR(A) and YUV444 pixel formats.
# FFv1 would offer more formats (e.g. high bit depths) and compression
# ratios similar to libx264 lossless, but it is much slower.
BuildOption:    -Ddefault_codec=utvideo
BuildOption:    -Ddefault_pixel_format=gbrp
# Opus would be perfectly fine, but we’re doing lossless video anyway,
# so let’s also pick a lossless audio codec.
BuildOption:    -Ddefault_audio_codec=flac

%description
Utility program for screen recording of wlroots-based compositors
(more specifically, those that support wlr-screencopy-v1 and xdg-output).

%package fish-completion
Summary:        Fish Completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command line completion support for %{name}.

%prep
# https://github.com/openSUSE/obs-service-source_validator/issues/156
%autosetup -C -p1

%files
%license LICENSE
%doc README.md
%attr(0755,root,root) %{_bindir}/wf-recorder
%{_mandir}/man?/%{name}*

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
