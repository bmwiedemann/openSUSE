#
# spec file for package brightnessctl
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 R Tyler Croy <rtyler@brokenco.de>
# Copyright (c) 2016 Fabio Alessandro Locati <fale@fedoraproject.org>
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


# use systemd-logind instead of udev for systemd >= 243
%if 0%{?sle_version} >= 150200 || 0%{?suse_version} > 1500
%global use_logind 1
%else
%global use_logind 0
%endif
Name:           brightnessctl
Version:        0.4
Release:        0
Summary:        Tool to read and control device brightness
License:        MIT
URL:            https://github.com/Hummer12007/%{name}
Source:         %{URL}/archive/%{version}.tar.gz
# required to resolve cherry pick conflicts
# https://github.com/Hummer12007/brightnessctl/commit/aa6a71cd8206992a64269239f038dbf5f516e54a
Patch0:         0001-Fixed-inconsistency-in-README-thanks-AJGQ.patch
# https://github.com/Hummer12007/brightnessctl/pull/33
Patch1:         0002-Support-the-new-SetBrightness-logind-API.patch
Patch2:         0003-Make-the-use-of-SetBrightness-dynamic.patch
# https://github.com/Hummer12007/brightnessctl/pull/41
Patch3:         0004-Use-non-suid-permissions-when-logind-is-used.patch
BuildRequires:  gcc
BuildRequires:  make
%if %{use_logind}
BuildRequires:  pkgconfig(libsystemd)
Requires:       systemd >= 243
%else
BuildRequires:  systemd-rpm-macros
%endif

%description
A utility to read and control the display brightness.

%prep
%autosetup -N
%if %{use_logind}
%autopatch -p1
%endif

%build
%if %{use_logind}
export ENABLE_SYSTEMD=1
%{set_build_flags}
%else
export MODE="4755"
export CFLAGS="%{optflags}"
%endif
%make_build

%install
%if %{use_logind}
%make_install INSTALL_UDEV_RULES=0 ENABLE_SYSTEMD=1 PREFIX=%{_prefix}
%else
%make_install UDEVDIR=%{_udevrulesdir}
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%if ! %{use_logind}
%{_udevrulesdir}/90-brightnessctl.rules
%endif
%{_mandir}/man1/brightnessctl.1%{?ext_man}

%changelog
