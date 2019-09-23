#
# spec file for package perl-Net-SSLeay
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Net-SSLeay
Name:           perl-Net-SSLeay
Version:        1.88
Release:        0
Summary:        Perl extension for using OpenSSL
License:        Artistic-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHRISN/%{cpan_name}-%{version}.tar.gz
BuildRequires:  libopenssl-devel
BuildRequires:  openssl
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  zlib-devel
%{perl_requires}
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Warn)

%description
Net::SSLeay module contains perl bindings to openssl (http://www.openssl.org) library.
Net::SSLeay module basically comprise of:
    High level functions for accessing web servers (by using HTTP/HTTPS)
    Low level API (mostly mapped 1:1 to openssl's C functions)
    Convenience functions (related to low level API but with more perl friendly interface)

%prep
%setup -q -n %{cpan_name}-%{version}

# replace rest of /usr/local/bin/perl with /usr/bin/perl
for f in $(find . -type f -exec grep -l "%{_prefix}/local/bin/perl" {} \; ); do
  sed -i -e "s@%{_prefix}/local/bin/perl@perl@g" $f
done
# delete .orig files created by patches
find . -type f -name "*.orig" -delete
# fix perm
pushd examples
chmod 0644 *.pl
popd

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags} -Wall" < /dev/null
make %{?_smp_mflags}

%check
%if ! 0%{?qemu_user_space_build}
make %{?_smp_mflags} test
%endif

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%license LICENSE
%doc Changes Credits QuickRef README examples

%changelog
