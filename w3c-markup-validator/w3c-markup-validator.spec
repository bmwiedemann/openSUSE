#
# spec file for package w3c-markup-validator
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2006-2009 Sierk Bornemann
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


%define pkgname validator
%define apxs %{_sbindir}/apxs2
%define apache_sysconfdir %(%{apxs} -q SYSCONFDIR)
%define apache_serverroot %(%{apxs} -q PREFIX)
%define apache_docroot %(%{apxs} -q PREFIX)/htdocs

Name:           w3c-markup-validator
Version:        1.3
Release:        0
%{expand: %%define tbver %(echo %{version} | tr . _)}
Summary:        W3C Markup Validator
License:        W3C
Group:          Productivity/Networking/Web/Utilities
Url:            http://validator.w3.org/
#Source0:        http://validator.w3.org/dist/validator-%{tbver}.tar.gz
Source0:        validator-%{tbver}.tar.gz
#Source1:        http://validator.w3.org/dist/sgml-lib-%{tbver}.tar.gz
Source1:        sgml-lib-%{tbver}.tar.gz
Source2:        %{pkgname}-opensuse-addons.tar.bz2
Patch0:         %{pkgname}-opensuse-addons-ap_sroot.patch
Patch1:         %{pkgname}-httpd.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  sgml-skel
%if 0%{?suse_version}
BuildRequires:  apache2-devel
%if 0%{?suse_version} >= 1100
BuildRequires:  fdupes
%endif
%else
BuildRequires:  httpd-devel
%endif
#
%if 0%{?suse_version}
Requires:       apache2
%else
Requires:       httpd
%endif
Requires:       %{name}-libs = %{version}
Requires:       opensp >= 1.5.2
Requires:       perl(CGI) >= 2.81
Requires:       perl(Class::Accessor)
Requires:       perl(Config::General) >= 2.31
#Requires:       perl(Encode) solved by perl(Encode::HanExtra)
Requires:       perl(Encode::HanExtra)
Requires:       perl(Encode::JIS2K)
Requires:       perl(File::Spec::Functions)
Requires:       perl(HTML::Encoding) >= 0.52
Requires:       perl(HTML::Parser) >= 3.24
Requires:       perl(HTML::Template) >= 2.6
Requires:       perl(HTML::Tidy)
#Requires:       perl-libwww-perl >= 5.825
Requires:       perl(LWP::UserAgent) >= 2.0.32
Requires:       perl(Net::IP)
Requires:       perl(Net::hostent)
Requires:       perl(SGML::Parser::OpenSP)
#Requires:       perl(Set::IntSpan)
Requires:       perl(String::Approx)
#Requires:       perl(Test::Exception)
#Requires:       perl(Text::Iconv)
Requires:       perl(URI)
Requires:       perl(XML::LibXML)

%description
The W3C Markup Validator checks documents like HTML and XHTML for
conformance to W3C Recommendations and other standards.

%package        libs
Summary:        SGML and XML DTDs for the W3C Markup Validator
Group:          Productivity/Publishing/XML
Requires:       sgml-skel

%description    libs
SGML and XML DTDs for the W3C Markup Validator.


%prep
%setup -q -n %{pkgname}-%{version} -a 1 -a 2
%patch0
%patch1 -p1
mv %{pkgname}-%{version}/htdocs/sgml-lib .
rm -r %{pkgname}-%{version}/

# Localize configs.
%{__perl} -pi -e \
  's|/usr/local/validator\b|%{apache_serverroot}/%{name}|' \
  htdocs/config/validator.conf httpd/conf/httpd.conf httpd/cgi-bin/*
%{__perl} -pi -e \
  's|^(\s*)#Base\s*=\s*(.*)|${1}Base = ${2}| ;
   s|^(\s*Library\s*=\s*).*|${1}%{_datadir}/sgml/%{name}| ;
   s|^(\s*TidyConf\s*=\s*).*|${1}%{_sysconfdir}/w3c/tidy.conf| ;
   s|\bwww-validator\@w3\.org\b|root\@localhost| ;
   s|/validator\.w3\.org/|/localhost/w3c-markup-validator/|' \
  htdocs/config/validator.conf
%{__perl} -pi -e \
  's|\@apache_serverroot\@|%{apache_serverroot}|' \
  %{pkgname}-opensuse-addons/validator-vhost.conf

# Move config out of the way
mv htdocs/config __config

# Fixup permissions
find . -type d | xargs chmod 755
find . -type f | xargs chmod 644
chmod 755 httpd/cgi-bin/check
chmod 755 httpd/cgi-bin/sendfeedback.pl

%build

%install
# Config files
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/w3c
install -pm 644 __config/* $RPM_BUILD_ROOT%{_sysconfdir}/w3c
install -Dpm 644 httpd/conf/httpd.conf $RPM_BUILD_ROOT%{apache_sysconfdir}/conf.d/%{name}.conf
install -Dpm 644 %{pkgname}-opensuse-addons/validator-vhost.conf $RPM_BUILD_ROOT%{apache_sysconfdir}/vhosts.d/%{name}.conf.template
# Scripts, HTML, etc.
install -dm 755 $RPM_BUILD_ROOT%{apache_serverroot}/%{name}
cp -pR httpd/cgi-bin htdocs share $RPM_BUILD_ROOT%{apache_serverroot}/%{name}
install -Dpm 644 httpd/mod_perl/startup.pl $RPM_BUILD_ROOT%{apache_serverroot}/%{name}/httpd/mod_perl/startup.pl
# SGML library
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/sgml
cp -pR sgml-lib $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sgml
touch $RPM_BUILD_ROOT%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat
# Files for local use
install -dm 755 $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}
mv %{pkgname}-opensuse-addons/README.openSUSE .

# rpmlint stuff
%if 0%{?suse_version} >= 1100
%fdupes $RPM_BUILD_ROOT%{apache_serverroot}/%{name}
%fdupes $RPM_BUILD_ROOT%{_datadir}/sgml/%{name}
%endif

%post
echo "
Please read %{_defaultdocdir}/%{name}/README.openSUSE to configure the W3C Markup Validator to your needs.
Finally, restart the webserver with 'rcapache2 graceful'.
"
%{_sbindir}/a2enmod proxy || :

%postun
%restart_on_update apache2

%preun libs
for catalog in sgml.soc xml.soc ; do
  install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/$catalog >/dev/null 2>&1 || :
done

%post libs
for catalog in sgml.soc xml.soc ; do
  install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/sgml/%{name}/$catalog >/dev/null 2>&1 || :
done

%files
%defattr(-, root, root)
# Configs not "noreplace", they're incompatible to some extent between releases
%doc README*
%config %{apache_sysconfdir}/conf.d/%{name}.conf
%config %{apache_sysconfdir}/vhosts.d/%{name}.conf.template
%config %{_sysconfdir}/w3c/
%dir %{apache_serverroot}/%{name}/
%{apache_serverroot}/%{name}/*

%files libs
%defattr(-, root, root)
%ghost %config %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat
%{_datadir}/sgml/%{name}/

%changelog
