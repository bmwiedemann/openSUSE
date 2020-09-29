#
# spec file for package sunxi-tools
#
# Copyright (c) 2020 SUSE LLC
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


# Now, the only TARGET_TOOLS is 'sunxi-meminfo' which is not buildable for aarch64.
# For more information, see: https://github.com/linux-sunxi/sunxi-tools/issues/76
%define sunxi_arch armv7hl

Name:           sunxi-tools
Version:        1.4.2+git20200914103652
Release:        0
Summary:        Tools for Allwinner A10 devices
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/linux-sunxi/sunxi-tools
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    %arm

%description
Tools to help hacking Allwinner A10 (aka sun4i) based devices
and its successors.

%prep
%setup -q

%build
# Suppress -static for target-tools
make %{?_smp_mflags} EXTRA_CFLAGS="%{optflags}" CROSS_COMPILE="" \
%ifarch %sunxi_arch
	TARGET_CFLAGS="-g -O0 -Wall -Wextra -std=c99 -D_POSIX_C_SOURCE=200112L -D_BSD_SOURCE -D_DEFAULT_SOURCE -Iinclude/ %{optflags}" \
	all
%else
	tools
%endif

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} PREFIX=%{_prefix} BINDIR=%{_bindir} \
%ifarch %sunxi_arch
	install-all
%else
	install
%endif

%files
%defattr(-,root,root)
%doc README.md LICENSE.md
%{_bindir}/bin2fex
%{_bindir}/fex2bin
%{_bindir}/sunxi-bootinfo
%{_bindir}/sunxi-fel
%{_bindir}/sunxi-fexc
%{_bindir}/sunxi-nand-part
%ifarch %sunxi_arch
%{_bindir}/sunxi-meminfo
%endif
%{_bindir}/sunxi-pio

%changelog
