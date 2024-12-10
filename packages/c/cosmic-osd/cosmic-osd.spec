#
# spec file for package cosmic-osd
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


Name:           cosmic-osd
Version:        1.0.0~alpha4+0
Release:        0
Summary:        COSMIC OSD
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-osd
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -a1

%build
%make_build

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}

%check
%{cargo_test}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
