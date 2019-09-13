#
# spec file for package patterns-openSUSE
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


%bcond_with betatest

Name:           patterns-devel-base
Version:        20170319
Release:        0
Summary:        Patterns for Installation (base devel patterns)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
Source1:        pattern-definition-32bit.txt
Source2:        create_32bit-patterns_file.pl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the base development patterns (and the other
development patterns that don't fit well anywhere else).

################################################################################

%package devel_basis
%pattern_development
Summary:        Base Development
Group:          Metapackages
Provides:       pattern() = devel_basis
Provides:       pattern-icon() = pattern-basis-devel
Provides:       pattern-order() = 3140
Provides:       pattern-visible()
%if ! 0%{?is_opensuse}
Provides:       patterns-sles-Basis-Devel = %{version}
Provides:       patterns-sled-Basis-Devel = %{version}
Obsoletes:      patterns-sles-Basis-Devel < %{version}
Obsoletes:      patterns-sled-Basis-Devel < %{version}
%endif
Requires:       pattern() = basesystem

Requires:       autoconf
Requires:       automake
Requires:       binutils
Requires:       bison
Requires:       cpp
Requires:       flex
Requires:       gcc
Requires:       gdbm-devel
Requires:       gettext-tools
Requires:       glibc-devel
Requires:       libtool
Requires:       m4
Requires:       make
Requires:       makeinfo
Requires:       ncurses-devel
Requires:       patch
Requires:       zlib-devel
Recommends:     bin86
Recommends:     db-devel
Recommends:     gcc-c++
Recommends:     gcc-info
Recommends:     git
Recommends:     glibc-info
Recommends:     gmp-devel
Recommends:     gperf
Recommends:     libaio-devel
Recommends:     libgcj-devel
Recommends:     libstdc++-devel
Recommends:     openldap2-devel
Recommends:     pam-devel
Recommends:     pkg-config
Recommends:     subversion
# most of our packages use this tool
Recommends:     fdupes
# applying patches
Recommends:     patch
Recommends:     binutils-devel
Recommends:     e2fsprogs-devel
Recommends:     libapparmor-devel
Recommends:     libosip2-devel
Suggests:       build
# bnc#804006
Suggests:       osc
Suggests:       gcc-fortran
Suggests:       gcc-objc
# Matz thinks people want that
Suggests:       mpfr-devel
Suggests:       ccache
Suggests:       icecream
Suggests:       subversion-doc
Suggests:       wiggle
Suggests:       oprofile
Suggests:       libgssglue-devel
Suggests:       audit-devel
Suggests:       nasm

%description devel_basis
Minimal set of tools for compiling and linking applications.

%files devel_basis
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_basis.txt

################################################################################

%package devel_kernel
%pattern_development
Summary:        Linux Kernel Development
Group:          Metapackages
Provides:       pattern() = devel_kernel
Provides:       pattern-icon() = pattern-kernel-devel
Provides:       pattern-order() = 3320
Provides:       pattern-visible()
Requires:       pattern() = devel_basis

Recommends:     kernel-source
# bnc#582415
Recommends:     ctags
Recommends:     diffstat
Recommends:     git-core
Recommends:     indent
Recommends:     patchutils
Recommends:     quilt
Recommends:     gitk
Recommends:     git-email
Recommends:     kernel-syms
Suggests:       kernel-debug
Suggests:       gitk
Suggests:       kernel-docs
Suggests:       cscope

%description devel_kernel
Tools for Linux kernel development.

%files devel_kernel
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_kernel.txt

################################################################################

%if 0%{?is_opensuse}
%package devel_rpm_build
%pattern_development
Summary:        RPM Build Environment
Group:          Metapackages
Provides:       pattern() = devel_rpm_build
Provides:       pattern-icon() = pattern-rpm-devel
Provides:       pattern-order() = 3280
Provides:       pattern-visible()
Requires:       pattern() = basesystem

Requires:       man
Requires:       netcfg
Requires:       rpm-build
Recommends:     libtool
Suggests:       build
Suggests:       inst-source-utils
Suggests:       libsolv-devel

%description devel_rpm_build
Minimal set of tools and libraries for building packages using the RPM package manager.

%files devel_rpm_build
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_rpm_build.txt
%endif

################################################################################

%if 0%{?is_opensuse}
%package devel_web
%pattern_development
Summary:        Web Development
Group:          Metapackages
Provides:       pattern() = devel_web
Provides:       pattern-icon() = pattern-web-devel
Provides:       pattern-order() = 3440
Provides:       pattern-visible()
Requires:       pattern() = lamp_server

Recommends:     apache2-devel
Suggests:       html-dtd
Suggests:       iso_ent
Suggests:       latex2html
Suggests:       perl-CGI-Application
Suggests:       perl-HTML-Clean
Suggests:       perl-HTML-FillInForm
Suggests:       perl-HTML-Format
Suggests:       perl-HTML-SimpleParse
Suggests:       perl-HTML-Tagset
Suggests:       perl-HTML-Template
Suggests:       perl-HTML-Template-Expr
Suggests:       perl-HTML-Template-JIT
Suggests:       perl-HTML-Tree
Suggests:       perl-HTTP-DAV
Suggests:       perl-HTTPS-Daemon
Suggests:       perl-Pod-HtmlPsPdf
Suggests:       php7
Suggests:       php7-bcmath
Suggests:       php7-bz2
Suggests:       php7-calendar
Suggests:       php7-ctype
Suggests:       php7-curl
Suggests:       php7-dba
Suggests:       php7-devel
Suggests:       php7-dom
Suggests:       php7-exif
Suggests:       php7-fastcgi
Suggests:       php7-ftp
Suggests:       php7-gd
Suggests:       php7-gettext
Suggests:       php7-gmp
Suggests:       php7-iconv
Suggests:       php7-imap
Suggests:       php7-ldap
Suggests:       php7-mbstring
Suggests:       php7-mcrypt
Suggests:       php7-mysql
Suggests:       php7-odbc
Suggests:       php7-openssl
Suggests:       php7-pear
Suggests:       php7-pgsql
Suggests:       php7-shmop
Suggests:       php7-snmp
Suggests:       php7-sockets
Suggests:       php7-sysvsem
Suggests:       php7-sysvshm
Suggests:       php7-tidy
Suggests:       php7-wddx
Suggests:       php7-xsl
Suggests:       php7-zlib
Suggests:       tidy
Suggests:       xhtml-dtd
Suggests:       xmlcharent
Suggests:       apache2-worker
Suggests:       apache2-mod_tidy
Suggests:       kfilereplace
Suggests:       kimagemapeditor
Suggests:       klinkstatus
Suggests:       kde3-quanta
Suggests:       kompozer
Suggests:       tomcat
Suggests:       tomcat-admin-webapps
Suggests:       tomcat-webapps
Suggests:       html2text

%description devel_web
Tools and libraries for Web application development.

%files devel_web
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_web.txt
%endif

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}/usr/share/doc/packages/patterns"
%if 0%{?is_opensuse}
for i in devel_rpm_build devel_web; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/usr/share/doc/packages/patterns/$i.txt"
done

%endif

for i in devel_basis devel_kernel; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}/usr/share/doc/packages/patterns/$i.txt"
	echo "This file marks the pattern $i-32bit to be installed." \
		>"%{buildroot}/usr/share/doc/packages/patterns/$i-32bit.txt"
done

#
# This file is created at check-in time. Sorry for the inconsistent workflow :(
#
%include %{SOURCE1}

%changelog
