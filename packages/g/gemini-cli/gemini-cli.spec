#
# spec file for package gemini-cli
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gemini-cli
Version:        0.38.1
Release:        0
Summary:        An AI agent that brings the power of Gemini directly into your terminal
License:        Apache-2.0
URL:            https://github.com/google-gemini/gemini-cli
Source0:        https://github.com/google-gemini/gemini-cli/releases/download/v%{version}/gemini-cli-bundle.zip#/%{name}-%{version}-cli-bundle.zip
Source1:        https://raw.githubusercontent.com/google-gemini/gemini-cli/refs/tags/v%{version}/LICENSE
BuildRequires:  unzip
BuildArch:      noarch
Requires:       /usr/bin/node
Requires:       git-core
Requires:       grep
Requires:       gzip
Requires:       tar
Requires:       zstd
Recommends:     codespell

%description
Gemini CLI is an open-source AI agent that brings the power of Gemini directly
into your terminal. It provides lightweight access to Gemini, giving you the
most direct path from your prompt to our model.

* Free tier: 60 requests/min and 1,000 requests/day with personal Google account.
* Powerful Gemini 3 Pro: Access to 1M token context window.
* Built-in tools: Google Search grounding, file operations, shell commands, web fetching.
* Extensible: MCP (Model Context Protocol) support for custom integrations.
* Terminal-first: Designed for developers who live in the command line.
* Open source: Apache 2.0 licensed.

%prep
%setup -c
cp -p %{SOURCE1} .

%build

%install
install -d -m 0755 %{buildroot}%{_defaultdocdir}/gemini-cli
cp -pr docs/* %{buildroot}%{_defaultdocdir}/gemini-cli/
rm -rf docs
install -d %{buildroot}%{_libexecdir}/gemini-cli
cp -pr *.js builtin policies bundled node_modules %{buildroot}%{_libexecdir}/gemini-cli
install -d -m 0755 %{buildroot}%{_bindir}
ln -s %{_libexecdir}/gemini-cli/gemini.js %{buildroot}%{_bindir}/gemini

%files
%license LICENSE
%doc %{_defaultdocdir}/gemini-cli/
%{_bindir}/gemini
%{_libexecdir}/gemini-cli

%changelog
