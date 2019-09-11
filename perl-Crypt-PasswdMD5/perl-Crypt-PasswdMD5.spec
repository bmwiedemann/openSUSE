#
# spec file for package perl-Crypt-PasswdMD5
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Crypt-PasswdMD5
Version:        1.40
Release:        0
%define cpan_name Crypt-PasswdMD5
Summary:        Provide interoperable MD5-based crypt() functions
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-PasswdMD5/
Source:         http://www.cpan.org/authors/id/R/RS/RSAVAGE/%{cpan_name}-%{version}.tgz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::MD5) >= 2.53
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.94
#BuildRequires: perl(Crypt::PasswdMD5)
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changelog.ini Changes README xt

%changelog
