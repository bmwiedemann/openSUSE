#
# spec file for package schily
#
# Copyright (c) 2022 SUSE LLC
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


# grep -Pir 'define\s+VERSION|strvers'
%define rver	2022-10-16
%global box_version	2022.10.16
%global cdr_version	3.02~a10
%global sccs_version	5.09
%global smake_version	1.6
%global star_version	1.6.1
%global libfind_version 1.8
%global ved_version     1.8

Name:           schily
Version:        %box_version
Release:        0
Summary:        A collection of command-line utilities originally written by J.Schilling
License:        BSD-2-Clause AND CDDL-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND BSD-3-Clause AND HPND AND ISC
Group:          Productivity/Multimedia/CD/Record
URL:            https://codeberg.org/schilytools/schilytools

Source:         http://fuz.su/pub/schilytools/%name-%rver.tar.bz2
Source1:        README-FIRST
# Honor https://en.opensuse.org/openSUSE:Packaging_Patches_guidelines#Upstream_policy
# and submit patches upstream FIRST (cc to the bspkg maintainer perhaps).
Patch1:         iconv-name.diff
Patch2:         schily-2018-05-25_star_configuration.patch
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
Conflicts:      cdrkit-cdrtools-compat

%description
The "Schily" Tool Box is a set of tools originally written by Jörg Schilling.

%package -n bosh
Summary:        Multibyte-capable POSIX-conforming Bourne shell
License:        CDDL-1.0
Group:          System/Shells
Conflicts:      bsh

%description -n bosh
bosh is a Bourne-style POSIX command interpreter (shell), similar to dash,
but supports multibyte input/output.

%package -n btcflash
Summary:        Firmware flash utility for BTC DRW1008 DVD±RW recorder
License:        CDDL-1.0
Group:          Hardware/Other

%description -n btcflash
Btcflash is used to read update the Firmware for a BTC DRW1008
DVD±RW recorder. Be very careful when writing firmware as this
program does not check for the correctness of the target device.

%package -n cdda2wav
Summary:        A CD Digital Audio Extraction tool
License:        CDDL-1.0
Group:          Productivity/Multimedia/CD/Grabbers
Version:        %cdr_version
Release:        0
Requires(post): permissions

%description -n cdda2wav
cdda2wav can retrieve CDDA audio tracks from CDROM drives that are
capable of reading audio data digitally to the host via SCSI.

%package -n cdrecord
Summary:        A CD/DVD/BD recording program
License:        CDDL-1.0
Group:          Productivity/Multimedia/CD/Record
Version:        %cdr_version
Release:        0
Requires(post): permissions
Conflicts:      cdrkit-cdrtools-compat

%description -n cdrecord
cdrecord is a program to record (slang: "burn") data or audio Compact Discs
on an Orange Book CD recorder, to write DVD media on a DVD recorder or to
write BluRay media on a BluRay recorder.

%package ctags
Summary:        A program to generate tag files for ex/vi
License:        BSD-2-Clause AND CDDL-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND BSD-3-Clause AND HPND AND ISC
Group:          Development/Tools/Building
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description ctags
Ctags makes a tags file for ex(1) from the specified C, Pascal,
Fortran, YACC, lex, and lisp sources. A tags file gives the locations
of specified objects in a group of files. Each line of the tags file
contains the object name, the file in which it is defined, and a
search pattern for the object definition, separated by whitespace.
Using the tags file, ex(1) can quickly locate these object
definitions.

%package -n libcdrdeflt1_0
Summary:        Library to parse the cdrecord config file
License:        CDDL-1.0
Group:          System/Libraries
Version:        %cdr_version
Release:        0

%description -n libcdrdeflt1_0
This library implements a mechanism to read the settings from
cdrecord's config file(s).

%package -n libdeflt1_0
Summary:        Library to parse sysconfig setting files
License:        CDDL-1.0
Group:          System/Libraries

%description -n libdeflt1_0
This library can be used to parse setting files that follow a trivial
"KEY=VALUE"-style pattern, similar to what can be found in files
located in /etc/sysconfig. libdeflt supports values with spaces
which are not quoted, and which therefore are not always compatible
with sh.

%package -n libedc_ecc1_0
Summary:        Reed-Solomon encoder for Compact Discs
License:        CDDL-1.0
Group:          System/Libraries
Version:        %cdr_version
Release:        0

%description -n libedc_ecc1_0
The library implements a Reed-Solomon encoder for Compact
Discs to generate Error Correcting Codes (ECC).

%package -n libedc_ecc_dec1_0
Summary:        Reed-Solomon decoder for Compact Discs
License:        CDDL-1.0
Group:          System/Libraries
Version:        %cdr_version
Release:        0

%description -n libedc_ecc_dec1_0
The library implements a Reed-Solomon decoder for Compact Discs with
a mechanism for Error Detection and Correction (EDC).

%package -n libfile1_0
Summary:        Library for heuristic file type determination based on content
License:        BSD-2-Clause
Group:          System/Libraries

%description -n libfile1_0
The library implements a heuristic file type determinator,
similar to file/libmagic1.

%package -n libfind4_0
Summary:        A library for /usr/bin/find-like functionality
License:        CDDL-1.0
Group:          System/Libraries
Version:        %libfind_version
Release:        0

%description -n libfind4_0
libfind allows to be used for adding find(1)-like command-line features
to programs.

%package -n libparanoia1_0
Summary:        Compact Disc Digital audio extraction library
License:        LGPL-2.1-only
Group:          System/Libraries
Version:        %cdr_version
Release:        0

%description -n libparanoia1_0
libparanoia is a Compact Disc Digital Audio (CD-DA) Digital Audio
Extraction (DAE) library for reading audio from the CD-ROM directly
as data, with no analog step between. Cdparanoia can read audio data
from inexpensive drives prone to misalignment, frame jitter and loss
of streaming during atomic reads, and attempt to repair data from CDs
that have been damaged in some way by use of the error correction
stored on the disc.

%package -n librmt1_0
Summary:        Remote tape client interface library
License:        CDDL-1.0
Group:          System/Libraries

%description -n librmt1_0
librmt offers a programmatic C interface for creating an IPC
channel to the rmt program.

%package -n librmt-devel-doc
Summary:        Manual pages for librmt functions
License:        CDDL-1.0
Group:          Documentation/Man
BuildArch:      noarch

%description -n librmt-devel-doc
This subpackage contains the manual pages for librmt's functions.

%package -n librscg1_0
Summary:        Remote SCSI user level command transport routines
License:        CDDL-1.0
Group:          System/Libraries

%description -n librscg1_0
A library containing additional routines on top of scg for dealing with
remote SCSI command transports.

%package -n libscg1_0
Summary:        SCSI transport library
License:        CDDL-1.0
Group:          System/Libraries

%description -n libscg1_0
libscg is a SCSI transport library, providing an abstraction
layer from operating systems' mechanisms to issue SCSI commands.

%package -n libscg-devel
Summary:        Development files for libscg, a SCSI transport library
License:        CDDL-1.0
Group:          Development/Libraries/C and C++
Requires:       librscg1_0 = %box_version
Requires:       libscg1_0 = %box_version
Requires:       libscgcmd1_0 = %box_version
Requires:       libschily-devel

%description -n libscg-devel
libscg is a SCSI transport library, providing an abstraction layer
from operating systems' mechanisms to issue SCSI commands.

This subpackage contains the header files for developing applications
that want to make use of libscg.

%package -n libscgcmd1_0
Summary:        SCSI command function library
License:        CDDL-1.0
Group:          System/Libraries

%description -n libscgcmd1_0
A library to create and parse SCSI commands (at the byte level).

%package -n libschily2_0
Summary:        Support library for utilities from the Schily toolbox
License:        CDDL-1.0
Group:          System/Libraries

%description -n libschily2_0
libschily contains many OS abstraction functions used by the Schily
tools.

%package -n libschily-devel
Summary:        Development files for libschily
License:        CDDL-1.0
Group:          Development/Libraries/C and C++
Requires:       libcdrdeflt1_0 = %cdr_version
Requires:       libdeflt1_0 = %box_version
Requires:       libedc_ecc1_0 = %cdr_version
Requires:       libedc_ecc_dec1_0 = %cdr_version
Requires:       libfile1_0 = %box_version
Requires:       libfind4_0 = %libfind_version
Requires:       librmt1_0 = %box_version
Requires:       libschily2_0 = %box_version
Requires:       libxtermcap1_0 = %box_version

%description -n libschily-devel
libschily contains many OS abstraction functions used by the Schily
tools.

This subpackage contains libraries and header files for developing
applications that want to make use of libschily.

%package -n libschily-devel-doc
Summary:        Manual pages for libschily functions
License:        CDDL-1.0
Group:          Documentation/Man
BuildArch:      noarch

%description -n libschily-devel-doc
libschily contains many portability functions used by the Schily
tools.

This subpackage contains manual pages for the APIs exposed by libschily.

%package -n libxtermcap1_0
Summary:        A termcap implementation
License:        CDDL-1.0
Group:          System/Libraries

%description -n libxtermcap1_0
An implementation of termcap, i.e. the termcap C functions tgetent, tputs,
etc., including the parser for the /usr/share/misc/termcap file.

%package -n mkisofs
Summary:        A program to generate an ISO-9660/Joliet/HFS/UDF hybrid filesystem
License:        GPL-2.0-only
Group:          Productivity/Multimedia/CD/Record
Version:        %cdr_version
Release:        0
Requires:       zisofs-tools
Conflicts:      cdrkit-cdrtools-compat

%description -n mkisofs
mkisofs is a pre-mastering program to generate filesystems following
the ISO-9660 specification. It supports the Joliet, Rock Ridge and
Apple extensions, as well as the creation of HFS/ISO-9660 and
UDF/ISO-9660 hybrid filesystem images (images that can be mounted
with either filesystem driver).

%package -n readcd
Summary:        Program to dump raw CD data to files
License:        CDDL-1.0
Group:          Productivity/Multimedia/CD/Record
Version:        %cdr_version
Release:        0
Requires(post): permissions
Provides:       cdrecord:/usr/bin/readcd

%description -n readcd
The readcd program can be used to read optical media and write the
contents, including subchannels and error correction codes, to files.
It can be used to write to DVD-RAM too, but other media types should
use cdrecord which supports a lot more media types.

%package -n rscsi
Summary:        Remote SCSI server
License:        CDDL-1.0
Group:          Productivity/Multimedia/CD/Record
Provides:       cdrecord:/usr/sbin/rscsi

%description -n rscsi
The rscsi command is a remote generic SCSI transport server program.
rscsi is a program that is run locally on the machine with SCSI
devices, it is used by remote programs like cdrecord(1), cdda2wav(1),
readcd(1), and sformat(1) that like to access SCSI devices through an
interprocess communication connection via libscg.  rscsi is normally
started up with an rexec(3) or rcmd(3) call but it may also be
connected via an internal pipe to an ssh(1) session that was set up
by the remote user.

%package mt
Summary:        Magnetic tape control
License:        CDDL-1.0
Group:          Productivity/Archiving/Backup
Provides:       mt
Obsoletes:      star-rmt
Provides:       star-rmt:/usr/bin/smt
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description mt
The mt/smt program sends commands to a local or a remote magnetic
tape drive.

%package rmt
Summary:        Remote magnetic tape protocol server
License:        CDDL-1.0
Group:          Productivity/Archiving/Backup
Provides:       rmt
Obsoletes:      star-rmt
Provides:       star-rmt:/usr/bin/srmt
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description rmt
rmt is a program that can be used by e.g. star and ufsdump
for accessing remote magnetic tape drives and files through an
interprocess communication connection.

A tape client would launch something like ssh for the actual
connection, and through that, have the rmt program executed.

%package -n sccs
Summary:        Source Code Control System
License:        CDDL-1.0
Group:          Development/Tools/Version Control
Conflicts:      delta
Conflicts:      ksh

%description -n sccs
Source Code Control System (SCCS) is a version control system for
tracking changes in source code and other text files during the
development of a piece of software. This allows the user to retrieve
any of the previous versions of the original source code and the
changes which are stored.

%package -n smake
Summary:        The Schily "make" program
License:        CDDL-1.0
Group:          Development/Tools/Building

%description -n smake
Smake executes command sequences based on relations of modification
dates of files. The command sequences are taken from a set of rules
found in a makefile or in the set of implicit rules. The argument
target is typically a program that is to be built from the known
rules.

%package -n spax
Summary:        Portable Archive Exchange
License:        CDDL-1.0
Group:          Productivity/Archiving/Backup
Version:        %star_version
Release:        0
Requires:       star = %star_version
Provides:       pax = 3.5
Obsoletes:      pax < 3.5

%description -n spax
pax is an archiving utility specified by POSIX.1-2001. The format is
basically tar, but with additional extended attributes.

%package -n star
Summary:        tar implementation compliant to POSIX.1-2001
License:        CDDL-1.0
Group:          Productivity/Archiving/Backup
Version:        %star_version
Release:        0

%description -n star
Star is a tar-like archiver (tar standing for Tape ARchiver).

Features:
* FIFO to keep the tape streaming
* Remote tape support
* Accurate sparse files
* Pattern matcher to archive and extract a subset of files
* User tailorable interface for comparing tar archives against file trees
* Path names up to 1024 bytes may be archived
* Stores and restores all 3 file times (even creation time). With POSIX.1-2001,
  the times are in nanosecond granularity.

%package -n ved
Summary:        The Visual Editor
License:        CDDL-1.0
Group:          Productivity/Editors/Other
Version:        %ved_version
Release:        0

%description -n ved
Ved (visual editor) is a screen-oriented editor that implements a
user interface somewhere between vi and emacs. It has almost no
limitations on file size and supports to edit large files (files >2
GB).

%prep
%autosetup -n %name-%rver -p1
find . "(" -type d -o -type f ")" -exec chmod u+w "{}" "+"
cp %{SOURCE1} .

%build
%define _lto_cflags %nil
perl -i -pe 's{\@echo}{echo}' RULES/cc-*
# Static link libhfs, only used by mkisofs.
rm -fv libhfs_iso/shlhfs.mk
# Static link libmdigest, very tiny.
rm -fv libmdigest/shlmdigest.mk
# Static link libshedit, used only by bosh.
rm -fv libshedit/shlshedit.mk
# Static link libsiconv. It forwards to glibc iconv for supported charsets.
rm -fv libsiconv/shlsiconv.mk

# - To enable verbosity, use with CC=cc LDCC=cc DYNLD=cc.
# - Not fully parallel safe, so stick to default.
#
mycf="%optflags -fno-strict-aliasing -fno-omit-frame-pointer -fPIC -finput-charset=ISO-8859-1 -fcommon"
gmake RUNPATH="" LINKMODE=dynamic COPTOPT="$mycf" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" config
gmake RUNPATH="" LINKMODE=dynamic COPTOPT="$mycf" LDOPTX="" SCCS_BIN_PRE="" SCCS_HELP_PRE="" all

%install
b="%buildroot"
# D'oh… not parallel safe
gmake GMAKE_NOWARN=true RUNPATH="" LINKMODE=dynamic SCCS_BIN_PRE="" \
	SCCS_HELP_PRE="" DESTDIR="$b" INS_BASE="%_prefix" install -j1
# Fix permissions again.
find "$b" "(" -type d -o -type f ")" -exec chmod u+w "{}" "+"

if test "%_lib" != lib; then
	mkdir -p "$b/%_libdir"
	mv "$b/%_prefix/lib"/* "$b/%_libdir/"
fi
find "$b/%_libdir" -type f -name "*.a" -print -delete
find "$b/%_libdir" -type f -name "*.so.*" -exec chmod a+x "{}" "+"

# Install documentation
mkdir -p "%_docdir"
for i in "$b/%_datadir/doc"/*; do
	test "$i" != "$b/%_docdir" && mv "$i" "$b/%_docdir/"
done
install -Dm 644 "%_sourcedir/README-FIRST" "$b/%_docdir/schily-rmt"

# bosh
mv -fv "$b/%_bindir/sh" "$b/%_bindir/bosh"
mv -fv "$b/%_mandir/man1/sh.1" "$b/%_mandir/man1/bosh.1"
ln -fsv bosh.1 "$b/%_mandir/man1/jsh.1"
ln -fsv bosh.1 "$b/%_mandir/man1/pfsh.1"
ln -fsv bosh.1 "$b/%_mandir/man1/pbosh.1"
ln -fsv bosh "$b/%_bindir/jsh"
ln -fsv bosh "$b/%_bindir/pfsh"

# Additional cdda2wav programs
install -pm 0755 cdda2wav/{cdda2mp3.new,inf2cdtext.pl,pitchplay,readmult,tracknames.pl} \
	mkisofs/hdisk.pl "$b/%_bindir/"
# Needed by cdda2wav (see cdda2wav.c)
ln -sf cdda2wav "$b/%_bindir/list_audio_tracks"
# Fix perl path
perl -pi -e 's#/usr/local/bin/perl#%_bindir/perl#g' "$b/%_bindir/tracknames.pl"
# Rename in order to not conflict with mkisofs/README in rpm doc section
#mv mkisofs/diag/README mkisofs/diag/README.diag

# libsiconv. tries to use libc's iconv first before trying its own tables.
rm -Rfv "$b/%_datadir/lib/siconv"

# spax/star
ln -sfv spax "$b/%_bindir/pax"
rm -fv "$b/%_bindir/tar" "$b/%_bindir/gnutar"

# Do not ship star_sym and suntar
rm -fv "$b/%_bindir/star_sym"
rm -fv "$b/%_bindir/suntar"
rm -fv "$b/%_mandir/man1/star_sym.1"
rm -fv "$b/%_mandir/man1/suntar.1"

# ctags
mv -v "$b/%_bindir/ctags" "$b/%_bindir/ctags-schily"
cp -v ctags/vctags.1 "$b/%_mandir/man1/"

# mt/rmt
rm -fv "$b/%_bindir/mt" # handled up u-a
ln -sv smt.1 "$b/%_mandir/man1/mt.1"
ln -sv srmt.1 "$b/%_mandir/man1/rmt.1"

# get rid of things that upset rpmlint
find "$b/usr/share/doc" -type f -name "*big*" -print -delete

# deal with this another time
find "$b"
rm -Rfv "$b/usr/ccs" "$b/usr/xpg4" "$b/%_bindir/sccs"
rm -Rfv \
   $b/etc/sformat.dat \
   $b/usr/etc/termcap \
   $b/usr/bin/Cstyle \
   $b/usr/bin/cal \
   $b/usr/bin/calc \
   $b/usr/bin/calltree \
   $b/usr/bin/change \
   $b/usr/bin/compare \
   $b/usr/bin/copy \
   $b/usr/bin/count \
   $b/usr/bin/cstyle.js \
   $b/usr/bin/diff \
   $b/usr/bin/dmake \
   $b/usr/bin/hdump \
   $b/usr/bin/krcpp \
   $b/usr/bin/label \
   $b/usr/bin/lndir \
   $b/usr/bin/make \
   $b/usr/bin/man2html \
   $b/usr/bin/match \
   $b/usr/bin/mdigest \
   $b/usr/bin/od \
   $b/usr/bin/opatch \
   $b/usr/bin/p \
   $b/usr/bin/printf \
   $b/usr/bin/pxupgrade \
   $b/usr/bin/scgcheck \
   $b/usr/bin/scgskeleton \
   $b/usr/bin/scut \
   $b/usr/bin/sfind \
   $b/usr/bin/sformat \
   $b/usr/bin/sgrow \
   $b/usr/bin/sh \
   $b/usr/bin/spaste \
   $b/usr/bin/spatch \
   $b/usr/bin/strar \
   $b/usr/bin/svr4.make \
   $b/usr/bin/termcap \
   $b/usr/bin/translit \
   $b/usr/lib*/cpp \
   $b/usr/lib*/libmakestate.so \
   $b/usr/lib*/libmakestate.so.1.0 \
   $b/usr/lib*/libhfs.so \
   $b/usr/lib*/libshedit.so \
   $b/usr/lib*/libstreamar.so \
   $b/usr/lib*/libstreamar.so.1.0 \
   $b/usr/lib*/svr4.make \
   $b/%_libdir/help/ \
   $b/%_libdir/diffh \
   $b/usr/sbin/mountcd \
   $b/usr/share/doc/packages/README \
   $b/usr/share/doc/packages/libparanoia/README.interface \
   $b/usr/share/doc/packages/libparanoia/README.paranoia \
   $b/usr/share/doc/packages/bsh/dotfiles.tar.bz2 \
   $b/usr/share/man/de/man1/sdd.1 \
   $b/usr/share/man/man1/cal.1 \
   $b/usr/share/man/man1/calc.1 \
   $b/usr/share/man/man1/calltree.1 \
   $b/usr/share/man/man1/change.1 \
   $b/usr/share/man/man1/compare.1 \
   $b/usr/share/man/man1/copy.1 \
   $b/usr/share/man/man1/count.1 \
   $b/usr/share/man/man1/cpp.1 \
   $b/usr/share/man/man1/cstyle.1 \
   $b/usr/share/man/man1/diff.1 \
   $b/usr/share/man/man1/dmake.1 \
   $b/usr/share/man/man1/gnutar.1 \
   $b/usr/share/man/man1/hdump.1 \
   $b/usr/share/man/man1/krcpp.1 \
   $b/usr/share/man/man1/label.1 \
   $b/usr/share/man/man1/lndir.1 \
   $b/usr/share/man/man1/make.1 \
   $b/usr/share/man/man1/man2html.1 \
   $b/usr/share/man/man1/match.1 \
   $b/usr/share/man/man1/mdigest.1 \
   $b/usr/share/man/man1/mountcd.1 \
   $b/usr/share/man/man1/od.1 \
   $b/usr/share/man/man1/opatch.1 \
   $b/usr/share/man/man1/p.1 \
   $b/usr/share/man/man1/patch.1 \
   $b/usr/share/man/man1/printf.1 \
   $b/usr/share/man/man1/pxupgrade.1 \
   $b/usr/share/man/man1/scgcheck.1 \
   $b/usr/share/man/man1/scgskeleton.1 \
   $b/usr/share/man/man1/scut.1 \
   $b/usr/share/man/man1/sfind.1 \
   $b/usr/share/man/man1/sgrow.1 \
   $b/usr/share/man/man1/spaste.1 \
   $b/usr/share/man/man1/spatch.1 \
   $b/usr/share/man/man1/strar.1 \
   $b/usr/share/man/man1/sysV-make.1 \
   $b/usr/share/man/man1/tartest.1 \
   $b/usr/share/man/man1/termcap.1 \
   $b/usr/share/man/man1/translit.1 \
   $b/usr/share/man/man3/getopt.3 \
   $b/usr/share/man/man3/getsubopt.3 \
   $b/usr/share/man/man3/starthandlecond.3 \
   $b/usr/share/man/man3/unhandlecond.3 \
   $b/usr/share/man/man5/makefiles.5 \
   $b/usr/share/man/man5/makerules.5 \
   $b/usr/share/man/man5/streamarchive.5 \
   $b/usr/share/man/man8/sformat.8 \
   $b/usr/share/doc/packages/dotfiles.tar.bz2

# Remove documentation (will be added in %_datadir/doc/packages/*)
#rm -Rf "$b/%_datadir/doc"/*

%fdupes -s %buildroot/%_prefix

%check
locale
export LD_LIBRARY_PATH="$(find "$PWD" -type d -name pic | perl -pe 's{\n}{:}gs')"
NO_RANDOM=TRUE make tests || :

%post -n cdrecord
%set_permissions %_bindir/cdrecord
true

%post -n cdda2wav
%set_permissions %_bindir/cdda2wav
true

%post ctags
"%_sbindir/update-alternatives" \
	--install "%_bindir/ctags" ctags "%_bindir/ctags-schily" 20
"%_sbindir/update-alternatives" --auto ctags

%postun ctags
if test "$1" = 0; then
	"%_sbindir/update-alternatives" --remove ctags "%_bindir/ctags-schily"
fi

%post -n readcd
%set_permissions %_bindir/readcd
true

%post mt
"%_sbindir/update-alternatives" \
	--install "%_bindir/mt" mt "%_bindir/smt" 10 \
	--slave "%_mandir/man1/mt.1%ext_man" "mt.1%ext_man" "%_mandir/man1/smt.1%ext_man"
"%_sbindir/update-alternatives" --auto mt

%postun mt
if test "$1" = 0; then
	"%_sbindir/update-alternatives" --remove mt "%_bindir/smt"
fi

%post rmt
"%_sbindir/update-alternatives" \
	--install "%_bindir/rmt" rmt "%_bindir/srmt" 10 \
	--slave "%_mandir/man1/rmt.1%ext_man" "rmt.1%ext_man" "%_mandir/man1/srmt.1%ext_man"
"%_sbindir/update-alternatives" --auto rmt

%postun rmt
if test "$1" = 0; then
	"%_sbindir/update-alternatives" --remove rmt "%_bindir/srmt"
fi

%post   -n libcdrdeflt1_0 -p /sbin/ldconfig
%postun -n libcdrdeflt1_0 -p /sbin/ldconfig
%post   -n libdeflt1_0 -p /sbin/ldconfig
%postun -n libdeflt1_0 -p /sbin/ldconfig
%post   -n libedc_ecc1_0 -p /sbin/ldconfig
%postun -n libedc_ecc1_0 -p /sbin/ldconfig
%post   -n libedc_ecc_dec1_0 -p /sbin/ldconfig
%postun -n libedc_ecc_dec1_0 -p /sbin/ldconfig
%post   -n libfile1_0 -p /sbin/ldconfig
%postun -n libfile1_0 -p /sbin/ldconfig
%post   -n libfind4_0 -p /sbin/ldconfig
%postun -n libfind4_0 -p /sbin/ldconfig
%post   -n libparanoia1_0 -p /sbin/ldconfig
%postun -n libparanoia1_0 -p /sbin/ldconfig
%post   -n librmt1_0 -p /sbin/ldconfig
%postun -n librmt1_0 -p /sbin/ldconfig
%post   -n librscg1_0 -p /sbin/ldconfig
%postun -n librscg1_0 -p /sbin/ldconfig
%post   -n libscg1_0 -p /sbin/ldconfig
%postun -n libscg1_0 -p /sbin/ldconfig
%post   -n libscgcmd1_0 -p /sbin/ldconfig
%postun -n libscgcmd1_0 -p /sbin/ldconfig
%post   -n libschily2_0 -p /sbin/ldconfig
%postun -n libschily2_0 -p /sbin/ldconfig
%post   -n libxtermcap1_0 -p /sbin/ldconfig
%postun -n libxtermcap1_0 -p /sbin/ldconfig

%verifyscript -n cdrecord
%verify_permissions -e %_bindir/cdrecord

%verifyscript -n cdda2wav
%verify_permissions -e %_bindir/cdda2wav

%verifyscript -n readcd
%verify_permissions -e %_bindir/readcd

%files -n bosh
%license CDDL.Schily.txt
%_bindir/bsh
%_bindir/bosh
%_bindir/jsh
%_bindir/obosh
%_bindir/pbosh
%_bindir/pfbsh
%_bindir/pfsh
%_mandir/man1/bsh.1*
%_mandir/man1/bosh.1*
%_mandir/man1/jsh.1*
%_mandir/man1/obosh.1*
%_mandir/man1/pbosh.1*
%_mandir/man1/pfbsh.1*
%_mandir/man1/pfsh.1*

%files -n btcflash
%license CDDL.Schily.txt COPYING
%_bindir/btcflash
%_mandir/man1/btcflash.1*

%files -n cdda2wav
%license CDDL.Schily.txt
%doc cdda2wav/Changelog cdda2wav/FAQ cdda2wav/Frontends cdda2wav/HOWTOUSE
%doc cdda2wav/NEEDED cdda2wav/README cdda2wav/THANKS cdda2wav/TODO
%doc cdda2wav/tracknames.txt
%_bindir/cdda2mp3
%_bindir/cdda2mp3.new
%_bindir/cdda2ogg
%attr(0755,root,root) %verify(not mode caps) %_bindir/cdda2wav
%_bindir/inf2cdtext.pl
%_bindir/list_audio_tracks
%_bindir/pitchplay
%_bindir/readmult
%_bindir/tracknames.pl
%_mandir/man1/cdda2mp3.1*
%_mandir/man1/cdda2ogg.1*
%_mandir/man1/cdda2wav.1*

%files -n cdrecord
%license CDDL.Schily.txt
%doc cdrecord/README*
%config %_sysconfdir/default/cdrecord
%verify(not mode caps) %attr(0755,root,root) %_bindir/cdrecord
%_mandir/man1/cdrecord.1*

%files ctags
%license CDDL.Schily.txt
%_bindir/ctags-schily
%_bindir/vctags
%_mandir/man1/vctags.1*

%files -n libcdrdeflt1_0
%license CDDL.Schily.txt
%_libdir/libcdrdeflt.so.1.0

%files -n libdeflt1_0
%license CDDL.Schily.txt
%_libdir/libdeflt.so.1.0

%files -n libedc_ecc1_0
%license CDDL.Schily.txt
%_libdir/libedc_ecc.so.1.0

%files -n libedc_ecc_dec1_0
%license CDDL.Schily.txt
%_libdir/libedc_ecc_dec.so.1.0

%files -n libfile1_0
%license libfile/LEGAL.NOTICE
%_libdir/libfile.so.1.0

%files -n libfind4_0
%license CDDL.Schily.txt
%_libdir/libfind.so.4.0

%files -n libparanoia1_0
%license libparanoia/LICENSE
%doc libparanoia/README*
%_libdir/libparanoia.so.1.0

%files -n librmt1_0
%license CDDL.Schily.txt
%_libdir/librmt.so.1.0

%files -n librmt-devel-doc
%_mandir/man3/librmt.3*
%_mandir/man3/mtg2rmtg.3*
%_mandir/man3/rmt*.3*

%files -n librscg1_0
%license CDDL.Schily.txt
%_libdir/librscg.so.1.0

%files -n libscg1_0
%license CDDL.Schily.txt
%_libdir/libscg.so.1.0

%files -n libscgcmd1_0
%license CDDL.Schily.txt
%_libdir/libscgcmd.so.1.0

%files -n libscg-devel
%_includedir/scg/
%_libdir/librscg.so
%_libdir/libscg.so
%_libdir/libscgcmd.so

%files -n libschily2_0
%license CDDL.Schily.txt
%_libdir/libschily.so.2.0

%files -n libschily-devel
%_includedir/schily/
%_libdir/libcdrdeflt.so
%_libdir/libdeflt.so
%_libdir/libedc_ecc.so
%_libdir/libedc_ecc_dec.so
%_libdir/libfile.so
%_libdir/libfind.so
%_libdir/libparanoia.so
%_libdir/librmt.so
%_libdir/libschily.so
%_libdir/libxtermcap.so

%files -n libschily-devel-doc
%_mandir/man3/absfpath.3*
%_mandir/man3/absnpath.3*
%_mandir/man3/abspath.3*
%_mandir/man3/astoi.3*
%_mandir/man3/astol.3*
%_mandir/man3/breakline.3*
%_mandir/man3/cmpbytes.3*
%_mandir/man3/comerr.3*
%_mandir/man3/comerrno.3*
%_mandir/man3/errmsg.3*
%_mandir/man3/errmsgno.3*
%exclude %_mandir/man3/error.3*
%_mandir/man3/fdown.3*
%_mandir/man3/fdup.3*
%_mandir/man3/fexecl.3*
%_mandir/man3/fexecle.3*
%_mandir/man3/fexecv.3*
%exclude %_mandir/man3/fexecve.3*
%_mandir/man3/fgetline.3*
%_mandir/man3/file_raise.3*
%_mandir/man3/fileclose.3*
%_mandir/man3/fileluopen.3*
%_mandir/man3/fileopen.3*
%_mandir/man3/filepos.3*
%_mandir/man3/fileread.3*
%_mandir/man3/filereopen.3*
%_mandir/man3/fileseek.3*
%_mandir/man3/filesize.3*
%_mandir/man3/filestat.3*
%_mandir/man3/filewrite.3*
%_mandir/man3/findline.3*
%_mandir/man3/flush.3*
%exclude %_mandir/man3/fnmatch.3*
%_mandir/man3/format.3*
%_mandir/man3/fpipe.3*
%exclude %_mandir/man3/fprintf.3*
%_mandir/man3/getallargs.3*
%_mandir/man3/getargerror.3*
%_mandir/man3/getarginit.3*
%_mandir/man3/getargs.3*
%_mandir/man3/geterrno.3*
%_mandir/man3/getfiles.3*
%_mandir/man3/getlallargs.3*
%_mandir/man3/getlargs.3*
%_mandir/man3/getlfiles.3*
%exclude %_mandir/man3/getline.3*
%_mandir/man3/getvallargs.3*
%_mandir/man3/getvargs.3*
%_mandir/man3/getvfiles.3*
%_mandir/man3/handlecond.3*
%_mandir/man3/movebytes.3*
%_mandir/man3/ofindline.3*
%_mandir/man3/patcompile.3*
%_mandir/man3/patmatch.3*
%_mandir/man3/peekc.3*
%exclude %_mandir/man3/printf.3*
%_mandir/man3/raisecond.3*
%_mandir/man3/resolvefpath.3*
%_mandir/man3/resolvenpath.3*
%_mandir/man3/resolvepath.3*
%_mandir/man3/spawnl.3*
%_mandir/man3/spawnv.3*
%exclude %_mandir/man3/sprintf.3*
%_mandir/man3/strcatl.3*
%_mandir/man3/streql.3*
%exclude %_mandir/man3/strlen.3*

%files -n libxtermcap1_0
%license CDDL.Schily.txt
%_libdir/libxtermcap.so.1.0

%files -n mkisofs
%license mkisofs/COPYING
%doc mkisofs/ChangeLog mkisofs/ChangeLog.mkhybrid mkisofs/README*
%doc mkisofs/RELEASE
%_bindir/devdump
%_bindir/hdisk.pl
%_bindir/isodebug
%_bindir/isodump
%_bindir/isoinfo
%_bindir/isovfy
%_bindir/mkhybrid
%_bindir/mkisofs
%_mandir/man8/devdump.8*
%_mandir/man8/isodebug.8*
%_mandir/man8/isodump.8*
%_mandir/man8/isoinfo.8*
%_mandir/man8/isovfy.8*
%_mandir/man8/mkhybrid.8*
%_mandir/man8/mkisofs.8*

%files -n readcd
%license CDDL.Schily.txt
%_bindir/readcd
%_bindir/sdd
%_mandir/man1/readcd.1*
%_mandir/man1/sdd.1*

%files -n rscsi
%license CDDL.Schily.txt
%config %_sysconfdir/default/rscsi
%_docdir/rscsi/
%_sbindir/rscsi
%_mandir/man1/rscsi.1*

%files -n sccs
%_bindir/admin
%_bindir/bdiff
%_bindir/cdc
%_bindir/comb
%_bindir/delta
%_bindir/fdiff
%_bindir/fsdiff
%_bindir/get
%_bindir/help
%_bindir/prs
%_bindir/prt
%_bindir/rcs2sccs
%_bindir/rmchg
%_bindir/rmdel
%_bindir/sact
%_bindir/sccscvt
%_bindir/sccsdiff
%_bindir/sccslog
%_bindir/udiff
%_bindir/unget
%_bindir/val
%_bindir/vc
%_bindir/what
%_mandir/man1/admin.1*
%_mandir/man1/bdiff.1*
%_mandir/man1/cdc.1*
%_mandir/man1/comb.1*
%_mandir/man1/delta.1*
%_mandir/man1/fdiff.1*
%_mandir/man1/fsdiff.1*
%_mandir/man1/get.1*
%_mandir/man1/help.1*
%_mandir/man1/prs.1*
%_mandir/man1/prt.1*
%_mandir/man1/rcs2sccs.1*
%_mandir/man1/rmdel.1*
%_mandir/man1/sact.1*
%_mandir/man1/sccs*.1*
%_mandir/man1/udiff.1*
%_mandir/man1/unget.1*
%_mandir/man1/val.1*
%_mandir/man1/vc.1*
%_mandir/man1/what.1*
%_mandir/man5/changeset.5*
%_mandir/man5/sccs*.5*

%files -n schily-mt
%license CDDL.Schily.txt
%_bindir/smt
%_mandir/man1/smt.1*
%ghost %_sysconfdir/alternatives/mt
%ghost %_sysconfdir/alternatives/mt.1%ext_man
%ghost %_mandir/man1/mt.1%ext_man

%files -n schily-rmt
%license CDDL.Schily.txt
%config(noreplace) %_sysconfdir/default/rmt
%_docdir/rmt/
%_docdir/schily-rmt
%_bindir/srmt
%_mandir/man1/srmt.1*
%ghost %_sysconfdir/alternatives/rmt
%ghost %_sysconfdir/alternatives/rmt.1%ext_man
%ghost %_mandir/man1/rmt.1%ext_man

%files -n smake
%_bindir/smake
%_datadir/lib/
%_mandir/man1/smake.1*

%files -n spax
%license CDDL.Schily.txt
%_bindir/pax
%_bindir/spax
%_mandir/man1/spax.1*

%files -n star
%license CDDL.Schily.txt
%doc AN-*
%config(noreplace) %_sysconfdir/default/star
%_bindir/fifo
%_bindir/scpio
%_bindir/star
%_bindir/tartest
%_bindir/ustar
%_docdir/star/
%_mandir/man1/fifo.1*
%_mandir/man1/scpio.1*
%_mandir/man1/star.1*
%_mandir/man1/ustar.1*
%_mandir/man5/star.5*

%files -n ved
%_bindir/ved*
%_mandir/help/
%_mandir/man1/ved*.1*
%_docdir/ved/

%changelog
