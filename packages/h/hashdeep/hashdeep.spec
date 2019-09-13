#
# spec file for package md5deep
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           hashdeep
Version:        4.4
Release:        0
Summary:        Compute MD5, SHA-1, SHA-256, Tiger or Whirlpool message digests
License:        SUSE-Public-Domain and GPL-2.0+
Group:          System/Base
Url:            http://md5deep.sourceforge.net/
Source0:        %{name}-release-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python
BuildRequires:  python-devel
Requires:       python
Provides:       md5deep = %{version}
Obsoletes:      md5deep < %{version}
BuildRoot:      %{_tmppath}/%{name}-release-%{version}-build

%description
hashdeep is a program to compute, match, and audit hashsets.
md5deep computes the MD5, SHA-1, SHA-256, Tiger, or Whirlpool message digest
for any number of files while optionally recursively digging through the
directory structure. md5deep can also match input files against lists of known
hashes in a variety of formats.

%prep
%setup -q -n %{name}-release-%{version}

%build
sh bootstrap.sh
if test -x ./configure; then
     %configure
fi
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install

%make_install

# create symlinks for man pages
%fdupes -s %{buildroot}/%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/hashdeep
%{_bindir}/md5deep
%{_bindir}/sha1deep
%{_bindir}/sha256deep
%{_bindir}/tigerdeep
%{_bindir}/whirlpooldeep
%{_mandir}/man1/hashdeep.1*
%{_mandir}/man1/md5deep.1*
%{_mandir}/man1/sha1deep.1*
%{_mandir}/man1/sha256deep.1*
%{_mandir}/man1/whirlpooldeep.1*
%{_mandir}/man1/tigerdeep.1*
%doc AUTHORS ChangeLog COPYING README NEWS

%changelog
