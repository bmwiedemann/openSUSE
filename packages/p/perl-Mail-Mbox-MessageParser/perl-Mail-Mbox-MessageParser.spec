#
# spec file for package perl-Mail-Mbox-MessageParser
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Mail-Mbox-MessageParser
Version:        1.5111
Release:        0
%define cpan_name Mail-Mbox-MessageParser
Summary:        Fast and Simple Mbox Folder Reader
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mail-Mbox-MessageParser/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.080000
BuildRequires:  perl(FileHandle::Unget)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Text::Diff)
BuildRequires:  perl(UNIVERSAL::require)
Requires:       perl(FileHandle::Unget)
%{perl_requires}

%description
This module implements a fast but simple mbox folder reader. One of three
implementations (Cache, Grep, Perl) will be used depending on the wishes of
the user and the system configuration. The first implementation is a
cached-based one which stores email information about mailboxes on the file
system. Subsequent accesses will be faster because no analysis of the
mailbox will be needed. The second implementation is one based on GNU grep,
and is significantly faster than the Perl version for mailboxes which
contain very large (10MB) emails. The final implementation is a fast
Perl-based one which should always be applicable.

The Cache implementation is about 6 times faster than the standard Perl
implementation. The Grep implementation is about 4 times faster than the
standard Perl implementation. If you have GNU grep, it's best to enable
both the Cache and Grep implementations. If the cache information is
available, you'll get very fast speeds. Otherwise, you'll take about a 1/3
performance hit when the Grep version is used instead.

The overriding requirement for this module is speed. If you wish more
sophisticated parsing, use Mail::MboxParser (which is based on this module)
or Mail::Box.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc anonymize_mailbox CHANGES README TODO
%license LICENSE

%changelog
