#
# spec file for package fbcat
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012-2021 Malcolm J Lewis <malcolmlewis@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           fbcat
Version:        0.5.2
Release:        0
Summary:        Framebuffer screenshot programs
License:        GPL-2.0
Group:          Productivity/Graphics/Convertors
URL:            https://github.com/jwilk/fbcat
Source0:        https://github.com/jwilk/fbcat/releases/download/%{version}/fbcat-%{version}.tar.gz
Source1:        https://github.com/jwilk/fbcat/releases/download/%{version}/fbcat-%{version}.tar.gz.asc

%description
Contains fbcat and fbgrab for taking a screenshot using the framebuffer
device.

Two executables are provided:
 - Low-level fbcat that operates on the current virtual terminal and writes the
   screenshot to stdout in the PPM format.
 - High-level fbgrab that supports the PNG format and virtual terminal switching.

%prep
%autosetup

%build
%make_build CFLAGS='%{optflags}'

%install
%make_install PREFIX=%{_prefix}

%files
%doc doc/changelog
%license doc/COPYING
%{_bindir}/fbcat
%{_bindir}/fbgrab
%{_mandir}/man1/fbcat.1%{?ext_man}
%{_mandir}/man1/fbgrab.1%{?ext_man}

%changelog
