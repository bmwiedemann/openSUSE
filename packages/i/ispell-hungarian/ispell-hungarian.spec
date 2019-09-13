#
# spec file for package ispell-hungarian
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


Name:           ispell-hungarian
Version:        1.6.1
Release:        0
Summary:        Hungarian Ispell Dictionary
License:        GPL-2.0+ or LGPL-2.1+ or MPL-1.1
Group:          Productivity/Text/Spell
Url:            http://magyarispell.sourceforge.net/
Source:         https://downloads.sourceforge.net/magyarispell/magyarispell-%{version}.tar.gz
Source1:        magyar.el
Patch0:         magyarispell-1.2.diff
BuildRequires:  ispell
BuildRequires:  m4
Provides:       ispell_dictionary
Provides:       locale(ispell:hu)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the hungarian ispell dictionary.

%prep
%setup -q -n magyarispell-%{version}
%patch0

%build
make %{?_smp_mflags} ispell

%install
pushd tmp
install -Dm644 magyar.aff %{buildroot}%{_prefix}/lib/ispell/magyar.aff
ln -s magyar.aff %{buildroot}%{_prefix}/lib/ispell/hungarian.aff
install -m 644 magyar4ispell.hash %{buildroot}%{_prefix}/lib/ispell/magyar.hash
ln -s magyar.hash %{buildroot}%{_prefix}/lib/ispell/hungarian.hash
popd
install -Dm644 %{SOURCE1} %{buildroot}%{_prefix}/lib/ispell/emacs/magyar.el
ln -s magyar.el %{buildroot}%{_prefix}/lib/ispell/emacs/hungarian.el

%files
%defattr(-,root,root)
%doc COPYING* ChangeLog README
%lang(hu) %doc GYIK OLVASSEL
%{_prefix}/lib/ispell/emacs/*
%{_prefix}/lib/ispell/hungarian*
%{_prefix}/lib/ispell/magyar*

%changelog
