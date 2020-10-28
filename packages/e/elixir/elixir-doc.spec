#
# spec file for package elixir-doc
#
# Copyright (c) 2020 SUSE LLC
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


Name:           elixir-doc
Version:        1.11.1
Release:        0
Summary:        Documentation for elixir
License:        Apache-2.0
Group:          Documentation/Other
URL:            http://elixir-lang.org
Source0:        https://github.com/elixir-lang/elixir/archive/v%{version}.tar.gz#/elixir-%{version}.tar.gz
BuildRequires:  elixir
BuildRequires:  elixir-ex_doc
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       elixir = %{version}

%description
Documentation for the Elixir language.

%prep
%setup -q -n elixir-%{version}

%build
# Elixir wants UTF-8 locale, force it
export LANG=en_US.UTF-8
ex_doc "Elixir" "%{version}" "lib/elixir/ebin" -m "Kernel" -u "https://github.com/elixir-lang/elixir" -o doc/elixir -p http://elixir-lang.org/docs.html
ex_doc "EEx" "%{version}" "lib/eex/ebin" -m "EEx" -u "https://github.com/elixir-lang/elixir" -o doc/eex -p http://elixir-lang.org/docs.html
ex_doc "Mix" "%{version}" "lib/mix/ebin" -m "Mix" -u "https://github.com/elixir-lang/elixir" -o doc/mix -p http://elixir-lang.org/docs.html
ex_doc "IEx" "%{version}" "lib/iex/ebin" -m "IEx" -u "https://github.com/elixir-lang/elixir" -o doc/iex -p http://elixir-lang.org/docs.html
ex_doc "ExUnit" "%{version}" "lib/ex_unit/ebin" -m "ExUint" -u "https://github.com/elixir-lang/elixir" -o doc/ex_unit -p http://elixir-lang.org/docs.html
ex_doc "Logger" "%{version}" "lib/logger/ebin" -m "Logger" -u "https://github.com/elixir-lang/elixir" -o doc/logger -p http://elixir-lang.org/docs.html

%install

%files
%defattr(-,root,root)
%doc doc

%changelog
