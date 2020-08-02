#
# spec file for package epson-inkjet-printer-escpr
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


Name:           epson-inkjet-printer-escpr
# SLE12 needs special BuildRequires.
# For suse_version values see https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} == 1315
# For SLE12 by default CUPS 1.7.5 is provided and alternatively CUPS 1.5.4 is provided in the "legacy" module.
# For SLE12 build it with traditional CUPS 1.5.4 to ensure it works on SLE12 both with CUPS 1.7.5 and CUPS 1.5.4
# because libcups and libcupsimage in CUPS 1.7.5 are backward compatible with CUPS 1.5.4 so that applications
# that have been built with CUPS 1.5.4 also work under CUPS 1.7.5 but the libraries in CUPS 1.7.5 provide
# some additional functions so that applications that have been built with CUPS 1.7.5 and use those
# additional functions would not work under CUPS 1.7.5.
# Only in the Printing project for SLE12 use cups154-ddk (a sub package of the cups154-SLE12 source package):
BuildRequires:  cups154
BuildRequires:  cups154-devel
%else
# Anything what is not SLE12 (i.e. SLE11 and all openSUSE versions) have "normal" BuildRequires:
BuildRequires:  cups
BuildRequires:  cups-devel
%endif
Version:        1.7.7
Release:        0
URL:            http://avasys.jp/english/linux_e/
Summary:        Epson ESC/P-R Inkjet Printer Driver
# Example URL to download Source0: http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX&productName=B700
License:        GPL-2.0-only
Group:          Hardware/Printing
Source0:        epson-inkjet-printer-escpr-%{version}-1lsb3.2.tar.gz
# PATCH-FIX-UPSTREAM bug_x86_64.patch -- fix a segfault on x64_64 (probably manifested with GCC7 use)
# https://aur.archlinux.org/cgit/aur.git/plain/bug_x86_64.patch?h=epson-inkjet-printer-escpr
Patch0:         bug_x86_64.patch
# This software is a filter program used with CUPS:
Requires:       cups
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ESC/P-R driver works as a filter program
used with CUPS.

It offers high quality printing with Seiko Epson
color inkjet printers.

This driver can only be used with printers that
support the Epson ESC/P-R language.

For a list of supported printers by a currently
installed package see the PPD files in this directory:

/usr/share/cups/model/manufacturer-PPDs/epson-inkjet-printer-escpr


%prep
# Be quiet when unpacking:
%setup -q
%patch0 -p1

%build
# Set our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
# Specify location of CUPS filter and ppd files explicitly.
# Use the explicite value 'epson-inkjet-printer-escpr' and not the RPM macro 'name'
# so that it could be built as well with a different package name
# (e.g. when someone likes to provide an epson-inkjet-printer-escpr SVN revision
#  with package name 'epson-inkjet-printer-escpr-SVN' or a specifically adapted
#  version as 'epson-inkjet-printer-escpr-only4me') because the installed PPDs
# must match exactly to the installed epson-escpr filter and the libescpr library:
%configure \
        --with-cupsfilterdir=/usr/lib/cups/filter \
        --with-cupsppddir=%{_datadir}/cups/model/manufacturer-PPDs
make

%install
# See lsb/lsb-rpm.spec
# Make directories:
install -d %{buildroot}/usr/lib/cups/filter
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_defaultdocdir}/%{name}
make install DESTDIR=%{buildroot}
install -m 644 README README.ja COPYING AUTHORS NEWS %{buildroot}%{_defaultdocdir}/%{name}
rm -f %{buildroot}%{_libdir}/libescpr.a
rm -f %{buildroot}%{_libdir}/libescpr.la
# Compress PPDs:
pushd %{buildroot}%{_datadir}/cups/model/manufacturer-PPDs/epson-inkjet-printer-escpr
# Do not pollute the build log file with meaningless messages:
set +x
# For now keep all PPDs even if cupstestppd FAILs.
# Reason:
# With each CUPS version upgrade cupstestppd finds more and more errors
# so that more and more PPDs would be no longer included in the RPM
# which have been included before which results a regression.
# As far as we know there have been no problems at all because of
# not strictly compliant PPDs so that it is much better to provide all PPDs
# so that the matching printers can be used than to be rigorous regarding
# enforcing compliance to the PPD specification:
for p in *.ppd
do echo -n "$p: "
   grep -E -v '^\*UIConstraints:|^\*NonUIConstraints:|^\*cupsFilter:' $p | cupstestppd - || true
   gzip -n9 $p
done
# Switch back to the usual build log messages:
set -x
popd

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
# The files sections list all mandatory files explicitly one by one.
# In particular all executables are listed explicitly.
# This avoids that the configure magic might silently
# not build and install an executable when whatever condition
# for configure's automated tests is not fulfilled in the build system.
# When all mandatory files are explicitly listed,
# the build fails intentionally if a mandatory file was not built
# which ensures that already existing correctly built binary RPMs
# are not overwritten by broken RPMs where mandatory files are missing.
%defattr(-,root,root)
%{_libdir}/libescpr.*
%dir /usr/lib/cups
%dir /usr/lib/cups/filter
/usr/lib/cups/filter/epson-escpr
/usr/lib/cups/filter/epson-escpr-wrapper
%dir %{_datadir}/cups
%dir %{_datadir}/cups/model
%dir %{_datadir}/cups/model/manufacturer-PPDs
%{_datadir}/cups/model/manufacturer-PPDs/epson-inkjet-printer-escpr/
%doc %{_defaultdocdir}/%{name}/

%changelog
