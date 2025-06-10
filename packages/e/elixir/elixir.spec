#
# spec file for package elixir
#
# Copyright (c) 2025 SUSE LLC
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


%define elixirdir %{_prefix}/lib/elixir
Name:           elixir
Version:        1.18.4
Release:        0
Summary:        Functional meta-programming aware language built atop Erlang
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://elixir-lang.org
Source0:        https://github.com/elixir-lang/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/elixir-lang/%{name}/releases/download/v%{version}/Docs.zip#/%{name}-%{version}-doc.zip
Source2:        macros.elixir
Patch0:         001-skip-translator-supervisor-test.patch
Patch1:         002-skip-tests-iex-helpers.patch
BuildRequires:  erlang >= 25
BuildRequires:  erlang-dialyzer
BuildRequires:  erlang-src
BuildRequires:  fdupes
BuildRequires:  gcc
# required by Mix.SCM.Git see also (https://github.com/elixir-lang/elixir/issues/1386)
BuildRequires:  git-core >= 1.7
BuildRequires:  make
BuildRequires:  unzip
Requires:       erlang >= 25
BuildArch:      noarch

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

%package doc
Summary:        Documentation for elixir
Group:          Documentation/Other
Requires:       elixir = %{version}
BuildArch:      noarch

%description doc
Documentation for the Elixir language.

%prep
%autosetup -p1

unzip -o %{SOURCE1}
find doc \( -name ".build" -or -name ".ex_doc" \) -delete

%build
# Elixir wants UTF-8 locale, force it
export LANG=en_US.UTF-8

# Enable deterministic builds in the Erlang compiler
export ERL_COMPILER_OPTIONS=deterministic

# Make Elixir
%make_build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_bindir}
for I in iex elixir elixirc mix
do
	ln -sf %{elixirdir}/bin/$I %{buildroot}%{_bindir}/$I
done

install -D -m 0644 %{SOURCE2} %{buildroot}%{_rpmmacrodir}/macros.elixir

mkdir -p %{buildroot}%{_defaultdocdir}
cp -pa doc %{buildroot}%{_defaultdocdir}/elixir-doc

%fdupes -s %{buildroot}/%{_mandir}
%fdupes %{buildroot}/%{_prefix}

%check
export LANG=en_US.UTF-8
%make_build test

%files
%doc CHANGELOG.md README.md NOTICE
%license LICENSE
%dir %{elixirdir}
%dir %{elixirdir}/bin
%dir %{elixirdir}/lib
%{_bindir}/iex
%{_bindir}/elixir
%{_bindir}/elixirc
%{_bindir}/mix
%{_mandir}/man1/iex.1%{?ext_man}
%{_mandir}/man1/elixir.1%{?ext_man}
%{_mandir}/man1/elixirc.1%{?ext_man}
%{_mandir}/man1/mix.1%{?ext_man}
%{elixirdir}/bin/iex
%{elixirdir}/bin/elixirc
%{elixirdir}/bin/mix
%{elixirdir}/bin/elixir
%{elixirdir}/lib/*
%{_rpmmacrodir}/macros.elixir

%files doc
%license LICENSE
%{_defaultdocdir}/elixir-doc

%changelog
