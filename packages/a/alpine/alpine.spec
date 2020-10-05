#
# spec file for package alpine
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


Name:           alpine
# For debugging only:
%define		build_vanilla		0
Version:        2.23.2
Release:        0
Summary:        Mail User Agent
License:        Apache-2.0
Group:          Productivity/Networking/Email/Clients
URL:            http://alpine.x10host.com/alpine/
#Git-Clone:     https://repo.or.cz/alpine.git

#Source:         http://alpine.x10host.com/alpine/release/src/%name-%version.tar.xz
Source:         %name-%version.tar.xz
Source1:        %name.png
Source2:        %name.desktop
Source9:        UPDATING.txt
Patch2:         make-use-of-strncat-safer.diff
Patch3:         operation-may-be-undefined-warning.diff
Patch4:         fix-implicit.patch
Patch5:         alpine-gcc44.diff
Patch6:         alpine-timestamp.patch
Patch10:        pico-fix-spurious-undef-warnings.diff
Patch20:        pine-expression-warnings.diff
Patch60:        signal-and-panic-improvements.diff
Patch61:        return-values.diff
#
# Eduardo Chappa's patches.
# http://patches.freeiz.com/alpine/
#
Source600:      chappa-colortext.txt
Patch600:       chappa-colortext.patch
Source601:      chappa-fancy.txt
Patch601:       chappa-fancy.patch
Source603:      chappa-insertpat.txt
Patch603:       chappa-insertpat.patch
Source604:      chappa-maildir.txt
Patch604:       chappa-maildir.patch
Source605:      chappa-WrtAcc.txt
Patch605:       chappa-WrtAcc.patch
Source614:      chappa-fillpara.txt
Patch614:       chappa-fillpara.patch
Source615:      chappa-fromheader.txt
Patch615:       chappa-fromheader.patch
Source616:      chappa-rules.txt
Patch616:       chappa-rules.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
# pgp4pine requires pine: (6.20 is what alpine writes to ~/.pinerc)
Provides:       pine = 6.20
Obsoletes:      pine4
Provides:       pine4

%description
Alpine is a display-oriented email client that is suitable for both
the inexperienced email user as well as for the most demanding of
power users. Alpine is based on the Pine® Message System, which was
also developed at the University of Washington. Alpine can be learned
by exploration and the use of context-sensitive help. The user
experience is highly customizable through the use of the Alpine Setup
command.

%package -n pico
Summary:        A small, easy to use editor
Group:          Productivity/Editors/Other
Version:        5.07
Release:        0

%description -n pico
Pico is a simple, display-oriented text editor based on the Pine
message system composer. As with Pine, commands are displayed at the
bottom of the screen, and context-sensitive help is provided.
Characters are inserted into the text as they are typed.

%package -n pilot
Summary:        Simple file system browser
Group:          Productivity/File utilities
Version:        2.99
Release:        0

%description -n pilot
Pilot is a simple, display-oriented file system browser based on the
Pine message system composer. As with Pine, commands are displayed at
the bottom of the screen, and context-sensitive help is provided.

%prep
%setup -q
%if !0%{?build_vanilla}
#
# This is here to support checking if any patches add new warnings:
#
if [ ! -s %{_sourcedir}/compile-warnings-%{suse_version}-%{_arch}.log ]; then
	echo "No warnings check possible, set build_vanilla to 1 and"
	echo "add compile-warnings-%{suse_version}-%{_arch}.log from"
	echo "that build to the rpm build process so that it's found here".
else
	sed 's/:[0-9]*//' %{_sourcedir}/compile-warnings-%{suse_version}-%{_arch}.log \
		>compile-warnings-allowed.log
fi
#
# "Chappa" patches
#
%patch600 -p1
%patch601 -p1
%patch603 -p1
%patch604 -p1
%patch605 -p1
%patch614 -p1
%patch615 -p1
%patch616 -p1
#
# SuSE patches - warning fixes, etc:
#
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch10 -p1
%patch20 -p1
%patch60 -p1
%patch61 -p1
%endif

%build
#
# Comment on disabled warnings: The disabled warnings are rather harmless
# and disabling them allows to focus on the really serious warnings:
#
export CFLAGS="${RPM_OPT_FLAGS/-O2/-Os} \
		-Wno-unused-value -fno-strict-aliasing -Wno-pointer-sign -Wno-unused \
		-Wno-address \
"
#
# On -Waddress:
#
# Added with gcc-4.2: It warns when the address of a variable (not a pointer)
# is used in an expression. Since addresses of variables are always non-zero,
# they are always true and can be safely removed from the expression,
# but the code is safe nontheless.
#
# -Waddress generates >100 warnings in alpine and we disabled them to
# concentrate on the really important warnings which could be real bugs better.
#
:
#
# Used in conjunction with signal-and-panic-improvements.diff:
#
export LDFLAGS="-rdynamic" # -rdynamic is used for backtrace_symbols:
:
autoreconf -fiv
%configure \
	--with-ssl-dir="%{_prefix}"			\
	--with-smtp-msa="%{_sbindir}/sendmail"		\
	--with-password-prog="%{_bindir}/passwd"	\
	--with-npa="%{_bindir}/inews"			\
	--with-spellcheck-prog="please set Speller to eg. 'aspell -c' in SETUP/Configuration"\
	--with-system-pinerc=%_sysconfdir/pine.conf		\
	--with-system-fixed-pinerc=%_sysconfdir/pine.conf.fixed \
	--with-debug-level=0				\
	--with-debug-files=2				\
	--with-file=.alpine-debug			\
	--with-default-mail-directory=Mail		\
	--with-web-bin=%_libdir/%name                   \
	--with-passfile=.pinepw || {
	grep -B9 -A20 'failed program was' config.log | grep -A24 checking
	exit 5
}
%{?fedora_version: tag=LFD}
%{?mandriva_version: tag=LMD}
%{?redhat_version: tag=LRH}
%{?centos_version: tag=LRH}
%{?suse_version: tag=LSU}
perl -i -pe 's{(define SYSTYPE) "LNX"}{$1 "'"$tag"'"}g' include/config.h

#
# imap does not use CFLAGS from configure, needs EXTRACFLAGS/EXTRALDFLAGS:
#
%make_build EXTRACFLAGS="$CFLAGS" EXTRALDFLAGS="$EXTRALDFLAGS"

%install
%make_install
#
# When called as alpinef, alpine uses function keys instead of Control keys:
#
ln %{buildroot}/%{_bindir}/alpine %{buildroot}/%{_bindir}/alpinef
install -D -m644 %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/%name.png
install -D -m644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%name.desktop
%suse_update_desktop_file %name
:
ln -sf		 alpine			%{buildroot}/%{_bindir}/pine
:
install -m755 pico/{pico,pilot}		%{buildroot}/%{_bindir}
install -m644 doc/man1/{pico.1,pilot.1}	%{buildroot}/%{_mandir}/man1/

%check
#since there are no logs in the package at the moment, there are no checks,
#but the warning logs can be recreated for regression tracking in warnings:
if [  -s %{_sourcedir}/compile-warnings-%{suse_version}-%{_arch}.log ]; then
    grep -e '^[a-z0-9_]*.[cho]:' -e 'Entering directory' make.log |
	sed "s/^make\[.\]: //;/Entering directory/s/[\`']//g;" \
	>compile-warnings-%{suse_version}-%{_arch}.log
    # Sort the combined allowed warnings:
    grep -v -e 'In function' -e 'Entering directory' \
	compile-warnings-allowed.log |
	    sort -u > compile-warnings-%{suse_version}-%{_arch}-reference.sort
    # Sort the warnings which occured now:
    grep -v -e 'In function' -e 'Entering directory' \
	compile-warnings-%{suse_version}-%{_arch}.log |
	    sed 's/:[0-9]*//' | sort -u \
		>compile-warnings-%{suse_version}-%{_arch}-thisbuild.sort
    # diff them:
    diff compile-warnings-%{suse_version}-%{_arch}-{reference,thisbuild}.sort |
	tee	  compile-warnings-%{suse_version}-%{_arch}-sorted.diff
    if test    -s compile-warnings-%{suse_version}-%{_arch}-sorted.diff; then
	grep '^>' compile-warnings-%{suse_version}-%{_arch}-sorted.diff >new-warnings ||:
	if [ -s new-warnings ]; then
		diff -u %{_sourcedir}/compile-warnings-%{suse_version}-%{_arch}.log \
			compile-warnings-%{suse_version}-%{_arch}.log ||
		echo "New warnings:"
		cat new-warnings
		sed 's/> //;s/:/:[0-9]*:/' new-warnings >new-warnings.pattern
		: diff:  %_builddir}/compile-warnings-%{suse_version}-%{_arch}-sorted.diff
		grep -B1 -f new-warnings.pattern compile-warnings-%{suse_version}-%{_arch}.log
		grep -e 'Entering directory' -f new-warnings.pattern \
			compile-warnings-%{suse_version}-%{_arch}.log |
				grep -B1 -f new-warnings.pattern |
					tee warnings.where
		while IFS='[: ]' read file line message; do
			if [ "$file" = Entering ]; then
				dir="${message#%_builddir/%buildsubdir/}"
			else
				path="$dir/$file"
				echo "$path:$line: $message"	>>warnings-with-code
				head -"$line" "$path"|tail -1	>>warnings-with-code
			fi
		done <warnings.where
		cat warnings-with-code
		exit 5
	else
		echo "Fixed warnings:"
		grep '^<' compile-warnings-%{suse_version}-%{_arch}-sorted.diff
	fi
    else
	echo "No fixed warnings and no new warnings"
    fi
fi

%files
%doc %{_mandir}/man1/alpine.*
%doc %{_mandir}/man1/rpdump.*
%doc %{_mandir}/man1/rpload.*
%doc README
%license LICENSE NOTICE
%doc doc/mailcap.unx doc/mime.types doc/tech-notes/tech-notes.txt doc/tech-notes/*.html
%{_bindir}/*pine
%{_bindir}/alpinef
%{_bindir}/rp*
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/%name.png

%files -n pico
%{_bindir}/pico
%doc %{_mandir}/man1/pico.*

%files -n pilot
%{_bindir}/pilot
%doc %{_mandir}/man1/pilot.*

%changelog
