#
# spec file for package mlmmj
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


Name:           mlmmj
Version:        1.3.0
Release:        0
Summary:        Mail Server Independent Reimplementation of the EZMLM Mailing List
License:        MIT
Group:          Productivity/Networking/Email/Mailinglists
Url:            http://mlmmj.org/
Source0:        http://mlmmj.org/releases/%{name}-%{version}.tar.bz2
Source1:        mlmmj-rpmlintrc
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is an attempt at implementing a mailing list manager with the same
functionality as EZMLM, but with the MIT/X11 license and no mail server
dependency.

%prep
%setup -q

%build
%configure --enable-receive-strip
make CFLAGS="%{optflags} -fstack-protector" %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

rm contrib/web/php-admin/htdocs/index.php.orig
rm contrib/web/php-user/mlmmj.php.orig

install -d -m 0755 %{buildroot}%{_datadir}/%{name}/contrib
install -d -m 0755 %{buildroot}%{_defaultdocdir}/%{name}/examples
cp -a contrib/{amime-receive,web} %{buildroot}%{_defaultdocdir}/%{name}/examples/
cp -a contrib/receivestrip/README README.receivestrip
%fdupes %{buildroot}

%files
%dir %{_defaultdocdir}/%{name}
%doc README* FAQ UPGRADE AUTHORS ChangeLog TUNABLES
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
%{_defaultdocdir}/%{name}/examples

%changelog
