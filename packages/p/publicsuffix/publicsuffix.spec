#
# spec file for package publicsuffix
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2015 yaneti@declera.com
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


Name:           publicsuffix
Version:        20240603
Release:        0
Summary:        Cross-vendor public domain suffix database
License:        MPL-2.0
URL:            https://publicsuffix.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  psl-make-dafsa
BuildArch:      noarch

%description
The Public Suffix List is a cross-vendor initiative to provide
an accurate list of domain name suffixes, maintained by the hard work
of Mozilla volunteers and by submissions from registries.
Software using the Public Suffix List will be able to determine where
cookies may and may not be set, protecting the user from being
tracked across sites.

%prep
%autosetup

%build
psl-make-dafsa \
    --input-format=psl \
    --output-format=binary \
    public_suffix_list.dat public_suffix_list.dafsa

%check
%make_build test-syntax

%install
install -m 644 -p -D public_suffix_list.dat \
  %{buildroot}/%{_datadir}/%{name}/public_suffix_list.dat
ln -s public_suffix_list.dat %{buildroot}/%{_datadir}/%{name}/effective_tld_names.dat
install -m 644 -p -D public_suffix_list.dafsa \
  %{buildroot}/%{_datadir}/%{name}/public_suffix_list.dafsa

%files
%license LICENSE
%{_datadir}/%{name}

%changelog
