#
# spec file for package elixir
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


Name:           elixir
Version:        1.11.4
Release:        0
Summary:        Functional meta-programming aware language built atop Erlang
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            http://elixir-lang.org
Source0:        https://github.com/elixir-lang/elixir/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        macros.elixir
BuildRequires:  gcc
BuildRequires:  make
# required by Mix.SCM.Git see also (https://github.com/elixir-lang/elixir/issues/1386)
Requires:       erlang >= 21
Requires:       git >= 1.7
BuildRequires:  erlang >= 21
BuildRequires:  erlang-dialyzer
BuildRequires:  erlang-src
BuildRequires:  git >= 1.7
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       erlang

%description
Elixir is a functional meta-programming aware language built on top
of the Erlang VM. It is a dynamic language with flexible syntax with
macros support that leverage Erlang's abilities to build concurrent,
distributed, fault-tolerant applications with hot code upgrades.

Elixir also provides first-class support for pattern matching,
polymorphism via protocols (similar to Clojure's), aliases and
associative data structures (usually known as dicts or hashes in
other programming languages).

Finally, Elixir and Erlang share the same bytecode and data types.
This means one can invoke Erlang code from Elixir (and vice-versa)
without any conversion or performance impact.

%package src
Summary:        Elixir programming language sources
Group:          Development/Sources
Requires:       %{name} = %{version}

%description src
Elixir source code.

%define elixirdir %{_prefix}/lib/elixir

%prep
%setup -q

%build
# Elixir wants UTF-8 locale, force it
export LANG=en_US.UTF-8
# Make Elixir
make

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}
# install -D -m 0644
# Relink
for I in iex elixir elixirc mix
do
	ln -sf %{elixirdir}/bin/$I %{buildroot}%{_bindir}/$I
done
install -D -m 0644 %{S:2} %{buildroot}%{_rpmmacrodir}/macros.elixir

%check
export LANG=en_US.UTF-8
make test

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md NOTICE
%license LICENSE
%dir %{elixirdir}
%dir %{elixirdir}/bin
%dir %{elixirdir}/lib
%{_bindir}/iex
%{_bindir}/elixir
%{_bindir}/elixirc
%{_bindir}/mix
%{_mandir}/man1/iex.1.gz
%{_mandir}/man1/elixir.1.gz
%{_mandir}/man1/elixirc.1.gz
%{_mandir}/man1/mix.1.gz
%{elixirdir}/bin/iex
%{elixirdir}/bin/elixirc
%{elixirdir}/bin/mix
%{elixirdir}/bin/elixir
%{elixirdir}/lib/*
%{_rpmmacrodir}/macros.elixir

%changelog
