#
# spec file for package perl-Contextual-Return
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


Name:           perl-Contextual-Return
Version:        0.004014
Release:        0
%define cpan_name Contextual-Return
Summary:        Create context-sensitive return values
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Contextual-Return/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Want)
BuildRequires:  perl(version)
Requires:       perl(Want)
Requires:       perl(version)
%{perl_requires}

%description
Usually, when you need to create a subroutine that returns different values
in different contexts (list, scalar, or void), you write something like:

    sub get_server_status {
        my ($server_ID) = @_;

        # Acquire server data somehow...
        my %server_data = _ascertain_server_status($server_ID);

        # Return different components of that data,
        # depending on call context...
        if (wantarray()) {
            return @server_data{ qw(name uptime load users) };
        }
        if (defined wantarray()) {
            return $server_data{load};
        }
        if (!defined wantarray()) {
            carp 'Useless use of get_server_status() in void context';
            return;
        }
        else {
            croak q{Bad context! No biscuit!};
        }
    }

That works okay, but the code could certainly be more readable. In its
simplest usage, this module makes that code more readable by providing
three subroutines--'LIST()', 'SCALAR()', 'VOID()'--that are true only when
the current subroutine is called in the corresponding context:

    use Contextual::Return;

    sub get_server_status {
        my ($server_ID) = @_;

        # Acquire server data somehow...
        my %server_data = _ascertain_server_status($server_ID);

        # Return different components of that data
        # depending on call context...
        if (LIST)   { return @server_data{ qw(name uptime load users) } }
        if (SCALAR) { return $server_data{load}                         }
        if (VOID)   { print "$server_data{load}\n"                      }
        else        { croak q{Bad context! No biscuit!}                 }
    }

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
%doc Changes README

%changelog
