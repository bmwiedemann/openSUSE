#
# spec file for package ex_doc
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


Name:           ex_doc
Version:        0.38.1
Release:        0
Summary:        ExDoc produces HTML and online documentation for Elixir projects
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Other
URL:            https://github.com/elixir-lang/ex_doc
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  elixir >= 1.15
BuildRequires:  elixir-hex
Obsoletes:      elixir-ex_doc < %{version}
Provides:       elixir-ex_doc = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# ex_doc package IS arch dependent
# See https://github.com/elixir-lang/elixir/issues/2785 for details
# BuildArch:      noarch

%description
ExDoc is a tool to generate documentation for your Elixir projects. In case you
are looking for documentation for Elixir itself, check out Elixir's website.

%prep
%autosetup -a1 -v

%build
export LANG=en_US.UTF-8
export MIX_ENV=prod
export MIX_PATH=%{elixir_libdir}/hex/ebin
%{__mix} escript.build

%install
sed -i -e '1s|/usr/bin/env escript|/usr/bin/escript|' ex_doc
install -D -m 0755 ex_doc %{buildroot}%{_bindir}/ex_doc

%files
%defattr(-,root,root)
%doc README.md CHANGELOG.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/ex_doc

%changelog
