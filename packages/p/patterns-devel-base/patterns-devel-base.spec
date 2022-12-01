#
# spec file for package patterns-devel-base
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


%bcond_with betatest

Name:           patterns-devel-base
Version:        20170319
Release:        0
Summary:        Patterns for Installation (base devel patterns)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
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
Provides:       patterns-sled-Basis-Devel = %{version}
Provides:       patterns-sles-Basis-Devel = %{version}
Obsoletes:      patterns-sled-Basis-Devel < %{version}
Obsoletes:      patterns-sles-Basis-Devel < %{version}
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
# required for make checks
Recommends:     sparse
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
Suggests:       smatch
Suggests:       coccinelle

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
# bsc#1147177
Recommends:     bc
# bnc#582415
Recommends:     ctags
Recommends:     diffstat
Recommends:     git-core
Recommends:     git-email
Recommends:     indent
Recommends:     kernel-syms
Recommends:     patchutils
Recommends:     quilt
# bsc#1147177
Recommends:     pkgconfig(libelf)
Recommends:     pkgconfig(openssl)
Suggests:       kernel-debug
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
Suggests:       php8
Suggests:       php8-bcmath
Suggests:       php8-bz2
Suggests:       php8-calendar
Suggests:       php8-ctype
Suggests:       php8-curl
Suggests:       php8-dba
Suggests:       php8-devel
Suggests:       php8-dom
Suggests:       php8-exif
Suggests:       php8-fastcgi
Suggests:       php8-ftp
Suggests:       php8-gd
Suggests:       php8-gettext
Suggests:       php8-gmp
Suggests:       php8-iconv
Suggests:       php8-imap
Suggests:       php8-ldap
Suggests:       php8-mbstring
Suggests:       php8-mcrypt
Suggests:       php8-mysql
Suggests:       php8-odbc
Suggests:       php8-openssl
Suggests:       php8-pear
Suggests:       php8-pgsql
Suggests:       php8-shmop
Suggests:       php8-snmp
Suggests:       php8-sockets
Suggests:       php8-sysvsem
Suggests:       php8-sysvshm
Suggests:       php8-tidy
Suggests:       php8-wddx
Suggests:       php8-xsl
Suggests:       php8-zlib
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
