#
# spec file for package perl-HTTP-Lite
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


Name:           perl-HTTP-Lite
Version:        2.44
Release:        0
%define cpan_name HTTP-Lite
Summary:        Lightweight HTTP implementation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Lite/
Source:         http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
*Note:* you should look at the HTTP::Tiny manpage or the LWP manpage before
using this module.

HTTP::Lite is a stand-alone lightweight HTTP/1.1 implementation for perl.
It is not intended as a replacement for the fully-featured LWP module.
Instead, it is intended for use in situations where it is desirable to
install the minimal number of modules to achieve HTTP support, or where LWP
is not a good candidate due to CPU overhead, such as slower processors.
HTTP::Lite is also significantly faster than LWP.

HTTP::Lite is ideal for CGI (or mod_perl) programs or for bundling for
redistribution with larger packages where only HTTP GET and POST
functionality are necessary.

HTTP::Lite supports basic POST and GET operations only. As of 0.2.1,
HTTP::Lite supports HTTP/1.1 and is compliant with the Host header,
necessary for name based virtual hosting. Additionally, HTTP::Lite now
supports Proxies.

As of 2.0.0 HTTP::Lite now supports a callback to allow processing of
request data as it arrives. This is useful for handling very large files
without consuming memory.

If you require more functionality, such as FTP or HTTPS, please see
libwwwperl (LWP). LWP is a significantly better and more comprehensive
package than HTTP::Lite, and should be used instead of HTTP::Lite whenever
possible.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
