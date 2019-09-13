#
# spec file for package stow
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


Name:           stow
Version:        2.2.2
Release:        0
Summary:        Manage the installation of software packages from source
License:        GPL-2.0+
Group:          System/Packages
Url:            http://www.gnu.org/software/stow/
Source:         http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2
Source1:        stow-rpmlintrc
Source2:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.bz2.sig
Source3:        http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=stow&download=1#/%name.keyring
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
Requires:       %{install_info_prereq}
Requires:       perl >= 5.6.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

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
make DESTDIR=%{buildroot} install %{?_smp_mflags}
rm %{buildroot}%{_docdir}/stow/version.texi
install -m 0644 COPYING README AUTHORS ChangeLog doc/ChangeLog.OLD \
                NEWS THANKS TODO \
    %{buildroot}%{_docdir}/stow

%check
make %{?_smp_mflags} test

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man8/stow.*
%{_infodir}/stow*
%dir %{_docdir}/stow
%{_docdir}/stow/COPYING
%{_docdir}/stow/README
%{_docdir}/stow/AUTHORS
%{_docdir}/stow/ChangeLog
%{_docdir}/stow/ChangeLog.OLD
%{_docdir}/stow/NEWS
%{_docdir}/stow/THANKS
%{_docdir}/stow/TODO
%{perl_vendorlib}/*

%files doc
%defattr(-,root,root)
%{_docdir}/stow/manual-single.html
%{_docdir}/stow/manual-split
%{_docdir}/stow/manual.pdf

%changelog
