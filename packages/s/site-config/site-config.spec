#
# spec file for package site-config
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


Name:           site-config
Version:        0.2
Release:        0
Summary:        Site Paths Configuration for autoconf Based configure Scripts
License:        GPL-2.0+
Group:          Development/Tools/Building
Source0:        %{name}.libdir1
Source1:        %{name}.libdir3.biarch
Source2:        %{name}.libdir3.uniarch
Source3:        %{name}.libdir4
Source4:        %{name}.libexecdir
Source5:        %{name}.AUTHORS
Source6:        %{name}.COPYING
Source7:        %{name}.README
BuildRequires:  autoconf
BuildRequires:  libtool
%if 0%{?suse_version}
Supplements:    make autoconf
%endif

%description
Site configuration for autoconf based configure scripts provides smart
defaults for paths that are not specified.

%prep
%setup -q -T -c %{name}-%{version}
cp -a %{S:0} %{S:1} %{S:2} %{S:3} %{S:4} .
cp -a %{S:5} AUTHORS
cp -a %{S:6} COPYING
cp -a %{S:7} README

%build
# Call libtool to get name of our architecture as seen by GNU tools.
if test -f %{_datadir}/libtool/build-aux/config.guess; then
	# libtool 2.4.6
	%{_datadir}/libtool/build-aux/config.guess >site_platform
elif test -f %{_datadir}/libtool/config/config.guess ; then
	# new libtool
	%{_datadir}/libtool/config/config.guess >site_platform
else
	# old libtool
	%{_datadir}/libtool/config.guess >site_platform
fi
SITE_PLATFORM=$(<site_platform)
if test -z "$SITE_PLATFORM" ; then
	echo "ERROR: libtool implementation changed. Please update SITE_PLATFORM definition."
	exit 1
fi

# Extract fully expanded needed parts of the actual implementation of AC_SITE_LOAD.
# Create dummy configure.in to generate configure.
cat >configure.in <<EOF
dnl AC_SITE_LOAD is included as part of AC_INIT
AC_INIT
EOF
autoconf
# Extract site script loading parts of configure and apply some rewrite rules.
if grep ac_site_file2 configure ; then
	# new autoconf
	sed -n <configure >ac_site_load_files '
		s/  /\t/g
		s:\$as_me:%{_datadir}/site/'$SITE_PLATFORM':g
		/^elif test "x\$prefix" != xNONE/s/elif/if/
		/^if test "x\$prefix" != xNONE/,/^done/p
	'
else
	# old autoconf
	sed -n <configure >ac_site_load_files '
		s:\$as_me:%{_datadir}/site/'$SITE_PLATFORM':g
		s/  /\t/g
		/^fi/d
		/^\tif test "x\$prefix" != xNONE; then/,/^\tfi/s/^\t//
		s/CONFIG_SITE/ac_site_files/
		/^if test "x\$prefix" != xNONE/,/^done/p
	'
fi
if test -z "$(<ac_site_load_files)" ; then
	echo "ERROR: AC_SITE_LOAD implementation changed. Please update extraction logic."
	exit 1
fi

# Now compile site-config script.
# Header.
echo -e '#!/bin/sh\n# Site script for configure. It is resourced via $CONFIG_SITE environment varaible.\n' >site-config
# libdir stuff.
cat site-config.libdir1 >>site-config
NATIVE_PLATFORM=`uname -i`
if test "%{_libdir}" = "%{_prefix}/lib" ; then
	echo -e "\t\t# The native platform $NATIVE_PLATFORM is not a bi-arch platform." >>site-config
	cat site-config.libdir3.uniarch >>site-config
else
	echo -e "\t\t# The native platform $NATIVE_PLATFORM is a bi-arch platform." >>site-config
	cat site-config.libdir3.biarch >>site-config
fi
cat site-config.libdir4 >>site-config
# libexec stuff.
cat site-config.libexecdir >>site-config
# And stuff to load site scripts from default locations.
echo '# Continue with the standard behavior of configure defined in AC_SITE_LOAD:' >>site-config
cat ac_site_load_files >>site-config

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/site $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

# Install site script.
SITE_PLATFORM=$(<site_platform)
cp site-config $RPM_BUILD_ROOT%{_datadir}/site/$SITE_PLATFORM

# Install Bourne Shell profile.
cat >$RPM_BUILD_ROOT%{_sysconfdir}/profile.d/site.sh <<EOF
CONFIG_SITE="%{_datadir}/site/$SITE_PLATFORM"
export CONFIG_SITE
EOF

# Install C Shell profile.
cat >$RPM_BUILD_ROOT%{_sysconfdir}/profile.d/site.csh <<EOF
setenv CONFIG_SITE "%{_datadir}/site/$SITE_PLATFORM"
EOF

%files
%defattr (-,root,root)
%doc AUTHORS COPYING README
%{_datadir}/site
%{_sysconfdir}/profile.d/*.*

%changelog
