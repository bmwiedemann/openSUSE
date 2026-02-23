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
Version:        0.29.5
Release:        0
Summary:        An AI agent that brings the power of Gemini directly into your terminal
License:        Apache-2.0
URL:            https://github.com/google-gemini/gemini-cli
Source0:        https://github.com/google-gemini/gemini-cli/releases/download/v%{version}/gemini.js#/%{name}-%{version}.js
Source1:        https://raw.githubusercontent.com/google-gemini/gemini-cli/refs/tags/v%{version}/LICENSE
Requires:       git-core
Requires:       grep
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
cp -p %{SOURCE1} .

%build
sed -i -e '1s,#!/usr/bin/env node,#!/usr/bin/node,' %{SOURCE0}

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/gemini

%files
%defattr(-,root,root)
%license LICENSE
%{_bindir}/gemini

%changelog
