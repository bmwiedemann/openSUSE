#
# spec file for package stow
#
# Copyright (c) 2021 SUSE LLC
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


Name:           stow
Version:        2.3.1
Release:        0
Summary:        Manage the installation of software packages from source
License:        GPL-3.0-or-later
Group:          System/Packages
URL:            https://gnu.org/software/stow/
Source:         https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=stow&download=1#/%name.keyring
Source3:        stow-rpmlintrc
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Requires:       perl >= 5.6.1
BuildArch:      noarch
%{?perl_requires}
%{?libperl_requires}

%description
GNU Stow is a symlink farm manager which takes distinct packages of
software and/or data located in separate directories on the
filesystem, and makes them appear to be installed in the same place.
For example, %{_prefix}/local/bin could contain symlinks to files within
%{_prefix}/local/stow/emacs/bin, %{_prefix}/local/stow/perl/bin etc., and
likewise recursively for any other subdirectories such as .../share,
.../man, and so on.

This is particularly useful for keeping track of system-wide and
per-user installations of software built from source, but can also
facilitate a more controlled approach to management of configuration
files in the user's home directory, especially when coupled with
version control systems.

Stow is implemented as a combination of a Perl script providing a CLI
interface, and a backend Perl module which does most of the work.

%package doc
Summary:        Documentation for GNU Stow
Group:          System/Packages
Requires:       %{name} = %{version}

%description doc
Documentation for GNU Stow %{version} in HTML and PDF format.

%prep
%setup -q

%build
%configure \
    --with-pmdir=%{perl_vendorlib} \
    --docdir=%{_defaultdocdir}/%{name}

%install
%make_install
rm %{buildroot}%{_docdir}/stow/version.texi
rm %{buildroot}%{_docdir}/%{name}/INSTALL.md

%check
%make_build test

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{?ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{?ext_info}

%files
%license COPYING
%doc AUTHORS ChangeLog doc/ChangeLog.OLD README.md NEWS THANKS TODO
%{_bindir}/*
%{_mandir}/man8/stow.*
%{_infodir}/stow*
%dir %{_docdir}/stow
%{perl_vendorlib}/*

%files doc
%{_docdir}/stow/manual-single.html
%{_docdir}/stow/manual-split
%{_docdir}/stow/manual.pdf

%changelog
