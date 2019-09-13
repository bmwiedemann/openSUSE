#
# spec file for package capi4hylafax
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


Name:           capi4hylafax
Version:        01.03.00
Release:        0
Summary:        Adds a faxcapi modem for hylafax
License:        GPL-2.0+
Group:          Hardware/Fax
Url:            http://www.avm.de

Source:         ftp://ftp.avm.de/tools/capi4hylafax.linux/%name-%version.tar.gz
Patch0:         capi4hylafax-suse.diff
Patch1:         capi4hylafax-secfix.diff
Patch2:         capi4hylafax-secfix2.diff
Patch3:         capi4hylafax-configure.diff
Patch4:         capi4hylafax-gcc48.diff
Patch5:         capi4hylafax-01.03.00-fix-bashisms.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  capi4linux
BuildRequires:  capi4linux-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript-library
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pwdutils
Requires:       a2ps
Requires:       gs_lib
Requires:       hylafax
Requires:       hylafax-client
Requires:       smtp_daemon
Requires:       tiff
Requires(pre):  sh-utils fileutils /usr/sbin/useradd /usr/sbin/usermod

%description
capi4hylafax adds a faxcapi modem to the hylafax environment. It allows
you to send and receive FAX documents with CAPI 2.0 fax controllers via
a hylafax server.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3
%patch4 -p1
%patch5 -p1
find ../ -name .cvsignore -delete

%build
%configure \
		--with-hylafax-spooldir=/var/spool/fax
#		--enable-debug 
make %{?_smp_mflags}

%install
install -d "%buildroot/var/spool/fax"
install -d "%buildroot/usr/lib"
install -d "%buildroot/%_libdir"
install -d "%buildroot/%_sbindir"
install -d "%buildroot/%_sysconfdir"
make install BIN="%buildroot/%_bindir" \
		SPOOL="%buildroot/var/spool/fax" \
		LIBEXEC="%buildroot/usr/lib/fax" \
		SBIN="%buildroot/%_sbindir" \
		LIBDIR="%buildroot/%_libdir" \
		DESTDIR="%buildroot"
install -m755 faxaddmodem.capi "%buildroot/%_sbindir/"
install -m755 setupconffile "%buildroot/%_sbindir/faxaddmodem.capi_dia"
cp -p config.faxCAPI "%buildroot/%_sysconfdir/config.faxCAPI.sample"
mkdir -p "%buildroot/%_defaultdocdir/capi4hylafax"
cp -p AUTHORS LIESMICH.html README.html fritz_pic.tif COPYING Readme_src \
	LIESMICH.SuSE README.SuSE \
	ChangeLog sample_AVMC4_config.faxCAPI sample_faxrcvd \
	config.faxCAPI \
	"%buildroot/%_defaultdocdir/capi4hylafax"

%pre
/usr/sbin/useradd -r -o -g uucp -u 33 -s /bin/bash -c "Facsimile agent" -d /var/spool/fax fax 2> /dev/null || :
/usr/sbin/usermod -g uucp -G dialout fax 2> /dev/null || :
test -f /var/spool/fax/etc/config.faxCAPI -a ! -f /etc/config.faxCAPI && \
    cp -a /var/spool/fax/etc/config.faxCAPI /etc/config.faxCAPI || :

%post
#!/bin/sh
cd etc
FILES=`grep -l "FaxReceiveUser:" config.fax*`
test -z "$FILES" && exit
CFG=""
for f in $FILES ; do
    case $f in
	*~);;
	*orig);;
	*save);;
	*new);;
	*sample);;
	*)  FRG=`grep "FaxReceiveGroup:" $f`
	    if [ -z "$FRG" ]; then
		CFG="${CFG} $f"
	    fi
	    ;;
    esac
done
test -z "$CFG" && exit
for f in $CFG ; do
    mv ${f} ${f}.orig
    cat ${f}.orig | while read line ; do
	case $line in
	    FaxReceiveUser:*)
		echo "FaxReceiveUser:         fax" >> ${f}
		echo "FaxReceiveGroup:        dialout" >> ${f}
		;;
	    *)  echo "$line" >> ${f}
		;;
	esac
    done
done

%files
%defattr(-, root, root)
%doc %{_defaultdocdir}/capi4hylafax
%_bindir/c2faxrecv
%_bindir/c2faxsend
%_sbindir/faxaddmodem.capi
%_sbindir/faxaddmodem.capi_dia
%_sysconfdir/config.faxCAPI.sample

%changelog
