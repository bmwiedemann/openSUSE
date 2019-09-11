#
# spec file for package perl-HTML-Clean
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


Name:           perl-HTML-Clean
BuildRequires:  perl
BuildRequires:  perl-macros
Version:        0.8
Release:        0
Provides:       HTML-Clean
Conflicts:      perlmod
Url:            http://cpan.org/modules/by-module/HTML/
Source:         HTML-Clean-%{version}.tar.gz
Patch:          %{name}-%{version}-IO.diff
Summary:        Cleans up HTML code for web browsers, not humans
License:        Artistic-1.0
Group:          Development/Libraries/Perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
The majority of the web pages of the internet today are much larger
than they need to be.  The reason for this is that HTML tends to be
stored in a human readable format, with indenting, newlines and
comments.

However, all of these comments, whitespace etc. are ignored by the
browser, and needlessly lengthen download times.

Second, many people are using WYSIWYG HTML editors these days. This
makes creating content easy.  However these editors can cause a number
of compatibility problems by tying themselves to a particular browser
or operating system.



Authors:
--------
    Paul Lindner <paul.lindner@itu.int>

%prep 
%setup -n HTML-Clean-%{version} -q
%patch

%build
perl Makefile.PL
make %{?_smp_mflags} all
make test

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc TODO Changes README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/HTML
%{perl_vendorlib}/auto/HTML
%{perl_vendorlib}/HTML
%{_bindir}/htmlclean

%changelog
