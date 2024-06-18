#
# spec file for package bugzilla
#
# Copyright (c) 2024 SUSE LLC
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


Name:           bugzilla
Version:        5.0.6
Release:        0
Summary:        Bug tracker for software development
License:        MPL-2.0
Group:          Development/Tools/Other
URL:            http://bugzilla.org/
Source:         http://ftp.mozilla.org/pub/mozilla.org/webtools/%{name}-%{version}.tar.gz
Source2:        http://downloads.sourceforge.net/project/bugzilla-de/5.0/5.0.4/%{name}-de-5.0.4-2.utf-8.tar.gz
Source3:        MPL-2.0.html
Source4:        %{name}.conf
Source5:        %{name}-rpmlintrc
Patch1:         fix_whine_error.patch
Patch2:         modernize-bugzilla-submit.patch
Patch3:         bugzilla-py3-jb2bz.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(systemd)
Requires:       patchutils
Requires:       perl-Authen-SASL
#Recommends:		RadiusPerl
Requires:       perl-Cache-Memcached
Requires:       perl-Chart >= 2.4.1
Requires:       perl-DBD-Pg >= 2.7.0
Requires:       perl-DBD-SQLite >= 1.29
Requires:       perl-DBD-mysql >= 4.001
Requires:       perl-DBI >= 1.614
Requires:       perl-Daemon-Generic
Requires:       perl-DateTime >= 0.75
Requires:       perl-DateTime-TimeZone >= 1.64
Requires:       perl-Digest-SHA1
Requires:       perl-Email-MIME >= 1.904
Requires:       perl-Email-Reply
Requires:       perl-Email-Send >= 2.02
Requires:       perl-Email-Sender >= v1.300011
Requires:       perl-Encode >= 2.21
Requires:       perl-Encode-Detect
Requires:       perl-File-Copy-Recursive
Requires:       perl-File-MimeInfo
Requires:       perl-File-Slurp >= 9999.13
Requires:       perl-File-Which
Requires:       perl-GD >= 1.20
Requires:       perl-GDGraph
Requires:       perl-GDTextUtil
Requires:       perl-HTML-FormatText-WithLinks >= 0.13
Requires:       perl-HTML-Parser >= 3.67
Requires:       perl-HTML-Scrubber
Requires:       perl-IO-stringy
Requires:       perl-JSON-RPC
Requires:       perl-JSON-XS >= 2.01
Requires:       perl-List-MoreUtils >= 0.32
Requires:       perl-MIME-tools >= 5.406
Requires:       perl-Math-Random-ISAAC >= 1.0.1
Requires:       perl-Module-Pluggable
Requires:       perl-Net-SMTP-SSL >= 1.01
Requires:       perl-Object-Pluggable
Requires:       perl-PatchReader >= 0.9.6
Requires:       perl-SOAP-Lite >= 0.712
Requires:       perl-Template-GD
Requires:       perl-Template-Toolkit >= 2.24
Requires:       perl-Test-Taint >= 1.0.6
Requires:       perl-TheSchwartz >= 1.07
Requires:       perl-TimeDate >= 2.23
Requires:       perl-URI >= 1.55
Requires:       perl-XML-Twig
Requires:       perl-XMLRPC-Lite >= 0.712
Requires:       perl-base >= 5.8.1
Requires:       perl-ldap
Requires:       perl-libwww-perl
Requires:       perl(CGI) >= 5.8.1
Recommends:     perl-DBD-Oracle >= 1.19
BuildArch:      noarch
%{?systemd_requires}

%description
Bugzilla is server software designed to help you manage software
development.

* Optimized database structure for increased performance and
  scalability
* Excellent security to protect confidentiality
* Advanced query tool that can remember your searches
* Integrated email capabilities
* Editable user profiles and comprehensive email preferences
* Comprehensive permissions system
* Proven under fire as Mozilla's bug tracking system

%package lang-de
Summary:        German language files for bugzilla
Group:          Development/Tools/Other
Requires:       %{name} = %{version}-%{release}

%description lang-de
This package includes german language files for bugzilla

%package apache
Summary:        Apache configuration for %{name}
Group:          Productivity/Networking/Web/Utilities
BuildRequires:  apache2
Requires:       apache2
Requires:       apache2-mod_perl >= 1.999022
#Recommonds:	Apache-SizeLimit
Supplements:    packageand(apache2:%name)

%description apache
This subpackage contains the Apache configuration files

%prep
%setup -q
%autopatch -p1
# rpmlint
sed -i -e 's|\/usr\/bin\/env perl|\/usr\/bin\/perl|g' contrib/perl-fmt
#
tar -xzf %{SOURCE2}  --directory "template"
cd template/de
cd ../..

%build

%install
# Ensure shebang shell scripts have executable bit set
for file in `find -type f -perm /664`; do
  if head -1 $file | grep -E '^\#!' &>/dev/null; then
    chmod a+x $file
  fi
done
# Remove the execute bit from files that don't start with #!
for file in `find -type f -perm /111`; do
  if head -1 $file | grep -E -v '^\#!' &>/dev/null; then
    chmod a-x $file
  fi
done
# Hello bugzilla devs...
find . -type d "(" -name .bzr -o -name .git ")" \
	-exec rm -Rf "{}" "+"
find . -type f "(" -name ".git*" -o -name ".bzr*" -o -name ".travis*" -o -name ".buildinfo*" ")" \
    -exec rm -Rf "{}" "+"
find . -type f -print0 | xargs -0r grep -l '^#!' | xargs -r chmod a+x
find . -type f -print0 | xargs -0r grep -l '^#!' | \
	xargs -r perl -i -pe 's{^#!%{_prefix}/local/}{#!%{_prefix}/}' "{}" "+"
mkdir -p "%{buildroot}%{apache_serverroot}"
cp -a . "%{buildroot}%{apache_serverroot}/%{name}"

%if %{suse_version} >= 1600
# both occurences of /usr/bin/python3 are introduced by our patches, is there a more straightforward way?
%python3_fix_shebang_path %{buildroot}%{apache_serverroot}/%{name}/contrib/bugzilla-submit/bugzilla-submit %{buildroot}%{apache_serverroot}/%{name}/contrib/jb2bz.py
%endif

%fdupes %{buildroot}/srv

cp "%{SOURCE3}" .
#install bugzilla.conf to apache conf.d
install -D -m0640 %{SOURCE4} %{buildroot}%{apache_sysconfdir}/conf.d/bugzilla.conf
# fix apache serverroot
sed -i -e 's|@APACHE_SERVERROOT@|%{apache_serverroot}|g' %{buildroot}%{apache_sysconfdir}/conf.d/bugzilla.conf
# remove included .htaccess which has been moved to bugzilla.conf
rm %{buildroot}%{apache_serverroot}/%{name}/.htaccess

%files
%doc MPL-2.0.html
%defattr(-,%{apache_user},root)
# exclude language de_DE
%exclude %{apache_serverroot}/bugzilla/template/de
%{apache_serverroot}/bugzilla

%files lang-de
%defattr(0644,%{apache_user},root,755)
%{apache_serverroot}/bugzilla/template/de

%files apache
%attr(-,%{apache_user},%{apache_group}) %config(noreplace) %{apache_sysconfdir}/conf.d/bugzilla.conf

%changelog
