#
# spec file for package drush
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


Name:           drush
Version:        8.3.0
Release:        0
Summary:        Command line shell and scripting interface for Drupal
# See licenses.txt for dependency licenses.
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Servers
Url:            http://www.drush.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-vendor.tar.xz
Source10:       extensions.php
Source11:       extensions.txt
Source12:       licenses.txt
Source13:       update.sh
BuildRequires:  xz
Requires:       php >= 5.4.5
Requires:       php-ctype
# Should fallback to polyfill, but does not actually work.
Requires:       php-iconv
Requires:       php-json
Requires:       which

Suggests:       php-iconv
Suggests:       php-mbstring
Suggests:       php-pcntl
Suggests:       php-posix
Suggests:       php-readline
Suggests:       php-sqlite

Obsoletes:      drush_make < %{version}
Provides:       drush_make = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Drush is a command line shell and scripting interface for Drupal, a veritable
Swiss Army knife designed to make life easier for those of us who spend some of
our working hours hacking away at the command prompt.

%prep
# -a 1: unpack Source1 vendor tarball
%setup -q -a 1

%build
find . -name ".travis.yml" -delete
cp %{SOURCE12} licenses.txt

%install
# install drush source
install -d -m 0755 . %{buildroot}%{_datadir}/%{name}
cp -r * %{buildroot}%{_datadir}/%{name}

# link to executable in bindir
mkdir -p %{buildroot}%{_bindir}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# link to bash complete script
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
ln -s %{_datadir}/%{name}/drush.complete.sh %{buildroot}%{_sysconfdir}/bash_completion.d/

%files
%defattr(-,root,root,-)
%doc licenses.txt
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_sysconfdir}/bash_completion.d/drush.complete.sh

%changelog
