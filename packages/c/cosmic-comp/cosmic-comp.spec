#
# spec file for package cosmic-comp
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


Name:           cosmic-comp
Version:        1.0.0~alpha4+0
Release:        0
Summary:        Compositor for the COSMIC DE
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-comp
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       Mesa-libEGL1
Recommends:     Mesa-libGL1

%description
%{summary}.

%prep
%autosetup -a1

%build
%make_build

%install
%make_install
install -d %{buildroot}%{_sysconfdir}/%{name}

%check
%{cargo_test}

%files
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%{_datadir}/cosmic

%changelog
