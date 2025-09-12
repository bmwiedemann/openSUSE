#
# spec file for package hardening-check
#
# Copyright (c) 2025 SUSE LLC
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


# the hardening checker script belongs to the hardening-wrapper, but we don't
# need the wrapper parts, it's been discontinued in Debian/Ubuntu recently
# anyways
%define upstream_pkg devscripts
Name:           hardening-check
# NOTE: there seems to exists a curious disappeared version 2.7 of
# hardening-wrapper that is shipped on Gentoo, for example, and also marked as released here:
#     https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=767269
# the sources have disappeared from the debian FTP server for some reason.
# They can still be fetched from FTP mirrors or Gentoo's distfiles. I've
# checked the differences and they don't concern the checker script, only the
# wrappers, so we don't need to spend to much work on this and stay with the
# latest one available on debian FTP
Version:        2.25.19
Release:        0
Requires:       perl
Summary:        A tool for inspecting low-level hardening characteristics of ELF binaries
License:        GPL-2.0-or-later
URL:            http://packages.debian.org/%{upstream_pkg}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{upstream_pkg}/%{upstream_pkg}_%{version}.tar.xz
Source1:        hardening-check-rpmlintrc
Patch0:         avoid_pod2man_errors.patch
Patch1:         makefile_fixes.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  help2man
BuildRequires:  po4a
BuildRequires:  python3-setuptools
# fixes a syntax error in a perl regex in the Makefile that came up with a
# newer perl version it seems
#Patch0:         perl_regex.patch

%description
This package contains a Perl script that allows checking
a number of hardening characteristics of ELF binaries.

This includes checks for:

- PIE executables
- stack protection
- source fortification macros
- read-only relocations
- immediate binding
- branch protection

%prep
%autosetup -p1 -n devscripts-%{version}

# hardening-check is now part of the larger devscripts project, which
# contains a bunch of Debian-specific utilities. We only want the
# hardening-check parts. The problem is that the man page is generated during
# build time, thus we need to run the build system, which gives us some pain,
# given that we are not Debian.

# The Makefiles contain some hard-coded references to docbook stylesheets we
# have to adjust.
XSL_NEEDLE="/usr/share/sgml/docbook/stylesheet/xsl/nwalsh/manpages/docbook.xsl"
XSL_REPLACE="/usr/share/xml/docbook/stylesheet/nwalsh/1.79.2/manpages/docbook.xsl"
XSL_EXPR="s:$XSL_NEEDLE:$XSL_REPLACE:g"
find -type f -name "Makefile" -exec sed -i -e "$XSL_EXPR" {} \;

%build
# the script is also filled with some values from libc during the `make` step
# thus this script cannot considered to be noarch, information extracted from
# libc may differ between archs
export DEB_HOST_ARCH=`uname -m`
export DEB_HOST_ARCH_OS=`uname -s`
# ignore any podchecker errors the hard way (it seems we're using a newer
# toolchain or a different toolchain which complains about some constructs)
alias podchecker=true
# generate a version file from our RPM version information (this would
# otherwise require a deb-parsechangelog utility).
echo "%{Version}" >version
make %{?_smp_mflags}

%install
# only pick what we need: the script and the man page
install -D -m 755 scripts/hardening-check %{buildroot}%{_bindir}/hardening-check
install -D -m 644 scripts/hardening-check.1 %{buildroot}%{_mandir}/man1/hardening-check.1

%files
%{_bindir}/hardening-check
%{_mandir}/man1/hardening-check.1*

%changelog
