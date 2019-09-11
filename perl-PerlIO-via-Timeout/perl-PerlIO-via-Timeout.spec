#
# spec file for package perl-PerlIO-via-Timeout
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


Name:           perl-PerlIO-via-Timeout
Version:        0.32
Release:        0
%define cpan_name PerlIO-via-Timeout
Summary:        PerlIO layer that adds read & write timeout to a handle
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/PerlIO-via-Timeout/
Source0:        http://www.cpan.org/authors/id/D/DA/DAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(Test::TCP)
%{perl_requires}

%description
This package implements a PerlIO layer, that adds read / write timeout.
This can be useful to avoid blocking while accessing a handle (file,
socket, ...), and fail after some time.

The timeout is implemented by using '<select'> on the handle before
reading/writing.

*WARNING* the handle won't timeout if you use 'sysread' or 'syswrite' on
it, because these functions works at a lower level. However if you're
trying to implement a timeout for a socket, see the IO::Socket::Timeout
manpage that implements exactly that.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
