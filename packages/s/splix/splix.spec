#
# spec file for package splix
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%if 0%{?suse_version} > 1110
%bcond_without jbigkit
%endif

Name:           splix
Summary:        Driver for Samsung Printer Language printers
License:        GPL-2.0
Group:          Hardware/Printing
Version:        2.0.0.315
Release:        0
Url:            http://splix.ap2c.org/
# revision 315 from svn://svn.code.sf.net/p/splix/code/splix
Source0:        splix-2.0.0.315.tar.bz2
Source1:        http://splix.ap2c.org/samsung_cms.tar.bz2
Source2:        README.SUSE
Patch1:         %name-libs.patch
Patch2:         %name-add-debuginfo.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
BuildRequires:  cups154-devel
%else
# Anything what is not SLE12 (i.e. SLE11 and all openSUSE versions) have "normal" BuildRequires:
BuildRequires:  cups-devel
%endif
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if (0%{?suse_version} > 1110) && ! %{without jbigkit}
BuildRequires:  libjbig-devel
%endif
Requires:       cups
# The Splix driver PPDs contain either
#   *cupsFilter: "application/vnd.cups-postscript 0 pstoqpdl"
# or
#   *cupsFilter: "application/vnd.cups-raster 0 rastertoqpdl"
# which means both require Ghostscript because
# either /usr/lib/cups/filter/pstoqpdl calls Ghostscript via
# /usr/lib/cups/filter/pstoraster or /usr/lib/cups/filter/gstoraster
# (see the post install scriptlet below)
# or /usr/lib/cups/filter/rastertoqpdl needs CUPS raster data as input
# that is produced by the cups device in Ghostscript
# (even the old ghostscript-library RPM e.g. in SLE11 provides ghostscript):
Requires:       ghostscript
# Provide and obsolete its old RPM package name "cups-drivers-splix"
# see https://bugzilla.novell.com/show_bug.cgi?id=659579
Provides:       cups-drivers-splix >= %version
Obsoletes:      cups-drivers-splix < %version

%description
SpliX is a set of CUPS printer drivers for SPL (Samsung Printer
Language) printers. Some Samsung, Xerox and Dell printers use that
language.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
cp %SOURCE2 .
mv -v *.ppd ppd/

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%if 0%{?suse_version} > 1110
make %{?_without_jbigkit:DISABLE_JBIG=1} %{?_smp_mflags} V=1
%else
make DISABLE_JBIG=1 %{_smp_mflags} V=1
%endif

%install
%if 0%{?suse_version} > 1110
%makeinstall %{?_without_jbigkit:DISABLE_JBIG=1}
%else
%makeinstall DISABLE_JBIG=1
%endif
pushd $RPM_BUILD_ROOT%_datadir/cups/model/samsung/
tar -xjvf "%{SOURCE1}"
popd
gzip -n -9 %buildroot/%_datadir/cups/model/*/*.ppd
# Run fdupes:
# The RPM macro fdupes runs /usr/bin/fdupes that links files with identical content.
# Never run fdupes carelessly over the whole buildroot directory
# because in older openSUSE and SLE11 versions fdupes
# links files with different owner, group, or permissions
# see https://bugzilla.novell.com/show_bug.cgi?id=784670
# and even in current openSUSE versions fdupes links across sub-package boundaries,
# compare https://bugzilla.novell.com/show_bug.cgi?id=784869
# so that fdupes can only run for specific directories where linking files is safe:
%fdupes -s %{buildroot}/%{_datadir}/cups/model/samsung/cms

%if 0%{?suse_version} > 1110
# Do not do this for SLE11 where ghostscript-library 8.62 is used.
# If Splix plus Ghostscript >= 9.02 is used on SLE11 the admin must do it manually as needed.
%post
# Use a real bash script with an explicit "exit 0" at the end to be by default fail safe
# an explicit "exit 1" must be use to enforce package install/upgrade/erase failure where needed
# see the "Shared_libraries" section in http://en.opensuse.org/openSUSE:Packaging_scriptlet_snippets
# Make Splix working also for Ghostscript version >= 9.02:
# In /usr/lib/cups/filter/pstoqpdl there is a hardcoded call for /usr/lib/cups/filter/pstoraster.
# Since Ghostscript version 9.02 /usr/lib/cups/filter/pstoraster is replaced by /usr/lib/cups/filter/gstoraster.
# Accordingly when no /usr/lib/cups/filter/pstoraster exists, create an appropriate symlink
# so that /usr/lib/cups/filter/pstoqpdl works (see https://bugzilla.novell.com/show_bug.cgi?id=803005).
# Intentionally there is no test that /usr/lib/cups/filter/gstoraster exists because
# the required (but not pre-required) ghostscript RPM could be installed after splix.
# Note that only "test -e /usr/lib/cups/filter/pstoraster" (or "test -f") is insufficient because
# test follows symlinks which means when /usr/lib/cups/filter/pstoraster is already a (possibly broken)
# symbolic link to /usr/lib/cups/filter/gstoraster then test results false so that
# additionally it must be tested if /usr/lib/cups/filter/pstoraster is a symlink:
if ! test -e /usr/lib/cups/filter/pstoraster -o -L /usr/lib/cups/filter/pstoraster
then ln -s /usr/lib/cups/filter/gstoraster /usr/lib/cups/filter/pstoraster
fi
exit 0
%endif

%files
%defattr(-,root,root)
%doc COPYING README.SUSE
%dir %_datadir/cups
%dir %_datadir/cups/model
%dir %_datadir/cups/model/dell
%dir %_datadir/cups/model/samsung
%dir %_datadir/cups/model/xerox
%dir %_datadir/cups/model/lexmark
%dir %_datadir/cups/model/toshiba
%if 0%{?suse_version} == 1110
# On SLE11 with its CUPS 1.3.9 there is still /usr/lib64/cups/ used on x86_64.
# For suse_version values see https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
# On SLE11 it installs automatically into /usr/lib64/cups/ on x86_64 and into /usr/lib/cups/ on x86:
%dir %_libdir/cups/
%dir %_libdir/cups/filter/
%_libdir/cups/filter/pstoqpdl
%_libdir/cups/filter/rastertoqpdl
%else
# Use a plain simple fixed /usr/lib/cups/filter/ according
# to what is actually used by CUPS >= 1.4 on all platforms:
%dir /usr/lib/cups/
%dir /usr/lib/cups/filter/
/usr/lib/cups/filter/pstoqpdl
/usr/lib/cups/filter/rastertoqpdl
%endif
%_datadir/cups/model/dell/*.ppd.gz
%_datadir/cups/model/samsung/*.ppd.gz
%_datadir/cups/model/samsung/cms
%_datadir/cups/model/xerox/*.ppd.gz
%_datadir/cups/model/lexmark/*.ppd.gz
%_datadir/cups/model/toshiba/*.ppd.gz

%changelog
