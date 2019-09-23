#
# spec file for package perl-FileHandle-Unget
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


Name:           perl-FileHandle-Unget
Version:        0.1634
Release:        0
%define cpan_name FileHandle-Unget
Summary:        FileHandle which supports multi-byte unget
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/FileHandle-Unget/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(UNIVERSAL::require)
%{perl_requires}

%description
FileHandle::Unget operates exactly the same as FileHandle, except that it
provides a version of ungetc that allows you to unget more than one
character. It also provides ungets to unget a string.

This module is useful if the filehandle refers to a stream for which you
can't just 'seek()' backwards. Some operating systems support multi-byte
'ungetc()', but this is not guaranteed. Use this module if you want a
portable solution. In addition, on some operating systems, eof() will not
be reset if you ungetc after having read to the end of the file.

NOTE: Using 'sysread()' with 'ungetc()' and other buffering functions is
still a bad idea.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

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
%doc CHANGES README TODO
%license LICENSE

%changelog
