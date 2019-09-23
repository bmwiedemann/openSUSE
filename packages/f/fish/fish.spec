#
# spec file for package fish
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fish
Version:        3.0.2
Release:        0
Summary:        The "friendly interactive shell"
License:        GPL-2.0-only
Group:          System/Shells
Url:            https://fishshell.com/
Source:         https://github.com/fish-shell/fish-shell/releases/download/%{version}/fish-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  groff
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel >= 10.21
BuildRequires:  pkgconfig
BuildRequires:  python
Requires:       bc
Requires:       man
Recommends:     terminfo

%description
fish is a command line shell.
It is geared towards interactive use and its features are focused on user
friendlieness and discoverability. The language syntax is simple but
incompatible with other shell languages.

%package devel
Summary:        Devel files for the fish shell
Group:          Development/Libraries/C and C++

%description devel
This package contains development files for the fish shell.

%prep
%setup -q

# fix E: env-script-interpreter
find share/tools -type f -name *.py -exec sed -i -r '1s|^#!%{_bindir}/env |#!%{_bindir}/|' {} +

%build
%configure \
  --without-included-pcre2
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name}

# Drop the curl completions, the curl packages provide a better version
rm %{buildroot}/%{_datadir}/fish/completions/curl.fish

%post
# Add fish to the list of allowed shells in /etc/shells
if ! grep -q '^%{_bindir}/%{name}$' %{_sysconfdir}/shells; then
	echo %{_bindir}/%{name} >>%{_sysconfdir}/shells
fi

%postun
# Remove fish from the list of allowed shells in /etc/shells
if [ "$1" = 0 ]; then
	grep -v '^%{_bindir}/%{name}$' %{_sysconfdir}/shells >%{_sysconfdir}/%{name}.tmp
	mv %{_sysconfdir}/%{name}.tmp %{_sysconfdir}/shells
fi

%files -f %{name}.lang
%dir %{_sysconfdir}/fish
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*.1%{?ext_man}

%files devel
%{_datadir}/pkgconfig/fish.pc

%changelog
