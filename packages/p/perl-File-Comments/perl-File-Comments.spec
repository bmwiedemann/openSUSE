#
# spec file for package perl-File-Comments
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-File-Comments
Version:        0.08
Release:        0
%define cpan_name File-Comments
Summary:        Recognizes file formats and extracts format-specific comments
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Tar) >= 1.22
BuildRequires:  perl(HTML::TokeParser) >= 2.28
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Log::Log4perl) >= 0.5
BuildRequires:  perl(Module::Pluggable) >= 2.4
BuildRequires:  perl(PPI) >= 1.115
BuildRequires:  perl(Pod::Parser) >= 1.14
BuildRequires:  perl(Sysadm::Install) >= 0.11
Requires:       perl(Archive::Tar) >= 1.22
Requires:       perl(HTML::TokeParser) >= 2.28
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(Log::Log4perl) >= 0.5
Requires:       perl(Module::Pluggable) >= 2.4
Requires:       perl(PPI) >= 1.115
Requires:       perl(Pod::Parser) >= 1.14
Requires:       perl(Sysadm::Install) >= 0.11
%{perl_requires}

%description
File::Comments guesses the type of a given file, determines the format used
for comments, extracts all comments, and returns them as a reference to an
array of chunks. Alternatively, it strips all comments from a file.

Currently supported are Perl scripts, C/C++ programs, Java, makefiles,
JavaScript, Python and PHP.

The plugin architecture used by File::Comments makes it easy to add new
formats. To support a new format, a new plugin module has to be installed.
No modifications to the File::Comments codebase are necessary, new plugins
will be picked up automatically.

File::Comments can also be used to simply guess a file's type. It it
somewhat more flexible than File::MMagic and File::Type. File types in
File::Comments are typically based on file name suffixes (*.c, *.pl, etc.).
If no suffix is available, or a given suffix is ambiguous (e.g. if several
plugins have registered a handler for the same suffix), then the file's
content is used to narrow down the possibilities and arrive at a decision.

WARNING: THIS MODULE IS UNDER DEVELOPMENT, QUALITY IS ALPHA. IF YOU FIND
BUGS, OR WANT TO CONTRIBUTE PLUGINS, PLEASE SEND THEM MY WAY.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
