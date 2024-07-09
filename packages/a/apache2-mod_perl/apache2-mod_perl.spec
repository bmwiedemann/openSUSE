#
# spec file for package apache2-mod_perl
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define srcname mod_perl
Name:           apache2-mod_perl
Version:        2.0.13
Release:        0
Summary:        Embedded Perl for Apache
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://perl.apache.org/
Source0:        https://archive.apache.org/dist/perl/%{srcname}-%{version}.tar.gz
Source1:        https://archive.apache.org/dist/perl/%{srcname}-%{version}.tar.gz.asc
Source2:        https://www.apache.org/dist/perl/KEYS#/%{name}.keyring
Patch1:         avoid-broken-provides.diff
# bsc#1091625, workaround, according to mls it should be solved in perl
Patch2:         apache2-mod_perl-prctl-short-name.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  db-devel
BuildRequires:  ed
BuildRequires:  netcfg
BuildRequires:  pcre-devel
BuildRequires:  perl
BuildRequires:  perl-BSD-Resource
BuildRequires:  perl-Tie-IxHash
BuildRequires:  perl-libwww-perl
BuildRequires:  sudo
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
Requires:       perl = %{perl_version}
Requires:       perl-HTML-Parser
Requires:       perl-Tie-IxHash
Requires:       perl-URI
Requires:       perl-libwww-perl
Requires:       perl(Linux::Pid)
Conflicts:      mod_perl
Obsoletes:      mod_perl_2

%description
The Apache/Perl integration project brings together the full power of
the Perl programming language and the Apache HTTP server.

With mod_perl, it is possible to write Apache modules entirely in Perl.
The persistent interpreter embedded in the server avoids the overhead
of starting an external interpreter and the penalty of Perl start-up
time.

Note that you do not need mod_perl to run perl scripts via the common
gateway interface (CGI). mod_perl enables you to run Perl scripts in an
embedded interpreter if the additional performance is needed, but may
require modifications to the scripts.

%package devel
Summary:        Embedded Perl for Apache - Development package
Group:          Development/Languages/Perl
Requires:       %{name} = %{version}

%description devel
The Apache/Perl integration project brings together the full power of
the Perl programming language and the Apache HTTP server.

This package contains the include files useful for developing new
software depending on apache2-mod_perl.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor MP_APXS=%{apache_apxs} MP_APR_CONFIG=%{_bindir}/apr-1-config MP_CCOPTS="%{apache_cflags} -fgnu89-inline"
make %{?_smp_mflags}

%check
%if !0%{?qemu_user_space_build}
mkdir t/run
t/TEST -start-httpd -port select -startup_timeout 720
t/TEST -run-tests || true
t/TEST -stop-httpd
%endif

%install
%perl_make_install
# install /srv/www/perl-lib
install -d %{buildroot}/%{apache_serverroot}/perl-lib
# install /etc/apache2/conf.d/mod_perl.conf
install -d %{buildroot}/%{apache_sysconfdir}/conf.d
cat > %{buildroot}/%{apache_sysconfdir}/conf.d/mod_perl.conf <<EOF
<Directory "%{apache_serverroot}/perl-lib">
    AllowOverride None
    Options None
    <IfModule !mod_authz_host.c>
      Order allow,deny
      Deny from all
    </IfModule>
    <IfModule mod_authz_host.c>
      Require all granted
    </IfModule>
</Directory>
<IfModule mod_perl.c>
    PerlRequire "%{_sysconfdir}/apache2/mod_perl-startup.pl"
    ScriptAlias /perl/ "%{apache_serverroot}/cgi-bin/"
    <Location /perl/>
	# mod_perl mode
	SetHandler perl-script
	PerlResponseHandler ModPerl::Registry
	PerlOptions +ParseHeaders
	Options +ExecCGI
    </Location>
    ScriptAlias /cgi-perl/ "%{apache_serverroot}/cgi-bin/"
    <Location /cgi-perl>
	# perl cgi mode
	SetHandler  perl-script
	PerlResponseHandler ModPerl::PerlRun
	PerlOptions +ParseHeaders
	Options +ExecCGI
    </Location>
    # The /cgi-bin/ ScriptAlias is already set up in httpd.conf
</IfModule>
EOF
# install /etc/apache2/mod_perl-startup.pl
cat > %{buildroot}/%{apache_sysconfdir}/mod_perl-startup.pl <<-EOF
  # Taken from http://perl.apache.org/docs/2.0/user/handlers/server.html#Startup_File
  if ( ! \$ENV{MOD_PERL}) { die "GATEWAY_INTERFACE not Perl!"; }
  use lib qw(/srv/www/perl-lib);
  # enable if the mod_perl 1.0 compatibility is needed
  # use Apache2::compat ();
  # preload all mp2 modules
  # use ModPerl::MethodLookup;
  # ModPerl::MethodLookup::preload_all_modules();
  use ModPerl::Util (); #for CORE::GLOBAL::exit
  use Apache2::RequestRec ();
  use Apache2::RequestIO ();
  use Apache2::RequestUtil ();
  use Apache2::ServerRec ();
  use Apache2::ServerUtil ();
  use Apache2::Connection ();
  use Apache2::Log ();
  use APR::Table ();
  use ModPerl::Registry ();
  use Apache2::Const -compile => ':common';
  use APR::Const -compile => ':common';
  1;
EOF
# install documentation files alongside perl modules, where applicable
cp -av docs/api/*.pod %{buildroot}/%{perl_vendorarch}/
cp -av docs/api/APR/*.pod %{buildroot}/%{perl_vendorarch}/APR/
cp -av docs/api/Apache2/*.pod %{buildroot}/%{perl_vendorarch}/Apache2/
cp -av docs/api/ModPerl/*.pod %{buildroot}/%{perl_vendorarch}/ModPerl/
### since 11.4 perl_process_packlist
### removes .packlist, perllocal.pod files
%if 0%{?suse_version} > 1130
%perl_process_packlist
%else
# do not perl_process_packlist
# remove .packlist file
find %{buildroot}%{perl_vendorarch}/auto -name .packlist -print0 | xargs -0 -r rm ;
# remove perllocal.pod file
rm -f %{buildroot}%{perl_archlib}/perllocal.pod
%endif

# taken from kdump/kdump.spec, thanks!
# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%files
%license LICENSE
%doc Changes README RELEASE STATUS
%doc docs
%dir %{apache_libexecdir}
%{apache_libexecdir}/mod_perl.so
%config(noreplace) %{apache_sysconfdir}/mod_perl-startup.pl
%config(noreplace) %{apache_sysconfdir}/conf.d/mod_perl.conf
%dir %{apache_serverroot}/perl-lib
%{_mandir}/man3/*
%{perl_vendorarch}/Apache
%{perl_vendorarch}/Apache2
%{perl_vendorarch}/APR
%{perl_vendorarch}/APR.pm
%{perl_vendorarch}/Bundle
%{perl_vendorarch}/ModPerl
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/mod_perl2.pm
%{perl_vendorarch}/*.pod
%{_bindir}/mp2bug

%files devel
%{apache_includedir}/*

%changelog
