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

Name:           patterns-devel-perl
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Perl devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Perl development pattern.

################################################################################

%package devel_perl
%pattern_development
Summary:        Perl Development
Group:          Metapackages
Provides:       pattern() = devel_perl
Provides:       pattern-icon() = pattern-perl-devel
Provides:       pattern-order() = 3340
Provides:       pattern-visible()

Recommends:     perlref
Recommends:     perl-doc
Suggests:       perl-Algorithm-Diff
Suggests:       perl-AppConfig
Suggests:       perl-Authen-SASL
Suggests:       perl-Authen-SASL-Cyrus
Suggests:       perl-BIND-Conf_Parser
Suggests:       perl-BSD-Resource
Suggests:       perl-CDDB_get
Suggests:       perl-CGI-Application
Suggests:       perl-Carp-Assert
Suggests:       perl-Class-Accessor
Suggests:       perl-Class-Data-Inheritable
Suggests:       perl-Class-Date
Suggests:       perl-Class-MethodMaker
Suggests:       perl-Class-Multimethods
Suggests:       perl-Class-WhiteHole
Suggests:       perl-Config-General
Suggests:       perl-Config-IniFiles
Suggests:       perl-Convert-TNEF
Suggests:       perl-Convert-UUlib
Suggests:       perl-Crypt-Blowfish
Suggests:       perl-Crypt-CBC
Suggests:       perl-Crypt-SSLeay
Suggests:       perl-DBD-CSV
Suggests:       perl-DBD-ODBC
Suggests:       perl-DBD-Pg
Suggests:       perl-DBD-SQLite
Suggests:       perl-DBD-XBase
Suggests:       perl-DBD-mysql
Suggests:       perl-Devel-CoreStack
Suggests:       perl-Devel-Symdump
Suggests:       perl-Encode-HanExtra
Suggests:       perl-Encode-JIS2K
Suggests:       perl-ExtUtils-F77
Suggests:       perl-File-MMagic
Suggests:       perl-File-Tail
Suggests:       perl-Font-AFM
Suggests:       perl-GD
Suggests:       perl-GD-Graph3d
Suggests:       perl-GDGraph
Suggests:       perl-GDTextUtil
Suggests:       perl-Getopt-Mixed
Suggests:       perl-Gtk2
Suggests:       perl-HTML-Clean
Suggests:       perl-HTML-FillInForm
Suggests:       perl-HTML-Format
Suggests:       perl-HTML-SimpleParse
Suggests:       perl-HTML-Template
Suggests:       perl-HTML-Template-Expr
Suggests:       perl-HTML-Template-JIT
Suggests:       perl-HTML-Tree
Suggests:       perl-HTTP-DAV
Suggests:       perl-HTTPS-Daemon
Suggests:       perl-IPC-Run
Suggests:       perl-Image-Size
Suggests:       perl-Inline
Suggests:       perl-Log-Dispatch
Suggests:       perl-Log-Log4perl
Suggests:       perl-MIME-Lite
Suggests:       perl-MLDBM
Suggests:       perl-MLDBM-Sync
Suggests:       perl-Mcrypt
Suggests:       perl-Module-Info
Suggests:       perl-Net-DNS
Suggests:       perl-Net-Daemon
Suggests:       perl-Net-IP
Suggests:       perl-Net-Jabber
Suggests:       perl-Net-Netmask
Suggests:       perl-Net-Server
Suggests:       perl-Net-Telnet
Suggests:       perl-PDL
Suggests:       perl-Params-Validate
Suggests:       perl-Parse-Yapp
Suggests:       perl-PerlMagick
Suggests:       perl-Pod-HtmlPsPdf
Suggests:       perl-PostScript-Simple
Suggests:       perl-Quantum-Superpositions
Suggests:       perl-RPC-XML
Suggests:       perl-SGMLS
Suggests:       perl-SOAP-Lite
Suggests:       perl-SQL-Statement
Suggests:       perl-Set-Crontab
Suggests:       perl-Set-Object
Suggests:       perl-Set-Scalar
Suggests:       perl-Socket6
Suggests:       perl-Template-Toolkit
Suggests:       perl-Text-CSV_XS
Suggests:       perl-Text-DelimMatch
Suggests:       perl-Text-Iconv
Suggests:       perl-Tie-Cache
Suggests:       perl-Time-modules
Suggests:       perl-Unicode-Map8
Suggests:       perl-Unicode-String
Suggests:       perl-XML-LibXML
Suggests:       perl-XML-Simple
Suggests:       perl-XML-Stream
Suggests:       perl-XML-XSLT
Suggests:       perl-YAML
Suggests:       perl-libxml-perl
Suggests:       perl-Apache-AuthCookie
Suggests:       perl-Apache-AuthNetLDAP
Suggests:       perl-Apache-DBI
Suggests:       perl-Apache-Session
Suggests:       perl-Apache-SessionX
Suggests:       perl-Cairo
Suggests:       perl-Chart
Suggests:       perl-Convert-ASN1
Suggests:       perl-ExtUtils-Depends
Suggests:       perl-ExtUtils-PkgConfig
Suggests:       perl-FileHandle-Unget
Suggests:       perl-File-Type
Suggests:       perl-IO-String
Suggests:       perl-IO-Stty
Suggests:       perl-ldap
Suggests:       perl-ldap-ssl
Suggests:       perl-libconfigfile
Suggests:       perl-Mail-Mbox-MessageParser
Suggests:       perl-MIME-Types
Suggests:       perl-NetAddr-IP
Suggests:       perl-Net-IPv4Addr
Suggests:       perl-Net-SNMP
Suggests:       perl-NKF
Suggests:       perl-PDA-Pilot
Suggests:       perl-SNMP
Suggests:       perl-SVN-Simple
Suggests:       perl-Text-ChaSen
Suggests:       perl-Text-Kakasi
Suggests:       perl-Time-Duration
Suggests:       perl-Time-Period
Suggests:       perl-WeakRef
Suggests:       perl-XML-LibXSLT

%description devel_perl
Tools and libraries for software development using the Perl programming language.

%files devel_perl
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_perl.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/
echo 'This file marks the pattern devel_perl to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/devel_perl.txt

