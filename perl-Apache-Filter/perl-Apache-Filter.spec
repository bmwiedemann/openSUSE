#
# spec file for package perl-Apache-Filter
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Apache-Filter
BuildRequires:  apache2-devel
BuildRequires:  apache2-mod_perl
BuildRequires:  libapr-util1-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-macros
Version:        1.024
Release:        0
Provides:       Apache-Filter
Requires:       apache
Requires:       apache2-mod_perl
Requires:       perl-URI
Conflicts:      perlmod
Url:            http://cpan.org/modules/by-module/Apache/
Summary:        Alter the output of previous handlers
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Source:         Apache-Filter-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
In basic operation, each of the handlers Filter1, Filter2, and Filter3
will make a call to $r->filter_input(), which will return a filehandle.
 For Filter1, the filehandle points to the requested file. For Filter2,
the filehandle contains whatever Filter1 wrote to STDOUT. For Filter3,
it contains whatever Filter3 wrote to STDOUT. The output of Filter3
goes directly to the browser.

Note that the modules Filter1, Filter2, and Filter3 are listed in
forward order, in contrast to the reverse-order listing of
Apache::OutputChain.

When you've got this module, you can use the same handler both as a
stand-alone handler, and as an element in a chain. Just make sure that
whenever you're chaining, all the handlers in the chain are "Filter-
aware," i.e. they each call $r->filter_register() exactly once, before
they start printing to STDOUT. There should be almost no overhead for
doing this when there's only one element in the chain.

%prep 
%setup -q -n Apache-Filter-%{version}

%build
if [ -x /usr/sbin/httpd2 ]; then
  export APACHE=/usr/sbin/httpd2
elif [ -x /usr/sbin/httpd ]; then
  export APACHE=/usr/sbin/httpd
else
  echo "could not find the apache main executable..."
  exit 1
fi
perl Makefile.PL
make %{?_smp_mflags}

%install
if [ -x /usr/sbin/httpd2 ]; then
  export APACHE=/usr/sbin/httpd2
elif [ -x /usr/sbin/httpd ]; then
  export APACHE=/usr/sbin/httpd
else
  echo "could not find the apache main executable..."
  exit 1
fi
%perl_make_install
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc Changes README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Apache
%{perl_vendorarch}/auto/Apache

%changelog
