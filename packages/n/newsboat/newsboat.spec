#
# spec file for package newsboat
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


Name:           newsboat
Version:        2.21
Release:        0
Summary:        RSS/Atom Feed Reader for Text Terminals
License:        MIT
Group:          Productivity/Networking/Web/Browsers
URL:            https://newsboat.org
Source:         https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz
Source1:        https://newsboat.org/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://newsboat.org/newsboat.pgp#/%{name}.keyring
Source3:        vendor.tar.xz
# pbleser: introduce OPTFLAGS make variable, instead of hard-coded -ggdb
Patch0:         newsbeuter-makefile.patch
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  libcurl-devel >= 7.18.0
BuildRequires:  libjson-c-devel >= 0.11
BuildRequires:  libopenssl-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libstfl-devel >= 0.21
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.25.0
BuildRequires:  sqlite3-devel >= 3.5
BuildRequires:  zlib-devel
BuildRequires:  rubygem(asciidoctor)
Recommends:     %{name}-lang
Recommends:     web_browser
Provides:       newsbeuter = %{version}
Obsoletes:      newsbeuter <= 2.9

%description
Newsboat is an RSS/Atom feedreader. RSS and Atom are a number of
widely-used XML formats to transmit, publish and syndicate articles,
for example news or blog articles. Newsboat is designed to be used on
text terminals.

%lang_package

%prep
%setup -qa3
%patch0 -p1
mkdir cargo-home
cat >cargo-home/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'
[source.vendored-sources]
directory = './vendor'
EOF
sed -i 's/#!\/usr\/bin\/env perl/#!\/usr\/bin\/perl/' ./contrib/pinboard.pl
sed -i 's/#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/' ./doc/examples/example-exec-script.py

%build
export CARGO_HOME=`pwd`/cargo-home/
./config.sh

%make_build \
    	  OPTFLAGS="%{optflags}"

%install
export CARGO_HOME=`pwd`/cargo-home/
%make_install prefix="%{_prefix}" docdir=%{_docdir}/%{name}

for l in zh; do
    rm -rf "%{buildroot}%{_datadir}/locale/${l}"
done

%find_lang %{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_bindir}/podboat
%dir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples
%{_docdir}/%{name}/faq.html
%{_docdir}/%{name}/%{name}.html
%{_docdir}/%{name}/contrib/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/podboat.1%{?ext_man}
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/newsboat.svg

%files lang -f %{name}.lang

%changelog
