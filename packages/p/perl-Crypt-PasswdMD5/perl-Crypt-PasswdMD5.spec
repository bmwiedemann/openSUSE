#
# spec file for package perl-Crypt-PasswdMD5
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Crypt-PasswdMD5
Name:           perl-Crypt-PasswdMD5
Version:        1.42
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Provide interoperable MD5-based crypt() functions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::MD5) >= 2.53
BuildRequires:  perl(Test::More) >= 1.001002
Requires:       perl(Digest::MD5) >= 2.53
%{perl_requires}

%description
'apache_md5_crypt()' provides a function compatible with Apache's
'.htpasswd' files. This was contributed by Bryan Hart <bryan@eai.com>. This
function is exported by default.

The 'unix_md5_crypt()' provides a crypt()-compatible interface to the
rather new MD5-based crypt() function found in modern operating systems.
It's based on the implementation found on FreeBSD 2.2.[56]-RELEASE. This
function is also exported by default.

For both functions, if a salt value is not supplied, a random salt will be
generated, using the function random_md5_salt(). This function is not
exported by default.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
