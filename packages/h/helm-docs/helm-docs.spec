#
# spec file for package helm-docs
#
# Copyright (c) 2022 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           helm-docs
Version:        1.11.0
Release:        0
Summary:        A tool for automatically generating markdown documentation for helm charts
License:        GPL-3.0-only
URL:            https://github.com/norwoodj/helm-docs
Source:         helm-docs-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.17

%description
The helm-docs tool auto-generates documentation from helm charts into markdown files. The resulting files contain metadata about their respective chart and a table with each of the chart's values, their defaults, and an optional description parsed from comments.

The markdown generation is entirely gotemplate driven. The tool parses metadata from charts and generates a number of sub-templates that can be referenced in a template file (by default README.md.gotmpl). If no template file is provided, the tool has a default internal template that will generate a reasonably formatted README.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/helm-docs ./cmd/helm-docs

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
