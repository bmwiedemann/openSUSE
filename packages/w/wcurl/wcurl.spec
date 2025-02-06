#
# spec file for package wcurl
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


Name:           wcurl
Version:        2024.12.08
Release:        0
Summary:        A simple wrapper around curl to easily download files
License:        curl
URL:            https://github.com/curl/wcurl
Source:         https://github.com/curl/wcurl/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  curl >= 7.46.0
%if 0%{?sle_version} > 150500 || 0%{?suse_version} >= 1600
BuildRequires:  shunit2
%endif
Requires:       curl >= 7.46.0
BuildArch:      noarch

%description
A simple curl wrapper which lets you use curl to download files
without having to remember any parameters.
Simply call wcurl with a list of URLs you want to download and
wcurl will pick sane defaults.

If you need anything more complex, you can provide any of curl's
supported parameters via the --curl-options option. Just beware
that you likely should be using curl directly if your use case is
not covered.

By default, wcurl will:
 * Percent-encode whitespaces in URLs;
 * Download multiple URLs in parallel if the installed curl's
   version is >= 7.66.0;
 * Follow redirects;
 * Automatically choose a filename as output;
 * Avoid overwriting files if the installed curl's version
   is >= 7.83.0 (--no-clobber);
 * Perform retries;
 * Set the downloaded file timestamp to the value provided by the
   server, if available;
 * Disable curl's URL globbing parser so {} and [] characters in
   URLs are not treated specially;
 * Percent-decode the resulting filename;
 * Use "index.html" as default filename if there's none in the
   URL.

%prep
%autosetup

%build

%install
install -Dm 755 wcurl %{buildroot}%{_bindir}/wcurl
install -Dm 644 wcurl.1 %{buildroot}%{_mandir}/man1/wcurl.1

%check
#---tests.sh needs shunit2 version >= 2.1.8 to be able to run all tests
%if 0%{?sle_version} > 150500 || 0%{?suse_version} >= 1600
%if %{pkg_vcmp shunit2 >= 2.1.8}
tests/tests.sh
%endif
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/wcurl
%{_mandir}/man1/wcurl.1%{?ext_man}*

%changelog
