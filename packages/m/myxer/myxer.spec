#
# spec file for package myxer
#
# Copyright (c) 2022 SUSE LLC
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


Name:           myxer
Version:        1.2.1~git0.f97f06a
Release:        0
Summary:        A modern Volume Mixer for PulseAudio
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        GPL-3.0-only
URL:            https://github.com/VixenUtils/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        install.yml
Patch1:         fix-gio-dep.patch
BuildRequires:  cargo-packaging
BuildRequires:  libpulse-devel
BuildRequires:  pkgconfig
BuildRequires:  rinstall
BuildRequires:  pkgconfig(atk) >= 2.14
BuildRequires:  pkgconfig(cairo) >= 1.12
BuildRequires:  pkgconfig(gdk-3.0) >= 3.22
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(pango) >= 1.36
ExclusiveArch:  %{rust_tier1_arches}

%description
A hello world with a number of the day printer.

%prep
%setup -q
%setup -qa1
%patch1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config
cp %{SOURCE3} .

%build
%{cargo_build}

%install
%{rinstall}

%check
%{cargo_test}

%files
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/README.md
%dir %{_datadir}/licenses/%{name}
%license %{_datadir}/licenses/%{name}/LICENSE.md
%{_bindir}/myxer
%{_datadir}/applications/Myxer.desktop

%changelog
