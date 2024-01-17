#
# spec file for package hardening-check
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


# the hardening checker script belongs to the hardening-wrapper, but we don't
# need the wrapper parts, it's been discontinued in Debian/Ubuntu recently
# anyways
%define upstream_pkg hardening-wrapper
Name:           hardening-check
# NOTE: there seems to exists a curious disappeared version 2.7 of
# hardening-wrapper that is shipped on Gentoo, for example, and also marked as released here:
#     https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=767269
# the sources have disappeared from the debian FTP server for some reason.
# They can still be fetched from FTP mirrors or Gentoo's distfiles. I've
# checked the differences and they don't concern the checker script, only the
# wrappers, so we don't need to spend to much work on this and stay with the
# latest one available on debian FTP
Version:        2.6
Release:        0
Requires:       perl
Summary:        A tool for inspecting low-level hardening characteristics of ELF binaries
License:        GPL-2.0+
Url:            http://packages.debian.org/%{upstream_pkg}
Source0:        http://ftp.debian.org/debian/pool/main/h/%{upstream_pkg}/%{upstream_pkg}_%{version}.tar.xz
Source1:        hardening-check-rpmlintrc
# fixes a syntax error in a perl regex in the Makefile that came up with a
# newer perl version it seems
Patch0:         perl_regex.patch

%description
This package contains a Perl script that allows checking
a number of hardening characteristics of ELF binaries.

This includes checks for PIE executables, stack protection, source
fortification, read-only relocations and immediate binding.

%prep
%setup -q -n hardening-wrapper
%patch0 -p1

%build
# this is to silence make errors but it doesn't influence our package, because
# the values only influence the wrapper scripts which aren't shipped, we only
# want the hardening-check script

# the script is also filled with some values from libc during the make step
# thus this script cannot considered to be noarch, information extracted from
# libc may differ between archs
export DEB_HOST_ARCH=`uname -m`
export DEB_HOST_ARCH_OS=`uname -s`
make %{?_smp_mflags}

%install
# NOTE: there are two variants of the check script, one written in bash, one
# written in perl. The perl one is more fancy so lets stick with that one
install -D -m 755 build-tree/hardening-check %{buildroot}%{_bindir}/hardening-check
install -D -m 644 build-tree/hardening-check.1 %{buildroot}%{_mandir}/man1/hardening-check.1

%files
%{_bindir}/hardening-check
%{_mandir}/man1/hardening-check.1*

%changelog
