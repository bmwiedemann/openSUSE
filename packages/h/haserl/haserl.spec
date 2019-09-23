#
# spec file for package haserl
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


Name:           haserl
BuildRequires:  automake
BuildRequires:  lua-devel
BuildRequires:  pkg-config
Version:        0.9.35
Release:        0
Url:            http://haserl.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{name}/haserl-devel/%{name}-%{version}.tar.gz
Summary:        CGI scripting with shell/lua
License:        GPL-2.0
Group:          Development/Tools/GUI Builders
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Haserl	is a small cgi wrapper that allows "PHP" style cgi programming,
but uses a UNIX bash-like shell or lua	as the programming language. It
is  very  small,  so  it can be used in embedded environments, or where
something like PHP is too big.

It combines three features into a small cgi engine: *  It parses 
   POST  and  GET  requests,  placing  form-elements  as name=value
   pairs into the environment for the CGI script to use. This is
   somewhat like the uncgi wrapper.

*  It opens a shell, and translates all text into printable
   statements. All text within <? ... ?> constructs are passed
   verbatim to the shell.  This is somewhat like writing PHP
   scripts.

*  It can optionally be installed to drop its  permissions  to	the
owner  of the script, giving it some of the security features of suexec
or cgiwrapper.

%prep
%setup

%build
%configure  --with-lua --enable-bash-extensions \
	--enable-subshell=/bin/bash
make

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/haserl
%{_mandir}/man1/haserl.1.gz

%changelog
